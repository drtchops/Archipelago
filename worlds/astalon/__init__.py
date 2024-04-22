from typing import Any, Dict, List

from BaseClasses import CollectionState, Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .Items import (
    CHARACTERS,
    EARLY_BLUE_DOORS,
    EARLY_ITEMS,
    EARLY_SWITCHES,
    EARLY_WHITE_DOORS,
    QOL_ITEMS,
    AstalonItem,
    Character,
    Elevator,
    ItemGroups,
    Key,
    filler_items,
    item_name_groups,
    item_name_to_id,
    item_table,
)
from .Locations import (
    AstalonLocation,
    LocationGroups,
    Locations,
    location_name_groups,
    location_name_to_id,
    location_table,
)
from .Options import AstalonOptions, RandomizeCharacters
from .Regions import Regions, astalon_regions
from .Rules import AstalonRules, Events


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
    game = "Astalon"
    web = AstalonWebWorld()
    options_dataclass = AstalonOptions
    options: AstalonOptions  # type: ignore
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    starting_characters: List[Character]
    location_count: int = 0
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

    def create_location(self, name: str):
        data = location_table[name]
        region = self.multiworld.get_region(data.region.value, self.player)
        location = AstalonLocation(self.player, name, location_name_to_id[name], region)
        region.locations.append(location)
        self.location_count += 1

    def create_regions(self) -> None:
        for region_name in astalon_regions:
            region = Region(region_name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in astalon_regions.items():
            region = self.multiworld.get_region(region_name.value, self.player)
            if exits:
                region.add_exits([e.value for e in exits])

        for group, location_names in location_name_groups.items():
            if group == LocationGroups.CHARACTER:
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
                if location_name == Locations.APEX_ELEVATOR and self.options.free_apex_elevator:
                    continue

                self.create_location(location_name)

        if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
            self.create_event(Events.MET_ZEEK, Regions.MECH_ZEEK)
            self.create_event(Events.ZEEK_JOINED, Regions.MECH_ZEEK)
            self.create_event(Events.BRAM_JOINED, Regions.TR_BRAM)
        else:
            if Character.ALGUS not in self.starting_characters:
                self.create_location(Locations.GT_ALGUS)
            if Character.ARIAS not in self.starting_characters:
                self.create_location(Locations.GT_ARIAS)
            if Character.KYULI not in self.starting_characters:
                self.create_location(Locations.GT_KYULI)
            if Character.ZEEK not in self.starting_characters:
                self.create_location(Locations.MECH_ZEEK)
            if Character.BRAM not in self.starting_characters:
                self.create_location(Locations.TR_BRAM)

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
        itempool = []

        for group, item_names in item_name_groups.items():
            if group == ItemGroups.CHARACTER:
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
                if self.options.open_early_doors and item_name in EARLY_ITEMS:
                    continue
                if self.options.free_apex_elevator and item_name == Elevator.APEX:
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

        while len(itempool) < self.location_count:
            itempool.append(self.create_item(self.get_filler_item_name()))
        self.multiworld.itempool += itempool

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
        settings = self.options.as_dict(
            # "campaign",
            "randomize_characters",
            "randomize_health_pickups",
            "randomize_attack_pickups",
            "randomize_white_keys",
            "randomize_blue_keys",
            "randomize_red_keys",
            "randomize_shop",
            "randomize_elevator",
            "randomize_switches",
            # "randomize_familiars",
            # "randomize_orb_crates",
            # "randomize_boss_orb_rewards",
            # "randomize_miniboss_orb_rewards",
            "skip_cutscenes",
            "free_apex_elevator",
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
