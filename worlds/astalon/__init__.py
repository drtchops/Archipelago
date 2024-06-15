from typing import Any, Dict, List

from BaseClasses import CollectionState, Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

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
    ItemGroups,
    Key,
    KeyItem,
    filler_items,
    item_name_groups,
    item_name_to_id,
    item_table,
)
from .locations import (
    AstalonLocation,
    LocationGroups,
    Locations,
    location_name_groups,
    location_name_to_id,
    location_table,
)
from .options import ApexElevator, AstalonOptions, Goal, RandomizeCharacters
from .regions import Regions, astalon_regions
from .rules import AstalonRules, Events

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
# ████░░░░██████████░███ hi_bubsette = 2
# ████████░░░░░░░░░░████


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

    game = "Astalon"
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

    def create_location(self, name: str):
        data = location_table[name]
        region = self.multiworld.get_region(data.region.value, self.player)
        location = AstalonLocation(self.player, name, location_name_to_id[name], region)
        region.locations.append(location)

    def create_regions(self) -> None:
        for region_name in astalon_regions:
            region = Region(region_name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in astalon_regions.items():
            region = self.multiworld.get_region(region_name.value, self.player)
            if exits:
                region.add_exits([e.value for e in exits])

        logic_groups = set(g.value for g in LocationGroups)
        for group, location_names in location_name_groups.items():
            if group not in logic_groups:
                continue
            if group == LocationGroups.CHARACTER:
                continue
            if group == LocationGroups.ITEM and not self.options.randomize_key_items:
                continue
            if group == LocationGroups.ATTACK and not self.options.randomize_attack_pickups:
                continue
            if group == LocationGroups.HEALTH and not self.options.randomize_health_pickups:
                continue
            if group == LocationGroups.KEY_WHITE and not self.options.randomize_white_keys:
                continue
            if group == LocationGroups.KEY_BLUE and not self.options.randomize_blue_keys:
                continue
            if group == LocationGroups.KEY_RED and not self.options.randomize_red_keys:
                continue
            if group == LocationGroups.SHOP and not self.options.randomize_shop:
                continue
            if group == LocationGroups.ELEVATOR and not self.options.randomize_elevator:
                continue
            if group == LocationGroups.SWITCH and not self.options.randomize_switches:
                continue

            for location_name in location_names:
                if location_name == Locations.SHOP_MAP_REVEAL:
                    # this requires way too much map completion
                    continue
                if (
                    location_name == Locations.APEX_ELEVATOR
                    and self.options.apex_elevator != ApexElevator.option_included
                ):
                    continue

                self.create_location(location_name)

        if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
            self.create_event(Events.ZEEK, Regions.MECH_ZEEK)
            self.create_event(Events.BRAM, Regions.TR_BRAM)
        else:
            if Character.ALGUS not in self.starting_characters:
                self.create_location(Locations.GT_ALGUS.value)
            if Character.ARIAS not in self.starting_characters:
                self.create_location(Locations.GT_ARIAS.value)
            if Character.KYULI not in self.starting_characters:
                self.create_location(Locations.GT_KYULI.value)
            if Character.ZEEK not in self.starting_characters:
                self.create_location(Locations.MECH_ZEEK.value)
            if Character.BRAM not in self.starting_characters:
                self.create_location(Locations.TR_BRAM.value)

        if not self.options.randomize_key_items:
            self.create_event(Events.EYE_RED, Regions.GT_BOSS)
            self.create_event(Events.EYE_BLUE, Regions.MECH_BOSS)
            self.create_event(Events.EYE_GREEN, Regions.ROA_BOSS)
            self.create_event(Events.SWORD, Regions.GT_SWORD)
            self.create_event(Events.ASCENDANT_KEY, Regions.GT_ASCENDANT_KEY)
            self.create_event(Events.ADORNED_KEY, Regions.TR_BOTTOM)
            self.create_event(Events.BANISH, Regions.GT_LEFT)
            self.create_event(Events.VOID, Regions.GT_VOID)
            self.create_event(Events.BOOTS, Regions.MECH_BOOTS_UPPER)
            self.create_event(Events.CLOAK, Regions.MECH_CLOAK)
            self.create_event(Events.CYCLOPS, Regions.MECH_ZEEK)
            self.create_event(Events.BELL, Regions.HOTP_BELL)
            self.create_event(Events.CLAW, Regions.HOTP_CLAW)
            self.create_event(Events.GAUNTLET, Regions.HOTP_GAUNTLET)
            self.create_event(Events.ICARUS, Regions.ROA_ICARUS)
            self.create_event(Events.CHALICE, Regions.APEX_CENTAUR)
            self.create_event(Events.BOW, Regions.CATA_BOW)
            self.create_event(Events.CROWN, Regions.CD_BOSS)
            self.create_event(Events.BLOCK, Regions.CATH_TOP)
            self.create_event(Events.STAR, Regions.SP_STAR)

        self.create_event(Events.VICTORY, Regions.FINAL_BOSS)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(Events.VICTORY.value, self.player)

    def create_item(self, name: str) -> AstalonItem:
        item_data = item_table[name]
        classification: ItemClassification
        if callable(item_data.classification):
            classification = item_data.classification(self)
        else:
            classification = item_data.classification
        return AstalonItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: Events, region_name: Regions) -> None:
        region = self.multiworld.get_region(region_name.value, self.player)
        location = AstalonLocation(self.player, event.value, None, region)
        location.place_locked_item(
            AstalonItem(event.value, ItemClassification.progression_skip_balancing, None, self.player)
        )
        region.locations.append(location)

    def create_items(self) -> None:
        itempool: List[Item] = []

        logic_groups = set(g.value for g in ItemGroups)
        for group, item_names in item_name_groups.items():
            if group not in logic_groups:
                continue
            if group == ItemGroups.CHARACTER:
                continue
            if group in {ItemGroups.EYE, ItemGroups.ITEM} and not self.options.randomize_key_items:
                continue
            if group == ItemGroups.ATTACK and not self.options.randomize_attack_pickups:
                continue
            if group == ItemGroups.HEALTH and not self.options.randomize_health_pickups:
                continue
            if group == ItemGroups.DOOR_WHITE and not self.options.randomize_white_keys:
                continue
            if group == ItemGroups.DOOR_BLUE and not self.options.randomize_blue_keys:
                continue
            if group == ItemGroups.DOOR_RED and not self.options.randomize_red_keys:
                continue
            if group == ItemGroups.SHOP and not self.options.randomize_shop:
                continue
            if group == ItemGroups.ELEVATOR and not self.options.randomize_elevator:
                continue
            if group == ItemGroups.SWITCH and not self.options.randomize_switches:
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

        if self.options.randomize_characters != RandomizeCharacters.option_vanilla:
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
            raise Exception("No space left for eye hunt. Lower your eye hunt goal or randomize more things.")
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

    def fill_slot_data(self) -> Dict[str, Any]:
        self.rules.clear_cache()

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
            "cheap_kyuli_ray",
            "death_link",
        )

        shop_items: Dict[str, Dict[str, Any]] = {}
        if self.options.randomize_shop:
            for location_name in location_name_groups[LocationGroups.SHOP.value]:
                if location_name == Locations.SHOP_MAP_REVEAL:
                    continue

                location = self.multiworld.get_location(location_name, self.player)
                item = location.item
                if item:
                    shop_items[location.name] = {
                        "id": item.code,
                        "name": item.name,
                        "player_name": self.multiworld.player_name.get(item.player),
                        "game": item.game,
                        "flags": item.flags,
                        "is_local": item.player == self.player,
                    }

        return {
            "settings": settings,
            "shop_items": shop_items,
            "starting_characters": [c.value for c in self.starting_characters],
        }

    def collect(self, state: "CollectionState", item: "Item"):
        if item.advancement:
            self.rules.clear_cache()
        return super().collect(state, item)
