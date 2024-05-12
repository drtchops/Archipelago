from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import TYPE_CHECKING, Callable, Dict, Set, Tuple, Union

from typing_extensions import TypeAlias

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import AstalonWorld


class ItemGroups(str, Enum):
    CHARACTER = "Characters"
    EYE = "Eyes"
    KEY = "Keys"
    ITEM = "Items"
    FAMILIAR = "Familiars"
    ATTACK = "Attack"
    HEALTH = "Health"
    ORBS = "Orbs"
    DOOR_WHITE = "White doors"
    DOOR_BLUE = "Blue doors"
    DOOR_RED = "Red doors"
    SHOP = "Shop upgrades"
    ELEVATOR = "Elevators"
    SWITCH = "Switches"


class Character(str, Enum):
    ARIAS = "Arias"
    KYULI = "Kyuli"
    ALGUS = "Algus"
    ZEEK = "Zeek"
    BRAM = "Bram"


class Eye(str, Enum):
    RED = "Gorgon Eye (Red)"
    BLUE = "Gorgon Eye (Blue)"
    GREEN = "Gorgon Eye (Green)"
    GOLD = "Gorgon Eye (Gold)"


class Key(str, Enum):
    WHITE = "White Key"
    BLUE = "Blue Key"
    RED = "Red Key"


class KeyItem(str, Enum):
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


class Familiar(str, Enum):
    MONSTER = "Monster Ball"
    GIL = "Gil"


class Upgrade(str, Enum):
    ATTACK_1 = "Attack +1"
    MAX_HP_1 = "Max HP +1"
    MAX_HP_2 = "Max HP +2"
    MAX_HP_3 = "Max HP +3"
    MAX_HP_4 = "Max HP +4"
    MAX_HP_5 = "Max HP +5"


class Orbs(str, Enum):
    ORBS_200 = "200 Orbs"
    ORBS_500 = "500 Orbs"
    ORBS_1000 = "1000 Orbs"


class WhiteDoor(str, Enum):
    GT_START = "GT White Door (1st Room)"
    GT_MAP = "GT White Door (Linus' Map)"
    GT_TAUROS = "GT White Door (Tauros)"
    MECH_2ND = "Mech White Door (2nd Room)"
    MECH_BK = "Mech White Door (Black Knight)"
    MECH_ARENA = "Mech White Door (Enemy Arena)"
    MECH_TOP = "Mech White Door (Top)"
    HOTP_START = "HotP White Door (1st Room)"
    HOTP_CLAW = "HotP White Door (Griffon Claw)"
    HOTP_BOSS = "HotP White Door (Boss)"
    ROA_WORMS = "RoA White Door (Worms)"
    ROA_ASCEND = "RoA White Door (Ascend)"
    ROA_BALLS = "RoA White Door (Spike Balls)"
    ROA_SPINNERS = "RoA White Door (Spike Spinners)"
    ROA_SKIP = "RoA White Door (Skippable)"
    CATA_TOP = "Cata White Door (Top)"
    CATA_BLUE = "Cata White Door (After Blue Door)"
    CATA_PRISON = "Cata White Door (Prison)"


class BlueDoor(str, Enum):
    GT_HUNTER = "GT Blue Door (Bestiary)"
    GT_RING = "GT Blue Door (Ring of the Ancients)"
    GT_ORBS = "GT Blue Door (Bonus Orbs)"
    GT_ASCENDANT = "GT Blue Door (Ascendant Key)"
    GT_SWORD = "GT Blue Door (Sword of Mirrors)"
    MECH_RED = "Mech Blue Door (Red Key)"
    MECH_SHORTCUT = "Mech Blue Door (Shortcut)"
    MECH_MUSIC = "Mech Blue Door (Music Test)"
    MECH_BOOTS = "Mech Blue Door (Talaria Boots)"
    MECH_VOID = "Mech Blue Door (Void Charm)"
    MECH_CD = "Mech Blue Door (Cyclops Den)"
    HOTP_START = "HotP Blue Door (Above Start)"
    HOTP_STATUE = "HotP Blue Door (Epimetheus)"
    HOTP_MAIDEN = "HotP Blue Door (Dead Maiden)"
    ROA_FLAMES = "RoA Blue Door (Flames)"
    ROA_BLOOD = "RoA Blue Door (Blood Pot)"
    APEX = "Apex Blue Door"
    CAVES = "Caves Blue Door"
    CATA_ORBS = "Cata Blue Door (Bonus Orbs)"
    CATA_SAVE = "Cata Blue Door (Checkpoint)"
    CATA_BOW = "Cata Blue Door (Lunarian Bow)"
    CATA_ROOTS = "Cata Blue Door (Poison Roots)"
    CATA_PRISON_CYCLOPS = "Cata Blue Door (Prison Cyclops)"
    CATA_PRISON_LEFT = "Cata Blue Door (Prison Left)"
    CATA_PRISON_RIGHT = "Cata Blue Door (Prison Right)"
    TR = "TR Blue Door"
    SP = "SP Blue Door"


