from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import TYPE_CHECKING, Callable, Dict, Literal, Set, Tuple, Union

from typing_extensions import TypeAlias

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
    DOORS_WHITE = "white doors"
    DOORS_BLUE = "blue doors"
    DOORS_RED = "red doors"
    SHOP = "shop upgrades"
    SWITCHES = "switches"


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
    ORBS_200 = "200 Orbs"
    ORBS_500 = "500 Orbs"
    ORBS_1000 = "1000 Orbs"

    DOOR_WHITE_GT_START = "GT White Door (1st Room)"
    DOOR_WHITE_GT_MAP = "GT White Door (Linus' Map)"
    DOOR_WHITE_GT_TAUROS = "GT White Door (Tauros)"
    DOOR_WHITE_MECH_2ND = "Mech White Door (2nd Room)"
    DOOR_WHITE_MECH_BK = "Mech White Door (Black Knight)"
    DOOR_WHITE_MECH_ARENA = "Mech White Door (Enemy Arena)"
    DOOR_WHITE_MECH_TOP = "Mech White Door (Top)"
    DOOR_WHITE_HOTP_START = "HotP White Door (1st Room)"
    DOOR_WHITE_HOTP_CLAW = "HotP White Door (Griffon Claw)"
    DOOR_WHITE_HOTP_BOSS = "HotP White Door (Boss)"
    DOOR_WHITE_ROA_WORMS = "RoA White Door (Worms)"
    DOOR_WHITE_ROA_ASCEND = "RoA White Door (Ascend)"
    DOOR_WHITE_ROA_BALLS = "RoA White Door (Spike Balls)"
    DOOR_WHITE_ROA_SPINNERS = "RoA White Door (Spike Spinners)"
    DOOR_WHITE_ROA_SKIP = "RoA White Door (Skippable)"
    DOOR_WHITE_CATA_TOP = "Cata White Door (Top)"
    DOOR_WHITE_CATA_BLUE = "Cata White Door (After Blue Door)"
    DOOR_WHITE_CATA_PRISON = "Cata White Door (Prison)"

    DOOR_BLUE_GT_HUNTER = "GT Blue Door (Bestiary)"
    DOOR_BLUE_GT_RING = "GT Blue Door (Ring of the Ancients)"
    DOOR_BLUE_GT_ORBS = "GT Blue Door (Bonus Orbs)"
    DOOR_BLUE_GT_ASCENDANT = "GT Blue Door (Ascendant Key)"
    DOOR_BLUE_GT_SWORD = "GT Blue Door (Sword of Mirrors)"
    DOOR_BLUE_MECH_RED = "Mech Blue Door (Red Key)"
    DOOR_BLUE_MECH_SHORTCUT = "Mech Blue Door (Shortcut)"
    DOOR_BLUE_MECH_MUSIC = "Mech Blue Door (Music Test)"
    DOOR_BLUE_MECH_BOOTS = "Mech Blue Door (Talaria Boots)"
    DOOR_BLUE_MECH_VOID = "Mech Blue Door (Void Charm)"
    DOOR_BLUE_MECH_CD = "Mech Blue Door (Cyclops Den)"
    DOOR_BLUE_HOTP_START = "HotP Blue Door (Above Start)"
    DOOR_BLUE_HOTP_STATUE = "HotP Blue Door (Epimetheus)"
    DOOR_BLUE_HOTP_MAIDEN = "HotP Blue Door (Dead Maiden)"
    DOOR_BLUE_ROA_FLAMES = "RoA Blue Door (Flames)"
    DOOR_BLUE_ROA_BLOOD = "RoA Blue Door (Blood Pot)"
    DOOR_BLUE_APEX = "Apex Blue Door"
    DOOR_BLUE_CATA_START = "Cata Blue Door (Start)"
    DOOR_BLUE_CATA_ORBS = "Cata Blue Door (Bonus Orbs)"
    DOOR_BLUE_CATA_SAVE = "Cata Blue Door (Checkpoint)"
    DOOR_BLUE_CATA_BOW = "Cata Blue Door (Lunarian Bow)"
    DOOR_BLUE_CATA_ROOTS = "Cata Blue Door (Poison Roots)"
    DOOR_BLUE_CATA_PRISON_CYCLOPS = "Cata Blue Door (Prison Cyclops)"
    DOOR_BLUE_CATA_PRISON_LEFT = "Cata Blue Door (Prison Left)"
    DOOR_BLUE_CATA_PRISON_RIGHT = "Cata Blue Door (Prison Right)"
    DOOR_BLUE_TR = "TR Blue Door"
    DOOR_BLUE_SP = "SP Blue Door"

    DOOR_RED_ZEEK = "Red Door (Zeek)"
    DOOR_RED_CATH = "Red Door (Cathedral)"
    DOOR_RED_SP = "Red Door (Serpent Path)"
    DOOR_RED_TR = "Red Door (Tower Roots)"
    DOOR_RED_DEV_ROOM = "Red Door (Dev Room)"

    GIFT = "Gift"
    KNOWLEDGE = "Knowledge"
    MERCY = "Mercy"
    ORB_SEEKER = "Orb Seeker"
    MAP_REVEAL = "Map Reveal"
    CARTOGRAPHER = "Cartographer"
    DEATH_ORB = "Death Orb"
    DEATH_POINT = "Death Point"
    TITANS_EGO = "Titan's Ego"
    ALGUS_ARCANIST = "Algus's Arcanist"
    ALGUS_SHOCK = "Algus's Shock Field"
    ALGUS_METEOR = "Algus's Meteor Rain"
    ARIAS_GORGONSLAYER = "Arias's Gorgonslayer"
    ARIAS_LAST_STAND = "Arias's Last Stand"
    ARIAS_LIONHEART = "Arias's Lionheart"
    KYULI_ASSASSIN = "Kyuli's Assassin Strike"
    KYULI_BULLSEYE = "Kyuli's Bullseye"
    KYULI_RAY = "Kyuli's Shining Ray"
    ZEEK_JUNKYARD = "Zeek's Junkyard Hunt"
    ZEEK_ORBS = "Zeek's Orb Monger"
    ZEEK_LOOT = "Zeek's Bigger Loot"
    BRAM_AXE = "Bram's Golden Axe"
    BRAM_HUNTER = "Bram's Monster Hunter"
    BRAM_WHIPLASH = "Bram's Whiplash"

    VICTORY = "Victory"


