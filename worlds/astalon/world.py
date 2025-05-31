import logging
from collections import defaultdict
from functools import cached_property
from typing import TYPE_CHECKING, Any, ClassVar, Final

from BaseClasses import CollectionState, Item, ItemClassification, Region, Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, Type, components, icon_paths, launch_subprocess

from .constants import GAME_NAME, VERSION
from .items import (
    CHARACTERS,
    EARLY_BLUE_DOORS,
    EARLY_ITEMS,
    EARLY_SWITCHES,
    EARLY_WHITE_DOORS,
    QOL_ITEMS,
    AstalonItem,
    Character,
    Elevator,
    Events,
    Eye,
    ItemGroup,
    Key,
    KeyItem,
    filler_items,
    item_name_groups,
    item_name_to_id,
    item_table,
    trap_items,
)
from .locations import (
    AstalonLocation,
    LocationGroup,
    LocationName,
    location_name_groups,
    location_name_to_id,
    location_table,
)
from .logic import MAIN_ENTRANCE_RULES, MAIN_LOCATION_RULES
from .options import ApexElevator, AstalonOptions, Goal, RandomizeCharacters
from .regions import RegionName, astalon_regions
from .tracker import TRACKER_WORLD

if TYPE_CHECKING:
    from BaseClasses import Location, MultiWorld
    from Options import Option

    from .logic import RuleInstance


# ██░░░██████░░███░░░███
# ██░░░░██░░░▓▓░░░▓░░███
# ██░█░▓░░▓▓▓▓▓▓░▓░░░███
# █░▓█░▓▓▓▓▓█░▓░░█▓▓▓░██
# █░▓▓▓▓▓▓▓▓██░███▓▓▓▓░█
# ░▓▓██▓▓▓▓▓▓▓███▓▓▓▓██░
# ░▓████▓▓▓░░░░░░░░░▓██░ THIS IS THE SAFETY BUBSETTE OF GOOD CODE.
# ░▓████▓▓░█████████░██░ MANY GOOD PROGRAMS AND FEW ERRORS WILL COME TO YOU
# █░▓██▓▓░███░███░██░▓░█ AS LONG AS YOU KEEP HER IN YOUR PROGRAM TO WATCH OVER IT
# ██░░▓▓▓░███░███░██░░██ INCREMENT THIS NUMBER EVERY TIME YOU SAY HI TO BUBSETTE
# ████░░░░██████████░███ hi_bubsette = 3
# ████████░░░░░░░░░░████


logger = logging.getLogger(__name__)

CHARACTER_LOCATIONS: Final[tuple[tuple[Character, str], ...]] = (
    (Character.ALGUS, LocationName.GT_ALGUS.value),
    (Character.ARIAS, LocationName.GT_ARIAS.value),
    (Character.KYULI, LocationName.GT_KYULI.value),
    (Character.ZEEK, LocationName.MECH_ZEEK.value),
    (Character.BRAM, LocationName.TR_BRAM.value),
)

CHARACTER_STARTS: Final[dict[int, tuple[Character, ...]]] = {
    RandomizeCharacters.option_trio: CHARACTERS[:3],
    RandomizeCharacters.option_all: CHARACTERS,
    RandomizeCharacters.option_algus: (Character.ALGUS,),
    RandomizeCharacters.option_arias: (Character.ARIAS,),
    RandomizeCharacters.option_kyuli: (Character.KYULI,),
    RandomizeCharacters.option_zeek: (Character.ZEEK,),
    RandomizeCharacters.option_bram: (Character.BRAM,),
}


def launch_client() -> None:
    from .client import launch

    launch_subprocess(launch, name="Astalon Tracker")


components.append(
    Component("Astalon Tracker", func=launch_client, component_type=Type.CLIENT, icon="astalon")
)

icon_paths["astalon"] = f"ap:{__name__}/images/pil.png"


class AstalonWebWorld(WebWorld):
    theme = "stone"
    tutorials = [  # noqa: RUF012
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up the Astalon randomizer.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["DrTChops"],
        )
    ]