class RedDoor(str, Enum):
    ZEEK = "Red Door (Zeek)"
    CATH = "Red Door (Cathedral)"
    SP = "Red Door (Serpent Path)"
    TR = "Red Door (Tower Roots)"
    DEV_ROOM = "Red Door (Dev Room)"


class ShopUpgrade(str, Enum):
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


class Elevator(str, Enum):
    GT_2 = "GT 2 Elevator"
    MECH_1 = "Mech 1 Elevator"
    MECH_2 = "Mech 2 Elevator"
    HOTP = "HotP Elevator"
    ROA_1 = "RoA 1 Elevator"
    ROA_2 = "RoA 2 Elevator"
    APEX = "Apex Elevator"
    CATA_1 = "Cata 1 Elevator"
    CATA_2 = "Cata 2 Elevator"
    TR = "TR Elevator"


class Switch(str, Enum):
    GT_2ND_ROOM = "GT Switch 2nd Room"
    GT_1ST_CYCLOPS = "GT Switch 1st Cyclops"
    GT_SPIKE_TUNNEL = "GT Switch Spike Tunnel"
    GT_BUTT_ACCESS = "GT Switch Butt Access"
    GT_GH = "GT Switch Gorgonheart"
    GT_UPPER_PATH_BLOCKS = "GT Switch Upper Path Blocks"
    GT_UPPER_PATH_ACCESS = "GT Switch Upper Path Access"
    GT_CROSSES = "GT Switch Crosses"
    GT_GH_SHORTCUT = "GT Switch GH Shortcut"
    GT_ARIAS = "GT Switch Arias"
    GT_SWORD_ACCESS = "GT Switch Sword Access"
    GT_SWORD_BACKTRACK = "GT Switch Sword Backtrack"
    GT_SWORD = "GT Switch Sword"
    GT_UPPER_ARIAS = "GT Switch Upper Arias"
    MECH_WATCHER = "Mech Switch Watcher"
    MECH_CHAINS = "Mech Switch Chains"
    MECH_BOSS_1 = "Mech Switch Boss 1"
    MECH_BOSS_2 = "Mech Switch Boss 2"
    MECH_SPLIT_PATH = "Mech Switch Split Path"
    MECH_SNAKE_1 = "Mech Switch Snake 1"
    MECH_BOOTS = "Mech Switch Boots"
    MECH_TO_UPPER_GT = "Mech Switch to Upper GT"
    MECH_UPPER_VOID_DROP = "Mech Switch Upper Void Drop"
    MECH_UPPER_VOID = "Mech Switch Upper Void"
    MECH_LINUS = "Mech Switch Linus"
    MECH_TO_BOSS_2 = "Mech Switch To Boss 2"
    MECH_POTS = "Mech Switch Pots"
    MECH_MAZE_BACKDOOR = "Mech Switch Maze Backdoor"
    MECH_TO_BOSS_1 = "Mech Switch To Boss 1"
    MECH_BLOCK_STAIRS = "Mech Switch Block Stairs"
    MECH_ARIAS_CYCLOPS = "Mech Switch Arias Cyclops"
    MECH_BOOTS_LOWER = "Mech Switch Boots Lower"
    MECH_CHAINS_GAP = "Mech Switch Chains Gap"
    MECH_LOWER_KEY = "Mech Switch Lower Key"
    MECH_ARIAS = "Mech Switch Arias"
    MECH_SNAKE_2 = "Mech Switch Snake 2"
    MECH_KEY_BLOCKS = "Mech Switch Key Blocks"
    MECH_CANNON = "Mech Switch Cannon"
    MECH_EYEBALL = "Mech Switch Eyeball"
    MECH_INVISIBLE = "Mech Switch Invisible"
    HOTP_ROCK = "HotP Switch Rock"
    HOTP_BELOW_START = "HotP Switch Below Start"
    HOTP_LEFT_2 = "HotP Switch Left 2"
    HOTP_LEFT_1 = "HotP Switch Left 1"
    HOTP_LOWER_SHORTCUT = "HotP Switch Lower Shortcut"
    HOTP_BELL = "HotP Switch Bell"
    HOTP_GHOST_BLOOD = "HotP Switch Ghost Blood"
    HOTP_TELEPORTS = "HotP Switch Teleports"
    HOTP_WORM_PILLAR = "HotP Switch Worm Pillar"
    HOTP_TO_CLAW_1 = "HotP Switch To Claw 1"
    HOTP_TO_CLAW_2 = "HotP Switch To Claw 2"
    HOTP_CLAW_ACCESS = "HotP Switch Claw Access"
    HOTP_GHOSTS = "HotP Switch Ghosts"
    HOTP_LEFT_3 = "HotP Switch Left 3"
    HOTP_ABOVE_OLD_MAN = "HotP Switch Above Old Man"
    HOTP_TO_ABOVE_OLD_MAN = "HotP Switch To Above Old Man"
    HOTP_TP_PUZZLE = "HotP Switch TP Puzzle"
    HOTP_EYEBALL_SHORTCUT = "HotP Switch Eyeball Shortcut"
    HOTP_BELL_ACCESS = "HotP Switch Bell Access"
    HOTP_1ST_ROOM = "HotP Switch 1st Room"
    HOTP_LEFT_BACKTRACK = "HotP Switch Left Backtrack"
    ROA_ASCEND = "RoA Switch Ascend"
    ROA_AFTER_WORMS = "RoA Switch After Worms"
    ROA_RIGHT_PATH = "RoA Switch Right Path"
    ROA_APEX_ACCESS = "RoA Switch Apex Access"
    ROA_ICARUS = "RoA Switch Icarus"
    ROA_SHAFT_L = "RoA Switch Shaft Left"
    ROA_SHAFT_R = "RoA Switch Shaft Right"
    ROA_ELEVATOR = "RoA Switch Elevator"
    ROA_SHAFT_DOWNWARDS = "RoA Switch Shaft Downwards"
    ROA_SPIDERS = "RoA Switch Spiders"
    ROA_DARK_ROOM = "RoA Switch Dark Room"
    ROA_ASCEND_SHORTCUT = "RoA Switch Ascend Shortcut"
    ROA_1ST_SHORTCUT = "RoA Switch 1st Shortcut"
    ROA_SPIKE_CLIMB = "RoA Switch Spike Climb"
    ROA_ABOVE_CENTAUR = "RoA Switch Above Centaur"
    ROA_BLOOD_POT = "RoA Switch Blood Pot"
    ROA_WORMS = "RoA Switch Worms"
    ROA_TRIPLE_1 = "RoA Switch Triple 1"
    ROA_TRIPLE_3 = "RoA Switch Triple 3"
    ROA_BABY_GORGON = "RoA Switch Baby Gorgon"
    ROA_BOSS_ACCESS = "RoA Switch Boss Access"
    ROA_BLOOD_POT_L = "RoA Switch Blood Pot Left"
    ROA_BLOOD_POT_R = "RoA Switch Blood Pot Right"
    ROA_LOWER_VOID = "RoA Switch Lower Void"
    DARKNESS = "Darkness Switch"
    APEX = "Apex Switch"
    CAVES_SKELETONS = "Caves Switch Skeletons"
    CAVES_CATA_1 = "Caves Switch Cata 1"
    CAVES_CATA_2 = "Caves Switch Cata 2"
    CAVES_CATA_3 = "Caves Switch Cata 3"
    CATA_ELEVATOR = "Cata Switch Elevator"
    CATA_VERTICAL_SHORTCUT = "Cata Switch Vertical Shortcut"
    CATA_TOP = "Cata Switch Top"
    CATA_CLAW_1 = "Cata Switch Claw 1"
    CATA_CLAW_2 = "Cata Switch Claw 2"
    CATA_WATER_1 = "Cata Switch Water 1"
    CATA_WATER_2 = "Cata Switch Water 2"
    CATA_DEV_ROOM = "Cata Switch Dev Room"
    CATA_AFTER_BLUE_DOOR = "Cata Switch After Blue Door"
    CATA_SHORTCUT_ACCESS = "Cata Switch Shortcut Access"
    CATA_LADDER_BLOCKS = "Cata Switch Ladder Blocks"
    CATA_MID_SHORTCUT = "Cata Switch Mid Shortcut"
    CATA_1ST_ROOM = "Cata Switch 1st Room"
    CATA_FLAMES_2 = "Cata Switch Flames 2"
    CATA_FLAMES_1 = "Cata Switch Flames 1"
    TR_ADORNED_L = "TR Switch Adorned Left"
    TR_ADORNED_M = "TR Switch Adorned Middle"
    TR_ADORNED_R = "TR Switch Adorned Right"
    TR_ELEVATOR = "TR Switch Elevator"
    TR_BOTTOM = "TR Switch Bottom"
    CD_1 = "CD Switch 1"
    CD_2 = "CD Switch 2"
    CD_3 = "CD Switch 3"
    CD_CAMPFIRE = "CD Switch Campfire"
    CD_TOP = "CD Switch Top"
    CATH_BOTTOM = "Cath Switch Bottom"
    CATH_BESIDE_SHAFT = "Cath Switch Beside Shaft"
    CATH_TOP_CAMPFIRE = "Cath Switch Top Campfire"
    SP_DOUBLE_DOORS = "SP Switch Double Doors"
    SP_BUBBLES = "SP Switch Bubbles"
    SP_AFTER_STAR = "SP Switch After Star"