Characters: TypeAlias = Literal[
    Items.ARIAS,
    Items.KYULI,
    Items.ALGUS,
    Items.ZEEK,
    Items.BRAM,
]

KeyItems: TypeAlias = Literal[
    Items.EYE_RED,
    Items.EYE_BLUE,
    Items.EYE_GREEN,
    Items.SWORD,
    Items.ASCENDANT_KEY,
    Items.ADORNED_KEY,
    Items.BANISH,
    Items.VOID,
    Items.BOOTS,
    Items.CLOAK,
    Items.CYCLOPS,
    Items.BELL,
    Items.CLAW,
    Items.GAUNTLET,
    Items.ICARUS,
    Items.CHALICE,
    Items.BOW,
    Items.CROWN,
    Items.BLOCK,
    Items.STAR,
]


WhiteDoors: TypeAlias = Literal[
    Items.DOOR_WHITE_GT_START,
    Items.DOOR_WHITE_GT_MAP,
    Items.DOOR_WHITE_GT_TAUROS,
    Items.DOOR_WHITE_MECH_2ND,
    Items.DOOR_WHITE_MECH_BK,
    Items.DOOR_WHITE_MECH_ARENA,
    Items.DOOR_WHITE_MECH_TOP,
    Items.DOOR_WHITE_HOTP_START,
    Items.DOOR_WHITE_HOTP_CLAW,
    Items.DOOR_WHITE_HOTP_BOSS,
    Items.DOOR_WHITE_ROA_WORMS,
    Items.DOOR_WHITE_ROA_ASCEND,
    Items.DOOR_WHITE_ROA_BALLS,
    Items.DOOR_WHITE_ROA_SPINNERS,
    Items.DOOR_WHITE_ROA_SKIP,
    Items.DOOR_WHITE_CATA_TOP,
    Items.DOOR_WHITE_CATA_BLUE,
    Items.DOOR_WHITE_CATA_PRISON,
]

