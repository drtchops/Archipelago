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
    "50 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
    "100 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
    "200 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
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
    # "Monster Ball": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Talaria Boots": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Cloak of Levitation": AstalonItemData(ItemClassification.progression, 1, "items"),
    # "Cyclops Idol": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Athena's Bell": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Amulet of Sol": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Griffon Claw": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Boreas Gauntlet": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Dead Maiden's Ring": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Icarus Emblem": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Blood Chalice": AstalonItemData(ItemClassification.useful, 1, "items"),
    "Lunarian Bow": AstalonItemData(ItemClassification.progression, 1, "items"),
    # "Gil": AstalonItemData(ItemClassification.filler, 1, "items"),
    "Adorned Key": AstalonItemData(ItemClassification.progression, 1, "items"),
    # "Prince's Crown": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Magic Block": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Morning Star": AstalonItemData(ItemClassification.progression, 1, "items"),
    "Attack +1": AstalonItemData(ItemClassification.useful, 12, "upgrades"),
    "Max HP +1": AstalonItemData(ItemClassification.useful, 14, "upgrades"),
    "Max HP +2": AstalonItemData(ItemClassification.useful, 9, "upgrades"),
    "Max HP +3": AstalonItemData(ItemClassification.useful, 1, "upgrades"),
    "Max HP +4": AstalonItemData(ItemClassification.useful, 1, "upgrades"),
    "Max HP +5": AstalonItemData(ItemClassification.useful, 8, "upgrades"),
}

item_name_to_id: dict[str, int] = {name: 1000 + i for i, name in enumerate(item_table)}


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: dict[str, set[str]] = {
    group: set(item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items = item_name_groups["orbs"]
