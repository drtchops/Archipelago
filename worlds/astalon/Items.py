from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import TYPE_CHECKING, Callable, Dict, Set, Tuple, Union

from typing_extensions import TypeAlias

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import AstalonWorld


class ItemGroups(str, Enum):
    CHARACTER = "characters"
    EYE = "eyes"
    KEY = "keys"
    ITEM = "items"
    FAMILIAR = "familiars"
    ATTACK = "attack"
    HEALTH = "health"
    ORBS = "orbs"
    DOOR_WHITE = "white doors"
    DOOR_BLUE = "blue doors"
    DOOR_RED = "red doors"
    SHOP = "shop upgrades"
    ELEVATOR = "elevators"
    SWITCH = "switches"


class Characters(str, Enum):
    ARIAS = "Arias"
    KYULI = "Kyuli"
    ALGUS = "Algus"
    ZEEK = "Zeek"
    BRAM = "Bram"


class Eyes(str, Enum):
    EYE_RED = "Gorgon Eye (Red)"
    EYE_BLUE = "Gorgon Eye (Blue)"
    EYE_GREEN = "Gorgon Eye (Green)"


class Keys(str, Enum):
    KEY_WHITE = "White Key"
    KEY_BLUE = "Blue Key"
    KEY_RED = "Red Key"


class KeyItems(str, Enum):
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


class Familiars(str, Enum):
    MONSTER = "Monster Ball"
    GIL = "Gil"


class Upgrades(str, Enum):
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


class WhiteDoors(str, Enum):
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


class BlueDoors(str, Enum):
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
    DOOR_BLUE_CAVES = "Caves Blue Door"
    DOOR_BLUE_CATA_ORBS = "Cata Blue Door (Bonus Orbs)"
    DOOR_BLUE_CATA_SAVE = "Cata Blue Door (Checkpoint)"
    DOOR_BLUE_CATA_BOW = "Cata Blue Door (Lunarian Bow)"
    DOOR_BLUE_CATA_ROOTS = "Cata Blue Door (Poison Roots)"
    DOOR_BLUE_CATA_PRISON_CYCLOPS = "Cata Blue Door (Prison Cyclops)"
    DOOR_BLUE_CATA_PRISON_LEFT = "Cata Blue Door (Prison Left)"
    DOOR_BLUE_CATA_PRISON_RIGHT = "Cata Blue Door (Prison Right)"
    DOOR_BLUE_TR = "TR Blue Door"
    DOOR_BLUE_SP = "SP Blue Door"


class RedDoors(str, Enum):
    DOOR_RED_ZEEK = "Red Door (Zeek)"
    DOOR_RED_CATH = "Red Door (Cathedral)"
    DOOR_RED_SP = "Red Door (Serpent Path)"
    DOOR_RED_TR = "Red Door (Tower Roots)"
    DOOR_RED_DEV_ROOM = "Red Door (Dev Room)"


class ShopUpgrades(str, Enum):
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


class Elevators(str, Enum):
    ELEVATOR_GT_2 = "GT 2 Elevator"
    ELEVATOR_MECH_1 = "Mech 1 Elevator"
    ELEVATOR_MECH_2 = "Mech 2 Elevator"
    ELEVATOR_HOTP = "HotP Elevator"
    ELEVATOR_ROA_1 = "RoA 1 Elevator"
    ELEVATOR_ROA_2 = "RoA 2 Elevator"
    ELEVATOR_APEX = "Apex Elevator"
    ELEVATOR_CATA_1 = "Cata 1 Elevator"
    ELEVATOR_CATA_2 = "Cata 2 Elevator"
    ELEVATOR_TR = "TR Elevator"