BlueDoors: TypeAlias = Literal[
    Items.DOOR_BLUE_GT_HUNTER,
    Items.DOOR_BLUE_GT_RING,
    Items.DOOR_BLUE_GT_ORBS,
    Items.DOOR_BLUE_GT_ASCENDANT,
    Items.DOOR_BLUE_GT_SWORD,
    Items.DOOR_BLUE_MECH_RED,
    Items.DOOR_BLUE_MECH_SHORTCUT,
    Items.DOOR_BLUE_MECH_MUSIC,
    Items.DOOR_BLUE_MECH_BOOTS,
    Items.DOOR_BLUE_MECH_VOID,
    Items.DOOR_BLUE_MECH_CD,
    Items.DOOR_BLUE_HOTP_START,
    Items.DOOR_BLUE_HOTP_STATUE,
    Items.DOOR_BLUE_HOTP_MAIDEN,
    Items.DOOR_BLUE_ROA_FLAMES,
    Items.DOOR_BLUE_ROA_BLOOD,
    Items.DOOR_BLUE_APEX,
    Items.DOOR_BLUE_CATA_START,
    Items.DOOR_BLUE_CATA_ORBS,
    Items.DOOR_BLUE_CATA_SAVE,
    Items.DOOR_BLUE_CATA_BOW,
    Items.DOOR_BLUE_CATA_ROOTS,
    Items.DOOR_BLUE_CATA_PRISON_CYCLOPS,
    Items.DOOR_BLUE_CATA_PRISON_LEFT,
    Items.DOOR_BLUE_CATA_PRISON_RIGHT,
    Items.DOOR_BLUE_TR,
    Items.DOOR_BLUE_SP,
]

RedDoors: TypeAlias = Literal[
    Items.DOOR_RED_ZEEK,
    Items.DOOR_RED_CATH,
    Items.DOOR_RED_SP,
    Items.DOOR_RED_TR,
    Items.DOOR_RED_DEV_ROOM,
]

ShopUpgrades: TypeAlias = Literal[
    Items.GIFT,
    Items.KNOWLEDGE,
    Items.MERCY,
    Items.ORB_SEEKER,
    Items.MAP_REVEAL,
    Items.CARTOGRAPHER,
    Items.DEATH_ORB,
    Items.DEATH_POINT,
    Items.TITANS_EGO,
    Items.ALGUS_ARCANIST,
    Items.ALGUS_SHOCK,
    Items.ALGUS_METEOR,
    Items.ARIAS_GORGONSLAYER,
    Items.ARIAS_LAST_STAND,
    Items.ARIAS_LIONHEART,
    Items.KYULI_ASSASSIN,
    Items.KYULI_BULLSEYE,
    Items.KYULI_RAY,
    Items.ZEEK_JUNKYARD,
    Items.ZEEK_ORBS,
    Items.ZEEK_LOOT,
    Items.BRAM_AXE,
    Items.BRAM_HUNTER,
    Items.BRAM_WHIPLASH,
]

CHARACTERS: Tuple[Characters, ...] = (
    Items.ALGUS,
    Items.ARIAS,
    Items.KYULI,
    Items.ZEEK,
    Items.BRAM,
)

EARLY_WHITE_DOORS: Tuple[Items, ...] = (
    Items.DOOR_WHITE_GT_START,
    Items.DOOR_WHITE_GT_MAP,
    Items.DOOR_WHITE_GT_TAUROS,
)

EARLY_BLUE_DOORS: Tuple[Items, ...] = (
    Items.DOOR_BLUE_GT_ASCENDANT,
    Items.DOOR_BLUE_CATA_START,
)

QOL_ITEMS: Tuple[Items, ...] = (
    Items.KNOWLEDGE,
    Items.ORB_SEEKER,
    Items.TITANS_EGO,
    Items.MAP_REVEAL,
    Items.GIFT,
    Items.CARTOGRAPHER,
)


class AstalonItem(Item):
    game = "Astalon"


