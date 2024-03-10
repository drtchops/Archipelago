from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import TYPE_CHECKING, Callable, Union

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import AstalonWorld


class ItemGroups(str, Enum):
    NONE = ""
    CHARACTERS = "characters"
    EYES = "eyes"
    KEYS = "keys"
    ITEMS = "items"
    FAMILIARS = "familiars"
    ATTACK = "attack"
    HEALTH = "health"
    ORBS = "orbs"
    DOORS_RED = "red doors"


class Items(str, Enum):
    ARIAS = "Arias"
    KYULI = "Kyuli"
    ALGUS = "Algus"
    ZEEK = "Zeek"
    BRAM = "Bram"

    EYE_RED = "Gorgon Eye (Red)"
    EYE_BLUE = "Gorgon Eye (Blue)"
    EYE_GREEN = "Gorgon Eye (Green)"

    KEY_WHITE = "White Key"
    KEY_BLUE = "Blue Key"
    KEY_RED = "Red Key"

    GORGONHEART = "Gorgonheart"
    ANCIENTS_RING = "Ring of the Ancients"
    MAIDEN_RING = "Dead Maiden's Ring"
    SWORD = "Sword of Mirrors"
    MAP = "Linus' Map"
    ASCENDANT_KEY = "Ascendant Key"
    ADORNED_KEY = "Adorned Key"
    BANISH = "Banish Spell"
    VOID = "Void Charm"
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

    MONSTER = "Monster Ball"
    GIL = "Gil"

    ATTACK_1 = "Attack +1"
    MAX_HP_1 = "Max HP +1"
    MAX_HP_2 = "Max HP +2"
    MAX_HP_3 = "Max HP +3"
    MAX_HP_4 = "Max HP +4"
    MAX_HP_5 = "Max HP +5"
    ORBS_50 = "50 Orbs"
    ORBS_100 = "100 Orbs"
    ORBS_200 = "200 Orbs"

    DOOR_RED_ZEEK = "Red Door (Zeek)"
    DOOR_RED_CATH = "Red Door (Cathedral)"
    DOOR_RED_SP = "Red Door (Serpent Path)"
    DOOR_RED_TR = "Red Door (Tower Roots)"
    DOOR_RED_DEV_ROOM = "Red Door (Dev Room)"

    VICTORY = "Victory"


class AstalonItem(Item):
    game = "Astalon"


@dataclass
class AstalonItemData:
    classification: Union[ItemClassification, Callable[["AstalonWorld"], ItemClassification]]
    quantity_in_item_pool: int
    item_group: ItemGroups = ItemGroups.NONE


item_table: dict[Items, AstalonItemData] = {
    # Items.ARIAS: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    # Items.KYULI: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    # Items.ALGUS: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    # Items.ZEEK: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    # Items.BRAM: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    Items.EYE_RED: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYES),
    Items.EYE_BLUE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYES),
    Items.EYE_GREEN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYES),
    Items.KEY_WHITE: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEYS),
    Items.KEY_BLUE: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEYS),
    Items.KEY_RED: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEYS),
    Items.GORGONHEART: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEMS),
    Items.ANCIENTS_RING: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEMS),
    Items.MAIDEN_RING: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEMS),
    Items.SWORD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.MAP: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEMS),
    Items.ASCENDANT_KEY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.ADORNED_KEY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BANISH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.VOID: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BOOTS: AstalonItemData(ItemClassification.useful, 1, ItemGroups.ITEMS),
    Items.CLOAK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    # Items.CYCLOPS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BELL: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.AMULET: AstalonItemData(ItemClassification.useful, 1, ItemGroups.ITEMS),
    Items.CLAW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.GAUNTLET: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.ICARUS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.CHALICE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    # Items.CROWN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BLOCK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.STAR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    # Items.MONSTER: AstalonItemData(ItemClassification.progression, 3, ItemGroups.FAMILIARS),
    # Items.GIL: AstalonItemData(ItemClassification.filler, 1, ItemGroups.FAMILIARS),
    Items.ATTACK_1: AstalonItemData(ItemClassification.useful, 12, ItemGroups.ATTACK),
    Items.MAX_HP_1: AstalonItemData(ItemClassification.useful, 14, ItemGroups.HEALTH),
    Items.MAX_HP_2: AstalonItemData(ItemClassification.useful, 10, ItemGroups.HEALTH),
    Items.MAX_HP_3: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Items.MAX_HP_4: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Items.MAX_HP_5: AstalonItemData(ItemClassification.useful, 8, ItemGroups.HEALTH),
    Items.ORBS_50: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.ORBS_100: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.ORBS_200: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.DOOR_RED_ZEEK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    Items.DOOR_RED_CATH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    Items.DOOR_RED_SP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    Items.DOOR_RED_TR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    # progression if gil is a check
    Items.DOOR_RED_DEV_ROOM: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_RED),
}

base_id = 333000
item_name_to_id: dict[str, int] = {name.value: base_id + i for i, name in enumerate(item_table)}


def get_item_group(item_name: Items):
    return item_table[item_name].item_group


item_name_groups: dict[str, set[str]] = {
    group.value: set(item.value for item in item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items = list(item_name_groups[ItemGroups.ORBS.value])