class Switches(str, Enum):
    SWITCH_GT_2ND_ROOM = "GT Switch 2nd Room"
    SWITCH_GT_1ST_CYCLOPS = "GT Switch 1st Cyclops"
    SWITCH_GT_SPIKE_TUNNEL = "GT Switch Spike Tunnel"
    SWITCH_GT_BUTT_ACCESS = "GT Switch Butt Access"
    SWITCH_GT_GH = "GT Switch Gorgonheart"
    SWITCH_GT_UPPER_PATH_BLOCKS = "GT Switch Upper Path Blocks"
    SWITCH_GT_UPPER_PATH_ACCESS = "GT Switch Upper Path Access"
    SWITCH_GT_CROSSES = "GT Switch Crosses"
    SWITCH_GT_GH_SHORTCUT = "GT Switch GH Shortcut"
    SWITCH_GT_ARIAS = "GT Switch Arias"
    SWITCH_GT_SWORD_ACCESS = "GT Switch Sword Access"
    SWITCH_GT_SWORD_BACKTRACK = "GT Switch Sword Backtrack"
    SWITCH_GT_SWORD = "GT Switch Sword"
    SWITCH_GT_UPPER_ARIAS = "GT Switch Upper Arias"
    SWITCH_MECH_WATCHER = "Mech Switch Watcher"
    SWITCH_MECH_CHAINS = "Mech Switch Chains"
    SWITCH_MECH_BOSS_1 = "Mech Switch Boss 1"
    SWITCH_MECH_BOSS_2 = "Mech Switch Boss 2"
    SWITCH_MECH_SPLIT_PATH = "Mech Switch Split Path"
    SWITCH_MECH_SNAKE_1 = "Mech Switch Snake 1"
    SWITCH_MECH_BOOTS = "Mech Switch Boots"
    SWITCH_MECH_TO_UPPER_GT = "Mech Switch to Upper GT"
    SWITCH_MECH_UPPER_VOID_DROP = "Mech Switch Upper Void Drop"
    SWITCH_MECH_UPPER_VOID = "Mech Switch Upper Void"
    SWITCH_MECH_LINUS = "Mech Switch Linus"
    SWITCH_MECH_TO_BOSS_2 = "Mech Switch To Boss 2"
    SWITCH_MECH_POTS = "Mech Switch Pots"
    SWITCH_MECH_MAZE_BACKDOOR = "Mech Switch Maze Backdoor"
    SWITCH_MECH_TO_BOSS_1 = "Mech Switch To Boss 1"
    SWITCH_MECH_BLOCK_STAIRS = "Mech Switch Block Stairs"
    SWITCH_MECH_ARIAS_CYCLOPS = "Mech Switch Arias Cyclops"
    SWITCH_MECH_BOOTS_LOWER = "Mech Switch Boots Lower"
    SWITCH_MECH_CHAINS_GAP = "Mech Switch Chains Gap"
    SWITCH_MECH_LOWER_KEY = "Mech Switch Lower Key"
    SWITCH_MECH_ARIAS = "Mech Switch Arias"
    SWITCH_MECH_SNAKE_2 = "Mech Switch Snake 2"
    SWITCH_MECH_KEY_BLOCKS = "Mech Switch Key Blocks"
    SWITCH_MECH_CANNON = "Mech Switch Cannon"
    SWITCH_MECH_EYEBALL = "Mech Switch Eyeball"
    SWITCH_MECH_INVISIBLE = "Mech Switch Invisible"
    SWITCH_HOTP_ROCK = "HotP Switch Rock"
    SWITCH_HOTP_BELOW_START = "HotP Switch Below Start"
    SWITCH_HOTP_LEFT_2 = "HotP Switch Left 2"
    SWITCH_HOTP_LEFT_1 = "HotP Switch Left 1"
    SWITCH_HOTP_LOWER_SHORTCUT = "HotP Switch Lower Shortcut"
    SWITCH_HOTP_BELL = "HotP Switch Bell"
    SWITCH_HOTP_GHOST_BLOOD = "HotP Switch Ghost Blood"
    SWITCH_HOTP_TELEPORTS = "HotP Switch Teleports"
    SWITCH_HOTP_WORM_PILLAR = "HotP Switch Worm Pillar"
    SWITCH_HOTP_TO_CLAW_1 = "HotP Switch To Claw 1"
    SWITCH_HOTP_TO_CLAW_2 = "HotP Switch To Claw 2"
    SWITCH_HOTP_CLAW_ACCESS = "HotP Switch Claw Access"
    SWITCH_HOTP_GHOSTS = "HotP Switch Ghosts"
    SWITCH_HOTP_LEFT_3 = "HotP Switch Left 3"
    SWITCH_HOTP_ABOVE_OLD_MAN = "HotP Switch Above Old Man"
    SWITCH_HOTP_TO_ABOVE_OLD_MAN = "HotP Switch To Above Old Man"
    SWITCH_HOTP_TP_PUZZLE = "HotP Switch TP Puzzle"
    SWITCH_HOTP_EYEBALL_SHORTCUT = "HotP Switch Eyeball Shortcut"
    SWITCH_HOTP_BELL_ACCESS = "HotP Switch Bell Access"
    SWITCH_HOTP_1ST_ROOM = "HotP Switch 1st Room"
    SWITCH_HOTP_LEFT_BACKTRACK = "HotP Switch Left Backtrack"
    SWITCH_ROA_ASCEND = "RoA Switch Ascend"
    SWITCH_ROA_AFTER_WORMS = "RoA Switch After Worms"
    SWITCH_ROA_RIGHT_PATH = "RoA Switch Right Path"
    SWITCH_ROA_APEX_ACCESS = "RoA Switch Apex Access"
    SWITCH_ROA_ICARUS = "RoA Switch Icarus"
    SWITCH_ROA_SHAFT_L = "RoA Switch Shaft Left"
    SWITCH_ROA_SHAFT_R = "RoA Switch Shaft Right"
    SWITCH_ROA_ELEVATOR = "RoA Switch Elevator"
    SWITCH_ROA_SHAFT_DOWNWARDS = "RoA Switch Shaft Downwards"
    SWITCH_ROA_SPIDERS = "RoA Switch Spiders"
    SWITCH_ROA_DARK_ROOM = "RoA Switch Dark Room"
    SWITCH_ROA_ASCEND_SHORTCUT = "RoA Switch Ascend Shortcut"
    SWITCH_ROA_1ST_SHORTCUT = "RoA Switch 1st Shortcut"
    SWITCH_ROA_SPIKE_CLIMB = "RoA Switch Spike Climb"
    SWITCH_ROA_ABOVE_CENTAUR = "RoA Switch Above Centaur"
    SWITCH_ROA_BLOOD_POT = "RoA Switch Blood Pot"
    SWITCH_ROA_WORMS = "RoA Switch Worms"
    SWITCH_ROA_TRIPLE_1 = "RoA Switch Triple 1"
    SWITCH_ROA_TRIPLE_3 = "RoA Switch Triple 3"
    SWITCH_ROA_BABY_GORGON = "RoA Switch Baby Gorgon"
    SWITCH_ROA_BOSS_ACCESS = "RoA Switch Boss Access"
    SWITCH_ROA_BLOOD_POT_L = "RoA Switch Blood Pot Left"
    SWITCH_ROA_BLOOD_POT_R = "RoA Switch Blood Pot Right"
    SWITCH_ROA_LOWER_VOID = "RoA Switch Lower Void"
    SWITCH_DARKNESS = "Darkness Switch"
    SWITCH_APEX = "Apex Switch"
    SWITCH_CAVES_SKELETONS = "Caves Switch Skeletons"
    SWITCH_CAVES_CATA_1 = "Caves Switch Cata 1"
    SWITCH_CAVES_CATA_2 = "Caves Switch Cata 2"
    SWITCH_CAVES_CATA_3 = "Caves Switch Cata 3"
    SWITCH_CATA_ELEVATOR = "Cata Switch Elevator"
    SWITCH_CATA_VERTICAL_SHORTCUT = "Cata Switch Vertical Shortcut"
    SWITCH_CATA_TOP = "Cata Switch Top"
    SWITCH_CATA_CLAW_1 = "Cata Switch Claw 1"
    SWITCH_CATA_CLAW_2 = "Cata Switch Claw 2"
    SWITCH_CATA_WATER_1 = "Cata Switch Water 1"
    SWITCH_CATA_WATER_2 = "Cata Switch Water 2"
    SWITCH_CATA_DEV_ROOM = "Cata Switch Dev Room"
    SWITCH_CATA_AFTER_BLUE_DOOR = "Cata Switch After Blue Door"
    SWITCH_CATA_SHORTCUT_ACCESS = "Cata Switch Shortcut Access"
    SWITCH_CATA_LADDER_BLOCKS = "Cata Switch Ladder Blocks"
    SWITCH_CATA_MID_SHORTCUT = "Cata Switch Mid Shortcut"
    SWITCH_CATA_1ST_ROOM = "Cata Switch 1st Room"
    SWITCH_CATA_FLAMES_2 = "Cata Switch Flames 2"
    SWITCH_CATA_FLAMES_1 = "Cata Switch Flames 1"
    SWITCH_TR_ADORNED_L = "TR Switch Adorned Left"
    SWITCH_TR_ADORNED_M = "TR Switch Adorned Middle"
    SWITCH_TR_ADORNED_R = "TR Switch Adorned Right"
    SWITCH_TR_ELEVATOR = "TR Switch Elevator"
    SWITCH_TR_BOTTOM = "TR Switch Bottom"
    SWITCH_CD_1 = "CD Switch 1"
    SWITCH_CD_2 = "CD Switch 2"
    SWITCH_CD_3 = "CD Switch 3"
    SWITCH_CD_CAMPFIRE = "CD Switch Campfire"
    SWITCH_CD_TOP = "CD Switch Top"
    SWITCH_CATH_BOTTOM = "Cath Switch Bottom"
    SWITCH_CATH_BESIDE_SHAFT = "Cath Switch Beside Shaft"
    SWITCH_CATH_TOP_CAMPFIRE = "Cath Switch Top Campfire"
    SWITCH_SP_DOUBLE_DOORS = "SP Switch Double Doors"
    SWITCH_SP_BUBBLES = "SP Switch Bubbles"
    SWITCH_SP_AFTER_STAR = "SP Switch After Star"

    CRYSTAL_GT_LADDER = "GT Crystal Ladder"
    CRYSTAL_GT_ROTA = "GT Crystal RotA"
    CRYSTAL_GT_OLD_MAN_1 = "GT Crystal Old Man 1"
    CRYSTAL_GT_OLD_MAN_2 = "GT Crystal Old Man 2"
    CRYSTAL_MECH_CANNON = "Mech Crystal Cannon"
    CRYSTAL_MECH_LINUS = "Mech Crystal Linus"
    CRYSTAL_MECH_LOWER = "Mech Crystal Lower"
    CRYSTAL_MECH_TO_BOSS_3 = "Mech Crystal To Boss 3"
    CRYSTAL_MECH_TRIPLE_1 = "Mech Crystal Triple 1"
    CRYSTAL_MECH_TRIPLE_2 = "Mech Crystal Triple 2"
    CRYSTAL_MECH_TRIPLE_3 = "Mech Crystal Triple 3"
    CRYSTAL_MECH_TOP = "Mech Crystal Top"
    CRYSTAL_MECH_CLOAK = "Mech Crystal Cloak"
    CRYSTAL_MECH_SLIMES = "Mech Crystal Slimes"
    CRYSTAL_MECH_TO_CD = "Mech Crystal To CD"
    CRYSTAL_MECH_CAMPFIRE = "Mech Crystal Campfire"
    CRYSTAL_MECH_1ST_ROOM = "Mech Crystal 1st Room"
    CRYSTAL_MECH_OLD_MAN = "Mech Crystal Old Man"
    CRYSTAL_MECH_TOP_CHAINS = "Mech Crystal Top Chains"
    CRYSTAL_MECH_BK = "Mech Crystal BK"
    CRYSTAL_HOTP_ROCK_ACCESS = "HotP Crystal Rock Access"
    CRYSTAL_HOTP_BOTTOM = "HotP Crystal Bottom"
    CRYSTAL_HOTP_LOWER = "HotP Crystal Lower"
    CRYSTAL_HOTP_AFTER_CLAW = "HotP Crystal After Claw"
    CRYSTAL_HOTP_MAIDEN_1 = "HotP Crystal Maiden 1"
    CRYSTAL_HOTP_MAIDEN_2 = "HotP Crystal Maiden 2"
    CRYSTAL_HOTP_BELL_ACCESS = "HotP Crystal Bell Access"
    CRYSTAL_HOTP_HEART = "HotP Crystal Heart"
    CRYSTAL_HOTP_BELOW_PUZZLE = "HotP Crystal Below Puzzle"
    CRYSTAL_ROA_1ST_ROOM = "RoA Crystal 1st Room"
    CRYSTAL_ROA_BABY_GORGON = "RoA Crystal Baby Gorgon"
    CRYSTAL_ROA_LADDER_R = "RoA Crystal Ladder Right"
    CRYSTAL_ROA_LADDER_L = "RoA Crystal Ladder Left"
    CRYSTAL_ROA_CENTAUR = "RoA Crystal Centaur"
    CRYSTAL_ROA_SPIKE_BALLS = "RoA Crystal Spike Balls"
    CRYSTAL_ROA_LEFT_ASCEND = "RoA Crystal Left Ascend"
    CRYSTAL_ROA_SHAFT = "RoA Crystal Shaft"
    CRYSTAL_ROA_BRANCH_R = "RoA Crystal Branch Right"
    CRYSTAL_ROA_BRANCH_L = "RoA Crystal Branch Left"
    CRYSTAL_ROA_3_REAPERS = "RoA Crystal 3 Reapers"
    CRYSTAL_ROA_TRIPLE_2 = "RoA Crystal Triple 2"
    CRYSTAL_CATA_POISON_ROOTS = "Cata Crystal Poison Roots"
    CRYSTAL_TR_GOLD = "TR Crystal Gold"
    CRYSTAL_TR_DARK_ARIAS = "TR Crystal Dark Arias"
    CRYSTAL_CD_BACKTRACK = "CD Crystal Backtrack"
    CRYSTAL_CD_START = "CD Crystal Start"
    CRYSTAL_CD_CAMPFIRE = "CD Crystal Campfire"
    CRYSTAL_CD_STEPS = "CD Crystal Steps"
    CRYSTAL_CATH_1ST_ROOM = "Cath Crystal 1st Room"
    CRYSTAL_CATH_SHAFT = "Cath Crystal Shaft"
    CRYSTAL_CATH_SPIKE_PIT = "Cath Crystal Spike Pit"
    CRYSTAL_CATH_TOP_L = "Cath Crystal Top Left"
    CRYSTAL_CATH_TOP_R = "Cath Crystal Top Right"
    CRYSTAL_CATH_SHAFT_ACCESS = "Cath Crystal Shaft Access"
    CRYSTAL_CATH_ORBS = "Cath Crystal Orbs"
    CRYSTAL_SP_BLOCKS = "SP Crystal Blocks"
    CRYSTAL_SP_STAR = "SP Crystal Star"

    FACE_MECH_VOLANTIS = "Mech Face Volantis"
    FACE_HOTP_OLD_MAN = "HotP Face Old Man"
    FACE_ROA_SPIDERS = "RoA Face Spiders"
    FACE_ROA_BLUE_KEY = "RoA Face Blue Key"
    FACE_CAVES_1ST_ROOM = "Caves Face 1st Room"
    FACE_CATA_AFTER_BOW = "Cata Face After Bow"
    FACE_CATA_BOW = "Cata Face Bow"
    FACE_CATA_X4 = "Cata Face x4"
    FACE_CATA_CAMPFIRE = "Cata Face Campfire"
    FACE_CATA_DOUBLE_DOOR = "Cata Face Double Door"
    FACE_CATA_BOTTOM = "Cata Face Bottom"
    FACE_CATH_L = "Cath Face Left"
    FACE_CATH_R = "Cath Face Right"