class Crystal(str, Enum):
    GT_LADDER = "GT Crystal Ladder"
    GT_ROTA = "GT Crystal RotA"
    GT_OLD_MAN_1 = "GT Crystal Old Man 1"
    GT_OLD_MAN_2 = "GT Crystal Old Man 2"
    MECH_CANNON = "Mech Crystal Cannon"
    MECH_LINUS = "Mech Crystal Linus"
    MECH_LOWER = "Mech Crystal Lower"
    MECH_TO_BOSS_3 = "Mech Crystal To Boss 3"
    MECH_TRIPLE_1 = "Mech Crystal Triple 1"
    MECH_TRIPLE_2 = "Mech Crystal Triple 2"
    MECH_TRIPLE_3 = "Mech Crystal Triple 3"
    MECH_TOP = "Mech Crystal Top"
    MECH_CLOAK = "Mech Crystal Cloak"
    MECH_SLIMES = "Mech Crystal Slimes"
    MECH_TO_CD = "Mech Crystal To CD"
    MECH_CAMPFIRE = "Mech Crystal Campfire"
    MECH_1ST_ROOM = "Mech Crystal 1st Room"
    MECH_OLD_MAN = "Mech Crystal Old Man"
    MECH_TOP_CHAINS = "Mech Crystal Top Chains"
    MECH_BK = "Mech Crystal BK"
    HOTP_ROCK_ACCESS = "HotP Crystal Rock Access"
    HOTP_BOTTOM = "HotP Crystal Bottom"
    HOTP_LOWER = "HotP Crystal Lower"
    HOTP_AFTER_CLAW = "HotP Crystal After Claw"
    HOTP_MAIDEN_1 = "HotP Crystal Maiden 1"
    HOTP_MAIDEN_2 = "HotP Crystal Maiden 2"
    HOTP_BELL_ACCESS = "HotP Crystal Bell Access"
    HOTP_HEART = "HotP Crystal Heart"
    HOTP_BELOW_PUZZLE = "HotP Crystal Below Puzzle"
    ROA_1ST_ROOM = "RoA Crystal 1st Room"
    ROA_BABY_GORGON = "RoA Crystal Baby Gorgon"
    ROA_LADDER_R = "RoA Crystal Ladder Right"
    ROA_LADDER_L = "RoA Crystal Ladder Left"
    ROA_CENTAUR = "RoA Crystal Centaur"
    ROA_SPIKE_BALLS = "RoA Crystal Spike Balls"
    ROA_LEFT_ASCEND = "RoA Crystal Left Ascend"
    ROA_SHAFT = "RoA Crystal Shaft"
    ROA_BRANCH_R = "RoA Crystal Branch Right"
    ROA_BRANCH_L = "RoA Crystal Branch Left"
    ROA_3_REAPERS = "RoA Crystal 3 Reapers"
    ROA_TRIPLE_2 = "RoA Crystal Triple 2"
    CATA_POISON_ROOTS = "Cata Crystal Poison Roots"
    TR_GOLD = "TR Crystal Gold"
    TR_DARK_ARIAS = "TR Crystal Dark Arias"
    CD_BACKTRACK = "CD Crystal Backtrack"
    CD_START = "CD Crystal Start"
    CD_CAMPFIRE = "CD Crystal Campfire"
    CD_STEPS = "CD Crystal Steps"
    CATH_1ST_ROOM = "Cath Crystal 1st Room"
    CATH_SHAFT = "Cath Crystal Shaft"
    CATH_SPIKE_PIT = "Cath Crystal Spike Pit"
    CATH_TOP_L = "Cath Crystal Top Left"
    CATH_TOP_R = "Cath Crystal Top Right"
    CATH_SHAFT_ACCESS = "Cath Crystal Shaft Access"
    CATH_ORBS = "Cath Crystal Orbs"
    SP_BLOCKS = "SP Crystal Blocks"
    SP_STAR = "SP Crystal Star"