class AstalonWorld(World):
    """
    Uphold your pact with the Titan of Death, Epimetheus!
    Fight, climb and solve your way through a twisted tower as three unique adventurers,
    on a mission to save their village from impending doom!
    """

    game = GAME_NAME
    web = AstalonWebWorld()
    options_dataclass = AstalonOptions
    options: AstalonOptions  # type: ignore
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    required_client_version = (0, 6, 0)

    starting_characters: "list[Character]"
    extra_gold_eyes: int = 0

    cached_spheres: ClassVar[list[set["Location"]]]

    # UT integration
    tracker_world: ClassVar = TRACKER_WORLD
    ut_can_gen_without_yaml = True
    glitches_item_name = Events.FAKE_OOL_ITEM.value

    rule_cache: "dict[int, RuleInstance]"
    _rule_deps: "dict[str, set[int]]"

    def __init__(self, multiworld: "MultiWorld", player: int) -> None:
        super().__init__(multiworld, player)
        self.rule_cache = {}
        self._rule_deps = defaultdict(set)
        self.starting_characters = []

    def generate_early(self) -> None:
        if self.options.randomize_characters == RandomizeCharacters.option_solo:
            self.starting_characters.append(self.random.choice(CHARACTERS))
        elif self.options.randomize_characters == RandomizeCharacters.option_random_selection:
            for character in CHARACTERS:
                if self.random.randint(0, 1):
                    self.starting_characters.append(character)
            if not self.starting_characters:
                self.starting_characters.append(self.random.choice(CHARACTERS))
        elif int(self.options.randomize_characters) in CHARACTER_STARTS:
            self.starting_characters.extend(CHARACTER_STARTS[int(self.options.randomize_characters)])

        if self.options.goal == Goal.option_eye_hunt:
            self.extra_gold_eyes = round(
                self.options.additional_eyes_required.value * (self.options.extra_eyes / 100)
            )

        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and GAME_NAME in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[GAME_NAME]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Option | None = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

            if "starting_characters" in slot_data:
                self.starting_characters = [Character(c) for c in slot_data["starting_characters"]]
            if "extra_gold_eyes" in slot_data:
                self.extra_gold_eyes = slot_data["extra_gold_eyes"]

    def create_location(self, name: str) -> AstalonLocation:
        location_name = LocationName(name)
        data = location_table[name]
        region = self.get_region(data.region.value)
        location = AstalonLocation(self.player, name, location_name_to_id.get(name), region)
        rule = MAIN_LOCATION_RULES.get(location_name)
        if rule is not None:
            rule = rule.resolve(self)
            if rule.always_false:
                logger.debug(f"No matching rules for {name}")
            for item_name, rules in rule.deps().items():
                self._rule_deps[item_name] |= rules
            location.access_rule = rule.test
        region.locations.append(location)
        return location

    def create_regions(self) -> None:
        for region_name in astalon_regions:
            region = Region(region_name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in astalon_regions.items():
            region = self.get_region(region_name.value)
            for exit_region_name in region_data.exits:
                region_pair = (region_name, exit_region_name)
                rule = MAIN_ENTRANCE_RULES.get(region_pair)
                if rule is not None:
                    rule = rule.resolve(self)
                    if rule.always_false:
                        logger.debug(f"No matching rules for {region_name.value} -> {exit_region_name.value}")
                        continue
                    for item_name, rules in rule.deps().items():
                        self._rule_deps[item_name] |= rules

                entrance = region.connect(
                    self.get_region(exit_region_name.value), rule=rule.test if rule else None
                )
                if rule:
                    for indirect_region in rule.indirect():
                        self.multiworld.register_indirect_condition(
                            self.get_region(indirect_region.value),
                            entrance,
                        )

        logic_groups: set[str] = set()
        if self.options.randomize_key_items:
            logic_groups.add(LocationGroup.ITEM.value)
        if self.options.randomize_attack_pickups:
            logic_groups.add(LocationGroup.ATTACK.value)
        if self.options.randomize_health_pickups:
            logic_groups.add(LocationGroup.HEALTH.value)
        if self.options.randomize_white_keys:
            logic_groups.add(LocationGroup.KEY_WHITE.value)
        if self.options.randomize_blue_keys:
            logic_groups.add(LocationGroup.KEY_BLUE.value)
        if self.options.randomize_red_keys:
            logic_groups.add(LocationGroup.KEY_RED.value)
        if self.options.randomize_shop:
            logic_groups.add(LocationGroup.SHOP.value)
        if self.options.randomize_elevator:
            logic_groups.add(LocationGroup.ELEVATOR.value)
        if self.options.randomize_switches:
            logic_groups.add(LocationGroup.SWITCH.value)
        if self.options.randomize_candles:
            logic_groups.add(LocationGroup.CANDLE.value)

        for group, location_names in location_name_groups.items():
            if group not in logic_groups:
                continue

            for location_name in location_names:
                if location_name == LocationName.SHOP_MAP_REVEAL:
                    # this requires way too much map completion
                    continue
                if (
                    location_name == LocationName.APEX_ELEVATOR
                    and self.options.apex_elevator != ApexElevator.option_included
                ):
                    continue

                self.create_location(location_name)

        if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
            self.create_event(Events.ZEEK, LocationName.MECH_ZEEK)
            self.create_event(Events.BRAM, LocationName.TR_BRAM)
        else:
            for character, location_name in CHARACTER_LOCATIONS:
                if character not in self.starting_characters:
                    self.create_location(location_name)

        if not self.options.randomize_key_items:
            self.create_event(Events.EYE_RED, LocationName.GT_EYE_RED)
            self.create_event(Events.EYE_BLUE, LocationName.MECH_EYE_BLUE)
            self.create_event(Events.EYE_GREEN, LocationName.ROA_EYE_GREEN)
            self.create_event(Events.SWORD, LocationName.GT_SWORD)
            self.create_event(Events.ASCENDANT_KEY, LocationName.GT_ASCENDANT_KEY)
            self.create_event(Events.ADORNED_KEY, LocationName.TR_ADORNED_KEY)
            self.create_event(Events.BANISH, LocationName.GT_BANISH)
            self.create_event(Events.VOID, LocationName.GT_VOID)
            self.create_event(Events.BOOTS, LocationName.MECH_BOOTS)
            self.create_event(Events.CLOAK, LocationName.MECH_CLOAK)
            self.create_event(Events.CYCLOPS, LocationName.MECH_CYCLOPS)
            self.create_event(Events.BELL, LocationName.HOTP_BELL)
            self.create_event(Events.CLAW, LocationName.HOTP_CLAW)
            self.create_event(Events.GAUNTLET, LocationName.HOTP_GAUNTLET)
            self.create_event(Events.ICARUS, LocationName.ROA_ICARUS)
            self.create_event(Events.CHALICE, LocationName.APEX_CHALICE)
            self.create_event(Events.BOW, LocationName.CATA_BOW)
            self.create_event(Events.CROWN, LocationName.CD_CROWN)
            self.create_event(Events.BLOCK, LocationName.CATH_BLOCK)
            self.create_event(Events.STAR, LocationName.SP_STAR)

        victory_region = self.get_region(RegionName.FINAL_BOSS.value)
        victory_location = AstalonLocation(self.player, Events.VICTORY.value, None, victory_region)
        victory_item = AstalonItem(
            Events.VICTORY.value,
            ItemClassification.progression_skip_balancing,
            None,
            self.player,
        )
        victory_location.place_locked_item(victory_item)
        victory_region.locations.append(victory_location)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            Events.VICTORY.value,
            self.player,
        )

    def create_item(self, name: str) -> AstalonItem:
        if name == Events.FAKE_OOL_ITEM:
            return AstalonItem(name, ItemClassification.progression, None, self.player)

        item_data = item_table[name]
        classification: ItemClassification
        if callable(item_data.classification):
            classification = item_data.classification(self)
        else:
            classification = item_data.classification
        return AstalonItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: Events, location_name: LocationName) -> None:
        item = AstalonItem(event.value, ItemClassification.progression_skip_balancing, None, self.player)
        location = self.create_location(location_name.value)
        location.address = None
        location.place_locked_item(item)

    def create_trap(self) -> AstalonItem:
        return self.create_item(self.get_trap_item_name())

    def create_items(self) -> None:
        itempool: list[Item] = []
        filler_items: list[Item] = []

        logic_groups: set[str] = set()
        if self.options.randomize_key_items:
            logic_groups.add(ItemGroup.EYE.value)
            logic_groups.add(ItemGroup.ITEM.value)
        if self.options.randomize_attack_pickups:
            logic_groups.add(ItemGroup.ATTACK.value)
        if self.options.randomize_health_pickups:
            logic_groups.add(ItemGroup.HEALTH.value)
        if self.options.randomize_white_keys:
            logic_groups.add(ItemGroup.DOOR_WHITE.value)
        if self.options.randomize_blue_keys:
            logic_groups.add(ItemGroup.DOOR_BLUE.value)
        if self.options.randomize_red_keys:
            logic_groups.add(ItemGroup.DOOR_RED.value)
        if self.options.randomize_shop:
            logic_groups.add(ItemGroup.SHOP.value)
        if self.options.randomize_elevator:
            logic_groups.add(ItemGroup.ELEVATOR.value)
        if self.options.randomize_switches:
            logic_groups.add(ItemGroup.SWITCH.value)
        if self.options.randomize_candles:
            logic_groups.add(ItemGroup.HEAL.value)

        for group, item_names in item_name_groups.items():
            if group not in logic_groups:
                continue

            for item_name in item_names:
                if self.options.start_with_qol and item_name in QOL_ITEMS:
                    continue
                if self.options.start_with_ascendant_key and item_name == KeyItem.ASCENDANT_KEY:
                    continue
                if self.options.start_with_bell and item_name == KeyItem.BELL:
                    continue
                if self.options.open_early_doors and item_name in EARLY_ITEMS:
                    continue
                if self.options.apex_elevator != ApexElevator.option_included and item_name == Elevator.APEX:
                    continue

                data = item_table[item_name]
                for _ in range(0, data.quantity_in_item_pool):
                    item = self.create_item(item_name)
                    if item.classification == ItemClassification.filler:
                        filler_items.append(item)
                    else:
                        itempool.append(item)

        if self.options.randomize_characters:
            for character in CHARACTERS:
                character_item = self.create_item(character.value)
                if character in self.starting_characters:
                    self.multiworld.push_precollected(character_item)
                else:
                    itempool.append(character_item)

        if self.options.start_with_qol:
            for qol_item in QOL_ITEMS:
                self.multiworld.push_precollected(self.create_item(qol_item.value))

        if self.options.start_with_ascendant_key:
            self.multiworld.push_precollected(self.create_item(KeyItem.ASCENDANT_KEY.value))
        if self.options.start_with_bell:
            self.multiworld.push_precollected(self.create_item(KeyItem.BELL.value))

        if self.options.open_early_doors:
            if self.options.randomize_white_keys:
                for white_door in EARLY_WHITE_DOORS:
                    self.multiworld.push_precollected(self.create_item(white_door.value))
            if self.options.randomize_blue_keys:
                for blue_door in EARLY_BLUE_DOORS:
                    self.multiworld.push_precollected(self.create_item(blue_door.value))
            if self.options.randomize_switches:
                for red_door in EARLY_SWITCHES:
                    self.multiworld.push_precollected(self.create_item(red_door.value))

        if self.options.goal.value == Goal.option_eye_hunt:
            for _ in range(0, self.options.additional_eyes_required.value + self.extra_gold_eyes):
                itempool.append(self.create_item(Eye.GOLD.value))

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        while len(itempool) + len(filler_items) < total_locations:
            filler_items.append(self.create_filler())

        if len(itempool) + len(filler_items) > total_locations:
            # should only happen when doing eye hunt with too few things randomized
            remove_count = len(itempool) + len(filler_items) - total_locations
            if remove_count > len(filler_items):
                raise OptionError(
                    f"Astalon player {self.player_name} failed: No space for eye hunt. "
                    "Lower your eye hunt goal or enable candle randomizer."
                )

            if remove_count == len(filler_items):
                filler_items = []
            else:
                filler_items = self.random.sample(filler_items, len(filler_items) - remove_count)

        if filler_items and self.options.trap_percentage > 0:
            total_filler = len(filler_items)
            trap_count = round(total_filler * (self.options.trap_percentage / 100))
            if trap_count > 0:
                filler_items = self.random.sample(filler_items, len(filler_items) - trap_count)
                for _ in range(trap_count):
                    filler_items.append(self.create_trap())

        self.multiworld.itempool += itempool + filler_items

    @cached_property
    def filler_item_names(self) -> tuple[str, ...]:
        items = list(filler_items)
        if not self.options.randomize_white_keys:
            items.append(Key.WHITE.value)
        if not self.options.randomize_blue_keys:
            items.append(Key.BLUE.value)
        if not self.options.randomize_red_keys:
            items.append(Key.RED.value)
        return tuple(items)

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    def get_trap_item_name(self) -> str:
        return self.random.choice(trap_items)

    @classmethod
    def stage_post_fill(cls, multiworld: "MultiWorld") -> None:
        # Cache spheres for hint calculation after fill completes.
        cls.cached_spheres = list(multiworld.get_spheres())
        if len(cls.cached_spheres) > 2 and not cls.cached_spheres[-2]:
            # remove unreachable locations
            cls.cached_spheres = cls.cached_spheres[:-2]

    @classmethod
    def stage_modify_multidata(cls, *_) -> None:
        # Clean up all references in cached spheres after generation completes.
        del cls.cached_spheres

    def fill_slot_data(self) -> dict[str, Any]:
        return {
            "version": VERSION,
            "options": self.options.as_dict(
                "difficulty",
                "goal",
                "additional_eyes_required",
                "randomize_characters",
                "randomize_key_items",
                "randomize_health_pickups",
                "randomize_attack_pickups",
                "randomize_white_keys",
                "randomize_blue_keys",
                "randomize_red_keys",
                "randomize_shop",
                "randomize_elevator",
                "randomize_switches",
                "randomize_candles",
                "skip_cutscenes",
                "apex_elevator",
                "cost_multiplier",
                "fast_blood_chalice",
                "campfire_warp",
                "allow_block_warping",
                "cheap_kyuli_ray",
                "always_restore_candles",
                "scale_character_stats",
                "tag_link",
                "death_link",
            ),
            "starting_characters": [c.value for c in self.starting_characters],
            "character_strengths": self._get_character_strengths(),
            "extra_gold_eyes": self.extra_gold_eyes,
        }

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        # Trigger a 2nd gen with passed along slot data
        return slot_data

    def _get_character_strengths(self) -> dict[str, float]:
        character_strengths: dict[str, float] = {c.value: 0 for c in CHARACTERS}
        if not self.options.scale_character_stats:
            return character_strengths

        spheres = self.cached_spheres
        sphere_count = len(spheres)
        found = len(self.starting_characters) if self.options.randomize_characters else 3
        limit = 5
        if found >= limit:
            return character_strengths

        for sphere_id, sphere in enumerate(spheres):
            for location in sphere:
                if (
                    location.item
                    and location.item.player == self.player
                    and location.item.name in character_strengths
                ):
                    scaling = (sphere_id + 1) / sphere_count
                    logger.debug(
                        f"{location.item.name} in sphere {sphere_id + 1} / {sphere_count}, scaling {scaling}"
                    )
                    character_strengths[location.item.name] = scaling
                    found += 1
                    if found >= limit:
                        return character_strengths

        logger.warning("Could not find all Astalon characters in spheres, something is likely wrong")
        return character_strengths

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        changed = super().collect(state, item)
        if changed and getattr(self, "_rule_deps", None):
            player_results: dict[int, bool] = state._astalon_rule_results[self.player]  # type: ignore
            for rule_id in self._rule_deps[item.name]:
                player_results.pop(rule_id, None)
        return changed

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        changed = super().remove(state, item)
        if changed and getattr(self, "_rule_deps", None):
            player_results: dict[int, bool] = state._astalon_rule_results[self.player]  # type: ignore
            for rule_id in self._rule_deps[item.name]:
                player_results.pop(rule_id, None)
        return changed