Items: TypeAlias = Union[
    Characters,
    Eyes,
    Keys,
    KeyItems,
    Familiars,
    Upgrades,
    Orbs,
    WhiteDoors,
    BlueDoors,
    RedDoors,
    ShopUpgrades,
    Elevators,
    Switches,
]


CHARACTERS: Tuple[Characters, ...] = (
    Characters.ALGUS,
    Characters.ARIAS,
    Characters.KYULI,
    Characters.ZEEK,
    Characters.BRAM,
)

EARLY_WHITE_DOORS: Tuple[WhiteDoors, ...] = (
    WhiteDoors.DOOR_WHITE_GT_START,
    WhiteDoors.DOOR_WHITE_GT_MAP,
    WhiteDoors.DOOR_WHITE_GT_TAUROS,
)

EARLY_BLUE_DOORS: Tuple[BlueDoors, ...] = (
    BlueDoors.DOOR_BLUE_GT_ASCENDANT,
    BlueDoors.DOOR_BLUE_CAVES,
)

EARLY_SWITCHES: Tuple[Switches, ...] = (
    Switches.SWITCH_GT_2ND_ROOM,
    Switches.SWITCH_GT_1ST_CYCLOPS,
    Switches.SWITCH_GT_SPIKE_TUNNEL,
    Switches.SWITCH_GT_BUTT_ACCESS,
    Switches.SWITCH_GT_GH,
    Switches.SWITCH_GT_ARIAS,
    Switches.SWITCH_CAVES_SKELETONS,
    Switches.SWITCH_CAVES_CATA_1,
    Switches.SWITCH_CAVES_CATA_2,
    Switches.SWITCH_CAVES_CATA_3,
)