class Face(str, Enum):
    MECH_VOLANTIS = "Mech Face Volantis"
    HOTP_OLD_MAN = "HotP Face Old Man"
    ROA_SPIDERS = "RoA Face Spiders"
    ROA_BLUE_KEY = "RoA Face Blue Key"
    CAVES_1ST_ROOM = "Caves Face 1st Room"
    CATA_AFTER_BOW = "Cata Face After Bow"
    CATA_BOW = "Cata Face Bow"
    CATA_X4 = "Cata Face x4"
    CATA_CAMPFIRE = "Cata Face Campfire"
    CATA_DOUBLE_DOOR = "Cata Face Double Door"
    CATA_BOTTOM = "Cata Face Bottom"
    CATH_L = "Cath Face Left"
    CATH_R = "Cath Face Right"


AllItems: TypeAlias = Union[
    Character,
    Eye,
    Key,
    KeyItem,
    Familiar,
    Upgrade,
    Orbs,
    WhiteDoor,
    BlueDoor,
    RedDoor,
    ShopUpgrade,
    Elevator,
    Switch,
    Crystal,
    Face,
]


CHARACTERS: Tuple[Character, ...] = (
    Character.ALGUS,
    Character.ARIAS,
    Character.KYULI,
    Character.ZEEK,
    Character.BRAM,
)

