from dataclasses import dataclass
from enum import StrEnum
from itertools import groupby

from BaseClasses import Location

from .constants import GAME_NAME
from .regions import RegionName


class Area(StrEnum):
    SHOP = "Shop"
    GT = "Gorgon Tomb"
    MECH = "Mechanism"
    HOP = "Hall of Phantoms"
    ROA = "Ruins of Ash"
    DARK = "Darkness"
    APEX = "The Apex"
    CAVES = "Caves"
    CATA = "Catacombs"
    TR = "Tower Roots"
    CD = "Cyclops Den"
    CATH = "Cathedral"
    SP = "Serpent Path"


class LocationGroup(StrEnum):
    CHARACTER = "Characters"
    ITEM = "Items"
    FAMILIAR = "Familiars"
    HEALTH = "Health"
    ATTACK = "Attack"
    KEY_WHITE = "White Keys"
    KEY_BLUE = "Blue Keys"
    KEY_RED = "Red Keys"
    SHOP = "Shop Upgrades"
    ELEVATOR = "Elevators"
    SWITCH = "Switches"
    CANDLE = "Candles"
    ORBS = "Orbs"


class LocationName(StrEnum):
    GT_ALGUS = "GT Algus"
    GT_ARIAS = "GT Arias"
    GT_KYULI = "GT Kyuli"
    GT_GORGONHEART = "GT Gorgonheart"
    GT_ANCIENTS_RING = "GT Ring of the Ancients"
    GT_SWORD = "GT Sword of Mirrors"
    GT_MAP = "GT Linus' Map"
    GT_ASCENDANT_KEY = "GT Ascendant Key"
    GT_BANISH = "GT Banish Spell"
    GT_VOID = "GT Void Charm"
    GT_EYE_RED = "GT Gorgon Eye Red"
    GT_ATTACK = "GT Attack Up"
    GT_HP_1_RING = "GT Max HP Up Ring of the Ancients"
    GT_HP_5_KEY = "GT Max HP Up Ascendant Key"
    GT_WHITE_KEY_START = "GT White Key 1st Room"
    GT_WHITE_KEY_RIGHT = "GT White Key Right Side"
    GT_WHITE_KEY_BOSS = "GT White Key Before Boss"
    GT_BLUE_KEY_BONESNAKE = "GT Blue Key Bonesnakes"
    GT_BLUE_KEY_BUTT = "GT Blue Key Butt"
    GT_BLUE_KEY_WALL = "GT Blue Key Inside Wall"
    GT_BLUE_KEY_POT = "GT Blue Key Pot"
    GT_RED_KEY = "GT Red Key"
    GT_ELEVATOR_1 = "GT Elevator 1"
    GT_ELEVATOR_2 = "GT Elevator 2"
    GT_SWITCH_2ND_ROOM = "GT Switch 2nd Room"
    GT_SWITCH_1ST_CYCLOPS = "GT Switch 1st Cyclops"
    GT_SWITCH_SPIKE_TUNNEL = "GT Switch Spike Tunnel Access"
    GT_SWITCH_BUTT_ACCESS = "GT Switch Butt Access"
    GT_SWITCH_GH = "GT Switch Gorgonheart"
    GT_SWITCH_UPPER_PATH_BLOCKS = "GT Switch Upper Path Blocks"
    GT_SWITCH_UPPER_PATH_ACCESS = "GT Switch Upper Path Access"
    GT_SWITCH_CROSSES = "GT Switch Crosses"
    GT_SWITCH_GH_SHORTCUT = "GT Switch Gorgonheart Shortcut"
    GT_SWITCH_ARIAS_PATH = "GT Switch Arias's Path"
    GT_SWITCH_SWORD_ACCESS = "GT Switch Sword Access"
    GT_SWITCH_SWORD_BACKTRACK = "GT Switch Sword Backtrack"
    GT_SWITCH_SWORD = "GT Switch Sword"
    GT_SWITCH_UPPER_ARIAS = "GT Switch Upper Arias"
    GT_CRYSTAL_LADDER = "GT Crystal Ladder"
    GT_CRYSTAL_ROTA = "GT Crystal Ring of the Ancients"
    GT_CRYSTAL_OLD_MAN_1 = "GT Crystal Old Man 1"
    GT_CRYSTAL_OLD_MAN_2 = "GT Crystal Old Man 2"
    GT_CANDLE_LINUS = "GT Candle Linus' Map"
    GT_CANDLE_1ST_CYCLOPS = "GT Candle 1st Cyclops"
    GT_CANDLE_BOSS = "GT Candle Boss"
    GT_CANDLE_BOTTOM = "GT Candle Bottom"
    GT_ORB_MULTI = "GT Orb Multiplier"

    MECH_ZEEK = "Mech Zeek"
    MECH_BOOTS = "Mech Talaria Boots"
    MECH_CLOAK = "Mech Cloak of Levitation"
    MECH_CYCLOPS = "Mech Cyclops Idol"
    MECH_EYE_BLUE = "Mech Gorgon Eye Blue"
    MECH_ATTACK_VOLANTIS = "Mech Attack Up Above Volantis"
    MECH_ATTACK_STAR = "Mech Attack Up Morning Star Blocks"
    MECH_HP_1_SWITCH = "Mech Max HP Up Secret Switch"
    MECH_HP_1_STAR = "Mech Max HP Up Morning Star Blocks"
    MECH_HP_3_CLAW = "Mech Max HP Up Above Checkpoint"
    MECH_WHITE_KEY_LINUS = "Mech White Key Below Linus"
    MECH_WHITE_KEY_BK = "Mech White Key Black Knight"
    MECH_WHITE_KEY_ARENA = "Mech White Key Enemy Arena"
    MECH_WHITE_KEY_TOP = "Mech White Key Top"
    MECH_BLUE_KEY_VOID = "Mech Blue Key Void Charm"
    MECH_BLUE_KEY_SNAKE = "Mech Blue Key Snake Head"
    MECH_BLUE_KEY_LINUS = "Mech Blue Key Linus"
    MECH_BLUE_KEY_SACRIFICE = "Mech Blue Key Sacrifice"
    MECH_BLUE_KEY_RED = "Mech Blue Key To Red Key"
    MECH_BLUE_KEY_ARIAS = "Mech Blue Key Arias"
    MECH_BLUE_KEY_BLOCKS = "Mech Blue Key Switch Blocks"
    MECH_BLUE_KEY_TOP = "Mech Blue Key Top Path"
    MECH_BLUE_KEY_OLD_MAN = "Mech Blue Key Old Man"
    MECH_BLUE_KEY_SAVE = "Mech Blue Key Checkpoint"
    MECH_BLUE_KEY_POT = "Mech Blue Key Pot"
    MECH_RED_KEY = "Mech Red Key"
    MECH_ELEVATOR_1 = "Mech Elevator 1"
    MECH_ELEVATOR_2 = "Mech Elevator 2"
    MECH_SWITCH_WATCHER = "Mech Switch Watcher"
    MECH_SWITCH_CHAINS = "Mech Switch Chains"
    MECH_SWITCH_BOSS_ACCESS_1 = "Mech Switch Boss Access 1"
    MECH_SWITCH_BOSS_ACCESS_2 = "Mech Switch Boss Access 2"
    MECH_SWITCH_SPLIT_PATH = "Mech Switch Split Path"
    MECH_SWITCH_SNAKE_1 = "Mech Switch Snake 1"
    MECH_SWITCH_BOOTS_ACCESS = "Mech Switch Boots Access"
    MECH_SWITCH_UPPER_GT_ACCESS = "Mech Switch Upper GT Access"
    MECH_SWITCH_UPPER_VOID_DROP = "Mech Switch Upper Void Drop"
    MECH_SWITCH_UPPER_VOID = "Mech Switch Upper Void"
    MECH_SWITCH_LINUS = "Mech Switch Linus"
    MECH_SWITCH_TO_BOSS_2 = "Mech Switch To Boss 2"
    MECH_SWITCH_POTS = "Mech Switch Pots"
    MECH_SWITCH_MAZE_BACKDOOR = "Mech Switch Maze Backdoor"
    MECH_SWITCH_TO_BOSS_1 = "Mech Switch To Boss 1"
    MECH_SWITCH_BLOCK_STAIRS = "Mech Switch Block Stairs"
    MECH_SWITCH_ARIAS_CYCLOPS = "Mech Switch Arias Cyclops"
    MECH_SWITCH_BOOTS_LOWER = "Mech Switch Boots Lower"
    MECH_SWITCH_CHAINS_GAP = "Mech Switch Chains Gap"
    MECH_SWITCH_LOWER_KEY = "Mech Switch Lower Key"
    MECH_SWITCH_ARIAS = "Mech Switch Arias"
    MECH_SWITCH_SNAKE_2 = "Mech Switch Snake 2"
    MECH_SWITCH_KEY_BLOCKS = "Mech Switch Key Blocks"
    MECH_SWITCH_CANNON = "Mech Switch Cannon"
    MECH_SWITCH_EYEBALL = "Mech Switch Eyeball"
    MECH_SWITCH_INVISIBLE = "Mech Switch Invisible"
    MECH_SKULL_PUZZLE = "Mech Skull Puzzle"
    MECH_CRYSTAL_CANNON = "Mech Crystal Cannon"
    MECH_CRYSTAL_LINUS = "Mech Crystal Linus"
    MECH_CRYSTAL_LOWER = "Mech Crystal Lower"
    MECH_CRYSTAL_TO_BOSS_3 = "Mech Crystal To Boss 3"
    MECH_CRYSTAL_TRIPLE_1 = "Mech Crystal Triple 1"
    MECH_CRYSTAL_TRIPLE_2 = "Mech Crystal Triple 2"
    MECH_CRYSTAL_TRIPLE_3 = "Mech Crystal Triple 3"
    MECH_CRYSTAL_TOP = "Mech Crystal Top"
    MECH_CRYSTAL_CLOAK = "Mech Crystal Cloak"
    MECH_CRYSTAL_SLIMES = "Mech Crystal Slimes"
    MECH_CRYSTAL_TO_CD = "Mech Crystal To CD"
    MECH_CRYSTAL_CAMPFIRE = "Mech Crystal Campfire"
    MECH_CRYSTAL_1ST_ROOM = "Mech Crystal 1st Room"
    MECH_CRYSTAL_OLD_MAN = "Mech Crystal Old Man"
    MECH_CRYSTAL_TOP_CHAINS = "Mech Crystal Top Chains"
    MECH_CRYSTAL_BK = "Mech Crystal Black Knight"
    MECH_FACE_ABOVE_VOLANTIS = "Mech Face Above Volantis"
    MECH_CANDLE_ROOTS = "Mech Candle Roots"
    MECH_CANDLE_BOTTOM = "Mech Candle Bottom"
    MECH_CANDLE_CHAINS = "Mech Candle Chains"
    MECH_CANDLE_RIGHT = "Mech Candle Right"
    MECH_CANDLE_POTS = "Mech Candle Pots"
    MECH_CANDLE_BOSS_1 = "Mech Candle Boss 1"
    MECH_CANDLE_BOSS_2 = "Mech Candle Boss 2"
    MECH_CANDLE_SLIMES = "Mech Candle Slimes"
    MECH_CANDLE_ZEEK = "Mech Candle Zeek"
    MECH_CANDLE_MAZE_BACKDOOR = "Mech Candle Maze Backdoor"
    MECH_CANDLE_CD_ACCESS_1 = "Mech Candle CD Access 1"
    MECH_CANDLE_CD_ACCESS_2 = "Mech Candle CD Access 2"
    MECH_CANDLE_CD_ACCESS_3 = "Mech Candle CD Access 3"
    MECH_CANDLE_1ST_ROOM = "Mech Candle 1st Room"
    MECH_CANDLE_BK = "Mech Candle Black Knight"
    MECH_CANDLE_CAMPFIRE_R = "Mech Candle Right Campfire"
    MECH_ORB_MULTI = "Mech Orb Multiplier"

    HOP_BELL = "HoP Athena's Bell"
    HOP_AMULET = "HoP Amulet of Sol"
    HOP_CLAW = "HoP Griffon Claw"
    HOP_GAUNTLET = "HoP Boreas Gauntlet"
    HOP_MAIDEN_RING = "HoP Dead Maiden's Ring"
    HOP_HP_1_CLAW = "HoP Max HP Up Griffon Claw"
    HOP_HP_2_LADDER = "HoP Max HP Up Secret Ladder"
    HOP_HP_2_GAUNTLET = "HoP Max HP Up Boreas Gauntlet"
    HOP_HP_5_OLD_MAN = "HoP Max HP Up Old Man"
    HOP_HP_5_MAZE = "HoP Max HP Up Teleport Maze"
    HOP_HP_5_START = "HoP Max HP Up Above Start"
    HOP_WHITE_KEY_LEFT = "HoP White Key Left of Start"
    HOP_WHITE_KEY_GHOST = "HoP White Key Ghost"
    HOP_WHITE_KEY_OLD_MAN = "HoP White Key Old Man"
    HOP_WHITE_KEY_BOSS = "HoP White Key Boss"
    HOP_BLUE_KEY_STATUE = "HoP Blue Key Epimetheus"
    HOP_BLUE_KEY_GOLD = "HoP Blue Key Gold Hint"
    HOP_BLUE_KEY_AMULET = "HoP Blue Key Amulet of Sol"
    HOP_BLUE_KEY_LADDER = "HoP Blue Key Secret Ladder"
    HOP_BLUE_KEY_TELEPORTS = "HoP Blue Key Spike Teleporters"
    HOP_BLUE_KEY_MAZE = "HoP Blue Key Teleport Maze"
    HOP_RED_KEY = "HoP Red Key"
    HOP_ELEVATOR = "HoP Elevator"
    HOP_SWITCH_ROCK = "HoP Switch Rock"
    HOP_SWITCH_BELOW_START = "HoP Switch Below Start"
    HOP_SWITCH_LEFT_2 = "HoP Switch Left 2"
    HOP_SWITCH_LEFT_1 = "HoP Switch Left 1"
    HOP_SWITCH_LOWER_SHORTCUT = "HoP Switch Lower Shortcut"
    HOP_SWITCH_BELL = "HoP Switch Bell"
    HOP_SWITCH_GHOST_BLOOD = "HoP Switch Ghost Blood"
    HOP_SWITCH_TELEPORTS = "HoP Switch Teleports"
    HOP_SWITCH_WORM_PILLAR = "HoP Switch Worm Pillar"
    HOP_SWITCH_TO_CLAW_1 = "HoP Switch To Claw 1"
    HOP_SWITCH_TO_CLAW_2 = "HoP Switch To Claw 2"
    HOP_SWITCH_CLAW_ACCESS = "HoP Switch Claw Access"
    HOP_SWITCH_GHOSTS = "HoP Switch Ghosts"
    HOP_SWITCH_LEFT_3 = "HoP Switch Left 3"
    HOP_SWITCH_ABOVE_OLD_MAN = "HoP Switch Above Old Man"
    HOP_SWITCH_TO_ABOVE_OLD_MAN = "HoP Switch To Above Old Man"
    HOP_SWITCH_TP_PUZZLE = "HoP Switch Teleport Puzzle"
    HOP_SWITCH_EYEBALL_SHORTCUT = "HoP Switch Eyeball Shortcut"
    HOP_SWITCH_BELL_ACCESS = "HoP Switch Bell Access"
    HOP_SWITCH_1ST_ROOM = "HoP Switch 1st Room"
    HOP_SWITCH_LEFT_BACKTRACK = "HoP Switch Left Backtrack"
    HOP_SKULL_PUZZLE = "HoP Skull Puzzle"
    HOP_CRYSTAL_ROCK_ACCESS = "HoP Crystal Rock Access"
    HOP_CRYSTAL_BOTTOM = "HoP Crystal Bottom"
    HOP_CRYSTAL_LOWER = "HoP Crystal Lower"
    HOP_CRYSTAL_AFTER_CLAW = "HoP Crystal After Claw"
    HOP_CRYSTAL_MAIDEN_1 = "HoP Crystal Dead Maiden 1"
    HOP_CRYSTAL_MAIDEN_2 = "HoP Crystal Dead Maiden 2"
    HOP_CRYSTAL_BELL_ACCESS = "HoP Crystal Bell Access"
    HOP_CRYSTAL_HEART = "HoP Crystal Heart"
    HOP_CRYSTAL_BELOW_PUZZLE = "HoP Crystal Below Puzzle"
    HOP_FACE_OLD_MAN = "HoP Face Old Man"
    HOP_CANDLE_1ST_ROOM = "HoP Candle 1st Room"
    HOP_CANDLE_LOWER = "HoP Candle Lower"
    HOP_CANDLE_BELL = "HoP Candle Bell"
    HOP_CANDLE_EYEBALL = "HoP Candle Eyeball"
    HOP_CANDLE_OLD_MAN = "HoP Candle Old Man"
    HOP_CANDLE_BEFORE_CLAW = "HoP Candle Before Claw"
    HOP_CANDLE_CLAW_CAMPFIRE = "HoP Candle Claw Campfire"
    HOP_CANDLE_TP_PUZZLE = "HoP Candle Teleport Puzzle"
    HOP_CANDLE_BOSS = "HoP Candle Boss"
    HOP_CANDLE_TP_FALL = "HoP Candle Teleport Fall"
    HOP_CANDLE_UPPER_VOID_1 = "HoP Candle Upper Void 1"
    HOP_CANDLE_UPPER_VOID_2 = "HoP Candle Upper Void 2"
    HOP_CANDLE_UPPER_VOID_3 = "HoP Candle Upper Void 3"
    HOP_CANDLE_UPPER_VOID_4 = "HoP Candle Upper Void 4"
    HOP_CANDLE_ELEVATOR = "HoP Candle Elevator"

    ROA_ICARUS = "RoA Icarus Emblem"
    ROA_EYE_GREEN = "RoA Gorgon Eye Green"
    ROA_ATTACK = "RoA Attack Up"
    ROA_HP_1_LEFT = "RoA Max HP Up Left of Ascent"
    ROA_HP_2_RIGHT = "RoA Max HP Up Right Side"
    ROA_HP_5_SOLARIA = "RoA Max HP Up After Solaria"
    ROA_WHITE_KEY_SAVE = "RoA White Key Checkpoint"
    ROA_WHITE_KEY_REAPERS = "RoA White Key 3 Reapers"
    ROA_WHITE_KEY_TORCHES = "RoA White Key Torches"
    ROA_WHITE_KEY_PORTAL = "RoA White Key Void Portal"
    ROA_BLUE_KEY_FACE = "RoA Blue Key Face"
    ROA_BLUE_KEY_FLAMES = "RoA Blue Key Flames"
    ROA_BLUE_KEY_BABY = "RoA Blue Key Baby Gorgon"
    ROA_BLUE_KEY_TOP = "RoA Blue Key Top"
    ROA_BLUE_KEY_POT = "RoA Blue Key Pot"
    ROA_RED_KEY = "RoA Red Key"
    ROA_ELEVATOR_1 = "RoA Elevator 1"
    ROA_ELEVATOR_2 = "RoA Elevator 2"
    ROA_SWITCH_ASCEND = "RoA Switch Ascend"
    ROA_SWITCH_AFTER_WORMS = "RoA Switch After Worms"
    ROA_SWITCH_RIGHT_PATH = "RoA Switch Right Path"
    ROA_SWITCH_APEX_ACCESS = "RoA Switch Apex Access"
    ROA_SWITCH_ICARUS = "RoA Switch Icarus Emblem"
    ROA_SWITCH_SHAFT_L = "RoA Switch Shaft Left"
    ROA_SWITCH_SHAFT_R = "RoA Switch Shaft Right"
    ROA_SWITCH_ELEVATOR = "RoA Switch Elevator"
    ROA_SWITCH_SHAFT_DOWNWARDS = "RoA Switch Shaft Downwards"
    ROA_SWITCH_SPIDERS = "RoA Switch Spiders"
    ROA_SWITCH_DARK_ROOM = "RoA Switch Dark Room"
    ROA_SWITCH_ASCEND_SHORTCUT = "RoA Switch Ascend Shortcut"
    ROA_SWITCH_1ST_SHORTCUT = "RoA Switch 1st Shortcut"
    ROA_SWITCH_SPIKE_CLIMB = "RoA Switch Spike Climb"
    ROA_SWITCH_ABOVE_CENTAUR = "RoA Switch Above Centaur"
    ROA_SWITCH_BLOOD_POT = "RoA Switch Blood Pot"
    ROA_SWITCH_WORMS = "RoA Switch Worms"
    ROA_SWITCH_TRIPLE_1 = "RoA Switch Triple 1"
    ROA_SWITCH_TRIPLE_3 = "RoA Switch Triple 3"
    ROA_SWITCH_BABY_GORGON = "RoA Switch Baby Gorgon"
    ROA_SWITCH_BOSS_ACCESS = "RoA Switch Boss Access"
    ROA_SWITCH_BLOOD_POT_L = "RoA Switch Blood Pot Left"
    ROA_SWITCH_BLOOD_POT_R = "RoA Switch Blood Pot Right"
    ROA_SWITCH_LOWER_VOID = "RoA Switch Lower Void"
    ROA_CRYSTAL_1ST_ROOM = "RoA Crystal 1st Room"
    ROA_CRYSTAL_BABY_GORGON = "RoA Crystal Baby Gorgon"
    ROA_CRYSTAL_LADDER_R = "RoA Crystal Ladder Right"
    ROA_CRYSTAL_LADDER_L = "RoA Crystal Ladder Left"
    ROA_CRYSTAL_CENTAUR = "RoA Crystal Centaur"
    ROA_CRYSTAL_SPIKE_BALLS = "RoA Crystal Spike Balls"
    ROA_CRYSTAL_LEFT_ASCEND = "RoA Crystal Left Ascend"
    ROA_CRYSTAL_SHAFT = "RoA Crystal Shaft"
    ROA_CRYSTAL_BRANCH_R = "RoA Crystal Branch Right"
    ROA_CRYSTAL_BRANCH_L = "RoA Crystal Branch Left"
    ROA_CRYSTAL_3_REAPERS = "RoA Crystal 3 Reapers"
    ROA_CRYSTAL_TRIPLE_2 = "RoA Crystal Triple 2"
    ROA_FACE_SPIDERS = "RoA Face Spiders"
    ROA_FACE_BLUE_KEY = "RoA Face Blue Key"
    ROA_CANDLE_1ST_ROOM = "RoA Candle 1st Room"
    ROA_CANDLE_3_REAPERS = "RoA Candle 3 Reapers"
    ROA_CANDLE_MIDDLE_CAMPFIRE = "RoA Candle Middle Campfire"
    ROA_CANDLE_LADDER_BOTTOM = "RoA Candle Ladder Bottom"
    ROA_CANDLE_SHAFT = "RoA Candle Shaft"
    ROA_CANDLE_SHAFT_TOP = "RoA Candle Shaft Top"
    ROA_CANDLE_ABOVE_CENTAUR = "RoA Candle Above Centaur"
    ROA_CANDLE_BABY_GORGON = "RoA Candle Baby Gorgon"
    ROA_CANDLE_TOP_CENTAUR = "RoA Candle Top Centaur"
    ROA_CANDLE_HIDDEN_1 = "RoA Candle Hidden 1"
    ROA_CANDLE_HIDDEN_2 = "RoA Candle Hidden 2"
    ROA_CANDLE_HIDDEN_3 = "RoA Candle Hidden 3"
    ROA_CANDLE_HIDDEN_4 = "RoA Candle Hidden 4"
    ROA_CANDLE_HIDDEN_5 = "RoA Candle Hidden 5"
    ROA_CANDLE_BOTTOM_ASCEND = "RoA Candle Bottom Ascend"
    ROA_CANDLE_BRANCH = "RoA Candle Branch"
    ROA_CANDLE_ICARUS_1 = "RoA Candle Icarus 1"
    ROA_CANDLE_ICARUS_2 = "RoA Candle Icarus 2"
    ROA_CANDLE_ELEVATOR = "RoA Candle Elevator"
    ROA_CANDLE_ELEVATOR_CAMPFIRE = "RoA Candle Elevator Campfire"
    ROA_CANDLE_BOSS_1 = "RoA Candle Boss 1"
    ROA_CANDLE_BOSS_2 = "RoA Candle Boss 2"
    ROA_CANDLE_SPIDERS = "RoA Candle Spiders"
    ROA_CANDLE_SPIKE_BALLS = "RoA Candle Spike Balls"
    ROA_CANDLE_LADDER_R = "RoA Candle Ladder Right"
    ROA_CANDLE_ARENA = "RoA Candle Enemy Arena"

    DARK_HP_4 = "Dark Max HP Up"
    DARK_WHITE_KEY = "Dark White Key"
    DARK_SWITCH = "Dark Switch"

    APEX_CHALICE = "Apex Blood Chalice"
    APEX_HP_1_CHALICE = "Apex Max HP Up Blood Chalice"
    APEX_HP_5_HEART = "Apex Max HP Up After Heart"
    APEX_BLUE_KEY = "Apex Blue Key"
    APEX_ELEVATOR = "Apex Elevator"
    APEX_SWITCH = "Apex Switch"
    APEX_CANDLE_ELEVATOR = "Apex Candle Elevator"
    APEX_CANDLE_CHALICE_1 = "Apex Candle Chalice 1"
    APEX_CANDLE_CHALICE_2 = "Apex Candle Chalice 2"
    APEX_CANDLE_CHALICE_3 = "Apex Candle Chalice 3"
    APEX_CANDLE_GARG_1 = "Apex Candle Gargoyle 1"
    APEX_CANDLE_GARG_2 = "Apex Candle Gargoyle 2"
    APEX_CANDLE_GARG_3 = "Apex Candle Gargoyle 3"
    APEX_CANDLE_GARG_4 = "Apex Candle Gargoyle 4"

    CAVES_ATTACK_RED = "Caves Attack Up Item Chain Red"
    CAVES_ATTACK_BLUE = "Caves Attack Up Item Chain Blue"
    CAVES_ATTACK_GREEN = "Caves Attack Up Item Chain Green"
    CAVES_HP_1_START = "Caves Max HP Up 1st Room"
    CAVES_HP_1_CYCLOPS = "Caves Max HP Up Cyclops Arena"
    CAVES_HP_5_CHAIN = "Caves Max HP Up Item Chain"
    CAVES_SWITCH_SKELETONS = "Caves Switch Skeletons"
    CAVES_SWITCH_CATA_ACCESS_1 = "Caves Switch Catacombs Access 1"
    CAVES_SWITCH_CATA_ACCESS_2 = "Caves Switch Catacombs Access 2"
    CAVES_SWITCH_CATA_ACCESS_3 = "Caves Switch Catacombs Access 3"
    CAVES_FACE_1ST_ROOM = "Caves Face 1st Room"

    CATA_BOW = "Cata Lunarian Bow"
    CATA_ATTACK_ROOT = "Cata Attack Up Climbable Root"
    CATA_ATTACK_POISON = "Cata Attack Up Poison Roots"
    CATA_HP_1_ABOVE_POISON = "Cata Max HP Up Above Poison Roots"
    CATA_HP_2_BEFORE_POISON = "Cata Max HP Up Before Poison Roots"
    CATA_HP_2_AFTER_POISON = "Cata Max HP Up After Poison Roots"
    CATA_HP_2_GEMINI_BOTTOM = "Cata Max HP Up Before Gemini Bottom"
    CATA_HP_2_GEMINI_TOP = "Cata Max HP Up Before Gemini Top"
    CATA_HP_2_ABOVE_GEMINI = "Cata Max HP Up Above Gemini"
    CATA_WHITE_KEY_HEAD = "Cata White Key On Head"
    CATA_WHITE_KEY_DEV_ROOM = "Cata White Key Dev Room"
    CATA_WHITE_KEY_PRISON = "Cata White Key Prison"
    CATA_BLUE_KEY_SLIMES = "Cata Blue Key Slime Water"
    CATA_BLUE_KEY_EYEBALLS = "Cata Blue Key Eyeballs"
    CATA_ELEVATOR_1 = "Cata Elevator 1"
    CATA_ELEVATOR_2 = "Cata Elevator 2"
    CATA_SWITCH_ELEVATOR = "Cata Switch Elevator"
    CATA_SWITCH_SHORTCUT = "Cata Switch Vertical Shortcut"
    CATA_SWITCH_TOP = "Cata Switch Top"
    CATA_SWITCH_CLAW_1 = "Cata Switch Claw 1"
    CATA_SWITCH_CLAW_2 = "Cata Switch Claw 2"
    CATA_SWITCH_WATER_1 = "Cata Switch Water 1"
    CATA_SWITCH_WATER_2 = "Cata Switch Water 2"
    CATA_SWITCH_DEV_ROOM = "Cata Switch Dev Room"
    CATA_SWITCH_AFTER_BLUE_DOOR = "Cata Switch After Blue Door"
    CATA_SWITCH_SHORTCUT_ACCESS = "Cata Switch Shortcut Access"
    CATA_SWITCH_LADDER_BLOCKS = "Cata Switch Ladder Blocks"
    CATA_SWITCH_MID_SHORTCUT = "Cata Switch Mid Shortcut"
    CATA_SWITCH_1ST_ROOM = "Cata Switch 1st Room"
    CATA_SWITCH_FLAMES_2 = "Cata Switch Flames 2"
    CATA_SWITCH_FLAMES_1 = "Cata Switch Flames 1"
    CATA_CRYSTAL_POISON_ROOTS = "Cata Crystal Poison Roots"
    CATA_FACE_AFTER_BOW = "Cata Face After Bow"
    CATA_FACE_BOW = "Cata Face Bow"
    CATA_FACE_X4 = "Cata Face x4"
    CATA_FACE_CAMPFIRE = "Cata Face Campfire"
    CATA_FACE_DOUBLE_DOOR = "Cata Face Double Door"
    CATA_FACE_BOTTOM = "Cata Face Bottom"
    CATA_CANDLE_1ST_ROOM = "Cata Candle 1st Room"
    CATA_CANDLE_ORB_MULTI = "Cata Candle Orb Multiplier"
    CATA_CANDLE_AFTER_BOW = "Cata Candle After Bow"
    CATA_CANDLE_DEV_ROOM = "Cata Candle Dev Room"
    CATA_CANDLE_GRIFFON = "Cata Candle Griffon"
    CATA_CANDLE_SHORTCUT = "Cata Candle Vertical Shortcut"
    CATA_CANDLE_PRISON = "Cata Candle Prison"
    CATA_CANDLE_ABOVE_ROOTS_1 = "Cata Candle Above Roots 1"
    CATA_CANDLE_ABOVE_ROOTS_2 = "Cata Candle Above Roots 2"
    CATA_CANDLE_ABOVE_ROOTS_3 = "Cata Candle Above Roots 3"
    CATA_CANDLE_ABOVE_ROOTS_4 = "Cata Candle Above Roots 4"
    CATA_CANDLE_ABOVE_ROOTS_5 = "Cata Candle Above Roots 5"
    CATA_CANDLE_VOID_R_1 = "Cata Candle Void Right 1"
    CATA_CANDLE_VOID_R_2 = "Cata Candle Void Right 2"
    CATA_ORB_MULTI = "Cata Orb Multiplier"

    TR_BRAM = "TR Bram"
    TR_ADORNED_KEY = "TR Adorned Key"
    TR_HP_1_BOTTOM = "TR Max HP Up Bottom"
    TR_HP_2_TOP = "TR Max HP Up Top"
    TR_RED_KEY = "TR Red Key"
    TR_ELEVATOR = "TR Elevator"
    TR_SWITCH_ADORNED_L = "TR Switch Adorned Key Left"
    TR_SWITCH_ADORNED_M = "TR Switch Adorned Key Middle"
    TR_SWITCH_ADORNED_R = "TR Switch Adorned Key Right"
    TR_SWITCH_ELEVATOR = "TR Switch Elevator"
    TR_SWITCH_BOTTOM = "TR Switch Bottom"
    TR_CRYSTAL_GOLD = "TR Crystal Gold"
    TR_CRYSTAL_DARK_ARIAS = "TR Crystal Dark Arias"
    TR_CANDLE_1ST_ROOM_1 = "TR Candle 1st Room 1"
    TR_CANDLE_1ST_ROOM_2 = "TR Candle 1st Room 2"
    TR_CANDLE_1ST_ROOM_3 = "TR Candle 1st Room 3"

    CD_CROWN = "CD Prince's Crown"
    CD_ATTACK = "CD Attack Up"
    CD_HP_1 = "CD Max HP Up"
    CD_SWITCH_1 = "CD Switch 1"
    CD_SWITCH_2 = "CD Switch 2"
    CD_SWITCH_3 = "CD Switch 3"
    CD_SWITCH_CAMPFIRE = "CD Switch Campfire"
    CD_SWITCH_TOP = "CD Switch Top"
    CD_CRYSTAL_BACKTRACK = "CD Crystal Backtrack"
    CD_CRYSTAL_START = "CD Crystal Start"
    CD_CRYSTAL_CAMPFIRE = "CD Crystal Campfire"
    CD_CRYSTAL_STEPS = "CD Crystal Steps"
    CD_CANDLE_1 = "CD Candle 1"
    CD_CANDLE_CAMPFIRE_2_1 = "CD Candle 2nd Campfire 1"
    CD_CANDLE_CAMPFIRE_2_2 = "CD Candle 2nd Campfire 2"
    CD_CANDLE_TOP_CAMPFIRE = "CD Candle Top Campfire"

    CATH_BLOCK = "Cath Magic Block"
    CATH_ATTACK = "Cath Attack Up"
    CATH_HP_1_TOP_LEFT = "Cath Max HP Up Top Left"
    CATH_HP_1_TOP_RIGHT = "Cath Max HP Up Top Right"
    CATH_HP_2_CLAW = "Cath Max HP Up Left Climb"
    CATH_HP_5_BELL = "Cath Max HP Up Bell"
    CATH_SWITCH_BOTTOM = "Cath Switch Bottom"
    CATH_SWITCH_BESIDE_SHAFT = "Cath Switch Beside Shaft"
    CATH_SWITCH_TOP_CAMPFIRE = "Cath Switch Top Campfire"
    CATH_CRYSTAL_1ST_ROOM = "Cath Crystal 1st Room"
    CATH_CRYSTAL_SHAFT = "Cath Crystal Shaft"
    CATH_CRYSTAL_SPIKE_PIT = "Cath Crystal Spike Pit"
    CATH_CRYSTAL_TOP_L = "Cath Crystal Top Left"
    CATH_CRYSTAL_TOP_R = "Cath Crystal Top Right"
    CATH_CRYSTAL_SHAFT_ACCESS = "Cath Crystal Shaft Access"
    CATH_CRYSTAL_ORBS = "Cath Crystal Orbs"
    CATH_FACE_LEFT = "Cath Face Left"
    CATH_FACE_RIGHT = "Cath Face Right"
    CATH_CANDLE_TOP_1 = "Cath Candle Top 1"
    CATH_CANDLE_TOP_2 = "Cath Candle Top 2"

    SP_STAR = "SP Morning Star"
    SP_ATTACK = "SP Attack Up"
    SP_HP_1 = "SP Max HP Up"
    SP_BLUE_KEY_BUBBLES = "SP Blue Key Bubbles"
    SP_BLUE_KEY_STAR = "SP Blue Key Morning Star"
    SP_BLUE_KEY_PAINTING = "SP Blue Key Painting"
    SP_BLUE_KEY_ARIAS = "SP Blue Key Arias"
    SP_SWITCH_DOUBLE_DOORS = "SP Switch Double Doors"
    SP_SWITCH_BUBBLES = "SP Switch Bubbles"
    SP_SWITCH_AFTER_STAR = "SP Switch After Star"
    SP_CRYSTAL_BLOCKS = "SP Crystal Blocks"
    SP_CRYSTAL_STAR = "SP Crystal Star"

    SHOP_GIFT = "Gift Purchase"
    SHOP_KNOWLEDGE = "Knowledge Purchase"
    SHOP_MERCY = "Mercy Purchase"
    SHOP_ORB_SEEKER = "Orb Seeker Purchase"
    SHOP_MAP_REVEAL = "Map Reveal Purchase"
    SHOP_CARTOGRAPHER = "Cartographer Purchase"
    SHOP_DEATH_ORB = "Death Orb Purchase"
    SHOP_DEATH_POINT = "Death Point Purchase"
    SHOP_TITANS_EGO = "Titan's Ego Purchase"
    SHOP_ALGUS_ARCANIST = "Arcanist Purchase"
    SHOP_ALGUS_SHOCK = "Shock Field Purchase"
    SHOP_ALGUS_METEOR = "Meteor Rain Purchase"
    SHOP_ARIAS_GORGONSLAYER = "Gorgonslayer Purchase"
    SHOP_ARIAS_LAST_STAND = "Last Stand Purchase"
    SHOP_ARIAS_LIONHEART = "Lionheart Purchase"
    SHOP_KYULI_ASSASSIN = "Assassin Strike Purchase"
    SHOP_KYULI_BULLSEYE = "Bullseye Purchase"
    SHOP_KYULI_RAY = "Shining Ray Purchase"
    SHOP_ZEEK_JUNKYARD = "Junkyard Hunt Purchase"
    SHOP_ZEEK_ORBS = "Orb Monger Purchase"
    SHOP_ZEEK_LOOT = "Bigger Loot Purchase"
    SHOP_BRAM_AXE = "Golden Axe Purchase"
    SHOP_BRAM_HUNTER = "Monster Hunter Purchase"
    SHOP_BRAM_WHIPLASH = "Whiplash Purchase"

    FINAL_BOSS = "Blackheart Medusa"


