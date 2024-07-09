from typing import List

from BaseClasses import Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .constants import GAME_NAME
from .items import ItemGroup, ToemItem, filler_items, item_name_groups, item_name_to_id, item_table
from .locations import LocationGroup, ToemLocation, location_name_groups, location_name_to_id, location_table
from .options import ToemOptions
from .regions import RegionName, toem_regions
from .rules import EventName, set_location_rules, set_region_rules


class ToemWebWorld(WebWorld):
    theme = "grassFlowers"
    tutorials = [
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up the TOEM randomizer.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["DrTChops"],
        )
    ]


class ToemWorld(World):
    game = GAME_NAME
    web = ToemWebWorld()
    options_dataclass = ToemOptions
    options: ToemOptions  # type: ignore
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def create_location(self, name: str) -> ToemLocation:
        data = location_table[name]
        region = self.get_region(data.region.value)
        location = ToemLocation(self.player, name, location_name_to_id[name], region)
        region.locations.append(location)
        return location

    def create_regions(self) -> None:
        for region_name in toem_regions:
            region = Region(region_name.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in toem_regions.items():
            region = self.get_region(region_name.value)
            if exits:
                region.add_exits([e.value for e in exits])

        for group, location_names in location_name_groups.items():
            if group == LocationGroup.QUEST:
                for location_name in location_names:
                    self.create_location(location_name)

        self.create_event(EventName.VICTORY, RegionName.MOUNTAIN_TOP)
        self.multiworld.completion_condition[self.player] = lambda state: (
            state.has(EventName.VICTORY.value, self.player)
        )

    def create_event(self, event: EventName, region_name: RegionName):
        item = ToemItem(event.value, ItemClassification.progression_skip_balancing, None, self.player)
        region = self.get_region(region_name.value)
        location = ToemLocation(self.player, event.value, None, region)
        location.place_locked_item(item)
        region.locations.append(location)

    def create_item(self, name: str) -> ToemItem:
        data = item_table[name]
        return ToemItem(name, data.classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        itempool: List[Item] = []

        for item_name, item_data in item_table.items():
            if item_data.group == ItemGroup.STAMP:
                for _ in range(item_data.quantity):
                    itempool.append(self.create_item(item_name))

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        while len(itempool) < total_locations:
            itempool.append(self.create_filler())

        self.multiworld.itempool += itempool

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)