EARLY_WHITE_DOORS: Tuple[WhiteDoor, ...] = (
    WhiteDoor.GT_START,
    WhiteDoor.GT_MAP,
    WhiteDoor.GT_TAUROS,
)

EARLY_BLUE_DOORS: Tuple[BlueDoor, ...] = (
    BlueDoor.GT_ASCENDANT,
    BlueDoor.CAVES,
)

EARLY_SWITCHES: Tuple[Switch, ...] = (
    Switch.GT_2ND_ROOM,
    Switch.GT_1ST_CYCLOPS,
    Switch.GT_SPIKE_TUNNEL,
    Switch.GT_BUTT_ACCESS,
    Switch.GT_GH,
    Switch.GT_ARIAS,
    Switch.CAVES_SKELETONS,
    Switch.CAVES_CATA_1,
    Switch.CAVES_CATA_2,
    Switch.CAVES_CATA_3,
)

EARLY_ITEMS: Set[AllItems] = set([*EARLY_WHITE_DOORS, *EARLY_BLUE_DOORS, *EARLY_SWITCHES])

QOL_ITEMS: Tuple[ShopUpgrade, ...] = (
    ShopUpgrade.KNOWLEDGE,
    ShopUpgrade.ORB_SEEKER,
    ShopUpgrade.TITANS_EGO,
    ShopUpgrade.MAP_REVEAL,
    ShopUpgrade.GIFT,
    ShopUpgrade.CARTOGRAPHER,
)


class AstalonItem(Item):
    game = "Astalon"


@dataclass(frozen=True)
class AstalonItemData:
    classification: Union[ItemClassification, Callable[["AstalonWorld"], ItemClassification]]
    quantity_in_item_pool: int
    group: ItemGroups