EARLY_ITEMS: Set[Items] = set([*EARLY_WHITE_DOORS, *EARLY_BLUE_DOORS, *EARLY_SWITCHES])

QOL_ITEMS: Tuple[ShopUpgrades, ...] = (
    ShopUpgrades.KNOWLEDGE,
    ShopUpgrades.ORB_SEEKER,
    ShopUpgrades.TITANS_EGO,
    ShopUpgrades.MAP_REVEAL,
    ShopUpgrades.GIFT,
    ShopUpgrades.CARTOGRAPHER,
)


class AstalonItem(Item):
    game = "Astalon"


@dataclass(frozen=True)
class AstalonItemData:
    classification: Union[ItemClassification, Callable[["AstalonWorld"], ItemClassification]]
    quantity_in_item_pool: int
    group: ItemGroups


item_table: Dict[str, AstalonItemData] = {
    Eyes.EYE_RED.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Eyes.EYE_BLUE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Eyes.EYE_GREEN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Keys.KEY_WHITE.value: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Keys.KEY_BLUE.value: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Keys.KEY_RED.value: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    KeyItems.GORGONHEART.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItems.ANCIENTS_RING.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItems.MAIDEN_RING.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItems.SWORD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.MAP.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    KeyItems.ASCENDANT_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.ADORNED_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.BANISH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.BOOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.CLOAK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.BELL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.AMULET.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.ITEM),
    KeyItems.CLAW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.GAUNTLET.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.ICARUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.CHALICE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.BOW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.BLOCK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.STAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Upgrades.ATTACK_1.value: AstalonItemData(ItemClassification.useful, 12, ItemGroups.ATTACK),
    Upgrades.MAX_HP_1.value: AstalonItemData(ItemClassification.useful, 14, ItemGroups.HEALTH),
    Upgrades.MAX_HP_2.value: AstalonItemData(ItemClassification.useful, 10, ItemGroups.HEALTH),
    Upgrades.MAX_HP_3.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Upgrades.MAX_HP_4.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Upgrades.MAX_HP_5.value: AstalonItemData(ItemClassification.useful, 8, ItemGroups.HEALTH),
    Orbs.ORBS_200.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Orbs.ORBS_500.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Orbs.ORBS_1000.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    WhiteDoors.DOOR_WHITE_GT_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_GT_MAP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_GT_TAUROS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_MECH_2ND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_MECH_BK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_MECH_ARENA.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_MECH_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_HOTP_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_HOTP_CLAW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_HOTP_BOSS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_ROA_WORMS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_ROA_ASCEND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_ROA_BALLS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_ROA_SPINNERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_ROA_SKIP.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_CATA_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_CATA_BLUE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    WhiteDoors.DOOR_WHITE_CATA_PRISON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    BlueDoors.DOOR_BLUE_GT_HUNTER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_GT_RING.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_GT_ORBS.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_GT_ASCENDANT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_GT_SWORD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_MECH_RED.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_MECH_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_MECH_MUSIC.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_MECH_BOOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_MECH_VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_MECH_CD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_HOTP_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_HOTP_STATUE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_HOTP_MAIDEN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_ROA_FLAMES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_ROA_BLOOD.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_APEX.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CAVES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_ORBS.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_SAVE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_BOW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_ROOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_PRISON_CYCLOPS.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_PRISON_LEFT.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_CATA_PRISON_RIGHT.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_TR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    BlueDoors.DOOR_BLUE_SP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    RedDoors.DOOR_RED_ZEEK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoors.DOOR_RED_CATH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoors.DOOR_RED_SP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoors.DOOR_RED_TR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    RedDoors.DOOR_RED_DEV_ROOM.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_RED),
    Characters.ARIAS.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Characters.KYULI.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Characters.ALGUS.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Characters.ZEEK.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Characters.BRAM.value: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    ShopUpgrades.GIFT.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.KNOWLEDGE.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrades.MERCY.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.ORB_SEEKER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.MAP_REVEAL.value: AstalonItemData(ItemClassification.filler, 0, ItemGroups.SHOP),
    ShopUpgrades.CARTOGRAPHER.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrades.DEATH_ORB.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.DEATH_POINT.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrades.TITANS_EGO.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    ShopUpgrades.ALGUS_ARCANIST.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrades.ALGUS_SHOCK.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.ALGUS_METEOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrades.ARIAS_GORGONSLAYER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.ARIAS_LAST_STAND.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.ARIAS_LIONHEART.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.KYULI_ASSASSIN.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.KYULI_BULLSEYE.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.KYULI_RAY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrades.ZEEK_JUNKYARD.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.ZEEK_ORBS.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.ZEEK_LOOT.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.BRAM_AXE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    ShopUpgrades.BRAM_HUNTER.value: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    ShopUpgrades.BRAM_WHIPLASH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SHOP),
    Elevators.ELEVATOR_GT_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_MECH_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_MECH_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_HOTP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_ROA_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_ROA_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_APEX.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_CATA_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_CATA_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Elevators.ELEVATOR_TR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Switches.SWITCH_GT_2ND_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_1ST_CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_SPIKE_TUNNEL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_BUTT_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_GH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_UPPER_PATH_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_UPPER_PATH_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_CROSSES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_GH_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_SWORD_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_SWORD_BACKTRACK.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_SWORD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_GT_UPPER_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_WATCHER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_CHAINS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_BOSS_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_BOSS_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_SPLIT_PATH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_SNAKE_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_BOOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_TO_UPPER_GT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_UPPER_VOID_DROP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_UPPER_VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_LINUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_TO_BOSS_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_POTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_MAZE_BACKDOOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_TO_BOSS_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_BLOCK_STAIRS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_ARIAS_CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_BOOTS_LOWER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_CHAINS_GAP.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_LOWER_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_SNAKE_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_KEY_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_CANNON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_EYEBALL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_MECH_INVISIBLE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_ROCK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_BELOW_START.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_LEFT_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_LEFT_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_LOWER_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_BELL.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_GHOST_BLOOD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_TELEPORTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_WORM_PILLAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_TO_CLAW_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_TO_CLAW_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_CLAW_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_GHOSTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_LEFT_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_ABOVE_OLD_MAN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_TO_ABOVE_OLD_MAN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_TP_PUZZLE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_EYEBALL_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_BELL_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_HOTP_LEFT_BACKTRACK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_ASCEND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_AFTER_WORMS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_RIGHT_PATH.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_APEX_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_ICARUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_SHAFT_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_SHAFT_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_ELEVATOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_SHAFT_DOWNWARDS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_SPIDERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_DARK_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_ASCEND_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_1ST_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_SPIKE_CLIMB.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_ABOVE_CENTAUR.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_BLOOD_POT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_WORMS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_TRIPLE_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_TRIPLE_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_BABY_GORGON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_BOSS_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_BLOOD_POT_L.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_BLOOD_POT_R.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_ROA_LOWER_VOID.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_DARKNESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_APEX.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CAVES_SKELETONS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CAVES_CATA_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CAVES_CATA_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CAVES_CATA_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_ELEVATOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_VERTICAL_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_CLAW_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_CLAW_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_WATER_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_WATER_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_DEV_ROOM.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_AFTER_BLUE_DOOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_SHORTCUT_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_LADDER_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_MID_SHORTCUT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_FLAMES_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATA_FLAMES_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_TR_ADORNED_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_TR_ADORNED_M.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_TR_ADORNED_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_TR_ELEVATOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_TR_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CD_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CD_2.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CD_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CD_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CD_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATH_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATH_BESIDE_SHAFT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_CATH_TOP_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_SP_DOUBLE_DOORS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_SP_BUBBLES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.SWITCH_SP_AFTER_STAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_GT_LADDER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_GT_ROTA.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_GT_OLD_MAN_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_GT_OLD_MAN_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_CANNON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_LINUS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_LOWER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TO_BOSS_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TRIPLE_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TRIPLE_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TRIPLE_3.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TOP.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_CLOAK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_SLIMES.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TO_CD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_1ST_ROOM.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_OLD_MAN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_TOP_CHAINS.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_MECH_BK.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_ROCK_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_LOWER.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_AFTER_CLAW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_MAIDEN_1.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_MAIDEN_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_BELL_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_HEART.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_HOTP_BELOW_PUZZLE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_BABY_GORGON.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_LADDER_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_LADDER_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_CENTAUR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_SPIKE_BALLS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_LEFT_ASCEND.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_SHAFT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_BRANCH_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_BRANCH_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_3_REAPERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_ROA_TRIPLE_2.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATA_POISON_ROOTS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_TR_GOLD.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_TR_DARK_ARIAS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CD_BACKTRACK.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CD_START.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CD_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CD_STEPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_SHAFT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_SPIKE_PIT.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_TOP_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_TOP_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_SHAFT_ACCESS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_CATH_ORBS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_SP_BLOCKS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.CRYSTAL_SP_STAR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_MECH_VOLANTIS.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.FACE_HOTP_OLD_MAN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_ROA_SPIDERS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_ROA_BLUE_KEY.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CAVES_1ST_ROOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATA_AFTER_BOW.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATA_BOW.value: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SWITCH),
    Switches.FACE_CATA_X4.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATA_CAMPFIRE.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATA_DOUBLE_DOOR.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATA_BOTTOM.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATH_L.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Switches.FACE_CATH_R.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    KeyItems.CYCLOPS.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    KeyItems.CROWN.value: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
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
