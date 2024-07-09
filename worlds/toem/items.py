from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import Dict, List, Set

from BaseClasses import Item, ItemClassification

from .constants import BASE_ID, GAME_NAME


class ItemGroup(str, Enum):
    STAMP = "Stamp"


class ItemName(str, Enum):
    HOMELANDA_STAMP = "Homelanda Stamp"
    OAKLAVILLE_STAMP = "Oaklaville Stamp"
    STANHAMN_STAMP = "Stanhamn Stamp"
    LOGCITY_STAMP = "Logcity Stamp"
    KIIRUBERG_STAMP = "Kiiruberg Stamp"
    BASTO_STAMP = "Basto Stamp"

    FRAMES_FILTERS = "Frames & Filters"


class ToemItem(Item):
    game = GAME_NAME


@dataclass(frozen=True)
class ItemData:
    classification: ItemClassification
    quantity: int
    group: ItemGroup


item_table: Dict[str, ItemData] = {
    ItemName.HOMELANDA_STAMP.value: ItemData(ItemClassification.progression, 3, ItemGroup.STAMP),
    ItemName.OAKLAVILLE_STAMP.value: ItemData(ItemClassification.progression_skip_balancing, 15, ItemGroup.STAMP),
    ItemName.STANHAMN_STAMP.value: ItemData(ItemClassification.progression_skip_balancing, 16, ItemGroup.STAMP),
    ItemName.LOGCITY_STAMP.value: ItemData(ItemClassification.progression_skip_balancing, 18, ItemGroup.STAMP),
    ItemName.KIIRUBERG_STAMP.value: ItemData(ItemClassification.progression_skip_balancing, 13, ItemGroup.STAMP),
    # ItemName.BASTO_STAMP.value: ItemData(ItemClassification.progression_skip_balancing, 20, ItemGroup.STAMP),
}

item_name_to_id: Dict[str, int] = {name: BASE_ID + i for i, name in enumerate(item_table)}


def get_item_group(item_name: str):
    return item_table[item_name].group


item_name_groups: Dict[str, Set[str]] = {
    group.value: set(item for item in item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items: List[str] = list([ItemName.HOMELANDA_STAMP.value])
