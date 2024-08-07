import logging
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Optional, Set

from BaseClasses import CollectionState, Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .constants import GAME_NAME
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
    Eye,
    ItemGroup,
    Key,
    KeyItem,
    filler_items,
    item_name_groups,
    item_name_to_id,
    item_table,
)
from .locations import (
    AstalonLocation,
    LocationGroup,
    LocationName,
    location_name_groups,
    location_name_to_id,
    location_table,
)
from .options import ApexElevator, AstalonOptions, Goal, RandomizeCharacters
from .regions import RegionName, astalon_regions
from .rules import AstalonRules, Events

if TYPE_CHECKING:
    from BaseClasses import Location, MultiWorld

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


class AstalonWebWorld(WebWorld):
    theme = "stone"
    tutorials = [
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
    why do they call it astalon when you ass to the vanilla lawn ass from rando the lawn
    """

    game = GAME_NAME
    web = AstalonWebWorld()
    options_dataclass = AstalonOptions
    options: AstalonOptions  # type: ignore
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    starting_characters: List[Character]
    required_gold_eyes: int = 0
    extra_gold_eyes: int = 0
    rules: AstalonRules

    cached_spheres: ClassVar[List[Set["Location"]]]

    def generate_early(self) -> None:
        self.rules = AstalonRules(self)

        self.starting_characters = []
        if self.options.randomize_characters == RandomizeCharacters.option_solo:
            self.starting_characters.append(self.random.choice(CHARACTERS))
        if self.options.randomize_characters == RandomizeCharacters.option_trio:
            self.starting_characters.extend(CHARACTERS[:3])
        if self.options.randomize_characters == RandomizeCharacters.option_all:
            self.starting_characters.extend(CHARACTERS)
        if self.options.randomize_characters == RandomizeCharacters.option_random_selection:
            for character in CHARACTERS:
                if self.random.randint(0, 1):
                    self.starting_characters.append(character)
            if not self.starting_characters:
                self.starting_characters.append(self.random.choice(CHARACTERS))
        if self.options.randomize_characters == RandomizeCharacters.option_algus:
            self.starting_characters.append(Character.ALGUS)
        if self.options.randomize_characters == RandomizeCharacters.option_arias:
            self.starting_characters.append(Character.ARIAS)
        if self.options.randomize_characters == RandomizeCharacters.option_kyuli:
            self.starting_characters.append(Character.KYULI)
        if self.options.randomize_characters == RandomizeCharacters.option_bram:
            self.starting_characters.append(Character.BRAM)
        if self.options.randomize_characters == RandomizeCharacters.option_zeek:
            self.starting_characters.append(Character.ZEEK)

        if self.options.goal == Goal.option_eye_hunt:
            self.required_gold_eyes = self.options.additional_eyes_required.value
            self.extra_gold_eyes = int(round(self.required_gold_eyes * (self.options.extra_eyes / 100)))

    def create_location(self, name: str) -> AstalonLocation:
        data = location_table[name]
        region = self.multiworld.get_region(data.region.value, self.player)
        location = AstalonLocation(self.player, name, location_name_to_id[name], region)
        region.locations.append(location)
        return location

    def create_regions(self) -> None:
        for region_name in astalon_regions:
            region = Region(region_name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in astalon_regions.items():
            region = self.multiworld.get_region(region_name.value, self.player)
            if region_data.exits:
                region.add_exits([e.value for e in region_data.exits])

        logic_groups = set(g.value for g in LocationGroup)
        for group, location_names in location_name_groups.items():
            if group not in logic_groups:
                continue
            if group == LocationGroup.CHARACTER:
                continue
            if group == LocationGroup.ITEM and not self.options.randomize_key_items:
                continue
            if group == LocationGroup.ATTACK and not self.options.randomize_attack_pickups:
                continue
            if group == LocationGroup.HEALTH and not self.options.randomize_health_pickups:
                continue
            if group == LocationGroup.KEY_WHITE and not self.options.randomize_white_keys:
                continue
            if group == LocationGroup.KEY_BLUE and not self.options.randomize_blue_keys:
                continue
            if group == LocationGroup.KEY_RED and not self.options.randomize_red_keys:
                continue
            if group == LocationGroup.SHOP and not self.options.randomize_shop:
                continue
            if group == LocationGroup.ELEVATOR and not self.options.randomize_elevator:
                continue
            if group == LocationGroup.SWITCH and not self.options.randomize_switches:
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
            self.create_event(Events.ZEEK, RegionName.MECH_ZEEK)
            self.create_event(Events.BRAM, RegionName.TR_BRAM)
        else:
            if Character.ALGUS not in self.starting_characters:
                self.create_location(LocationName.GT_ALGUS.value)
            if Character.ARIAS not in self.starting_characters:
                self.create_location(LocationName.GT_ARIAS.value)
            if Character.KYULI not in self.starting_characters:
                self.create_location(LocationName.GT_KYULI.value)
            if Character.ZEEK not in self.starting_characters:
                self.create_location(LocationName.MECH_ZEEK.value)
            if Character.BRAM not in self.starting_characters:
                self.create_location(LocationName.TR_BRAM.value)

        if not self.options.randomize_key_items:
            self.create_event(Events.EYE_RED, RegionName.GT_BOSS)
            self.create_event(Events.EYE_BLUE, RegionName.MECH_BOSS)
            self.create_event(Events.EYE_GREEN, RegionName.ROA_BOSS)
            self.create_event(Events.SWORD, RegionName.GT_SWORD)
            self.create_event(Events.ASCENDANT_KEY, RegionName.GT_ASCENDANT_KEY)
            self.create_event(Events.ADORNED_KEY, RegionName.TR_BOTTOM)
            self.create_event(Events.BANISH, RegionName.GT_LEFT)
            self.create_event(Events.VOID, RegionName.GT_VOID)
            self.create_event(Events.BOOTS, RegionName.MECH_BOOTS_UPPER)
            self.create_event(Events.CLOAK, RegionName.MECH_CLOAK)
            self.create_event(Events.CYCLOPS, RegionName.MECH_ZEEK)
            self.create_event(Events.BELL, RegionName.HOTP_BELL)
            self.create_event(Events.CLAW, RegionName.HOTP_CLAW)
            self.create_event(Events.GAUNTLET, RegionName.HOTP_GAUNTLET)
            self.create_event(Events.ICARUS, RegionName.ROA_ICARUS)
            self.create_event(Events.CHALICE, RegionName.APEX_CENTAUR)
            self.create_event(Events.BOW, RegionName.CATA_BOW)
            self.create_event(Events.CROWN, RegionName.CD_BOSS)
            self.create_event(Events.BLOCK, RegionName.CATH_TOP)
            self.create_event(Events.STAR, RegionName.SP_STAR)

        self.create_event(Events.VICTORY, RegionName.FINAL_BOSS)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(Events.VICTORY.value, self.player)

    def create_item(self, name: str) -> AstalonItem:
        item_data = item_table[name]
        classification: ItemClassification
        if callable(item_data.classification):
            classification = item_data.classification(self)
        else:
            classification = item_data.classification
        return AstalonItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: Events, region_name: RegionName) -> None:
        region = self.multiworld.get_region(region_name.value, self.player)
        location = AstalonLocation(self.player, event.value, None, region)
        location.place_locked_item(
            AstalonItem(event.value, ItemClassification.progression_skip_balancing, None, self.player)
        )
        region.locations.append(location)

    def create_items(self) -> None:
        itempool: List[Item] = []

        logic_groups = set(g.value for g in ItemGroup)
        for group, item_names in item_name_groups.items():
            if group not in logic_groups:
                continue
            if group == ItemGroup.CHARACTER:
                continue
            if group in {ItemGroup.EYE, ItemGroup.ITEM} and not self.options.randomize_key_items:
                continue
            if group == ItemGroup.ATTACK and not self.options.randomize_attack_pickups:
                continue
            if group == ItemGroup.HEALTH and not self.options.randomize_health_pickups:
                continue
            if group == ItemGroup.DOOR_WHITE and not self.options.randomize_white_keys:
                continue
            if group == ItemGroup.DOOR_BLUE and not self.options.randomize_blue_keys:
                continue
            if group == ItemGroup.DOOR_RED and not self.options.randomize_red_keys:
                continue
            if group == ItemGroup.SHOP and not self.options.randomize_shop:
                continue
            if group == ItemGroup.ELEVATOR and not self.options.randomize_elevator:
                continue
            if group == ItemGroup.SWITCH and not self.options.randomize_switches:
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
                    itempool.append(self.create_item(item_name))

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

        for _ in range(0, self.required_gold_eyes + self.extra_gold_eyes):
            itempool.append(self.create_item(Eye.GOLD.value))

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        if len(itempool) > total_locations:
            remove_count = len(itempool) - total_locations
            itempool = self.remove_filler(itempool, remove_count)

        while len(itempool) < total_locations:
            itempool.append(self.create_filler())

        self.multiworld.itempool += itempool

    def remove_filler(self, itempool: List[Item], count: int) -> List[Item]:
        new_pool = list(itempool)

        filler = [i for i in new_pool if i.classification == ItemClassification.filler]
        if len(filler) > count:
            filler = self.random.sample(filler, count)
        for f in filler:
            new_pool.remove(f)
            count -= 1
        if count <= 0:
            return new_pool

        useful = [i for i in new_pool if i.classification != ItemClassification.progression]
        if len(useful) < count:
            raise Exception(
                f"Astalon player #{self.player} failed: No space left for eye hunt. "
                "Lower your eye hunt goal or randomize more things."
            )
        if len(useful) > count:
            useful = self.random.sample(useful, count)
        for u in useful:
            new_pool.remove(u)
            count -= 1

        return new_pool

    def get_filler_item_name(self) -> str:
        items = list(filler_items)
        if not self.options.randomize_white_keys:
            items.append(Key.WHITE.value)
        if not self.options.randomize_blue_keys:
            items.append(Key.BLUE.value)
        if not self.options.randomize_red_keys:
            items.append(Key.RED.value)
        return self.random.choice(items)

    def set_rules(self) -> None:
        self.rules.set_region_rules()
        self.rules.set_location_rules()
        self.rules.set_indirect_conditions()

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

    def fill_slot_data(self) -> Dict[str, Any]:
        settings = self.options.as_dict(
            "campaign",
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
            "randomize_familiars",
            "randomize_orb_rocks",
            "randomize_miniboss_rewards",
            "skip_cutscenes",
            "apex_elevator",
            "cost_multiplier",
            "fast_blood_chalice",
            "campfire_warp",
            "allow_block_warping",
            "cheap_kyuli_ray",
            "always_restore_candles",
            "scale_character_stats",
            "death_link",
        )

        return {
            "settings": settings,
            "starting_characters": [c.value for c in self.starting_characters],
            "character_strengths": self._get_character_strengths(),
        }

    def _get_character_strengths(self) -> Dict[str, float]:
        character_strengths: Dict[str, float] = {c.value: 0 for c in CHARACTERS}
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
                if location.item and location.item.player == self.player and location.item.name in character_strengths:
                    scaling = (sphere_id + 1) / sphere_count
                    logger.debug(f"{location.item.name} in sphere {sphere_id+1} / {sphere_count}, scaling {scaling}")
                    character_strengths[location.item.name] = scaling
                    found += 1
                    if found >= limit:
                        return character_strengths

        logger.warning("Could not find all Astalon characters in spheres, something is likely wrong")
        return character_strengths

    def collect_item(self, state: "CollectionState", item: "Item", remove=False) -> Optional[str]:
        if item.advancement and getattr(self, "rules", None):
            self.rules.clear_cache()
        return super().collect_item(state, item, remove)
