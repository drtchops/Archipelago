from dataclasses import dataclass
from enum import Enum
from itertools import groupby

from BaseClasses import Item, ItemClassification


class KeyItem(str, Enum):
    EYE_RED = "Gorgon Eye (Red)"
    EYE_BLUE = "Gorgon Eye (Blue)"
    EYE_GREEN = "Gorgon Eye (Green)"
    GORGONHEART = "Gorgonheart"
    RING_ANCIENTS = "Ring of the Ancients"
    RING_DEAD_MAIDEN = "Dead Maiden's Ring"
    SWORD = "Sword of Mirrors"
    MAP = "Linus' Map"
    KEY_ASCENDANT = "Ascendant Key"
    KEY_ADORNED = "Adorned Key"
    BANISH = "Banish Spell"
    VOID = "Void Charm"
    MONSTER = "Monster Ball"
    BOOTS = "Talaria Boots"
    CLOAK = "Cloak of Levitation"
    CYCLOPS = "Cyclops Idol"
    BELL = "Athena's Bell"
    AMULET = "Amulet of Sol"
    CLAW = "Griffon Claw"
    GAUNTLET = "Boreas Gauntlet"
    ICARUS = "Icarus Emblem"
    CHALICE = "Blood Chalice"
    BOW = "Lunarian Bow"
    CROWN = "Prince's Crown"
    BLOCK = "Magic Block"
    STAR = "Morning Star"


class AstalonItem(Item):
    game = "Astalon"


@dataclass
class AstalonItemData:
    classification: ItemClassification
    quantity_in_item_pool: int
    item_group: str = ""


item_table: dict[str, AstalonItemData] = {
    KeyItem.EYE_RED.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.EYE_BLUE.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.EYE_GREEN.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.GORGONHEART.value: AstalonItemData(ItemClassification.filler, 1, "items"),
    KeyItem.RING_ANCIENTS.value: AstalonItemData(ItemClassification.filler, 1, "items"),
    KeyItem.RING_DEAD_MAIDEN.value: AstalonItemData(ItemClassification.filler, 1, "items"),
    KeyItem.SWORD.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.MAP.value: AstalonItemData(ItemClassification.filler, 1, "items"),
    KeyItem.KEY_ASCENDANT.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.KEY_ADORNED.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.BANISH.value: AstalonItemData(ItemClassification.useful, 1, "items"),
    KeyItem.VOID.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    # KeyItem.MONSTER.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.BOOTS.value: AstalonItemData(ItemClassification.useful, 1, "items"),
    KeyItem.CLOAK.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    # KeyItem.CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.BELL.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.AMULET.value: AstalonItemData(ItemClassification.useful, 1, "items"),
    KeyItem.CLAW.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.GAUNTLET.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.ICARUS.value: AstalonItemData(ItemClassification.useful, 1, "items"),
    KeyItem.CHALICE.value: AstalonItemData(ItemClassification.useful, 1, "items"),
    KeyItem.BOW.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    # KeyItem.CROWN.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.BLOCK.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    KeyItem.STAR.value: AstalonItemData(ItemClassification.progression, 1, "items"),
    # "Gil": AstalonItemData(ItemClassification.filler, 1, "items"),
    "50 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
    "100 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
    "200 Orbs": AstalonItemData(ItemClassification.filler, 0, "orbs"),
    "Attack +1": AstalonItemData(ItemClassification.useful, 12, "attack"),
    "Max HP +1": AstalonItemData(ItemClassification.useful, 14, "health"),
    "Max HP +2": AstalonItemData(ItemClassification.useful, 10, "health"),
    "Max HP +3": AstalonItemData(ItemClassification.useful, 1, "health"),
    "Max HP +4": AstalonItemData(ItemClassification.useful, 1, "health"),
    "Max HP +5": AstalonItemData(ItemClassification.useful, 8, "health"),
}

base_id = 333000
item_name_to_id: dict[str, int] = {name: base_id + i for i, name in enumerate(item_table)}


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: dict[str, set[str]] = {
    group: set(item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items = list(item_name_groups["orbs"])