class AstalonLocation(Location):
    game = GAME_NAME


@dataclass(frozen=True)
class LocationData:
    name: LocationName
    region: RegionName
    group: LocationGroup
    area: Area
    room: str = ""
    description: str = ""


ALL_LOCATIONS: tuple[LocationData, ...] = (
    LocationData(LocationName.GT_GORGONHEART, RegionName.GT_GORGONHEART, LocationGroup.ITEM, Area.GT, room="J21"),
    LocationData(LocationName.GT_ANCIENTS_RING, RegionName.GT_BOTTOM, LocationGroup.ITEM, Area.GT, room="N21"),
    LocationData(LocationName.GT_SWORD, RegionName.GT_SWORD, LocationGroup.ITEM, Area.GT, room="O22"),
    LocationData(LocationName.GT_MAP, RegionName.GT_BOTTOM, LocationGroup.ITEM, Area.GT, room="L21"),
    LocationData(LocationName.GT_ASCENDANT_KEY, RegionName.GT_ASCENDANT_KEY, LocationGroup.ITEM, Area.GT, room="G25"),
    LocationData(LocationName.GT_BANISH, RegionName.GT_LEFT, LocationGroup.ITEM, Area.GT, room="I22"),
    LocationData(LocationName.GT_VOID, RegionName.GT_VOID, LocationGroup.ITEM, Area.GT, room="R21"),
    LocationData(
        LocationName.GT_EYE_RED,
        RegionName.GT_BOSS,
        LocationGroup.ITEM,
        Area.GT,
        room="M26",
        description="Default Tauros, the boss of Gorgon Tomb",
    ),
    LocationData(LocationName.GT_ATTACK, RegionName.GT_BABY_GORGON, LocationGroup.ATTACK, Area.GT, room="L19"),
    LocationData(LocationName.GT_HP_1_RING, RegionName.GT_BOTTOM, LocationGroup.HEALTH, Area.GT, room="N21"),
    LocationData(LocationName.GT_HP_5_KEY, RegionName.GT_ASCENDANT_KEY, LocationGroup.HEALTH, Area.GT, room="G26"),
    LocationData(LocationName.GT_WHITE_KEY_START, RegionName.GT_ENTRANCE, LocationGroup.KEY_WHITE, Area.GT, room="J20"),
    LocationData(LocationName.GT_WHITE_KEY_RIGHT, RegionName.GT_BOTTOM, LocationGroup.KEY_WHITE, Area.GT, room="P21"),
    LocationData(LocationName.GT_WHITE_KEY_BOSS, RegionName.GT_TOP_RIGHT, LocationGroup.KEY_WHITE, Area.GT, room="I25"),
    LocationData(
        LocationName.GT_BLUE_KEY_BONESNAKE,
        RegionName.GT_BOTTOM,
        LocationGroup.KEY_BLUE,
        Area.GT,
        room="O20",
        description="Kill the 4 bonesnakes to make the item drop from the face.",
    ),
    LocationData(LocationName.GT_BLUE_KEY_BUTT, RegionName.GT_BUTT, LocationGroup.KEY_BLUE, Area.GT, room="I26"),
    LocationData(LocationName.GT_BLUE_KEY_WALL, RegionName.GT_BUTT, LocationGroup.KEY_BLUE, Area.GT, room="J26"),
    LocationData(LocationName.GT_BLUE_KEY_POT, RegionName.GT_UPPER_PATH, LocationGroup.KEY_BLUE, Area.GT, room="O21"),
    LocationData(LocationName.GT_RED_KEY, RegionName.GT_BOSS, LocationGroup.KEY_RED, Area.GT, room="K27"),
    LocationData(LocationName.MECH_BOOTS, RegionName.MECH_BOOTS_UPPER, LocationGroup.ITEM, Area.MECH, room="T26"),
    LocationData(LocationName.MECH_CLOAK, RegionName.MECH_CLOAK, LocationGroup.ITEM, Area.MECH, room="O35"),
    LocationData(
        LocationName.MECH_EYE_BLUE,
        RegionName.MECH_BOSS,
        LocationGroup.ITEM,
        Area.MECH,
        room="M33",
        description="Defeat Volantis, the boss of Mechanism",
    ),
    LocationData(LocationName.MECH_ATTACK_VOLANTIS, RegionName.HOP_START, LocationGroup.ATTACK, Area.MECH, room="M34"),
    LocationData(LocationName.MECH_ATTACK_STAR, RegionName.MECH_CHAINS, LocationGroup.ATTACK, Area.MECH, room="R32"),
    LocationData(LocationName.MECH_HP_1_SWITCH, RegionName.MECH_RIGHT, LocationGroup.HEALTH, Area.MECH, room="T33"),
    LocationData(LocationName.MECH_HP_1_STAR, RegionName.MECH_BRAM_TUNNEL, LocationGroup.HEALTH, Area.MECH, room="M32"),
    LocationData(
        LocationName.MECH_HP_3_CLAW,
        RegionName.MECH_BOTTOM_CAMPFIRE,
        LocationGroup.HEALTH,
        Area.MECH,
        room="R23",
    ),
    LocationData(
        LocationName.MECH_WHITE_KEY_LINUS,
        RegionName.MECH_SWORD_CONNECTION,
        LocationGroup.KEY_WHITE,
        Area.MECH,
        room="Q23",
    ),
    LocationData(
        LocationName.MECH_WHITE_KEY_BK,
        RegionName.MECH_AFTER_BK,
        LocationGroup.KEY_WHITE,
        Area.MECH,
        room="O30",
    ),
    LocationData(
        LocationName.MECH_WHITE_KEY_ARENA,
        RegionName.MECH_RIGHT,
        LocationGroup.KEY_WHITE,
        Area.MECH,
        room="U35",
    ),
    LocationData(LocationName.MECH_WHITE_KEY_TOP, RegionName.MECH_TOP, LocationGroup.KEY_WHITE, Area.MECH, room="S38"),
    LocationData(LocationName.MECH_BLUE_KEY_VOID, RegionName.GT_VOID, LocationGroup.KEY_BLUE, Area.MECH, room="S21"),
    LocationData(
        LocationName.MECH_BLUE_KEY_SNAKE,
        RegionName.MECH_SNAKE,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="T21",
    ),
    LocationData(
        LocationName.MECH_BLUE_KEY_LINUS,
        RegionName.MECH_LOWER_ARIAS,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="P25",
    ),
    LocationData(
        LocationName.MECH_BLUE_KEY_SACRIFICE,
        RegionName.MECH_SACRIFICE,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="R26",
    ),
    LocationData(LocationName.MECH_BLUE_KEY_RED, RegionName.MECH_START, LocationGroup.KEY_BLUE, Area.MECH, room="M27"),
    LocationData(
        LocationName.MECH_BLUE_KEY_ARIAS,
        RegionName.MECH_ARIAS_EYEBALL,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="R30",
    ),
    LocationData(
        LocationName.MECH_BLUE_KEY_BLOCKS,
        RegionName.MECH_CHAINS,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="Q31",
    ),
    LocationData(
        LocationName.MECH_BLUE_KEY_TOP,
        RegionName.MECH_SPLIT_PATH,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="T32",
    ),
    LocationData(
        LocationName.MECH_BLUE_KEY_OLD_MAN,
        RegionName.MECH_RIGHT,
        LocationGroup.KEY_BLUE,
        Area.MECH,
        room="V33",
    ),
    LocationData(LocationName.MECH_BLUE_KEY_SAVE, RegionName.MECH_TOP, LocationGroup.KEY_BLUE, Area.MECH, room="S36"),
    LocationData(LocationName.MECH_BLUE_KEY_POT, RegionName.MECH_POTS, LocationGroup.KEY_BLUE, Area.MECH, room="T35"),
    LocationData(LocationName.MECH_RED_KEY, RegionName.MECH_LOWER_VOID, LocationGroup.KEY_RED, Area.MECH, room="K28"),
    LocationData(LocationName.HOP_BELL, RegionName.HOP_BELL, LocationGroup.ITEM, Area.HOP, room="F29"),
    LocationData(LocationName.HOP_AMULET, RegionName.HOP_AMULET, LocationGroup.ITEM, Area.HOP, room="I28"),
    LocationData(LocationName.HOP_CLAW, RegionName.HOP_CLAW, LocationGroup.ITEM, Area.HOP, room="N36"),
    LocationData(LocationName.HOP_GAUNTLET, RegionName.HOP_GAUNTLET, LocationGroup.ITEM, Area.HOP, room="R42"),
    LocationData(LocationName.HOP_MAIDEN_RING, RegionName.HOP_MAIDEN, LocationGroup.ITEM, Area.HOP, room="K43"),
    LocationData(LocationName.HOP_HP_1_CLAW, RegionName.HOP_CLAW_LEFT, LocationGroup.HEALTH, Area.HOP, room="K36"),
    LocationData(LocationName.HOP_HP_2_LADDER, RegionName.HOP_ELEVATOR, LocationGroup.HEALTH, Area.HOP, room="H33"),
    LocationData(
        LocationName.HOP_HP_2_GAUNTLET,
        RegionName.HOP_TP_FALL_TOP,
        LocationGroup.HEALTH,
        Area.HOP,
        room="R39",
    ),
    LocationData(
        LocationName.HOP_HP_5_OLD_MAN,
        RegionName.HOP_ABOVE_OLD_MAN,
        LocationGroup.HEALTH,
        Area.HOP,
        room="G39",
    ),
    LocationData(
        LocationName.HOP_HP_5_MAZE,
        RegionName.HOP_LOWER_VOID_CONNECTION,
        LocationGroup.HEALTH,
        Area.HOP,
        room="K34",
    ),
    LocationData(LocationName.HOP_HP_5_START, RegionName.HOP_START, LocationGroup.HEALTH, Area.HOP, room="L35"),
    LocationData(
        LocationName.HOP_WHITE_KEY_LEFT,
        RegionName.HOP_START_LEFT,
        LocationGroup.KEY_WHITE,
        Area.HOP,
        room="I33",
    ),
    LocationData(
        LocationName.HOP_WHITE_KEY_GHOST,
        RegionName.HOP_LOWER,
        LocationGroup.KEY_WHITE,
        Area.HOP,
        room="J31",
    ),
    LocationData(
        LocationName.HOP_WHITE_KEY_OLD_MAN,
        RegionName.HOP_ELEVATOR,
        LocationGroup.KEY_WHITE,
        Area.HOP,
        room="G35",
    ),
    LocationData(
        LocationName.HOP_WHITE_KEY_BOSS,
        RegionName.HOP_UPPER_ARIAS,
        LocationGroup.KEY_WHITE,
        Area.HOP,
        room="L39",
    ),
    LocationData(
        LocationName.HOP_BLUE_KEY_STATUE,
        RegionName.HOP_EPIMETHEUS,
        LocationGroup.KEY_BLUE,
        Area.HOP,
        room="L30",
    ),
    LocationData(LocationName.HOP_BLUE_KEY_GOLD, RegionName.HOP_LOWER, LocationGroup.KEY_BLUE, Area.HOP, room="K29"),
    LocationData(
        LocationName.HOP_BLUE_KEY_AMULET,
        RegionName.HOP_AMULET_CONNECTION,
        LocationGroup.KEY_BLUE,
        Area.HOP,
        room="J28",
    ),
    LocationData(
        LocationName.HOP_BLUE_KEY_LADDER,
        RegionName.HOP_ELEVATOR,
        LocationGroup.KEY_BLUE,
        Area.HOP,
        room="H33",
    ),
    LocationData(
        LocationName.HOP_BLUE_KEY_TELEPORTS,
        RegionName.HOP_SPIKE_TP_SECRET,
        LocationGroup.KEY_BLUE,
        Area.HOP,
        room="E33",
    ),
    LocationData(
        LocationName.HOP_BLUE_KEY_MAZE,
        RegionName.HOP_TP_FALL_TOP,
        LocationGroup.KEY_BLUE,
        Area.HOP,
        room="N39",
    ),
    LocationData(LocationName.HOP_RED_KEY, RegionName.HOP_RED_KEY, LocationGroup.KEY_RED, Area.HOP, room="I30"),
    LocationData(LocationName.ROA_ICARUS, RegionName.ROA_ICARUS, LocationGroup.ITEM, Area.ROA, room="N55"),
    LocationData(
        LocationName.ROA_EYE_GREEN,
        RegionName.ROA_BOSS,
        LocationGroup.ITEM,
        Area.ROA,
        room="L60",
        description="Defeat Solaria, the boss of Ruins of Ash",
    ),
    LocationData(LocationName.ROA_ATTACK, RegionName.ROA_MIDDLE, LocationGroup.ATTACK, Area.ROA, room="L47"),
    LocationData(LocationName.ROA_HP_1_LEFT, RegionName.ROA_LEFT_ASCENT, LocationGroup.HEALTH, Area.ROA, room="M46"),
    LocationData(LocationName.ROA_HP_2_RIGHT, RegionName.ROA_RIGHT_BRANCH, LocationGroup.HEALTH, Area.ROA, room="Q48"),
    LocationData(LocationName.ROA_HP_5_SOLARIA, RegionName.APEX, LocationGroup.HEALTH, Area.ROA, room="M60"),
    LocationData(LocationName.ROA_WHITE_KEY_SAVE, RegionName.ROA_WORMS, LocationGroup.KEY_WHITE, Area.ROA, room="P41"),
    LocationData(
        LocationName.ROA_WHITE_KEY_REAPERS,
        RegionName.ROA_LEFT_ASCENT,
        LocationGroup.KEY_WHITE,
        Area.ROA,
        room="N44",
    ),
    LocationData(
        LocationName.ROA_WHITE_KEY_TORCHES,
        RegionName.ROA_MIDDLE,
        LocationGroup.KEY_WHITE,
        Area.ROA,
        room="M48",
    ),
    LocationData(
        LocationName.ROA_WHITE_KEY_PORTAL,
        RegionName.ROA_UPPER_VOID,
        LocationGroup.KEY_WHITE,
        Area.ROA,
        room="M52",
    ),
    LocationData(
        LocationName.ROA_BLUE_KEY_FACE,
        RegionName.ROA_BOTTOM_ASCEND,
        LocationGroup.KEY_BLUE,
        Area.ROA,
        room="M43",
    ),
    LocationData(
        LocationName.ROA_BLUE_KEY_FLAMES,
        RegionName.ROA_ARIAS_BABY_GORGON,
        LocationGroup.KEY_BLUE,
        Area.ROA,
        room="Q44",
    ),
    LocationData(
        LocationName.ROA_BLUE_KEY_BABY,
        RegionName.ROA_LEFT_BABY_GORGON,
        LocationGroup.KEY_BLUE,
        Area.ROA,
        room="L48",
    ),
    LocationData(
        LocationName.ROA_BLUE_KEY_TOP,
        RegionName.ROA_ABOVE_CENTAUR_L,
        LocationGroup.KEY_BLUE,
        Area.ROA,
        room="N59",
    ),
    LocationData(
        LocationName.ROA_BLUE_KEY_POT,
        RegionName.ROA_TRIPLE_REAPER,
        LocationGroup.KEY_BLUE,
        Area.ROA,
        room="N43",
    ),
    LocationData(LocationName.ROA_RED_KEY, RegionName.ROA_RED_KEY, LocationGroup.KEY_RED, Area.ROA, room="Q53"),
    LocationData(LocationName.DARK_HP_4, RegionName.DARK_END, LocationGroup.HEALTH, Area.DARK, room="J60"),
    LocationData(LocationName.DARK_WHITE_KEY, RegionName.DARK_END, LocationGroup.KEY_WHITE, Area.DARK, room="I60"),
    LocationData(LocationName.APEX_CHALICE, RegionName.APEX_CENTAUR, LocationGroup.ITEM, Area.APEX, room="T58"),
    LocationData(LocationName.APEX_HP_1_CHALICE, RegionName.APEX, LocationGroup.HEALTH, Area.APEX, room="P58"),
    LocationData(LocationName.APEX_HP_5_HEART, RegionName.APEX_HEART, LocationGroup.HEALTH, Area.APEX, room="R60"),
    LocationData(LocationName.APEX_BLUE_KEY, RegionName.APEX, LocationGroup.KEY_BLUE, Area.APEX, room="O60"),
    LocationData(LocationName.CATA_BOW, RegionName.CATA_BOW, LocationGroup.ITEM, Area.CATA, room="K14"),
    LocationData(
        LocationName.CAVES_ATTACK_RED,
        RegionName.CAVES_ITEM_CHAIN,
        LocationGroup.ATTACK,
        Area.CAVES,
        room="Q17",
    ),
    LocationData(
        LocationName.CAVES_ATTACK_BLUE,
        RegionName.CAVES_ITEM_CHAIN,
        LocationGroup.ATTACK,
        Area.CAVES,
        room="Q17",
    ),
    LocationData(
        LocationName.CAVES_ATTACK_GREEN,
        RegionName.CAVES_ITEM_CHAIN,
        LocationGroup.ATTACK,
        Area.CAVES,
        room="R17",
    ),
    LocationData(
        LocationName.CATA_ATTACK_ROOT,
        RegionName.CATA_CLIMBABLE_ROOT,
        LocationGroup.ATTACK,
        Area.CATA,
        room="N17",
    ),
    LocationData(
        LocationName.CATA_ATTACK_POISON,
        RegionName.CATA_POISON_ROOTS,
        LocationGroup.ATTACK,
        Area.CATA,
        room="S9",
    ),
    LocationData(LocationName.CAVES_HP_1_START, RegionName.CAVES_START, LocationGroup.HEALTH, Area.CAVES, room="P20"),
    LocationData(LocationName.CAVES_HP_1_CYCLOPS, RegionName.CAVES_ARENA, LocationGroup.HEALTH, Area.CAVES, room="S19"),
    LocationData(
        LocationName.CATA_HP_1_ABOVE_POISON,
        RegionName.CATA_POISON_ROOTS,
        LocationGroup.HEALTH,
        Area.CATA,
        room="Q10",
    ),
    LocationData(
        LocationName.CATA_HP_2_BEFORE_POISON,
        RegionName.CATA_POISON_ROOTS,
        LocationGroup.HEALTH,
        Area.CATA,
        room="Q9",
    ),
    LocationData(
        LocationName.CATA_HP_2_AFTER_POISON,
        RegionName.CATA_POISON_ROOTS,
        LocationGroup.HEALTH,
        Area.CATA,
        room="S9",
    ),
    LocationData(
        LocationName.CATA_HP_2_GEMINI_BOTTOM,
        RegionName.CATA_DOUBLE_DOOR,
        LocationGroup.HEALTH,
        Area.CATA,
        room="N7",
    ),
    LocationData(
        LocationName.CATA_HP_2_GEMINI_TOP,
        RegionName.CATA_CENTAUR,
        LocationGroup.HEALTH,
        Area.CATA,
        room="N7",
    ),
    LocationData(
        LocationName.CATA_HP_2_ABOVE_GEMINI,
        RegionName.CATA_FLAMES,
        LocationGroup.HEALTH,
        Area.CATA,
        room="K10",
    ),
    LocationData(
        LocationName.CAVES_HP_5_CHAIN,
        RegionName.CAVES_ITEM_CHAIN,
        LocationGroup.HEALTH,
        Area.CAVES,
        room="S18",
    ),
    LocationData(LocationName.CATA_WHITE_KEY_HEAD, RegionName.CATA_TOP, LocationGroup.KEY_WHITE, Area.CATA, room="M15"),
    LocationData(
        LocationName.CATA_WHITE_KEY_DEV_ROOM,
        RegionName.CATA_DEV_ROOM_CONNECTION,
        LocationGroup.KEY_WHITE,
        Area.CATA,
        room="R13",
    ),
    LocationData(
        LocationName.CATA_WHITE_KEY_PRISON,
        RegionName.CATA_BOSS,
        LocationGroup.KEY_WHITE,
        Area.CATA,
        room="M7",
    ),
    LocationData(
        LocationName.CATA_BLUE_KEY_SLIMES,
        RegionName.CATA_BOW_CAMPFIRE,
        LocationGroup.KEY_BLUE,
        Area.CATA,
        room="O13",
    ),
    LocationData(
        LocationName.CATA_BLUE_KEY_EYEBALLS,
        RegionName.CATA_CENTAUR,
        LocationGroup.KEY_BLUE,
        Area.CATA,
        room="O9",
    ),
    LocationData(LocationName.TR_ADORNED_KEY, RegionName.TR_BOTTOM, LocationGroup.ITEM, Area.TR, room="O2"),
    LocationData(LocationName.TR_HP_1_BOTTOM, RegionName.TR_BOTTOM_LEFT, LocationGroup.HEALTH, Area.TR, room="N1"),
    LocationData(LocationName.TR_HP_2_TOP, RegionName.TR_LEFT, LocationGroup.HEALTH, Area.TR, room="O3"),
    LocationData(LocationName.TR_RED_KEY, RegionName.CATA_BOSS, LocationGroup.KEY_RED, Area.TR, room="J9"),
    LocationData(LocationName.CD_ATTACK, RegionName.CD_TOP, LocationGroup.ATTACK, Area.CD, room="V45"),
    LocationData(LocationName.CD_HP_1, RegionName.CD_TOP, LocationGroup.HEALTH, Area.CD, room="V45"),
    LocationData(LocationName.CATH_BLOCK, RegionName.CATH_TOP, LocationGroup.ITEM, Area.CATH, room="B42"),
    LocationData(
        LocationName.CATH_ATTACK,
        RegionName.CATH_UPPER_SPIKE_PIT,
        LocationGroup.ATTACK,
        Area.CATH,
        room="A37",
    ),
    LocationData(LocationName.CATH_HP_1_TOP_LEFT, RegionName.CATH_TOP, LocationGroup.HEALTH, Area.CATH, room="B39"),
    LocationData(LocationName.CATH_HP_1_TOP_RIGHT, RegionName.CATH_TOP, LocationGroup.HEALTH, Area.CATH, room="B39"),
    LocationData(LocationName.CATH_HP_2_CLAW, RegionName.CATH_LEFT_SHAFT, LocationGroup.HEALTH, Area.CATH, room="A36"),
    LocationData(LocationName.CATH_HP_5_BELL, RegionName.CATH_CAMPFIRE_1, LocationGroup.HEALTH, Area.CATH, room="B35"),
    LocationData(LocationName.SP_STAR, RegionName.SP_STAR, LocationGroup.ITEM, Area.SP, room="D53"),
    LocationData(LocationName.SP_ATTACK, RegionName.SP_CAMPFIRE_2, LocationGroup.ATTACK, Area.SP, room="H45"),
    LocationData(LocationName.SP_HP_1, RegionName.SP_FROG, LocationGroup.HEALTH, Area.SP, room="E44"),
    LocationData(LocationName.SP_BLUE_KEY_BUBBLES, RegionName.SP_START, LocationGroup.KEY_BLUE, Area.SP, room="H51"),
    LocationData(LocationName.SP_BLUE_KEY_STAR, RegionName.SP_STAR_END, LocationGroup.KEY_BLUE, Area.SP, room="G52"),
    LocationData(
        LocationName.SP_BLUE_KEY_PAINTING,
        RegionName.SP_PAINTING,
        LocationGroup.KEY_BLUE,
        Area.SP,
        room="D48",
    ),
    LocationData(LocationName.SP_BLUE_KEY_ARIAS, RegionName.SP_CAMPFIRE_2, LocationGroup.KEY_BLUE, Area.SP, room="F45"),
    LocationData(LocationName.SHOP_GIFT, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_KNOWLEDGE, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_MERCY, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ORB_SEEKER, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_MAP_REVEAL, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_CARTOGRAPHER, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_DEATH_ORB, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_DEATH_POINT, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_TITANS_EGO, RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ALGUS_ARCANIST, RegionName.SHOP_ALGUS, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ALGUS_SHOCK, RegionName.SHOP_ALGUS, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ALGUS_METEOR, RegionName.SHOP_ALGUS, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ARIAS_GORGONSLAYER, RegionName.SHOP_ARIAS, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ARIAS_LAST_STAND, RegionName.SHOP_ARIAS, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ARIAS_LIONHEART, RegionName.SHOP_ARIAS, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_KYULI_ASSASSIN, RegionName.SHOP_KYULI, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_KYULI_BULLSEYE, RegionName.SHOP_KYULI, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_KYULI_RAY, RegionName.SHOP_KYULI, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ZEEK_JUNKYARD, RegionName.SHOP_ZEEK, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ZEEK_ORBS, RegionName.SHOP_ZEEK, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_ZEEK_LOOT, RegionName.SHOP_ZEEK, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_BRAM_AXE, RegionName.SHOP_BRAM, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_BRAM_HUNTER, RegionName.SHOP_BRAM, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.SHOP_BRAM_WHIPLASH, RegionName.SHOP_BRAM, LocationGroup.SHOP, Area.SHOP),
    LocationData(LocationName.GT_ALGUS, RegionName.GT_ENTRANCE, LocationGroup.CHARACTER, Area.GT, room="I17"),
    LocationData(LocationName.GT_ARIAS, RegionName.GT_ENTRANCE, LocationGroup.CHARACTER, Area.GT, room="H18"),
    LocationData(LocationName.GT_KYULI, RegionName.GT_ENTRANCE, LocationGroup.CHARACTER, Area.GT, room="J18"),
    LocationData(LocationName.MECH_ZEEK, RegionName.MECH_ZEEK, LocationGroup.CHARACTER, Area.MECH, room="U29"),
    LocationData(LocationName.TR_BRAM, RegionName.TR_BRAM, LocationGroup.CHARACTER, Area.TR, room="L4"),
    LocationData(LocationName.GT_ELEVATOR_2, RegionName.GT_BOSS, LocationGroup.ELEVATOR, Area.GT, room="L26"),
    LocationData(LocationName.GT_SWITCH_2ND_ROOM, RegionName.GT_ENTRANCE, LocationGroup.SWITCH, Area.GT, room="K20"),
    LocationData(
        LocationName.GT_SWITCH_1ST_CYCLOPS,
        RegionName.GT_GORGONHEART,
        LocationGroup.SWITCH,
        Area.GT,
        room="K22",
    ),
    LocationData(
        LocationName.GT_SWITCH_SPIKE_TUNNEL,
        RegionName.GT_TOP_LEFT,
        LocationGroup.SWITCH,
        Area.GT,
        room="J25",
    ),
    LocationData(
        LocationName.GT_SWITCH_BUTT_ACCESS,
        RegionName.GT_SPIKE_TUNNEL_SWITCH,
        LocationGroup.SWITCH,
        Area.GT,
        room="I25",
    ),
    LocationData(LocationName.GT_SWITCH_GH, RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT, room="J21"),
    LocationData(
        LocationName.GT_SWITCH_UPPER_PATH_BLOCKS,
        RegionName.GT_UPPER_PATH_CONNECTION,
        LocationGroup.SWITCH,
        Area.GT,
        room="P22",
    ),
    LocationData(
        LocationName.GT_SWITCH_UPPER_PATH_ACCESS,
        RegionName.GT_UPPER_PATH_CONNECTION,
        LocationGroup.SWITCH,
        Area.GT,
        room="P22",
    ),
    LocationData(LocationName.GT_SWITCH_CROSSES, RegionName.GT_LEFT, LocationGroup.SWITCH, Area.GT, room="J22"),
    LocationData(
        LocationName.GT_SWITCH_GH_SHORTCUT,
        RegionName.GT_GORGONHEART,
        LocationGroup.SWITCH,
        Area.GT,
        room="J20",
    ),
    LocationData(LocationName.GT_SWITCH_ARIAS_PATH, RegionName.GT_TOP_LEFT, LocationGroup.SWITCH, Area.GT, room="I24"),
    LocationData(
        LocationName.GT_SWITCH_SWORD_ACCESS,
        RegionName.GT_SWORD_FORK,
        LocationGroup.SWITCH,
        Area.GT,
        room="N22",
    ),
    LocationData(
        LocationName.GT_SWITCH_SWORD_BACKTRACK,
        RegionName.GT_SWORD_FORK,
        LocationGroup.SWITCH,
        Area.GT,
        room="N22",
    ),
    LocationData(LocationName.GT_SWITCH_SWORD, RegionName.GT_SWORD, LocationGroup.SWITCH, Area.GT, room="O22"),
    LocationData(
        LocationName.GT_SWITCH_UPPER_ARIAS,
        RegionName.GT_ARIAS_SWORD_SWITCH,
        LocationGroup.SWITCH,
        Area.GT,
        room="O24",
    ),
    LocationData(
        LocationName.GT_CRYSTAL_LADDER,
        RegionName.GT_LADDER_SWITCH,
        LocationGroup.SWITCH,
        Area.GT,
        room="N24",
    ),
    LocationData(LocationName.GT_CRYSTAL_ROTA, RegionName.GT_UPPER_PATH, LocationGroup.SWITCH, Area.GT, room="N21"),
    LocationData(
        LocationName.GT_CRYSTAL_OLD_MAN_1,
        RegionName.GT_OLD_MAN_FORK,
        LocationGroup.SWITCH,
        Area.GT,
        room="M24",
    ),
    LocationData(
        LocationName.GT_CRYSTAL_OLD_MAN_2,
        RegionName.GT_OLD_MAN_FORK,
        LocationGroup.SWITCH,
        Area.GT,
        room="M24",
    ),
    LocationData(
        LocationName.MECH_ELEVATOR_1,
        RegionName.MECH_ZEEK_CONNECTION,
        LocationGroup.ELEVATOR,
        Area.MECH,
        room="Q29",
    ),
    LocationData(LocationName.MECH_ELEVATOR_2, RegionName.MECH_BOSS, LocationGroup.ELEVATOR, Area.MECH, room="N33"),
    LocationData(LocationName.MECH_SWITCH_WATCHER, RegionName.MECH_ROOTS, LocationGroup.SWITCH, Area.MECH, room="O27"),
    LocationData(LocationName.MECH_SWITCH_CHAINS, RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH, room="Q33"),
    LocationData(
        LocationName.MECH_SWITCH_BOSS_ACCESS_1,
        RegionName.MECH_BOSS_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="O32",
    ),
    LocationData(
        LocationName.MECH_SWITCH_BOSS_ACCESS_2,
        RegionName.MECH_BRAM_TUNNEL_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="O32",
    ),
    LocationData(
        LocationName.MECH_SWITCH_SPLIT_PATH,
        RegionName.MECH_CHAINS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R32",
    ),
    LocationData(
        LocationName.MECH_SWITCH_SNAKE_1,
        RegionName.MECH_BOTTOM_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.MECH,
        room="S21",
    ),
    LocationData(
        LocationName.MECH_SWITCH_BOOTS_ACCESS,
        RegionName.MECH_BOOTS_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="S24",
    ),
    LocationData(
        LocationName.MECH_SWITCH_UPPER_GT_ACCESS,
        RegionName.MECH_BOTTOM_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.MECH,
        room="Q22",
    ),
    LocationData(
        LocationName.MECH_SWITCH_UPPER_VOID_DROP,
        RegionName.MECH_RIGHT,
        LocationGroup.SWITCH,
        Area.MECH,
        room="S34",
    ),
    LocationData(
        LocationName.MECH_SWITCH_UPPER_VOID,
        RegionName.MECH_UPPER_VOID,
        LocationGroup.SWITCH,
        Area.MECH,
        room="T33",
    ),
    LocationData(LocationName.MECH_SWITCH_LINUS, RegionName.MECH_LINUS, LocationGroup.SWITCH, Area.MECH, room="Q25"),
    LocationData(
        LocationName.MECH_SWITCH_TO_BOSS_2,
        RegionName.MECH_BOSS_SWITCHES,
        LocationGroup.SWITCH,
        Area.MECH,
        room="P32",
    ),
    LocationData(
        LocationName.MECH_SWITCH_POTS,
        RegionName.MECH_BELOW_POTS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="T35",
    ),
    LocationData(
        LocationName.MECH_SWITCH_MAZE_BACKDOOR,
        RegionName.HOP_FALL_BOTTOM,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R36",
    ),
    LocationData(
        LocationName.MECH_SWITCH_TO_BOSS_1,
        RegionName.MECH_BOSS_SWITCHES,
        LocationGroup.SWITCH,
        Area.MECH,
        room="P32",
    ),
    LocationData(
        LocationName.MECH_SWITCH_BLOCK_STAIRS,
        RegionName.MECH_CLOAK_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="Q33",
    ),
    LocationData(
        LocationName.MECH_SWITCH_ARIAS_CYCLOPS,
        RegionName.MECH_CHARACTER_SWAPS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R35",
    ),
    LocationData(
        LocationName.MECH_SWITCH_BOOTS_LOWER,
        RegionName.MECH_BOOTS_LOWER,
        LocationGroup.SWITCH,
        Area.MECH,
        room="T24",
    ),
    LocationData(
        LocationName.MECH_SWITCH_CHAINS_GAP,
        RegionName.MECH_CHAINS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="P30",
    ),
    LocationData(
        LocationName.MECH_SWITCH_LOWER_KEY,
        RegionName.MECH_SWORD_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="Q23",
    ),
    LocationData(
        LocationName.MECH_SWITCH_ARIAS,
        RegionName.MECH_ARIAS_EYEBALL,
        LocationGroup.SWITCH,
        Area.MECH,
        room="S30",
    ),
    LocationData(LocationName.MECH_SWITCH_SNAKE_2, RegionName.MECH_SNAKE, LocationGroup.SWITCH, Area.MECH, room="S21"),
    LocationData(
        LocationName.MECH_SWITCH_KEY_BLOCKS,
        RegionName.MECH_CHAINS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="Q31",
    ),
    LocationData(LocationName.MECH_SWITCH_CANNON, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH, room="N27"),
    LocationData(
        LocationName.MECH_SWITCH_EYEBALL,
        RegionName.MECH_BELOW_POTS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="U34",
    ),
    LocationData(
        LocationName.MECH_SWITCH_INVISIBLE,
        RegionName.MECH_RIGHT,
        LocationGroup.SWITCH,
        Area.MECH,
        room="T33",
    ),
    LocationData(LocationName.MECH_CRYSTAL_CANNON, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH, room="N27"),
    LocationData(LocationName.MECH_CRYSTAL_LINUS, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH, room="Q25"),
    LocationData(
        LocationName.MECH_CRYSTAL_LOWER,
        RegionName.MECH_SWORD_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="Q24",
    ),
    LocationData(
        LocationName.MECH_CRYSTAL_TO_BOSS_3,
        RegionName.MECH_BOSS_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="O32",
    ),
    LocationData(
        LocationName.MECH_CRYSTAL_TRIPLE_1,
        RegionName.MECH_TRIPLE_SWITCHES,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R33",
    ),
    LocationData(
        LocationName.MECH_CRYSTAL_TRIPLE_2,
        RegionName.MECH_TRIPLE_SWITCHES,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R33",
    ),
    LocationData(
        LocationName.MECH_CRYSTAL_TRIPLE_3,
        RegionName.MECH_TRIPLE_SWITCHES,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R33",
    ),
    LocationData(LocationName.MECH_CRYSTAL_TOP, RegionName.MECH_TOP, LocationGroup.SWITCH, Area.MECH, room="S36"),
    LocationData(
        LocationName.MECH_CRYSTAL_CLOAK,
        RegionName.MECH_CLOAK_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
        room="P34",
    ),
    LocationData(
        LocationName.MECH_CRYSTAL_SLIMES,
        RegionName.MECH_BOSS_SWITCHES,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R34",
    ),
    LocationData(LocationName.MECH_CRYSTAL_TO_CD, RegionName.MECH_TOP, LocationGroup.SWITCH, Area.MECH, room="U36"),
    LocationData(LocationName.MECH_CRYSTAL_CAMPFIRE, RegionName.MECH_BK, LocationGroup.SWITCH, Area.MECH, room="P28"),
    LocationData(
        LocationName.MECH_CRYSTAL_1ST_ROOM,
        RegionName.MECH_START,
        LocationGroup.SWITCH,
        Area.MECH,
        room="N26",
    ),
    LocationData(LocationName.MECH_CRYSTAL_OLD_MAN, RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH, room="V33"),
    LocationData(
        LocationName.MECH_CRYSTAL_TOP_CHAINS,
        RegionName.MECH_CHAINS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="R32",
    ),
    LocationData(LocationName.MECH_CRYSTAL_BK, RegionName.MECH_BK, LocationGroup.SWITCH, Area.MECH, room="P29"),
    LocationData(
        LocationName.MECH_FACE_ABOVE_VOLANTIS,
        RegionName.MECH_BOSS,
        LocationGroup.SWITCH,
        Area.MECH,
        room="M34",
    ),
    LocationData(LocationName.HOP_ELEVATOR, RegionName.HOP_ELEVATOR, LocationGroup.ELEVATOR, Area.HOP, room="F34"),
    LocationData(
        LocationName.HOP_SWITCH_ROCK,
        RegionName.HOP_AMULET_CONNECTION,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J27",
    ),
    LocationData(
        LocationName.HOP_SWITCH_BELOW_START,
        RegionName.HOP_START_BOTTOM_MID,
        LocationGroup.SWITCH,
        Area.HOP,
        room="L32",
    ),
    LocationData(
        LocationName.HOP_SWITCH_LEFT_2,
        RegionName.HOP_START_MID,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J33",
    ),
    LocationData(
        LocationName.HOP_SWITCH_LEFT_1,
        RegionName.HOP_START_MID,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J33",
    ),
    LocationData(
        LocationName.HOP_SWITCH_LOWER_SHORTCUT,
        RegionName.HOP_LOWER,
        LocationGroup.SWITCH,
        Area.HOP,
        room="K31",
    ),
    LocationData(LocationName.HOP_SWITCH_BELL, RegionName.HOP_BELL, LocationGroup.SWITCH, Area.HOP, room="F29"),
    LocationData(
        LocationName.HOP_SWITCH_GHOST_BLOOD,
        RegionName.HOP_GHOST_BLOOD,
        LocationGroup.SWITCH,
        Area.HOP,
        room="G32",
    ),
    LocationData(
        LocationName.HOP_SWITCH_TELEPORTS,
        RegionName.HOP_LOWER_ARIAS,
        LocationGroup.SWITCH,
        Area.HOP,
        room="G31",
    ),
    LocationData(
        LocationName.HOP_SWITCH_WORM_PILLAR,
        RegionName.HOP_ELEVATOR,
        LocationGroup.SWITCH,
        Area.HOP,
        room="G33",
    ),
    LocationData(
        LocationName.HOP_SWITCH_TO_CLAW_1,
        RegionName.HOP_ELEVATOR,
        LocationGroup.SWITCH,
        Area.HOP,
        room="H35",
    ),
    LocationData(
        LocationName.HOP_SWITCH_TO_CLAW_2,
        RegionName.HOP_ELEVATOR,
        LocationGroup.SWITCH,
        Area.HOP,
        room="H35",
    ),
    LocationData(
        LocationName.HOP_SWITCH_CLAW_ACCESS,
        RegionName.HOP_CLAW_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.HOP,
        room="L36",
    ),
    LocationData(
        LocationName.HOP_SWITCH_GHOSTS,
        RegionName.HOP_START_MID,
        LocationGroup.SWITCH,
        Area.HOP,
        room="K32",
    ),
    LocationData(
        LocationName.HOP_SWITCH_LEFT_3,
        RegionName.HOP_START_MID,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J33",
    ),
    LocationData(
        LocationName.HOP_SWITCH_ABOVE_OLD_MAN,
        RegionName.HOP_ABOVE_OLD_MAN,
        LocationGroup.SWITCH,
        Area.HOP,
        room="G38",
    ),
    LocationData(
        LocationName.HOP_SWITCH_TO_ABOVE_OLD_MAN,
        RegionName.HOP_TOP_LEFT,
        LocationGroup.SWITCH,
        Area.HOP,
        room="H37",
    ),
    LocationData(
        LocationName.HOP_SWITCH_TP_PUZZLE,
        RegionName.HOP_TP_PUZZLE,
        LocationGroup.SWITCH,
        Area.HOP,
        room="N40",
    ),
    LocationData(
        LocationName.HOP_SWITCH_EYEBALL_SHORTCUT,
        RegionName.HOP_WORM_SHORTCUT,
        LocationGroup.SWITCH,
        Area.HOP,
        room="G32",
    ),
    LocationData(
        LocationName.HOP_SWITCH_BELL_ACCESS,
        RegionName.HOP_BELL_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.HOP,
        room="G29",
    ),
    LocationData(LocationName.HOP_SWITCH_1ST_ROOM, RegionName.HOP_START, LocationGroup.SWITCH, Area.HOP, room="L33"),
    LocationData(
        LocationName.HOP_SWITCH_LEFT_BACKTRACK,
        RegionName.HOP_ELEVATOR,
        LocationGroup.SWITCH,
        Area.HOP,
        room="I33",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_ROCK_ACCESS,
        RegionName.HOP_MECH_VOID_CONNECTION,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J27",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_BOTTOM,
        RegionName.HOP_MECH_VOID_CONNECTION,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J29",
    ),
    LocationData(LocationName.HOP_CRYSTAL_LOWER, RegionName.HOP_LOWER, LocationGroup.SWITCH, Area.HOP, room="K31"),
    LocationData(
        LocationName.HOP_CRYSTAL_AFTER_CLAW,
        RegionName.HOP_CLAW_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.HOP,
        room="K38",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_MAIDEN_1,
        RegionName.HOP_MAIDEN,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J41",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_MAIDEN_2,
        RegionName.HOP_MAIDEN,
        LocationGroup.SWITCH,
        Area.HOP,
        room="J42",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_BELL_ACCESS,
        RegionName.HOP_BELL_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.HOP,
        room="H29",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_HEART,
        RegionName.HOP_BOSS_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.HOP,
        room="L38",
    ),
    LocationData(
        LocationName.HOP_CRYSTAL_BELOW_PUZZLE,
        RegionName.HOP_TP_FALL_TOP,
        LocationGroup.SWITCH,
        Area.HOP,
        room="N39",
    ),
    LocationData(LocationName.HOP_FACE_OLD_MAN, RegionName.HOP_ELEVATOR, LocationGroup.SWITCH, Area.HOP, room="F36"),
    LocationData(LocationName.ROA_ELEVATOR_1, RegionName.HOP_BOSS, LocationGroup.ELEVATOR, Area.ROA, room="M41"),
    LocationData(LocationName.ROA_ELEVATOR_2, RegionName.ROA_ELEVATOR, LocationGroup.ELEVATOR, Area.ROA, room="O57"),
    LocationData(
        LocationName.ROA_SWITCH_ASCEND,
        RegionName.ROA_BOTTOM_ASCEND,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N43",
    ),
    LocationData(
        LocationName.ROA_SWITCH_AFTER_WORMS,
        RegionName.ROA_WORMS_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N42",
    ),
    LocationData(
        LocationName.ROA_SWITCH_RIGHT_PATH,
        RegionName.ROA_RIGHT_SWITCH_1,
        LocationGroup.SWITCH,
        Area.ROA,
        room="O48",
    ),
    LocationData(
        LocationName.ROA_SWITCH_APEX_ACCESS,
        RegionName.ROA_APEX_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="M60",
    ),
    LocationData(LocationName.ROA_SWITCH_ICARUS, RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA, room="N55"),
    LocationData(
        LocationName.ROA_SWITCH_SHAFT_L,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N51",
    ),
    LocationData(
        LocationName.ROA_SWITCH_SHAFT_R,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N51",
    ),
    LocationData(LocationName.ROA_SWITCH_ELEVATOR, RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA, room="N57"),
    LocationData(
        LocationName.ROA_SWITCH_SHAFT_DOWNWARDS,
        RegionName.ROA_SP_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N53",
    ),
    LocationData(LocationName.ROA_SWITCH_SPIDERS, RegionName.ROA_SPIDERS_2, LocationGroup.SWITCH, Area.ROA, room="P54"),
    LocationData(
        LocationName.ROA_SWITCH_DARK_ROOM,
        RegionName.ROA_ELEVATOR,
        LocationGroup.SWITCH,
        Area.ROA,
        room="L54",
    ),
    LocationData(
        LocationName.ROA_SWITCH_ASCEND_SHORTCUT,
        RegionName.ROA_MIDDLE,
        LocationGroup.SWITCH,
        Area.ROA,
        room="M46",
    ),
    LocationData(
        LocationName.ROA_SWITCH_1ST_SHORTCUT,
        RegionName.ROA_BOTTOM_ASCEND,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N42",
    ),
    LocationData(
        LocationName.ROA_SWITCH_SPIKE_CLIMB,
        RegionName.ROA_SPIKE_CLIMB,
        LocationGroup.SWITCH,
        Area.ROA,
        room="L42",
    ),
    LocationData(
        LocationName.ROA_SWITCH_ABOVE_CENTAUR,
        RegionName.ROA_SP_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="L54",
    ),
    LocationData(
        LocationName.ROA_SWITCH_BLOOD_POT,
        RegionName.ROA_TOP_CENTAUR,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N58",
    ),
    LocationData(LocationName.ROA_SWITCH_WORMS, RegionName.ROA_WORMS, LocationGroup.SWITCH, Area.ROA, room="P42"),
    LocationData(
        LocationName.ROA_SWITCH_TRIPLE_1,
        RegionName.ROA_TRIPLE_SWITCH,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N46",
    ),
    LocationData(
        LocationName.ROA_SWITCH_TRIPLE_3,
        RegionName.ROA_TRIPLE_SWITCH,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N46",
    ),
    LocationData(
        LocationName.ROA_SWITCH_BABY_GORGON,
        RegionName.ROA_FLAMES,
        LocationGroup.SWITCH,
        Area.ROA,
        room="Q44",
    ),
    LocationData(
        LocationName.ROA_SWITCH_BOSS_ACCESS,
        RegionName.ROA_BOSS_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="L59",
    ),
    LocationData(
        LocationName.ROA_SWITCH_BLOOD_POT_L,
        RegionName.ROA_BOSS_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="M59",
    ),
    LocationData(
        LocationName.ROA_SWITCH_BLOOD_POT_R,
        RegionName.ROA_BOSS_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="M59",
    ),
    LocationData(
        LocationName.ROA_SWITCH_LOWER_VOID,
        RegionName.ROA_LOWER_VOID,
        LocationGroup.SWITCH,
        Area.ROA,
        room="P43",
    ),
    LocationData(LocationName.ROA_CRYSTAL_1ST_ROOM, RegionName.ROA_START, LocationGroup.SWITCH, Area.ROA, room="O41"),
    LocationData(
        LocationName.ROA_CRYSTAL_BABY_GORGON,
        RegionName.ROA_LOWER_VOID_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="P44",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_LADDER_R,
        RegionName.ROA_RIGHT_SWITCH_2,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N48",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_LADDER_L,
        RegionName.ROA_LEFT_SWITCH,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N48",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_CENTAUR,
        RegionName.ROA_CRYSTAL_ABOVE_CENTAUR,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N59",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_SPIKE_BALLS,
        RegionName.ROA_UPPER_VOID,
        LocationGroup.SWITCH,
        Area.ROA,
        room="O52",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_LEFT_ASCEND,
        RegionName.ROA_LEFT_ASCENT_CRYSTAL,
        LocationGroup.SWITCH,
        Area.ROA,
        room="M45",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_SHAFT,
        RegionName.ROA_SP_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N52",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_BRANCH_R,
        RegionName.ROA_RIGHT_BRANCH,
        LocationGroup.SWITCH,
        Area.ROA,
        room="Q48",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_BRANCH_L,
        RegionName.ROA_RIGHT_BRANCH,
        LocationGroup.SWITCH,
        Area.ROA,
        room="Q48",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_3_REAPERS,
        RegionName.ROA_TRIPLE_REAPER,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N44",
    ),
    LocationData(
        LocationName.ROA_CRYSTAL_TRIPLE_2,
        RegionName.ROA_TRIPLE_SWITCH,
        LocationGroup.SWITCH,
        Area.ROA,
        room="N46",
    ),
    LocationData(LocationName.ROA_FACE_SPIDERS, RegionName.ROA_SPIDERS_1, LocationGroup.SWITCH, Area.ROA, room="P53"),
    LocationData(
        LocationName.ROA_FACE_BLUE_KEY,
        RegionName.ROA_BOTTOM_ASCEND,
        LocationGroup.SWITCH,
        Area.ROA,
        room="M43",
    ),
    LocationData(LocationName.DARK_SWITCH, RegionName.DARK_START, LocationGroup.SWITCH, Area.DARK, room="J59"),
    LocationData(LocationName.APEX_ELEVATOR, RegionName.APEX, LocationGroup.ELEVATOR, Area.APEX, room="N60"),
    LocationData(LocationName.APEX_SWITCH, RegionName.APEX, LocationGroup.SWITCH, Area.APEX, room="P61"),
    LocationData(
        LocationName.CAVES_SWITCH_SKELETONS,
        RegionName.CAVES_UPPER,
        LocationGroup.SWITCH,
        Area.CAVES,
        room="P18",
    ),
    LocationData(
        LocationName.CAVES_SWITCH_CATA_ACCESS_1,
        RegionName.CAVES_LOWER,
        LocationGroup.SWITCH,
        Area.CAVES,
        room="P16",
    ),
    LocationData(
        LocationName.CAVES_SWITCH_CATA_ACCESS_2,
        RegionName.CAVES_LOWER,
        LocationGroup.SWITCH,
        Area.CAVES,
        room="P16",
    ),
    LocationData(
        LocationName.CAVES_SWITCH_CATA_ACCESS_3,
        RegionName.CAVES_LOWER,
        LocationGroup.SWITCH,
        Area.CAVES,
        room="P16",
    ),
    LocationData(
        LocationName.CAVES_FACE_1ST_ROOM,
        RegionName.CAVES_START,
        LocationGroup.SWITCH,
        Area.CAVES,
        room="P20",
    ),
    LocationData(LocationName.CATA_ELEVATOR_1, RegionName.CATA_ELEVATOR, LocationGroup.ELEVATOR, Area.CATA, room="L16"),
    LocationData(LocationName.CATA_ELEVATOR_2, RegionName.CATA_BOSS, LocationGroup.ELEVATOR, Area.CATA, room="L8"),
    LocationData(LocationName.CATA_SWITCH_ELEVATOR, RegionName.CATA_TOP, LocationGroup.SWITCH, Area.CATA, room="M16"),
    LocationData(
        LocationName.CATA_SWITCH_SHORTCUT,
        RegionName.CATA_VERTICAL_SHORTCUT,
        LocationGroup.SWITCH,
        Area.CATA,
        room="M14",
    ),
    LocationData(LocationName.CATA_SWITCH_TOP, RegionName.CATA_TOP, LocationGroup.SWITCH, Area.CATA, room="N15"),
    LocationData(
        LocationName.CATA_SWITCH_CLAW_1,
        RegionName.CATA_SNAKE_MUSHROOMS,
        LocationGroup.SWITCH,
        Area.CATA,
        room="O12",
    ),
    LocationData(
        LocationName.CATA_SWITCH_CLAW_2,
        RegionName.CATA_SNAKE_MUSHROOMS,
        LocationGroup.SWITCH,
        Area.CATA,
        room="O12",
    ),
    LocationData(
        LocationName.CATA_SWITCH_WATER_1,
        RegionName.CATA_DOUBLE_SWITCH,
        LocationGroup.SWITCH,
        Area.CATA,
        room="N11",
    ),
    LocationData(
        LocationName.CATA_SWITCH_WATER_2,
        RegionName.CATA_DOUBLE_SWITCH,
        LocationGroup.SWITCH,
        Area.CATA,
        room="N11",
    ),
    LocationData(
        LocationName.CATA_SWITCH_DEV_ROOM,
        RegionName.CATA_SNAKE_MUSHROOMS,
        LocationGroup.SWITCH,
        Area.CATA,
        room="Q12",
    ),
    LocationData(
        LocationName.CATA_SWITCH_AFTER_BLUE_DOOR,
        RegionName.CATA_BLUE_EYE_DOOR,
        LocationGroup.SWITCH,
        Area.CATA,
        room="N10",
    ),
    LocationData(
        LocationName.CATA_SWITCH_SHORTCUT_ACCESS,
        RegionName.CATA_FLAMES_FORK,
        LocationGroup.SWITCH,
        Area.CATA,
        room="M10",
    ),
    LocationData(
        LocationName.CATA_SWITCH_LADDER_BLOCKS,
        RegionName.CATA_FLAMES_FORK,
        LocationGroup.SWITCH,
        Area.CATA,
        room="M10",
    ),
    LocationData(
        LocationName.CATA_SWITCH_MID_SHORTCUT,
        RegionName.CATA_VERTICAL_SHORTCUT,
        LocationGroup.SWITCH,
        Area.CATA,
        room="M13",
    ),
    LocationData(LocationName.CATA_SWITCH_1ST_ROOM, RegionName.CATA_START, LocationGroup.SWITCH, Area.CATA, room="O16"),
    LocationData(
        LocationName.CATA_SWITCH_FLAMES_2,
        RegionName.CATA_FLAMES_FORK,
        LocationGroup.SWITCH,
        Area.CATA,
        room="L10",
    ),
    LocationData(
        LocationName.CATA_SWITCH_FLAMES_1,
        RegionName.CATA_FLAMES_FORK,
        LocationGroup.SWITCH,
        Area.CATA,
        room="L10",
    ),
    LocationData(
        LocationName.CATA_CRYSTAL_POISON_ROOTS,
        RegionName.CATA_POISON_ROOTS,
        LocationGroup.SWITCH,
        Area.CATA,
        room="Q10",
    ),
    LocationData(
        LocationName.CATA_FACE_AFTER_BOW,
        RegionName.CATA_BOW_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.CATA,
        room="O14",
    ),
    LocationData(LocationName.CATA_FACE_BOW, RegionName.CATA_BOW, LocationGroup.SWITCH, Area.CATA, room="L14"),
    LocationData(LocationName.CATA_FACE_X4, RegionName.CATA_4_FACES, LocationGroup.SWITCH, Area.CATA, room="O8"),
    LocationData(LocationName.CATA_FACE_CAMPFIRE, RegionName.CATA_BOSS, LocationGroup.SWITCH, Area.CATA, room="M8"),
    LocationData(
        LocationName.CATA_FACE_DOUBLE_DOOR,
        RegionName.CATA_DOUBLE_DOOR,
        LocationGroup.SWITCH,
        Area.CATA,
        room="P8",
    ),
    LocationData(
        LocationName.CATA_FACE_BOTTOM,
        RegionName.CATA_DOUBLE_DOOR,
        LocationGroup.SWITCH,
        Area.CATA,
        room="O7",
    ),
    LocationData(LocationName.TR_ELEVATOR, RegionName.TR_START, LocationGroup.ELEVATOR, Area.TR, room="L3"),
    LocationData(LocationName.TR_SWITCH_ADORNED_L, RegionName.TR_BOTTOM, LocationGroup.SWITCH, Area.TR, room="O2"),
    LocationData(LocationName.TR_SWITCH_ADORNED_M, RegionName.TR_LEFT, LocationGroup.SWITCH, Area.TR, room="O2"),
    LocationData(LocationName.TR_SWITCH_ADORNED_R, RegionName.TR_DARK_ARIAS, LocationGroup.SWITCH, Area.TR, room="O2"),
    LocationData(LocationName.TR_SWITCH_ELEVATOR, RegionName.CATA_BOSS, LocationGroup.SWITCH, Area.TR, room="J5"),
    LocationData(LocationName.TR_SWITCH_BOTTOM, RegionName.TR_MIDDLE_RIGHT, LocationGroup.SWITCH, Area.TR, room="P1"),
    LocationData(LocationName.TR_CRYSTAL_GOLD, RegionName.TR_TOP_RIGHT, LocationGroup.SWITCH, Area.TR, room="P3"),
    LocationData(
        LocationName.TR_CRYSTAL_DARK_ARIAS,
        RegionName.TR_DARK_ARIAS,
        LocationGroup.SWITCH,
        Area.TR,
        room="P2",
    ),
    LocationData(LocationName.CD_SWITCH_1, RegionName.CD_START, LocationGroup.SWITCH, Area.CD, room="W38"),
    LocationData(LocationName.CD_SWITCH_2, RegionName.CD_2, LocationGroup.SWITCH, Area.CD, room="X38"),
    LocationData(LocationName.CD_SWITCH_3, RegionName.CD_3, LocationGroup.SWITCH, Area.CD, room="X39"),
    LocationData(LocationName.CD_SWITCH_CAMPFIRE, RegionName.CD_MIDDLE, LocationGroup.SWITCH, Area.CD, room="U40"),
    LocationData(LocationName.CD_SWITCH_TOP, RegionName.CD_TOP, LocationGroup.SWITCH, Area.CD, room="V45"),
    LocationData(LocationName.CD_CRYSTAL_BACKTRACK, RegionName.CD_2, LocationGroup.SWITCH, Area.CD, room="W38"),
    LocationData(LocationName.CD_CRYSTAL_START, RegionName.CD_START, LocationGroup.SWITCH, Area.CD, room="W37"),
    LocationData(LocationName.CD_CRYSTAL_CAMPFIRE, RegionName.CD_CAMPFIRE_3, LocationGroup.SWITCH, Area.CD, room="U42"),
    LocationData(LocationName.CD_CRYSTAL_STEPS, RegionName.CD_STEPS, LocationGroup.SWITCH, Area.CD, room="T43"),
    LocationData(
        LocationName.CATH_SWITCH_BOTTOM,
        RegionName.CATH_START_RIGHT,
        LocationGroup.SWITCH,
        Area.CATH,
        room="B32",
    ),
    LocationData(
        LocationName.CATH_SWITCH_BESIDE_SHAFT,
        RegionName.CATH_SHAFT_ACCESS,
        LocationGroup.SWITCH,
        Area.CATH,
        room="A35",
    ),
    LocationData(
        LocationName.CATH_SWITCH_TOP_CAMPFIRE,
        RegionName.CATH_TOP,
        LocationGroup.SWITCH,
        Area.CATH,
        room="C38",
    ),
    LocationData(
        LocationName.CATH_CRYSTAL_1ST_ROOM,
        RegionName.CATH_START_TOP_LEFT,
        LocationGroup.SWITCH,
        Area.CATH,
        room="B31",
    ),
    LocationData(
        LocationName.CATH_CRYSTAL_SHAFT,
        RegionName.CATH_LEFT_SHAFT,
        LocationGroup.SWITCH,
        Area.CATH,
        room="A33",
    ),
    LocationData(LocationName.CATH_CRYSTAL_SPIKE_PIT, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH, room="A38"),
    LocationData(LocationName.CATH_CRYSTAL_TOP_L, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH, room="B42"),
    LocationData(LocationName.CATH_CRYSTAL_TOP_R, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH, room="B42"),
    LocationData(
        LocationName.CATH_CRYSTAL_SHAFT_ACCESS,
        RegionName.CATH_SHAFT_ACCESS,
        LocationGroup.SWITCH,
        Area.CATH,
        room="A35",
    ),
    LocationData(LocationName.CATH_CRYSTAL_ORBS, RegionName.CATH_ORB_ROOM, LocationGroup.SWITCH, Area.CATH, room="B36"),
    LocationData(LocationName.CATH_FACE_LEFT, RegionName.CATH_START_LEFT, LocationGroup.SWITCH, Area.CATH, room="A32"),
    LocationData(LocationName.CATH_FACE_RIGHT, RegionName.CATH_START_LEFT, LocationGroup.SWITCH, Area.CATH, room="A32"),
    LocationData(LocationName.SP_SWITCH_DOUBLE_DOORS, RegionName.SP_HEARTS, LocationGroup.SWITCH, Area.SP, room="F46"),
    LocationData(LocationName.SP_SWITCH_BUBBLES, RegionName.SP_CAMPFIRE_1, LocationGroup.SWITCH, Area.SP, room="F48"),
    LocationData(
        LocationName.SP_SWITCH_AFTER_STAR,
        RegionName.SP_STAR_CONNECTION,
        LocationGroup.SWITCH,
        Area.SP,
        room="F52",
    ),
    LocationData(LocationName.SP_CRYSTAL_BLOCKS, RegionName.SP_START, LocationGroup.SWITCH, Area.SP, room="G50"),
    LocationData(LocationName.SP_CRYSTAL_STAR, RegionName.SP_SHAFT, LocationGroup.SWITCH, Area.SP, room="D51"),
    LocationData(LocationName.MECH_CYCLOPS, RegionName.MECH_ZEEK, LocationGroup.ITEM, Area.MECH, room="U29"),
    LocationData(LocationName.CD_CROWN, RegionName.CD_BOSS, LocationGroup.ITEM, Area.CD, room="Z37"),
    LocationData(LocationName.GT_CANDLE_LINUS, RegionName.GT_BOTTOM, LocationGroup.CANDLE, Area.GT, room="L21"),
    LocationData(LocationName.GT_CANDLE_1ST_CYCLOPS, RegionName.GT_LEFT, LocationGroup.CANDLE, Area.GT, room="K22"),
    LocationData(LocationName.GT_CANDLE_BOSS, RegionName.GT_BOSS, LocationGroup.CANDLE, Area.GT, room="J26"),
    LocationData(LocationName.GT_CANDLE_BOTTOM, RegionName.GT_BOTTOM, LocationGroup.CANDLE, Area.GT, room="L20"),
    LocationData(LocationName.MECH_CANDLE_ROOTS, RegionName.MECH_ROOTS, LocationGroup.CANDLE, Area.MECH, room="P27"),
    LocationData(
        LocationName.MECH_CANDLE_BOTTOM,
        RegionName.MECH_BOTTOM_CAMPFIRE,
        LocationGroup.CANDLE,
        Area.MECH,
        room="S22",
    ),
    LocationData(
        LocationName.MECH_CANDLE_CHAINS,
        RegionName.MECH_CHAINS_CANDLE,
        LocationGroup.CANDLE,
        Area.MECH,
        room="Q30",
    ),
    LocationData(
        LocationName.MECH_CANDLE_RIGHT,
        RegionName.MECH_SPLIT_PATH,
        LocationGroup.CANDLE,
        Area.MECH,
        room="T31",
    ),
    LocationData(
        LocationName.MECH_CANDLE_POTS,
        RegionName.MECH_BELOW_POTS,
        LocationGroup.CANDLE,
        Area.MECH,
        room="T34",
    ),
    LocationData(
        LocationName.MECH_CANDLE_BOSS_1,
        RegionName.MECH_BOSS_CONNECTION,
        LocationGroup.CANDLE,
        Area.MECH,
        room="O32",
    ),
    LocationData(LocationName.MECH_CANDLE_BOSS_2, RegionName.MECH_BOSS, LocationGroup.CANDLE, Area.MECH, room="O32"),
    LocationData(
        LocationName.MECH_CANDLE_SLIMES,
        RegionName.MECH_CLOAK_CONNECTION,
        LocationGroup.CANDLE,
        Area.MECH,
        room="R33",
    ),
    LocationData(
        LocationName.MECH_CANDLE_ZEEK,
        RegionName.MECH_ZEEK_CONNECTION,
        LocationGroup.CANDLE,
        Area.MECH,
        room="S29",
    ),
    LocationData(
        LocationName.MECH_CANDLE_MAZE_BACKDOOR,
        RegionName.HOP_FALL_BOTTOM,
        LocationGroup.CANDLE,
        Area.MECH,
        room="R36",
    ),
    LocationData(
        LocationName.MECH_CANDLE_CD_ACCESS_1,
        RegionName.MECH_CD_ACCESS,
        LocationGroup.CANDLE,
        Area.MECH,
        room="V36",
    ),
    LocationData(
        LocationName.MECH_CANDLE_CD_ACCESS_2,
        RegionName.MECH_CD_ACCESS,
        LocationGroup.CANDLE,
        Area.MECH,
        room="V36",
    ),
    LocationData(
        LocationName.MECH_CANDLE_CD_ACCESS_3,
        RegionName.MECH_CD_ACCESS,
        LocationGroup.CANDLE,
        Area.MECH,
        room="V36",
    ),
    LocationData(LocationName.MECH_CANDLE_1ST_ROOM, RegionName.MECH_START, LocationGroup.CANDLE, Area.MECH, room="N26"),
    LocationData(LocationName.MECH_CANDLE_BK, RegionName.MECH_BK, LocationGroup.CANDLE, Area.MECH, room="P28"),
    LocationData(
        LocationName.MECH_CANDLE_CAMPFIRE_R,
        RegionName.MECH_RIGHT,
        LocationGroup.CANDLE,
        Area.MECH,
        room="T32",
    ),
    LocationData(LocationName.HOP_CANDLE_1ST_ROOM, RegionName.HOP_START, LocationGroup.CANDLE, Area.HOP, room="L33"),
    LocationData(LocationName.HOP_CANDLE_LOWER, RegionName.HOP_LOWER, LocationGroup.CANDLE, Area.HOP, room="K30"),
    LocationData(
        LocationName.HOP_CANDLE_BELL,
        RegionName.HOP_BELL_CAMPFIRE,
        LocationGroup.CANDLE,
        Area.HOP,
        room="H30",
    ),
    LocationData(
        LocationName.HOP_CANDLE_EYEBALL,
        RegionName.HOP_EYEBALL,
        LocationGroup.CANDLE,
        Area.HOP,
        room="F32",
    ),
    LocationData(
        LocationName.HOP_CANDLE_OLD_MAN,
        RegionName.HOP_ELEVATOR,
        LocationGroup.CANDLE,
        Area.HOP,
        room="F36",
    ),
    LocationData(
        LocationName.HOP_CANDLE_BEFORE_CLAW,
        RegionName.HOP_TOP_LEFT,
        LocationGroup.CANDLE,
        Area.HOP,
        room="H36",
    ),
    LocationData(
        LocationName.HOP_CANDLE_CLAW_CAMPFIRE,
        RegionName.HOP_CLAW_CAMPFIRE,
        LocationGroup.CANDLE,
        Area.HOP,
        room="K37",
    ),
    LocationData(
        LocationName.HOP_CANDLE_TP_PUZZLE,
        RegionName.HOP_BOSS_CAMPFIRE,
        LocationGroup.CANDLE,
        Area.HOP,
        room="L40",
    ),
    LocationData(
        LocationName.HOP_CANDLE_BOSS,
        RegionName.HOP_BOSS_CAMPFIRE,
        LocationGroup.CANDLE,
        Area.HOP,
        room="L41",
    ),
    LocationData(
        LocationName.HOP_CANDLE_TP_FALL,
        RegionName.HOP_TP_FALL_TOP,
        LocationGroup.CANDLE,
        Area.HOP,
        room="P40",
    ),
    LocationData(
        LocationName.HOP_CANDLE_UPPER_VOID_1,
        RegionName.HOP_UPPER_VOID,
        LocationGroup.CANDLE,
        Area.HOP,
        room="O37",
    ),
    LocationData(
        LocationName.HOP_CANDLE_UPPER_VOID_2,
        RegionName.HOP_UPPER_VOID,
        LocationGroup.CANDLE,
        Area.HOP,
        room="O37",
    ),
    LocationData(
        LocationName.HOP_CANDLE_UPPER_VOID_3,
        RegionName.HOP_UPPER_VOID,
        LocationGroup.CANDLE,
        Area.HOP,
        room="O37",
    ),
    LocationData(
        LocationName.HOP_CANDLE_UPPER_VOID_4,
        RegionName.HOP_UPPER_VOID,
        LocationGroup.CANDLE,
        Area.HOP,
        room="O37",
    ),
    LocationData(
        LocationName.HOP_CANDLE_ELEVATOR,
        RegionName.HOP_ELEVATOR,
        LocationGroup.CANDLE,
        Area.HOP,
        room="G34",
    ),
    LocationData(LocationName.ROA_CANDLE_1ST_ROOM, RegionName.ROA_START, LocationGroup.CANDLE, Area.ROA, room="O41"),
    LocationData(
        LocationName.ROA_CANDLE_3_REAPERS,
        RegionName.ROA_LEFT_ASCENT,
        LocationGroup.CANDLE,
        Area.ROA,
        room="M44",
    ),
    LocationData(
        LocationName.ROA_CANDLE_MIDDLE_CAMPFIRE,
        RegionName.ROA_MIDDLE,
        LocationGroup.CANDLE,
        Area.ROA,
        room="O47",
    ),
    LocationData(
        LocationName.ROA_CANDLE_LADDER_BOTTOM,
        RegionName.ROA_MIDDLE,
        LocationGroup.CANDLE,
        Area.ROA,
        room="N48",
    ),
    LocationData(LocationName.ROA_CANDLE_SHAFT, RegionName.ROA_UPPER_VOID, LocationGroup.CANDLE, Area.ROA, room="N52"),
    LocationData(
        LocationName.ROA_CANDLE_SHAFT_TOP,
        RegionName.ROA_SP_CONNECTION,
        LocationGroup.CANDLE,
        Area.ROA,
        room="N54",
    ),
    LocationData(
        LocationName.ROA_CANDLE_ABOVE_CENTAUR,
        RegionName.ROA_SP_CONNECTION,
        LocationGroup.CANDLE,
        Area.ROA,
        room="M54",
    ),
    LocationData(
        LocationName.ROA_CANDLE_BABY_GORGON,
        RegionName.ROA_ELEVATOR,
        LocationGroup.CANDLE,
        Area.ROA,
        room="N56",
    ),
    LocationData(
        LocationName.ROA_CANDLE_TOP_CENTAUR,
        RegionName.ROA_TOP_CENTAUR,
        LocationGroup.CANDLE,
        Area.ROA,
        room="N59",
    ),
    LocationData(
        LocationName.ROA_CANDLE_HIDDEN_1,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.CANDLE,
        Area.ROA,
        room="P50",
    ),
    LocationData(
        LocationName.ROA_CANDLE_HIDDEN_2,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.CANDLE,
        Area.ROA,
        room="P50",
    ),
    LocationData(
        LocationName.ROA_CANDLE_HIDDEN_3,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.CANDLE,
        Area.ROA,
        room="P50",
    ),
    LocationData(
        LocationName.ROA_CANDLE_HIDDEN_4,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.CANDLE,
        Area.ROA,
        room="P50",
    ),
    LocationData(
        LocationName.ROA_CANDLE_HIDDEN_5,
        RegionName.ROA_MIDDLE_LADDER,
        LocationGroup.CANDLE,
        Area.ROA,
        room="P50",
    ),
    LocationData(
        LocationName.ROA_CANDLE_BOTTOM_ASCEND,
        RegionName.ROA_BOTTOM_ASCEND,
        LocationGroup.CANDLE,
        Area.ROA,
        room="N43",
    ),
    LocationData(
        LocationName.ROA_CANDLE_BRANCH,
        RegionName.ROA_RIGHT_BRANCH,
        LocationGroup.CANDLE,
        Area.ROA,
        room="Q48",
    ),
    LocationData(LocationName.ROA_CANDLE_ICARUS_1, RegionName.ROA_ICARUS, LocationGroup.CANDLE, Area.ROA, room="N55"),
    LocationData(LocationName.ROA_CANDLE_ICARUS_2, RegionName.ROA_ICARUS, LocationGroup.CANDLE, Area.ROA, room="N55"),
    LocationData(LocationName.ROA_CANDLE_ELEVATOR, RegionName.ROA_ELEVATOR, LocationGroup.CANDLE, Area.ROA, room="O57"),
    LocationData(
        LocationName.ROA_CANDLE_ELEVATOR_CAMPFIRE,
        RegionName.ROA_ELEVATOR,
        LocationGroup.CANDLE,
        Area.ROA,
        room="O56",
    ),
    LocationData(LocationName.ROA_CANDLE_BOSS_1, RegionName.ROA_BOSS, LocationGroup.CANDLE, Area.ROA, room="K60"),
    LocationData(LocationName.ROA_CANDLE_BOSS_2, RegionName.ROA_BOSS, LocationGroup.CANDLE, Area.ROA, room="K60"),
    LocationData(LocationName.ROA_CANDLE_SPIDERS, RegionName.ROA_SPIDERS_1, LocationGroup.CANDLE, Area.ROA, room="P53"),
    LocationData(
        LocationName.ROA_CANDLE_SPIKE_BALLS,
        RegionName.ROA_UPPER_VOID,
        LocationGroup.CANDLE,
        Area.ROA,
        room="O52",
    ),
    LocationData(
        LocationName.ROA_CANDLE_LADDER_R,
        RegionName.ROA_RIGHT_SWITCH_CANDLE,
        LocationGroup.CANDLE,
        Area.ROA,
        room="N49",
    ),
    LocationData(LocationName.ROA_CANDLE_ARENA, RegionName.ROA_ARENA, LocationGroup.CANDLE, Area.ROA, room="O44"),
    LocationData(LocationName.APEX_CANDLE_ELEVATOR, RegionName.APEX, LocationGroup.CANDLE, Area.APEX, room="O60"),
    LocationData(
        LocationName.APEX_CANDLE_CHALICE_1,
        RegionName.APEX_CENTAUR_ACCESS,
        LocationGroup.CANDLE,
        Area.APEX,
        room="Q58",
    ),
    LocationData(
        LocationName.APEX_CANDLE_CHALICE_2,
        RegionName.APEX_CENTAUR_ACCESS,
        LocationGroup.CANDLE,
        Area.APEX,
        room="R58",
    ),
    LocationData(
        LocationName.APEX_CANDLE_CHALICE_3,
        RegionName.APEX_CENTAUR_ACCESS,
        LocationGroup.CANDLE,
        Area.APEX,
        room="R58",
    ),
    LocationData(LocationName.APEX_CANDLE_GARG_1, RegionName.APEX, LocationGroup.CANDLE, Area.APEX, room="O59"),
    LocationData(LocationName.APEX_CANDLE_GARG_2, RegionName.APEX, LocationGroup.CANDLE, Area.APEX, room="O59"),
    LocationData(LocationName.APEX_CANDLE_GARG_3, RegionName.APEX, LocationGroup.CANDLE, Area.APEX, room="O59"),
    LocationData(LocationName.APEX_CANDLE_GARG_4, RegionName.APEX, LocationGroup.CANDLE, Area.APEX, room="O59"),
    LocationData(LocationName.CATA_CANDLE_1ST_ROOM, RegionName.CATA_START, LocationGroup.CANDLE, Area.CATA, room="O16"),
    LocationData(
        LocationName.CATA_CANDLE_ORB_MULTI,
        RegionName.CATA_MULTI,
        LocationGroup.CANDLE,
        Area.CATA,
        room="K16",
    ),
    LocationData(
        LocationName.CATA_CANDLE_AFTER_BOW,
        RegionName.CATA_EYEBALL_BONES,
        LocationGroup.CANDLE,
        Area.CATA,
        room="O14",
    ),
    LocationData(
        LocationName.CATA_CANDLE_DEV_ROOM,
        RegionName.CATA_SNAKE_MUSHROOMS,
        LocationGroup.CANDLE,
        Area.CATA,
        room="Q12",
    ),
    LocationData(
        LocationName.CATA_CANDLE_GRIFFON,
        RegionName.CATA_DOUBLE_SWITCH,
        LocationGroup.CANDLE,
        Area.CATA,
        room="O12",
    ),
    LocationData(
        LocationName.CATA_CANDLE_SHORTCUT,
        RegionName.CATA_VERTICAL_SHORTCUT,
        LocationGroup.CANDLE,
        Area.CATA,
        room="M14",
    ),
    LocationData(LocationName.CATA_CANDLE_PRISON, RegionName.CATA_BOSS, LocationGroup.CANDLE, Area.CATA, room="M7"),
    LocationData(
        LocationName.CATA_CANDLE_ABOVE_ROOTS_1,
        RegionName.CATA_ABOVE_ROOTS,
        LocationGroup.CANDLE,
        Area.CATA,
        room="P11",
    ),
    LocationData(
        LocationName.CATA_CANDLE_ABOVE_ROOTS_2,
        RegionName.CATA_ABOVE_ROOTS,
        LocationGroup.CANDLE,
        Area.CATA,
        room="P11",
    ),
    LocationData(
        LocationName.CATA_CANDLE_ABOVE_ROOTS_3,
        RegionName.CATA_ABOVE_ROOTS,
        LocationGroup.CANDLE,
        Area.CATA,
        room="P11",
    ),
    LocationData(
        LocationName.CATA_CANDLE_ABOVE_ROOTS_4,
        RegionName.CATA_ABOVE_ROOTS,
        LocationGroup.CANDLE,
        Area.CATA,
        room="P11",
    ),
    LocationData(
        LocationName.CATA_CANDLE_ABOVE_ROOTS_5,
        RegionName.CATA_ABOVE_ROOTS,
        LocationGroup.CANDLE,
        Area.CATA,
        room="P11",
    ),
    LocationData(LocationName.CATA_CANDLE_VOID_R_1, RegionName.CATA_VOID_R, LocationGroup.CANDLE, Area.CATA, room="Q8"),
    LocationData(LocationName.CATA_CANDLE_VOID_R_2, RegionName.CATA_VOID_R, LocationGroup.CANDLE, Area.CATA, room="Q8"),
    LocationData(LocationName.TR_CANDLE_1ST_ROOM_1, RegionName.TR_START, LocationGroup.CANDLE, Area.TR, room="M3"),
    LocationData(LocationName.TR_CANDLE_1ST_ROOM_2, RegionName.TR_START, LocationGroup.CANDLE, Area.TR, room="M3"),
    LocationData(LocationName.TR_CANDLE_1ST_ROOM_3, RegionName.TR_START, LocationGroup.CANDLE, Area.TR, room="M3"),
    LocationData(LocationName.CD_CANDLE_1, RegionName.CD_START, LocationGroup.CANDLE, Area.CD, room="W38"),
    LocationData(LocationName.CD_CANDLE_CAMPFIRE_2_1, RegionName.CD_MIDDLE, LocationGroup.CANDLE, Area.CD, room="U40"),
    LocationData(LocationName.CD_CANDLE_CAMPFIRE_2_2, RegionName.CD_MIDDLE, LocationGroup.CANDLE, Area.CD, room="U40"),
    LocationData(LocationName.CD_CANDLE_TOP_CAMPFIRE, RegionName.CD_TOP, LocationGroup.CANDLE, Area.CD, room="S45"),
    LocationData(LocationName.CATH_CANDLE_TOP_1, RegionName.CATH_TOP, LocationGroup.CANDLE, Area.CATH, room="B42"),
    LocationData(LocationName.CATH_CANDLE_TOP_2, RegionName.CATH_TOP, LocationGroup.CANDLE, Area.CATH, room="B42"),
    LocationData(LocationName.GT_ELEVATOR_1, RegionName.GT_ENTRANCE, LocationGroup.ELEVATOR, Area.GT, room="I20"),
    LocationData(
        LocationName.MECH_SKULL_PUZZLE,
        RegionName.MECH_SPLIT_PATH,
        LocationGroup.SWITCH,
        Area.MECH,
        room="S31",
    ),
    LocationData(
        LocationName.HOP_SKULL_PUZZLE,
        RegionName.HOP_TP_TUTORIAL,
        LocationGroup.SWITCH,
        Area.HOP,
        room="I31",
    ),
    LocationData(LocationName.GT_ORB_MULTI, RegionName.GT_ENTRANCE, LocationGroup.ORBS, Area.GT, room="K19"),
    LocationData(LocationName.MECH_ORB_MULTI, RegionName.MECH_AFTER_BK, LocationGroup.ORBS, Area.MECH, room="P31"),
    LocationData(LocationName.CATA_ORB_MULTI, RegionName.CATA_MULTI, LocationGroup.ORBS, Area.CATA, room="K16"),
)

location_table: dict[str, LocationData] = {location.name.value: location for location in ALL_LOCATIONS}
location_name_to_id: dict[str, int] = {data.name.value: i for i, data in enumerate(ALL_LOCATIONS, start=1)}


def get_location_group(location_name: str) -> LocationGroup:
    return location_table[location_name].group


def get_location_area(location_name: str) -> Area:
    return location_table[location_name].area


location_name_groups: dict[str, set[str]] = {
    group.value: set(location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
location_name_groups.update(
    {
        group.value: set(location_names)
        for group, location_names in groupby(sorted(location_table, key=get_location_area), get_location_area)
    }
)