item_table: Dict[str, AstalonItemData] = {
    Eye.RED.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Eye.BLUE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Eye.GREEN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Key.WHITE.value: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Key.BLUE.value: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Key.RED.value: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    KeyItem.GORGONHEART.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItem.ANCIENTS_RING.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItem.MAIDEN_RING.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItem.SWORD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.MAP.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItem.ASCENDANT_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.ADORNED_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.BANISH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.BOOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.CLOAK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.BELL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.AMULET.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.ITEM),
    KeyItem.CLAW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.GAUNTLET.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.ICARUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.CHALICE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.BOW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.BLOCK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.STAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Upgrade.ATTACK_1.value: AstalonItemData(ItemClassification.useful, 12, ItemGroups.ATTACK),
    Upgrade.MAX_HP_1.value: AstalonItemData(ItemClassification.useful, 14, ItemGroups.HEALTH),
    Upgrade.MAX_HP_2.value: AstalonItemData(ItemClassification.useful, 10, ItemGroups.HEALTH),
    Upgrade.MAX_HP_3.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Upgrade.MAX_HP_4.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Upgrade.MAX_HP_5.value: AstalonItemData(ItemClassification.useful, 8, ItemGroups.HEALTH),
    Orbs.ORBS_200.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Orbs.ORBS_500.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Orbs.ORBS_1000.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    WhiteDoor.GT_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.GT_MAP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.GT_TAUROS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.MECH_2ND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.MECH_BK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.MECH_ARENA.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.MECH_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.HOTP_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.HOTP_CLAW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.HOTP_BOSS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.ROA_WORMS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.ROA_ASCEND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.ROA_BALLS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.ROA_SPINNERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.ROA_SKIP.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.CATA_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.CATA_BLUE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoor.CATA_PRISON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    BlueDoor.GT_HUNTER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.GT_RING.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.GT_ORBS.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.GT_ASCENDANT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.GT_SWORD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.MECH_RED.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.MECH_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.MECH_MUSIC.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.MECH_BOOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.MECH_VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.MECH_CD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.HOTP_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.HOTP_STATUE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.HOTP_MAIDEN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.ROA_FLAMES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.ROA_BLOOD.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.APEX.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CAVES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_ORBS.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_SAVE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_BOW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_ROOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_PRISON_CYCLOPS.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_PRISON_LEFT.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.CATA_PRISON_RIGHT.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.TR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoor.SP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    RedDoor.ZEEK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoor.CATH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoor.SP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoor.TR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoor.DEV_ROOM.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_RED),
    Character.ARIAS.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Character.KYULI.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Character.ALGUS.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Character.ZEEK.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Character.BRAM.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    ShopUpgrade.GIFT.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.KNOWLEDGE.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrade.MERCY.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.ORB_SEEKER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.MAP_REVEAL.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.SHOP),
    ShopUpgrade.CARTOGRAPHER.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrade.DEATH_ORB.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.DEATH_POINT.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrade.TITANS_EGO.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrade.ALGUS_ARCANIST.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrade.ALGUS_SHOCK.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.ALGUS_METEOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrade.ARIAS_GORGONSLAYER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.ARIAS_LAST_STAND.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.ARIAS_LIONHEART.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.KYULI_ASSASSIN.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.KYULI_BULLSEYE.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.KYULI_RAY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrade.ZEEK_JUNKYARD.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.ZEEK_ORBS.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.ZEEK_LOOT.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.BRAM_AXE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrade.BRAM_HUNTER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrade.BRAM_WHIPLASH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    Elevator.GT_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.MECH_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.MECH_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.HOTP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.ROA_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.ROA_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.APEX.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.CATA_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.CATA_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevator.TR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Switch.GT_2ND_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_1ST_CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_SPIKE_TUNNEL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_BUTT_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_GH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_UPPER_PATH_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_UPPER_PATH_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_CROSSES.value: AstalonItemData(
        lambda world: ItemClassification.filler if world.options.open_early_doors else ItemClassification.progression,
        1,
        ItemGroups.SWITCH,
    ),
    Switch.GT_GH_SHORTCUT.value: AstalonItemData(
        lambda world: ItemClassification.filler if world.options.open_early_doors else ItemClassification.progression,
        1,
        ItemGroups.SWITCH,
    ),
    Switch.GT_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_SWORD_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_SWORD_BACKTRACK.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.GT_SWORD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.GT_UPPER_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_WATCHER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_CHAINS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_BOSS_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_BOSS_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_SPLIT_PATH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_SNAKE_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_BOOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_TO_UPPER_GT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_UPPER_VOID_DROP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_UPPER_VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_LINUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_TO_BOSS_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_POTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_MAZE_BACKDOOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_TO_BOSS_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_BLOCK_STAIRS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_ARIAS_CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_BOOTS_LOWER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_CHAINS_GAP.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.MECH_LOWER_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_SNAKE_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_KEY_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_CANNON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_EYEBALL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.MECH_INVISIBLE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_ROCK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_BELOW_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_LEFT_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_LEFT_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_LOWER_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_BELL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_GHOST_BLOOD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_TELEPORTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_WORM_PILLAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_TO_CLAW_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_TO_CLAW_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_CLAW_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_GHOSTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_LEFT_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_ABOVE_OLD_MAN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_TO_ABOVE_OLD_MAN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_TP_PUZZLE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_EYEBALL_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_BELL_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.HOTP_LEFT_BACKTRACK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_ASCEND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_AFTER_WORMS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_RIGHT_PATH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_APEX_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_ICARUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_SHAFT_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_SHAFT_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_ELEVATOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_SHAFT_DOWNWARDS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_SPIDERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_DARK_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_ASCEND_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_1ST_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_SPIKE_CLIMB.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.ROA_ABOVE_CENTAUR.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.ROA_BLOOD_POT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_WORMS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_TRIPLE_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_TRIPLE_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_BABY_GORGON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_BOSS_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.ROA_BLOOD_POT_L.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.ROA_BLOOD_POT_R.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.ROA_LOWER_VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.DARKNESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.APEX.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.CAVES_SKELETONS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CAVES_CATA_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CAVES_CATA_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CAVES_CATA_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_ELEVATOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_VERTICAL_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_CLAW_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_CLAW_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_WATER_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_WATER_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_DEV_ROOM.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.CATA_AFTER_BLUE_DOOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_SHORTCUT_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_LADDER_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_MID_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_FLAMES_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATA_FLAMES_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.TR_ADORNED_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.TR_ADORNED_M.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.TR_ADORNED_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.TR_ELEVATOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.TR_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CD_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CD_2.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switch.CD_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CD_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CD_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATH_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATH_BESIDE_SHAFT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.CATH_TOP_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.SP_DOUBLE_DOORS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.SP_BUBBLES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switch.SP_AFTER_STAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.GT_LADDER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.GT_ROTA.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.GT_OLD_MAN_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.GT_OLD_MAN_2.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Crystal.MECH_CANNON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_LINUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_LOWER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_TO_BOSS_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_TRIPLE_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_TRIPLE_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_TRIPLE_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_CLOAK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_SLIMES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_TO_CD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.MECH_1ST_ROOM.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Crystal.MECH_OLD_MAN.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Crystal.MECH_TOP_CHAINS.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Crystal.MECH_BK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_ROCK_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_LOWER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_AFTER_CLAW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_MAIDEN_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_MAIDEN_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_BELL_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_HEART.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.HOTP_BELOW_PUZZLE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_BABY_GORGON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_LADDER_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_LADDER_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_CENTAUR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_SPIKE_BALLS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_LEFT_ASCEND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_SHAFT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_BRANCH_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_BRANCH_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_3_REAPERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.ROA_TRIPLE_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATA_POISON_ROOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.TR_GOLD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.TR_DARK_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CD_BACKTRACK.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Crystal.CD_START.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Crystal.CD_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CD_STEPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_SHAFT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_SPIKE_PIT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_TOP_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_TOP_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_SHAFT_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.CATH_ORBS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.SP_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Crystal.SP_STAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.MECH_VOLANTIS.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Face.HOTP_OLD_MAN.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Face.ROA_SPIDERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.ROA_BLUE_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CAVES_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATA_AFTER_BOW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATA_BOW.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Face.CATA_X4.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATA_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATA_DOUBLE_DOOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATA_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATH_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Face.CATH_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    KeyItem.CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItem.CROWN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Eye.GOLD.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.EYE),
    # Familiars.MONSTER.value: AstalonItemData(ItemClassification.useful, 3, ItemGroups.FAMILIAR),
    # Familiars.GIL.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.FAMILIAR),
}

base_id = 333000
item_name_to_id: Dict[str, int] = {name: base_id + i for i, name in enumerate(item_table)}


def get_item_group(item_name: str):
    return item_table[item_name].group


item_name_groups: Dict[str, Set[str]] = {
    group.value: set(item for item in item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

filler_items = list(item_name_groups[ItemGroups.ORBS.value])
