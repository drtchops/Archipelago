from itertools import groupby
from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class AstalonItem(Item):
    game = "Astalon"


class AstalonItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_group: str = ""


item_table: dict[str, AstalonItemData] = {
    "10 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
    "Gorgon Eye (Red)": AstalonItemData(ItemClassification.progression, 1, "eyes"),
    "Gorgon Eye (Blue)": AstalonItemData(ItemClassification.progression, 1, "eyes"),
    "Gorgon Eye (Green)": AstalonItemData(ItemClassification.progression, 1, "eyes"),
    "Gorgonheart": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Ring of the Ancients": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Sword of Mirrors": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Linus' Map": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Ascendant Key": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Banish Spell": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Void Charm": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Monster Ball": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Talaria Boots": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Cape of Levitation": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Cyclops Idol": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Athena's Bell": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Amulet of Sol": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Griffon Claw": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Boreas Gauntlet": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Dead Maiden's Ring": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Icarus Emblem": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Blood Chalice": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Lunarian Bow": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Gil": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Adorned Key": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Prince's Crown": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Magic Block": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Morning Star": AstalonItemData(ItemClassification.progression, 1, "items"),
}

item_name_to_id: dict[str, int] = {name: 1000 + i for i, name in enumerate(item_table)}

filler_items: list[str] = [
    name for name, data in item_table.items() if data.classification == ItemClassification.filler
]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: dict[str, set[str]] = {
    group: set(item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items = ["10 Orbs"]