@dataclass
class AstalonItemData:
    classification: Union[ItemClassification, Callable[["AstalonWorld"], ItemClassification]]
    quantity_in_item_pool: int
    item_group: ItemGroups = ItemGroups.NONE


item_table: Dict[Items, AstalonItemData] = {
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
    Items.BOOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.CLOAK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BELL: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.AMULET: AstalonItemData(ItemClassification.useful, 1, ItemGroups.ITEMS),
    Items.CLAW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.GAUNTLET: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.ICARUS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.CHALICE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.BLOCK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.STAR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    Items.ATTACK_1: AstalonItemData(ItemClassification.useful, 12, ItemGroups.ATTACK),
    Items.MAX_HP_1: AstalonItemData(ItemClassification.useful, 14, ItemGroups.HEALTH),
    Items.MAX_HP_2: AstalonItemData(ItemClassification.useful, 10, ItemGroups.HEALTH),
    Items.MAX_HP_3: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Items.MAX_HP_4: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Items.MAX_HP_5: AstalonItemData(ItemClassification.useful, 8, ItemGroups.HEALTH),
    Items.ORBS_200: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.ORBS_500: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.ORBS_1000: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.DOOR_WHITE_GT_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_GT_MAP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_GT_TAUROS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_MECH_2ND: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_MECH_BK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_MECH_ARENA: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_MECH_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_HOTP_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_HOTP_CLAW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_HOTP_BOSS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_ROA_WORMS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_ROA_ASCEND: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_ROA_BALLS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_ROA_SPINNERS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_ROA_SKIP: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_CATA_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_CATA_BLUE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_WHITE_CATA_PRISON: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_WHITE),
    Items.DOOR_BLUE_GT_HUNTER: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_GT_RING: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_GT_ORBS: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_GT_ASCENDANT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_GT_SWORD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_MECH_RED: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_MECH_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_MECH_MUSIC: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_MECH_BOOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_MECH_VOID: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_MECH_CD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_HOTP_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_HOTP_STATUE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_HOTP_MAIDEN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_ROA_FLAMES: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_ROA_BLOOD: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_APEX: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_ORBS: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_SAVE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_ROOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_PRISON_CYCLOPS: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_PRISON_LEFT: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_CATA_PRISON_RIGHT: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_TR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_BLUE_SP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_BLUE),
    Items.DOOR_RED_ZEEK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    Items.DOOR_RED_CATH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    Items.DOOR_RED_SP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    Items.DOOR_RED_TR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOORS_RED),
    # progression if gil is a check
    Items.DOOR_RED_DEV_ROOM: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOORS_RED),
    Items.ARIAS: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    Items.KYULI: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    Items.ALGUS: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    Items.ZEEK: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    Items.BRAM: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTERS),
    Items.GIFT: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.KNOWLEDGE: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    Items.MERCY: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ORB_SEEKER: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.MAP_REVEAL: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    Items.CARTOGRAPHER: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    Items.DEATH_ORB: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.DEATH_POINT: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    Items.TITANS_EGO: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    Items.ALGUS_ARCANIST: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    Items.ALGUS_SHOCK: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ALGUS_METEOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    Items.ARIAS_GORGONSLAYER: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ARIAS_LAST_STAND: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ARIAS_LIONHEART: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.KYULI_ASSASSIN: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.KYULI_BULLSEYE: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.KYULI_RAY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    Items.ZEEK_JUNKYARD: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ZEEK_ORBS: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ZEEK_LOOT: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.BRAM_AXE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    Items.BRAM_HUNTER: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.BRAM_WHIPLASH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    # Items.CYCLOPS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    # Items.CROWN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEMS),
    # Items.MONSTER: AstalonItemData(ItemClassification.progression, 3, ItemGroups.FAMILIARS),
    # Items.GIL: AstalonItemData(ItemClassification.filler, 1, ItemGroups.FAMILIARS),
}

base_id = 333000
item_name_to_id: Dict[str, int] = {name.value: base_id + i for i, name in enumerate(item_table)}


def get_item_group(item_name: Items):
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group.value: set(item.value for item in item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items = list(item_name_groups[ItemGroups.ORBS.value])
