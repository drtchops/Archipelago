from BaseClasses import ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .Items import (
    AstalonItem,
    filler_items,
    item_name_groups,
    item_name_to_id,
    item_table,
)
from .Locations import AstalonLocation, location_name_groups, location_name_to_id
from .Options import AstalonOptions
from .Regions import astalon_regions
from .Rules import set_location_rules, set_region_rules


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
            region = Region(name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for name, exits in astalon_regions.items():
            region = self.get_region(name)
            region.add_exits(exits)

            for location_name in location_name_groups.get(name, []):
                location = AstalonLocation(
                    self.player, location_name, location_name_to_id[location_name], region,
                )
                region.locations.append(location)

        final_boss = self.get_region("Final Boss")
        victory = AstalonLocation(self.player, "Victory", None, final_boss)
        victory.place_locked_item(
            AstalonItem("Victory", ItemClassification.progression_skip_balancing, None, self.player)
        )
        final_boss.locations.append(victory)
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "Victory", self.player
        )

    def create_item(self, name: str) -> AstalonItem:
        item_data = item_table[name]
        return AstalonItem(name, item_data.classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        for name, data in item_table.items():
            for _ in range(0, data.quantity_in_item_pool):
                item = self.create_item(name)
                self.multiworld.itempool.append(item)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(filler_items)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)
