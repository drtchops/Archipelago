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

    ELEVATOR_GT_1 = "GT 1 Elevator"
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

    SWITCH_GT_2ND_ROOM = "GT Switch 2nd Room"
    SWITCH_GT_1ST_CYCLOPS = "GT Switch 1st Cyclops"
    SWITCH_GT_SPIKE_TUNNEL = "GT Switch Spike Tunnel"
    SWITCH_GT_BUTT_ACCESS = "GT Switch Butt Access"
    SWITCH_GT_GH = "GT Switch Gorgonheart"
    SWITCH_GT_ROTA = "GT Switch RotA"
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
    SWITCH_ROA_SPIDERS_TOP = "RoA Switch Spiders Top"
    SWITCH_ROA_SPIDERS_BOTTOM = "RoA Switch Spiders Bottom"
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
    Items.DOOR_BLUE_CAVES,
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

Elevators: TypeAlias = Literal[
    Items.ELEVATOR_GT_1,
    Items.ELEVATOR_GT_2,
    Items.ELEVATOR_MECH_1,
    Items.ELEVATOR_MECH_2,
    Items.ELEVATOR_HOTP,
    Items.ELEVATOR_ROA_1,
    Items.ELEVATOR_ROA_2,
    Items.ELEVATOR_APEX,
    Items.ELEVATOR_CATA_1,
    Items.ELEVATOR_CATA_2,
    Items.ELEVATOR_TR,
]

