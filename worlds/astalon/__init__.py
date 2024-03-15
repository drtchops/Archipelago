from typing import Any

from BaseClasses import ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .Items import (
    AstalonItem,
    ItemGroups,
    Items,
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
from .Options import AstalonOptions
from .Regions import Regions, astalon_regions
from .Rules import AstalonRules


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
    options: AstalonOptions
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_regions(self) -> None:
        for name in astalon_regions:
            region = Region(name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for name, exits in astalon_regions.items():
            region = self.multiworld.get_region(name.value, self.player)
            region.add_exits(exits)

            for location_name in location_name_groups.get(name.value, []):
                data = location_table[Locations(location_name)]
                if data.item_group == LocationGroups.ATTACK and not self.options.randomize_attack_pickups:
                    continue
                if data.item_group == LocationGroups.HEALTH and not self.options.randomize_health_pickups:
                    continue
                # if data.item_group == LocationGroups.KEYS_WHITE and not self.options.randomize_white_keys:
                #     continue
                # if data.item_group == LocationGroups.KEYS_BLUE and not self.options.randomize_blue_keys:
                #     continue
                if data.item_group == LocationGroups.KEYS_RED and not self.options.randomize_red_keys:
                    continue

                location = AstalonLocation(
                    self.player,
                    location_name,
                    location_name_to_id[location_name],
                    region,
                )
                region.locations.append(location)

        final_boss = self.multiworld.get_region(Regions.BOSS.value, self.player)
        victory = AstalonLocation(self.player, Locations.VICTORY.value, None, final_boss)
        victory.place_locked_item(
            AstalonItem(Items.VICTORY.value, ItemClassification.progression_skip_balancing, None, self.player)
        )
        final_boss.locations.append(victory)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(Items.VICTORY.value, self.player)

    def create_item(self, name: str) -> AstalonItem:
        item_data = item_table[Items(name)]
        classification: ItemClassification
        if callable(item_data.classification):
            classification = item_data.classification(self)
        else:
            classification = item_data.classification
        return AstalonItem(name, classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        for name, data in item_table.items():
            if data.item_group == ItemGroups.ATTACK and not self.options.randomize_attack_pickups:
                continue
            if data.item_group == ItemGroups.HEALTH and not self.options.randomize_health_pickups:
                continue
            # if data.item_group == ItemGroups.DOORS_WHITE and not self.options.randomize_white_keys:
            #     continue
            # if data.item_group == ItemGroups.DOORS_BLUE and not self.options.randomize_blue_keys:
            #     continue
            if data.item_group == ItemGroups.DOORS_RED and not self.options.randomize_red_keys:
                continue

            for _ in range(0, data.quantity_in_item_pool):
                item = self.create_item(name.value)
                self.multiworld.itempool.append(item)

    def get_filler_item_name(self) -> str:
        items = list(filler_items) + [Items.KEY_WHITE.value, Items.KEY_BLUE.value]
        # if not self.options.randomize_white_keys:
        #     items.append(Items.KEY_WHITE.value)
        # if not self.options.randomize_blue_keys:
        #     items.append(Items.KEY_BLUE.value)
        if not self.options.randomize_red_keys:
            items.append(Items.KEY_RED.value)
        return self.multiworld.random.choice(items)

    def set_rules(self) -> None:
        rules = AstalonRules(self)
        rules.set_region_rules()
        rules.set_location_rules()

    def fill_slot_data(self) -> dict[str, Any]:
        settings = self.options.as_dict(
            # "campaign",
            "randomize_health_pickups",
            "randomize_attack_pickups",
            # "randomize_white_keys",
            # "randomize_blue_keys",
            "randomize_red_keys",
            # "randomize_familiars",
            "skip_cutscenes",
            "start_with_zeek",
            "start_with_bram",
            "start_with_qol",
            "free_apex_elevator",
            "cost_multiplier",
            "death_link",
        )
        return {
            "settings": settings,
            # TODO: return list of items in world so they can display in-game correctly?
        }