Switches: TypeAlias = Literal[
    Items.SWITCH_GT_2ND_ROOM,
    Items.SWITCH_GT_1ST_CYCLOPS,
    Items.SWITCH_GT_SPIKE_TUNNEL,
    Items.SWITCH_GT_BUTT_ACCESS,
    Items.SWITCH_GT_GH,
    Items.SWITCH_GT_ROTA,
    Items.SWITCH_GT_UPPER_PATH_BLOCKS,
    Items.SWITCH_GT_UPPER_PATH_ACCESS,
    Items.SWITCH_GT_CROSSES,
    Items.SWITCH_GT_GH_SHORTCUT,
    Items.SWITCH_GT_ARIAS,
    Items.SWITCH_GT_SWORD_ACCESS,
    Items.SWITCH_GT_SWORD_BACKTRACK,
    Items.SWITCH_GT_SWORD,
    Items.SWITCH_GT_UPPER_ARIAS,
    Items.SWITCH_MECH_WATCHER,
    Items.SWITCH_MECH_CHAINS,
    Items.SWITCH_MECH_BOSS_1,
    Items.SWITCH_MECH_BOSS_2,
    Items.SWITCH_MECH_SPLIT_PATH,
    Items.SWITCH_MECH_SNAKE_1,
    Items.SWITCH_MECH_BOOTS,
    Items.SWITCH_MECH_TO_UPPER_GT,
    Items.SWITCH_MECH_UPPER_VOID_DROP,
    Items.SWITCH_MECH_UPPER_VOID,
    Items.SWITCH_MECH_LINUS,
    Items.SWITCH_MECH_TO_BOSS_2,
    Items.SWITCH_MECH_POTS,
    Items.SWITCH_MECH_MAZE_BACKDOOR,
    Items.SWITCH_MECH_TO_BOSS_1,
    Items.SWITCH_MECH_BLOCK_STAIRS,
    Items.SWITCH_MECH_ARIAS_CYCLOPS,
    Items.SWITCH_MECH_BOOTS_LOWER,
    Items.SWITCH_MECH_CHAINS_GAP,
    Items.SWITCH_MECH_LOWER_KEY,
    Items.SWITCH_MECH_ARIAS,
    Items.SWITCH_MECH_SNAKE_2,
    Items.SWITCH_MECH_KEY_BLOCKS,
    Items.SWITCH_MECH_CANNON,
    Items.SWITCH_MECH_EYEBALL,
    Items.SWITCH_MECH_INVISIBLE,
    Items.SWITCH_HOTP_ROCK,
    Items.SWITCH_HOTP_BELOW_START,
    Items.SWITCH_HOTP_LEFT_2,
    Items.SWITCH_HOTP_LEFT_1,
    Items.SWITCH_HOTP_LOWER_SHORTCUT,
    Items.SWITCH_HOTP_BELL,
    Items.SWITCH_HOTP_GHOST_BLOOD,
    Items.SWITCH_HOTP_TELEPORTS,
    Items.SWITCH_HOTP_WORM_PILLAR,
    Items.SWITCH_HOTP_TO_CLAW_1,
    Items.SWITCH_HOTP_TO_CLAW_2,
    Items.SWITCH_HOTP_CLAW_ACCESS,
    Items.SWITCH_HOTP_GHOSTS,
    Items.SWITCH_HOTP_LEFT_3,
    Items.SWITCH_HOTP_ABOVE_OLD_MAN,
    Items.SWITCH_HOTP_TO_ABOVE_OLD_MAN,
    Items.SWITCH_HOTP_TP_PUZZLE,
    Items.SWITCH_HOTP_EYEBALL_SHORTCUT,
    Items.SWITCH_HOTP_BELL_ACCESS,
    Items.SWITCH_HOTP_1ST_ROOM,
    Items.SWITCH_HOTP_LEFT_BACKTRACK,
    Items.SWITCH_ROA_ASCEND,
    Items.SWITCH_ROA_AFTER_WORMS,
    Items.SWITCH_ROA_RIGHT_PATH,
    Items.SWITCH_ROA_APEX_ACCESS,
    Items.SWITCH_ROA_ICARUS,
    Items.SWITCH_ROA_SHAFT_L,
    Items.SWITCH_ROA_SHAFT_R,
    Items.SWITCH_ROA_ELEVATOR,
    Items.SWITCH_ROA_SHAFT_DOWNWARDS,
    Items.SWITCH_ROA_SPIDERS_TOP,
    Items.SWITCH_ROA_SPIDERS_BOTTOM,
    Items.SWITCH_ROA_DARK_ROOM,
    Items.SWITCH_ROA_ASCEND_SHORTCUT,
    Items.SWITCH_ROA_1ST_SHORTCUT,
    Items.SWITCH_ROA_SPIKE_CLIMB,
    Items.SWITCH_ROA_ABOVE_CENTAUR,
    Items.SWITCH_ROA_BLOOD_POT,
    Items.SWITCH_ROA_WORMS,
    Items.SWITCH_ROA_TRIPLE_1,
    Items.SWITCH_ROA_TRIPLE_3,
    Items.SWITCH_ROA_BABY_GORGON,
    Items.SWITCH_ROA_BOSS_ACCESS,
    Items.SWITCH_ROA_BLOOD_POT_L,
    Items.SWITCH_ROA_BLOOD_POT_R,
    Items.SWITCH_ROA_LOWER_VOID,
    Items.SWITCH_DARKNESS,
    Items.SWITCH_APEX,
    Items.SWITCH_CAVES_SKELETONS,
    Items.SWITCH_CAVES_CATA_1,
    Items.SWITCH_CAVES_CATA_2,
    Items.SWITCH_CAVES_CATA_3,
    Items.SWITCH_CATA_ELEVATOR,
    Items.SWITCH_CATA_VERTICAL_SHORTCUT,
    Items.SWITCH_CATA_TOP,
    Items.SWITCH_CATA_CLAW_1,
    Items.SWITCH_CATA_CLAW_2,
    Items.SWITCH_CATA_WATER_1,
    Items.SWITCH_CATA_WATER_2,
    Items.SWITCH_CATA_DEV_ROOM,
    Items.SWITCH_CATA_AFTER_BLUE_DOOR,
    Items.SWITCH_CATA_SHORTCUT_ACCESS,
    Items.SWITCH_CATA_LADDER_BLOCKS,
    Items.SWITCH_CATA_MID_SHORTCUT,
    Items.SWITCH_CATA_1ST_ROOM,
    Items.SWITCH_CATA_FLAMES_2,
    Items.SWITCH_CATA_FLAMES_1,
    Items.SWITCH_TR_ADORNED_L,
    Items.SWITCH_TR_ADORNED_M,
    Items.SWITCH_TR_ADORNED_R,
    Items.SWITCH_TR_ELEVATOR,
    Items.SWITCH_TR_BOTTOM,
    Items.SWITCH_CD_1,
    Items.SWITCH_CD_2,
    Items.SWITCH_CD_3,
    Items.SWITCH_CD_CAMPFIRE,
    Items.SWITCH_CD_TOP,
    Items.SWITCH_CATH_BOTTOM,
    Items.SWITCH_CATH_BESIDE_SHAFT,
    Items.SWITCH_CATH_TOP_CAMPFIRE,
    Items.SWITCH_SP_DOUBLE_DOORS,
    Items.SWITCH_SP_BUBBLES,
    Items.SWITCH_SP_AFTER_STAR,
    Items.CRYSTAL_GT_LADDER,
    Items.CRYSTAL_GT_OLD_MAN_1,
    Items.CRYSTAL_GT_OLD_MAN_2,
    Items.CRYSTAL_MECH_CANNON,
    Items.CRYSTAL_MECH_LINUS,
    Items.CRYSTAL_MECH_LOWER,
    Items.CRYSTAL_MECH_TO_BOSS_3,
    Items.CRYSTAL_MECH_TRIPLE_1,
    Items.CRYSTAL_MECH_TRIPLE_2,
    Items.CRYSTAL_MECH_TRIPLE_3,
    Items.CRYSTAL_MECH_TOP,
    Items.CRYSTAL_MECH_CLOAK,
    Items.CRYSTAL_MECH_SLIMES,
    Items.CRYSTAL_MECH_TO_CD,
    Items.CRYSTAL_MECH_CAMPFIRE,
    Items.CRYSTAL_MECH_1ST_ROOM,
    Items.CRYSTAL_MECH_OLD_MAN,
    Items.CRYSTAL_MECH_TOP_CHAINS,
    Items.CRYSTAL_MECH_BK,
    Items.CRYSTAL_HOTP_ROCK_ACCESS,
    Items.CRYSTAL_HOTP_BOTTOM,
    Items.CRYSTAL_HOTP_LOWER,
    Items.CRYSTAL_HOTP_AFTER_CLAW,
    Items.CRYSTAL_HOTP_MAIDEN_1,
    Items.CRYSTAL_HOTP_MAIDEN_2,
    Items.CRYSTAL_HOTP_BELL_ACCESS,
    Items.CRYSTAL_HOTP_HEART,
    Items.CRYSTAL_HOTP_BELOW_PUZZLE,
    Items.CRYSTAL_ROA_1ST_ROOM,
    Items.CRYSTAL_ROA_BABY_GORGON,
    Items.CRYSTAL_ROA_LADDER_R,
    Items.CRYSTAL_ROA_LADDER_L,
    Items.CRYSTAL_ROA_CENTAUR,
    Items.CRYSTAL_ROA_SPIKE_BALLS,
    Items.CRYSTAL_ROA_LEFT_ASCEND,
    Items.CRYSTAL_ROA_SHAFT,
    Items.CRYSTAL_ROA_BRANCH_R,
    Items.CRYSTAL_ROA_BRANCH_L,
    Items.CRYSTAL_ROA_3_REAPERS,
    Items.CRYSTAL_ROA_TRIPLE_2,
    Items.CRYSTAL_CATA_POISON_ROOTS,
    Items.CRYSTAL_TR_GOLD,
    Items.CRYSTAL_TR_DARK_ARIAS,
    Items.CRYSTAL_CD_BACKTRACK,
    Items.CRYSTAL_CD_START,
    Items.CRYSTAL_CD_CAMPFIRE,
    Items.CRYSTAL_CD_STEPS,
    Items.CRYSTAL_CATH_1ST_ROOM,
    Items.CRYSTAL_CATH_SHAFT,
    Items.CRYSTAL_CATH_SPIKE_PIT,
    Items.CRYSTAL_CATH_TOP_L,
    Items.CRYSTAL_CATH_TOP_R,
    Items.CRYSTAL_CATH_SHAFT_ACCESS,
    Items.CRYSTAL_CATH_ORBS,
    Items.CRYSTAL_SP_BLOCKS,
    Items.CRYSTAL_SP_STAR,
    Items.FACE_MECH_VOLANTIS,
    Items.FACE_HOTP_OLD_MAN,
    Items.FACE_ROA_BLUE_KEY,
    Items.FACE_CAVES_1ST_ROOM,
    Items.FACE_CATA_AFTER_BOW,
    Items.FACE_CATA_BOW,
    Items.FACE_CATA_X4,
    Items.FACE_CATA_CAMPFIRE,
    Items.FACE_CATA_DOUBLE_DOOR,
    Items.FACE_CATA_BOTTOM,
    Items.FACE_CATH_L,
    Items.FACE_CATH_R,
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
    Items.DOOR_BLUE_CAVES,
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
    Items.EYE_RED: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Items.EYE_BLUE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Items.EYE_GREEN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.EYE),
    Items.KEY_WHITE: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Items.KEY_BLUE: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Items.KEY_RED: AstalonItemData(ItemClassification.useful, 0, ItemGroups.KEY),
    Items.GORGONHEART: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    Items.ANCIENTS_RING: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    Items.MAIDEN_RING: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    Items.SWORD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.MAP: AstalonItemData(ItemClassification.filler, 1, ItemGroups.ITEM),
    Items.ASCENDANT_KEY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.ADORNED_KEY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.BANISH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.VOID: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.BOOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.CLOAK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.BELL: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.AMULET: AstalonItemData(ItemClassification.useful, 1, ItemGroups.ITEM),
    Items.CLAW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.GAUNTLET: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.ICARUS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.CHALICE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.BLOCK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.STAR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ITEM),
    Items.ATTACK_1: AstalonItemData(ItemClassification.useful, 12, ItemGroups.ATTACK),
    Items.MAX_HP_1: AstalonItemData(ItemClassification.useful, 14, ItemGroups.HEALTH),
    Items.MAX_HP_2: AstalonItemData(ItemClassification.useful, 10, ItemGroups.HEALTH),
    Items.MAX_HP_3: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Items.MAX_HP_4: AstalonItemData(ItemClassification.useful, 1, ItemGroups.HEALTH),
    Items.MAX_HP_5: AstalonItemData(ItemClassification.useful, 8, ItemGroups.HEALTH),
    Items.ORBS_200: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.ORBS_500: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.ORBS_1000: AstalonItemData(ItemClassification.filler, 0, ItemGroups.ORBS),
    Items.DOOR_WHITE_GT_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_GT_MAP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_GT_TAUROS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_MECH_2ND: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_MECH_BK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_MECH_ARENA: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_MECH_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_HOTP_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_HOTP_CLAW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_HOTP_BOSS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_ROA_WORMS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_ROA_ASCEND: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_ROA_BALLS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_ROA_SPINNERS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_ROA_SKIP: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_CATA_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_CATA_BLUE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_WHITE_CATA_PRISON: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_WHITE),
    Items.DOOR_BLUE_GT_HUNTER: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_GT_RING: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_GT_ORBS: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_GT_ASCENDANT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_GT_SWORD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_MECH_RED: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_MECH_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_MECH_MUSIC: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_MECH_BOOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_MECH_VOID: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_MECH_CD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_HOTP_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_HOTP_STATUE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_HOTP_MAIDEN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_ROA_FLAMES: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_ROA_BLOOD: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_APEX: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CAVES: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_ORBS: AstalonItemData(ItemClassification.useful, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_SAVE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_ROOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_PRISON_CYCLOPS: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_PRISON_LEFT: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_CATA_PRISON_RIGHT: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_TR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_BLUE_SP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_BLUE),
    Items.DOOR_RED_ZEEK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    Items.DOOR_RED_CATH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    Items.DOOR_RED_SP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    Items.DOOR_RED_TR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.DOOR_RED),
    # progression if gil is a check
    Items.DOOR_RED_DEV_ROOM: AstalonItemData(ItemClassification.filler, 1, ItemGroups.DOOR_RED),
    Items.ARIAS: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Items.KYULI: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Items.ALGUS: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Items.ZEEK: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Items.BRAM: AstalonItemData(ItemClassification.progression, 0, ItemGroups.CHARACTER),
    Items.GIFT: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.KNOWLEDGE: AstalonItemData(ItemClassification.filler, 1, ItemGroups.SHOP),
    Items.MERCY: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.ORB_SEEKER: AstalonItemData(ItemClassification.useful, 1, ItemGroups.SHOP),
    Items.MAP_REVEAL: AstalonItemData(ItemClassification.filler, 0, ItemGroups.SHOP),
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
    Items.ELEVATOR_GT_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_MECH_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_MECH_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_HOTP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_ROA_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_ROA_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_APEX: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_CATA_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_CATA_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.ELEVATOR_TR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.ELEVATOR),
    Items.SWITCH_GT_2ND_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_1ST_CYCLOPS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_SPIKE_TUNNEL: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_BUTT_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_GH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_ROTA: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_UPPER_PATH_BLOCKS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_UPPER_PATH_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_CROSSES: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_GH_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_ARIAS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_SWORD_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_SWORD_BACKTRACK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_SWORD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_GT_UPPER_ARIAS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_WATCHER: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_CHAINS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_BOSS_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_BOSS_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_SPLIT_PATH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_SNAKE_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_BOOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_TO_UPPER_GT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_UPPER_VOID_DROP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_UPPER_VOID: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_LINUS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_TO_BOSS_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_POTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_MAZE_BACKDOOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_TO_BOSS_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_BLOCK_STAIRS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_ARIAS_CYCLOPS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_BOOTS_LOWER: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_CHAINS_GAP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_LOWER_KEY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_ARIAS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_SNAKE_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_KEY_BLOCKS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_CANNON: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_EYEBALL: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_MECH_INVISIBLE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_ROCK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_BELOW_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_LEFT_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_LEFT_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_LOWER_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_BELL: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_GHOST_BLOOD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_TELEPORTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_WORM_PILLAR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_TO_CLAW_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_TO_CLAW_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_CLAW_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_GHOSTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_LEFT_3: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_ABOVE_OLD_MAN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_TO_ABOVE_OLD_MAN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_TP_PUZZLE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_EYEBALL_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_BELL_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_1ST_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_HOTP_LEFT_BACKTRACK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_ASCEND: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_AFTER_WORMS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_RIGHT_PATH: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_APEX_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_ICARUS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_SHAFT_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_SHAFT_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_ELEVATOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_SHAFT_DOWNWARDS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_SPIDERS_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_SPIDERS_BOTTOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_DARK_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_ASCEND_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_1ST_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_SPIKE_CLIMB: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_ABOVE_CENTAUR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_BLOOD_POT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_WORMS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_TRIPLE_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_TRIPLE_3: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_BABY_GORGON: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_BOSS_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_BLOOD_POT_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_BLOOD_POT_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_ROA_LOWER_VOID: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_DARKNESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_APEX: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CAVES_SKELETONS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CAVES_CATA_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CAVES_CATA_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CAVES_CATA_3: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_ELEVATOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_VERTICAL_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_CLAW_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_CLAW_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_WATER_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_WATER_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_DEV_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_AFTER_BLUE_DOOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_SHORTCUT_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_LADDER_BLOCKS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_MID_SHORTCUT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_1ST_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_FLAMES_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATA_FLAMES_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_TR_ADORNED_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_TR_ADORNED_M: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_TR_ADORNED_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_TR_ELEVATOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_TR_BOTTOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CD_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CD_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CD_3: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CD_CAMPFIRE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CD_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATH_BOTTOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATH_BESIDE_SHAFT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_CATH_TOP_CAMPFIRE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_SP_DOUBLE_DOORS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_SP_BUBBLES: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.SWITCH_SP_AFTER_STAR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_GT_LADDER: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_GT_OLD_MAN_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_GT_OLD_MAN_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_CANNON: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_LINUS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_LOWER: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TO_BOSS_3: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TRIPLE_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TRIPLE_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TRIPLE_3: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TOP: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_CLOAK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_SLIMES: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TO_CD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_CAMPFIRE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_1ST_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_OLD_MAN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_TOP_CHAINS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_MECH_BK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_ROCK_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_BOTTOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_LOWER: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_AFTER_CLAW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_MAIDEN_1: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_MAIDEN_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_BELL_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_HEART: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_HOTP_BELOW_PUZZLE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_1ST_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_BABY_GORGON: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_LADDER_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_LADDER_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_CENTAUR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_SPIKE_BALLS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_LEFT_ASCEND: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_SHAFT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_BRANCH_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_BRANCH_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_3_REAPERS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_ROA_TRIPLE_2: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATA_POISON_ROOTS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_TR_GOLD: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_TR_DARK_ARIAS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CD_BACKTRACK: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CD_START: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CD_CAMPFIRE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CD_STEPS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_1ST_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_SHAFT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_SPIKE_PIT: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_TOP_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_TOP_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_SHAFT_ACCESS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_CATH_ORBS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_SP_BLOCKS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.CRYSTAL_SP_STAR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_MECH_VOLANTIS: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_HOTP_OLD_MAN: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_ROA_BLUE_KEY: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CAVES_1ST_ROOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATA_AFTER_BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATA_BOW: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATA_X4: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATA_CAMPFIRE: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATA_DOUBLE_DOOR: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATA_BOTTOM: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATH_L: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
    Items.FACE_CATH_R: AstalonItemData(ItemClassification.progression, 1, ItemGroups.SWITCH),
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
