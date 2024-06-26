from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import Dict, Set

from BaseClasses import Location

from .regions import RegionName


class Area(str, Enum):
    SHOP = "Shop"
    GT = "Gorgon Tomb"
    MECH = "Mechanism"
    HOTP = "Hall of the Phantoms"
    ROA = "Ruins of Ash"
    DARK = "Darkness"
    APEX = "The Apex"
    CAVES = "Caves"
    CATA = "Catacombs"
    TR = "Tower Roots"
    CD = "Cyclops Den"
    CATH = "Cathedral"
    SP = "Serpent Path"


class LocationGroup(str, Enum):
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


class LocationName(str, Enum):
    GT_ALGUS = "Gorgon Tomb - Algus"
    GT_ARIAS = "Gorgon Tomb - Arias"
    GT_KYULI = "Gorgon Tomb - Kyuli"
    GT_GORGONHEART = "Gorgon Tomb - Gorgonheart"
    GT_ANCIENTS_RING = "Gorgon Tomb - Ring of the Ancients"
    GT_SWORD = "Gorgon Tomb - Sword of Mirrors"
    GT_MAP = "Gorgon Tomb - Linus' Map"
    GT_ASCENDANT_KEY = "Gorgon Tomb - Ascendant Key"
    GT_BANISH = "Gorgon Tomb - Banish Spell"
    GT_VOID = "Gorgon Tomb - Void Charm"
    GT_EYE_RED = "Gorgon Tomb - Gorgon Eye (Red)"
    GT_OLD_MAN = "Gorgon Tomb - Old Man"
    GT_ATTACK = "Gorgon Tomb - Attack +1"
    GT_HP_1_RING = "Gorgon Tomb - Max HP +1 (Ring of the Ancients)"
    GT_HP_5_KEY = "Gorgon Tomb - Max HP +5 (Ascendant Key)"
    GT_WHITE_KEY_START = "Gorgon Tomb - White Key (First Room)"
    GT_WHITE_KEY_RIGHT = "Gorgon Tomb - White Key (Right Side)"
    GT_WHITE_KEY_BOSS = "Gorgon Tomb - White Key (Before Boss)"
    GT_BLUE_KEY_BONESNAKE = "Gorgon Tomb - Blue Key (Bonesnakes)"
    GT_BLUE_KEY_BUTT = "Gorgon Tomb - Blue Key (Butt)"
    GT_BLUE_KEY_WALL = "Gorgon Tomb - Blue Key (Inside Wall)"
    GT_BLUE_KEY_POT = "Gorgon Tomb - Blue Key (Pot)"
    GT_RED_KEY = "Gorgon Tomb - Red Key"
    GT_ELEVATOR_2 = "Gorgon Tomb - Elevator 2"
    GT_SWITCH_2ND_ROOM = "Gorgon Tomb - Switch (2nd Room)"
    GT_SWITCH_1ST_CYCLOPS = "Gorgon Tomb - Switch (1st Cyclops)"
    GT_SWITCH_SPIKE_TUNNEL = "Gorgon Tomb - Switch (Spike Tunnel Access)"
    GT_SWITCH_BUTT_ACCESS = "Gorgon Tomb - Switch (Butt Access)"
    GT_SWITCH_GH = "Gorgon Tomb - Switch (Gorgonheart)"
    GT_SWITCH_UPPER_PATH_BLOCKS = "Gorgon Tomb - Switch (Upper Path Blocks)"
    GT_SWITCH_UPPER_PATH_ACCESS = "Gorgon Tomb - Switch (Upper Path Access)"
    GT_SWITCH_CROSSES = "Gorgon Tomb - Switch (Crosses)"
    GT_SWITCH_GH_SHORTCUT = "Gorgon Tomb - Switch (Gorgonheart Shortcut)"
    GT_SWITCH_ARIAS_PATH = "Gorgon Tomb - Switch (Arias's Path)"
    GT_SWITCH_SWORD_ACCESS = "Gorgon Tomb - Switch (Sword Access)"
    GT_SWITCH_SWORD_BACKTRACK = "Gorgon Tomb - Switch (Sword Backtrack)"
    GT_SWITCH_SWORD = "Gorgon Tomb - Switch (Sword)"
    GT_SWITCH_UPPER_ARIAS = "Gorgon Tomb - Switch (Upper Arias)"
    GT_CRYSTAL_LADDER = "Gorgon Tomb - Crystal (Ladder)"
    GT_CRYSTAL_ROTA = "Gorgon Tomb - Crystal (Ring of the Ancients)"
    GT_CRYSTAL_OLD_MAN_1 = "Gorgon Tomb - Crystal (Old Man 1)"
    GT_CRYSTAL_OLD_MAN_2 = "Gorgon Tomb - Crystal (Old Man 2)"

    MECH_ZEEK = "Mechanism - Zeek"
    MECH_BOOTS = "Mechanism - Talaria Boots"
    MECH_CLOAK = "Mechanism - Cloak of Levitation"
    MECH_CYCLOPS = "Mechanism - Cyclops Idol"
    MECH_EYE_BLUE = "Mechanism - Gorgon Eye (Blue)"
    MECH_OLD_MAN = "Mechanism - Old Man"
    MECH_ATTACK_VOLANTIS = "Mechanism - Attack +1 (Above Volantis)"
    MECH_ATTACK_STAR = "Mechanism - Attack +1 (Morning Star Blocks)"
    MECH_HP_1_SWITCH = "Mechanism - Max HP +1 (Secret Switch)"
    MECH_HP_1_STAR = "Mechanism - Max HP +1 (Morning Star Blocks)"
    MECH_HP_3_CLAW = "Mechanism - Max HP +3 (Above Checkpoint)"
    MECH_WHITE_KEY_LINUS = "Mechanism - White Key (Below Linus)"
    MECH_WHITE_KEY_BK = "Mechanism - White Key (Black Knight)"
    MECH_WHITE_KEY_ARENA = "Mechanism - White Key (Enemy Arena)"
    MECH_WHITE_KEY_TOP = "Mechanism - White Key (Top)"
    MECH_BLUE_KEY_VOID = "Mechanism - Blue Key (Void Charm)"
    MECH_BLUE_KEY_SNAKE = "Mechanism - Blue Key (Snake Head)"
    MECH_BLUE_KEY_LINUS = "Mechanism - Blue Key (Linus)"
    MECH_BLUE_KEY_SACRIFICE = "Mechanism - Blue Key (Sacrifice)"
    MECH_BLUE_KEY_RED = "Mechanism - Blue Key (To Red Key)"
    MECH_BLUE_KEY_ARIAS = "Mechanism - Blue Key (Arias)"
    MECH_BLUE_KEY_BLOCKS = "Mechanism - Blue Key (Switch Blocks)"
    MECH_BLUE_KEY_TOP = "Mechanism - Blue Key (Top Path)"
    MECH_BLUE_KEY_OLD_MAN = "Mechanism - Blue Key (Old Man)"
    MECH_BLUE_KEY_SAVE = "Mechanism - Blue Key (Checkpoint)"
    MECH_BLUE_KEY_POT = "Mechanism - Blue Key (Pot)"
    MECH_RED_KEY = "Mechanism - Red Key"
    MECH_ELEVATOR_1 = "Mechanism - Elevator 1"
    MECH_ELEVATOR_2 = "Mechanism - Elevator 2"
    MECH_SWITCH_WATCHER = "Mechanism - Switch (Watcher)"
    MECH_SWITCH_CHAINS = "Mechanism - Switch (Chains)"
    MECH_SWITCH_BOSS_ACCESS_1 = "Mechanism - Switch (Boss Access 1)"
    MECH_SWITCH_BOSS_ACCESS_2 = "Mechanism - Switch (Boss Access 2)"
    MECH_SWITCH_SPLIT_PATH = "Mechanism - Switch (Split Path)"
    MECH_SWITCH_SNAKE_1 = "Mechanism - Switch (Snake 1)"
    MECH_SWITCH_BOOTS_ACCESS = "Mechanism - Switch (Boots Access)"
    MECH_SWITCH_UPPER_GT_ACCESS = "Mechanism - Switch (Upper GT Access)"
    MECH_SWITCH_UPPER_VOID_DROP = "Mechanism - Switch (Upper Void Drop)"
    MECH_SWITCH_UPPER_VOID = "Mechanism - Switch (Upper Void)"
    MECH_SWITCH_LINUS = "Mechanism - Switch (Linus)"
    MECH_SWITCH_TO_BOSS_2 = "Mechanism - Switch (To Boss 2)"
    MECH_SWITCH_POTS = "Mechanism - Switch (Pots)"
    MECH_SWITCH_MAZE_BACKDOOR = "Mechanism - Switch (Maze Backdoor)"
    MECH_SWITCH_TO_BOSS_1 = "Mechanism - Switch (To Boss 1)"
    MECH_SWITCH_BLOCK_STAIRS = "Mechanism - Switch (Block Stairs)"
    MECH_SWITCH_ARIAS_CYCLOPS = "Mechanism - Switch (Arias Cyclops)"
    MECH_SWITCH_BOOTS_LOWER = "Mechanism - Switch (Boots Lower)"
    MECH_SWITCH_CHAINS_GAP = "Mechanism - Switch (Chains Gap)"
    MECH_SWITCH_LOWER_KEY = "Mechanism - Switch (Lower Key)"
    MECH_SWITCH_ARIAS = "Mechanism - Switch (Arias)"
    MECH_SWITCH_SNAKE_2 = "Mechanism - Switch (Snake 2)"
    MECH_SWITCH_KEY_BLOCKS = "Mechanism - Switch (Key Blocks)"
    MECH_SWITCH_CANNON = "Mechanism - Switch (Cannon)"
    MECH_SWITCH_EYEBALL = "Mechanism - Switch (Eyeball)"
    MECH_SWITCH_INVISIBLE = "Mechanism - Switch (Invisible)"
    MECH_CRYSTAL_CANNON = "Mechanism - Crystal (Cannon)"
    MECH_CRYSTAL_LINUS = "Mechanism - Crystal (Linus)"
    MECH_CRYSTAL_LOWER = "Mechanism - Crystal (Lower)"
    MECH_CRYSTAL_TO_BOSS_3 = "Mechanism - Crystal (To Boss 3)"
    MECH_CRYSTAL_TRIPLE_1 = "Mechanism - Crystal (Triple 1)"
    MECH_CRYSTAL_TRIPLE_2 = "Mechanism - Crystal (Triple 2)"
    MECH_CRYSTAL_TRIPLE_3 = "Mechanism - Crystal (Triple 3)"
    MECH_CRYSTAL_TOP = "Mechanism - Crystal (Top)"
    MECH_CRYSTAL_CLOAK = "Mechanism - Crystal (Cloak)"
    MECH_CRYSTAL_SLIMES = "Mechanism - Crystal (Slimes)"
    MECH_CRYSTAL_TO_CD = "Mechanism - Crystal (To CD)"
    MECH_CRYSTAL_CAMPFIRE = "Mechanism - Crystal (Campfire)"
    MECH_CRYSTAL_1ST_ROOM = "Mechanism - Crystal (1st Room)"
    MECH_CRYSTAL_OLD_MAN = "Mechanism - Crystal (Old Man)"
    MECH_CRYSTAL_TOP_CHAINS = "Mechanism - Crystal (Top Chains)"
    MECH_CRYSTAL_BK = "Mechanism - Crystal (Black Knight)"
    MECH_FACE_ABOVE_VOLANTIS = "Mechanism - Face (Above Volantis)"

    HOTP_BELL = "Hall of the Phantoms - Athena's Bell"
    HOTP_AMULET = "Hall of the Phantoms - Amulet of Sol"
    HOTP_CLAW = "Hall of the Phantoms - Griffon Claw"
    HOTP_GAUNTLET = "Hall of the Phantoms - Boreas Gauntlet"
    HOTP_MAIDEN_RING = "Hall of the Phantoms - Dead Maiden's Ring"
    HOTP_OLD_MAN = "Hall of the Phantoms - Old Man"
    HOTP_HP_1_CLAW = "Hall of the Phantoms - Max HP +1 (Griffon Claw)"
    HOTP_HP_2_LADDER = "Hall of the Phantoms - Max HP +2 (Secret Ladder)"
    HOTP_HP_2_GAUNTLET = "Hall of the Phantoms - Max HP +2 (Boreas Gauntlet)"
    HOTP_HP_5_OLD_MAN = "Hall of the Phantoms - Max HP +5 (Old Man)"
    HOTP_HP_5_MAZE = "Hall of the Phantoms - Max HP +5 (Teleport Maze)"
    HOTP_HP_5_START = "Hall of the Phantoms - Max HP +5 (Above Start)"
    HOTP_WHITE_KEY_LEFT = "Hall of the Phantoms - White Key (Left of Start)"
    HOTP_WHITE_KEY_GHOST = "Hall of the Phantoms - White Key (Ghost)"
    HOTP_WHITE_KEY_OLD_MAN = "Hall of the Phantoms - White Key (Old Man)"
    HOTP_WHITE_KEY_BOSS = "Hall of the Phantoms - White Key (Boss)"
    HOTP_BLUE_KEY_STATUE = "Hall of the Phantoms - Blue Key (Epimetheus)"
    HOTP_BLUE_KEY_GOLD = "Hall of the Phantoms - Blue Key (Gold Hint)"
    HOTP_BLUE_KEY_AMULET = "Hall of the Phantoms - Blue Key (Amulet of Sol)"
    HOTP_BLUE_KEY_LADDER = "Hall of the Phantoms - Blue Key (Secret Ladder)"
    HOTP_BLUE_KEY_TELEPORTS = "Hall of the Phantoms - Blue Key (Spike Teleporters)"
    HOTP_BLUE_KEY_MAZE = "Hall of the Phantoms - Blue Key (Teleport Maze)"
    HOTP_RED_KEY = "Hall of the Phantoms - Red Key"
    HOTP_ELEVATOR = "Hall of the Phantoms - Elevator"
    HOTP_SWITCH_ROCK = "Hall of the Phantoms - Switch (Rock)"
    HOTP_SWITCH_BELOW_START = "Hall of the Phantoms - Switch (Below Start)"
    HOTP_SWITCH_LEFT_2 = "Hall of the Phantoms - Switch (Left 2)"
    HOTP_SWITCH_LEFT_1 = "Hall of the Phantoms - Switch (Left 1)"
    HOTP_SWITCH_LOWER_SHORTCUT = "Hall of the Phantoms - Switch (Lower Shortcut)"
    HOTP_SWITCH_BELL = "Hall of the Phantoms - Switch (Bell)"
    HOTP_SWITCH_GHOST_BLOOD = "Hall of the Phantoms - Switch (Ghost Blood)"
    HOTP_SWITCH_TELEPORTS = "Hall of the Phantoms - Switch (Teleports)"
    HOTP_SWITCH_WORM_PILLAR = "Hall of the Phantoms - Switch (Worm Pillar)"
    HOTP_SWITCH_TO_CLAW_1 = "Hall of the Phantoms - Switch (To Claw 1)"
    HOTP_SWITCH_TO_CLAW_2 = "Hall of the Phantoms - Switch (To Claw 2)"
    HOTP_SWITCH_CLAW_ACCESS = "Hall of the Phantoms - Switch (Claw Access)"
    HOTP_SWITCH_GHOSTS = "Hall of the Phantoms - Switch (Ghosts)"
    HOTP_SWITCH_LEFT_3 = "Hall of the Phantoms - Switch (Left 3)"
    HOTP_SWITCH_ABOVE_OLD_MAN = "Hall of the Phantoms - Switch (Above Old Man)"
    HOTP_SWITCH_TO_ABOVE_OLD_MAN = "Hall of the Phantoms - Switch (To Above Old Man)"
    HOTP_SWITCH_TP_PUZZLE = "Hall of the Phantoms - Switch (Teleport Puzzle)"
    HOTP_SWITCH_EYEBALL_SHORTCUT = "Hall of the Phantoms - Switch (Eyeball Shortcut)"
    HOTP_SWITCH_BELL_ACCESS = "Hall of the Phantoms - Switch (Bell Access)"
    HOTP_SWITCH_1ST_ROOM = "Hall of the Phantoms - Switch (1st Room)"
    HOTP_SWITCH_LEFT_BACKTRACK = "Hall of the Phantoms - Switch (Left Backtrack)"
    HOTP_CRYSTAL_ROCK_ACCESS = "Hall of the Phantoms - Crystal (Rock Access)"
    HOTP_CRYSTAL_BOTTOM = "Hall of the Phantoms - Crystal (Bottom)"
    HOTP_CRYSTAL_LOWER = "Hall of the Phantoms - Crystal (Lower)"
    HOTP_CRYSTAL_AFTER_CLAW = "Hall of the Phantoms - Crystal (After Claw)"
    HOTP_CRYSTAL_MAIDEN_1 = "Hall of the Phantoms - Crystal (Dead Maiden 1)"
    HOTP_CRYSTAL_MAIDEN_2 = "Hall of the Phantoms - Crystal (Dead Maiden 2)"
    HOTP_CRYSTAL_BELL_ACCESS = "Hall of the Phantoms - Crystal (Bell Access)"
    HOTP_CRYSTAL_HEART = "Hall of the Phantoms - Crystal (Heart)"
    HOTP_CRYSTAL_BELOW_PUZZLE = "Hall of the Phantoms - Crystal (Below Puzzle)"
    HOTP_FACE_OLD_MAN = "Hall of the Phantoms - Face (Old Man)"

    ROA_ICARUS = "Ruins of Ash - Icarus Emblem"
    ROA_EYE_GREEN = "Ruins of Ash - Gorgon Eye (Green)"
    ROA_ATTACK = "Ruins of Ash - Attack +1"
    ROA_HP_1_LEFT = "Ruins of Ash - Max HP +1 (Left of Ascent)"
    ROA_HP_2_RIGHT = "Ruins of Ash - Max HP +2 (Right Side)"
    ROA_HP_5_SOLARIA = "Ruins of Ash - Max HP +5 (After Solaria)"
    ROA_WHITE_KEY_SAVE = "Ruins of Ash - White Key (Checkpoint)"
    ROA_WHITE_KEY_REAPERS = "Ruins of Ash - White Key (Three Reapers)"
    ROA_WHITE_KEY_TORCHES = "Ruins of Ash - White Key (Torches)"
    ROA_WHITE_KEY_PORTAL = "Ruins of Ash - White Key (Void Portal)"
    ROA_BLUE_KEY_FACE = "Ruins of Ash - Blue Key (Face)"
    ROA_BLUE_KEY_FLAMES = "Ruins of Ash - Blue Key (Flames)"
    ROA_BLUE_KEY_BABY = "Ruins of Ash - Blue Key (Baby Gorgon)"
    ROA_BLUE_KEY_TOP = "Ruins of Ash - Blue Key (Top)"
    ROA_BLUE_KEY_POT = "Ruins of Ash - Blue Key (Pot)"
    ROA_RED_KEY = "Ruins of Ash - Red Key"
    ROA_ELEVATOR_1 = "Ruins of Ash - Elevator 1"
    ROA_ELEVATOR_2 = "Ruins of Ash - Elevator 2"
    ROA_SWITCH_ASCEND = "Ruins of Ash - Switch (Ascend)"
    ROA_SWITCH_AFTER_WORMS = "Ruins of Ash - Switch (After Worms)"
    ROA_SWITCH_RIGHT_PATH = "Ruins of Ash - Switch (Right Path)"
    ROA_SWITCH_APEX_ACCESS = "Ruins of Ash - Switch (Apex Access)"
    ROA_SWITCH_ICARUS = "Ruins of Ash - Switch (Icarus Emblem)"
    ROA_SWITCH_SHAFT_L = "Ruins of Ash - Switch (Shaft Left)"
    ROA_SWITCH_SHAFT_R = "Ruins of Ash - Switch (Shaft Right)"
    ROA_SWITCH_ELEVATOR = "Ruins of Ash - Switch (Elevator)"
    ROA_SWITCH_SHAFT_DOWNWARDS = "Ruins of Ash - Switch (Shaft Downwards)"
    ROA_SWITCH_SPIDERS = "Ruins of Ash - Switch (Spiders)"
    ROA_SWITCH_DARK_ROOM = "Ruins of Ash - Switch (Dark Room)"
    ROA_SWITCH_ASCEND_SHORTCUT = "Ruins of Ash - Switch (Ascend Shortcut)"
    ROA_SWITCH_1ST_SHORTCUT = "Ruins of Ash - Switch (1st Shortcut)"
    ROA_SWITCH_SPIKE_CLIMB = "Ruins of Ash - Switch (Spike Climb)"
    ROA_SWITCH_ABOVE_CENTAUR = "Ruins of Ash - Switch (Above Centaur)"
    ROA_SWITCH_BLOOD_POT = "Ruins of Ash - Switch (Blood Pot)"
    ROA_SWITCH_WORMS = "Ruins of Ash - Switch (Worms)"
    ROA_SWITCH_TRIPLE_1 = "Ruins of Ash - Switch (Triple 1)"
    ROA_SWITCH_TRIPLE_3 = "Ruins of Ash - Switch (Triple 3)"
    ROA_SWITCH_BABY_GORGON = "Ruins of Ash - Switch (Baby Gorgon)"
    ROA_SWITCH_BOSS_ACCESS = "Ruins of Ash - Switch (Boss Access)"
    ROA_SWITCH_BLOOD_POT_L = "Ruins of Ash - Switch (Blood Pot Left)"
    ROA_SWITCH_BLOOD_POT_R = "Ruins of Ash - Switch (Blood Pot Right)"
    ROA_SWITCH_LOWER_VOID = "Ruins of Ash - Switch (Lower Void)"
    ROA_CRYSTAL_1ST_ROOM = "Ruins of Ash - Crystal (1st Room)"
    ROA_CRYSTAL_BABY_GORGON = "Ruins of Ash - Crystal (Baby Gorgon)"
    ROA_CRYSTAL_LADDER_R = "Ruins of Ash - Crystal (Ladder Right)"
    ROA_CRYSTAL_LADDER_L = "Ruins of Ash - Crystal (Ladder Left)"
    ROA_CRYSTAL_CENTAUR = "Ruins of Ash - Crystal (Centaur)"
    ROA_CRYSTAL_SPIKE_BALLS = "Ruins of Ash - Crystal (Spike Balls)"
    ROA_CRYSTAL_LEFT_ASCEND = "Ruins of Ash - Crystal (Left Ascend)"
    ROA_CRYSTAL_SHAFT = "Ruins of Ash - Crystal (Shaft)"
    ROA_CRYSTAL_BRANCH_R = "Ruins of Ash - Crystal (Branch Right)"
    ROA_CRYSTAL_BRANCH_L = "Ruins of Ash - Crystal (Branch Left)"
    ROA_CRYSTAL_3_REAPERS = "Ruins of Ash - Crystal (3 Reapers)"
    ROA_CRYSTAL_TRIPLE_2 = "Ruins of Ash - Crystal (Triple 2)"
    ROA_FACE_SPIDERS = "Ruins of Ash - Face (Spiders)"
    ROA_FACE_BLUE_KEY = "Ruins of Ash - Face (Blue Key)"

    DARK_HP_4 = "Darkness - Max HP +4"
    DARK_WHITE_KEY = "Darkness - White Key"
    DARK_SWITCH = "Darkness - Switch"

    APEX_CHALICE = "The Apex - Blood Chalice"
    APEX_HP_1_CHALICE = "The Apex - Max HP +1 (Blood Chalice)"
    APEX_HP_5_HEART = "The Apex - Max HP +5 (After Heart)"
    APEX_BLUE_KEY = "The Apex - Blue Key"
    APEX_ELEVATOR = "The Apex - Elevator"
    APEX_SWITCH = "The Apex - Switch"

    CAVES_ATTACK_RED = "Caves - Attack +1 (Item Chain Red)"
    CAVES_ATTACK_BLUE = "Caves - Attack +1 (Item Chain Blue)"
    CAVES_ATTACK_GREEN = "Caves - Attack +1 (Item Chain Green)"
    CAVES_HP_1_START = "Caves - Max HP +1 (First Room)"
    CAVES_HP_1_CYCLOPS = "Caves - Max HP +1 (Cyclops Arena)"
    CAVES_HP_5_CHAIN = "Caves - Max HP +5 (Item Chain)"
    CAVES_SWITCH_SKELETONS = "Caves - Switch (Skeletons)"
    CAVES_SWITCH_CATA_ACCESS_1 = "Caves - Switch (Catacombs Access 1)"
    CAVES_SWITCH_CATA_ACCESS_2 = "Caves - Switch (Catacombs Access 2)"
    CAVES_SWITCH_CATA_ACCESS_3 = "Caves - Switch (Catacombs Access 3)"
    CAVES_FACE_1ST_ROOM = "Caves - Face (1st Room)"

    CATA_BOW = "Catacombs - Lunarian Bow"
    CATA_GIL = "Catacombs - Gil"
    CATA_ATTACK_ROOT = "Catacombs - Attack +1 (Climbable Root)"
    CATA_ATTACK_POISON = "Catacombs - Attack +1 (Poison Roots)"
    CATA_HP_1_ABOVE_POISON = "Catacombs - Max HP +1 (Above Poison Roots)"
    CATA_HP_2_BEFORE_POISON = "Catacombs - Max HP +2 (Before Poison Roots)"
    CATA_HP_2_AFTER_POISON = "Catacombs - Max HP +2 (After Poison Roots)"
    CATA_HP_2_GEMINI_BOTTOM = "Catacombs - Max HP +2 (Before Gemini Bottom)"
    CATA_HP_2_GEMINI_TOP = "Catacombs - Max HP +2 (Before Gemini Top)"
    CATA_HP_2_ABOVE_GEMINI = "Catacombs - Max HP +2 (Above Gemini)"
    CATA_WHITE_KEY_HEAD = "Catacombs - White Key (On Head)"
    CATA_WHITE_KEY_DEV_ROOM = "Catacombs - White Key (Dev Room)"
    CATA_WHITE_KEY_PRISON = "Catacombs - White Key (Prison)"
    CATA_BLUE_KEY_SLIMES = "Catacombs - Blue Key (Slime Water)"
    CATA_BLUE_KEY_EYEBALLS = "Catacombs - Blue Key (Eyeballs)"
    CATA_ELEVATOR_1 = "Catacombs - Elevator 1"
    CATA_ELEVATOR_2 = "Catacombs - Elevator 2"
    CATA_SWITCH_ELEVATOR = "Catacombs - Switch (Elevator)"
    CATA_SWITCH_SHORTCUT = "Catacombs - Switch (Vertical Shortcut)"
    CATA_SWITCH_TOP = "Catacombs - Switch (Top)"
    CATA_SWITCH_CLAW_1 = "Catacombs - Switch (Claw 1)"
    CATA_SWITCH_CLAW_2 = "Catacombs - Switch (Claw 2)"
    CATA_SWITCH_WATER_1 = "Catacombs - Switch (Water 1)"
    CATA_SWITCH_WATER_2 = "Catacombs - Switch (Water 2)"
    CATA_SWITCH_DEV_ROOM = "Catacombs - Switch (Dev Room)"
    CATA_SWITCH_AFTER_BLUE_DOOR = "Catacombs - Switch (After Blue Door)"
    CATA_SWITCH_SHORTCUT_ACCESS = "Catacombs - Switch (Shortcut Access)"
    CATA_SWITCH_LADDER_BLOCKS = "Catacombs - Switch (Ladder Blocks)"
    CATA_SWITCH_MID_SHORTCUT = "Catacombs - Switch (Mid Shortcut)"
    CATA_SWITCH_1ST_ROOM = "Catacombs - Switch (1st Room)"
    CATA_SWITCH_FLAMES_2 = "Catacombs - Switch (Flames 2)"
    CATA_SWITCH_FLAMES_1 = "Catacombs - Switch (Flames 1)"
    CATA_CRYSTAL_POISON_ROOTS = "Catacombs - Crystal (Poison Roots)"
    CATA_FACE_AFTER_BOW = "Catacombs - Face (After Bow)"
    CATA_FACE_BOW = "Catacombs - Face (Bow)"
    CATA_FACE_X4 = "Catacombs - Face (x4)"
    CATA_FACE_CAMPFIRE = "Catacombs - Face (Campfire)"
    CATA_FACE_DOUBLE_DOOR = "Catacombs - Face (Double Door)"
    CATA_FACE_BOTTOM = "Catacombs - Face (Bottom)"

    TR_BRAM = "Tower Roots - Bram"
    TR_ADORNED_KEY = "Tower Roots - Adorned Key"
    TR_HP_1_BOTTOM = "Tower Roots - Max HP +1 (Bottom)"
    TR_HP_2_TOP = "Tower Roots - Max HP +2 (Top)"
    TR_RED_KEY = "Tower Roots - Red Key"
    TR_ELEVATOR = "Tower Roots - Elevator"
    TR_SWITCH_ADORNED_L = "Tower Roots - Switch (Adorned Key Left)"
    TR_SWITCH_ADORNED_M = "Tower Roots - Switch (Adorned Key Middle)"
    TR_SWITCH_ADORNED_R = "Tower Roots - Switch (Adorned Key Right)"
    TR_SWITCH_ELEVATOR = "Tower Roots - Switch (Elevator)"
    TR_SWITCH_BOTTOM = "Tower Roots - Switch (Bottom)"
    TR_CRYSTAL_GOLD = "Tower Roots - Crystal (Gold)"
    TR_CRYSTAL_DARK_ARIAS = "Tower Roots - Crystal (Dark Arias)"

    CD_CROWN = "Cyclops Den - Prince's Crown"
    CD_ATTACK = "Cyclops Den - Attack +1"
    CD_HP_1 = "Cyclops Den - Max HP +1"
    CD_SWITCH_1 = "Cyclops Den - Switch 1"
    CD_SWITCH_2 = "Cyclops Den - Switch 2"
    CD_SWITCH_3 = "Cyclops Den - Switch 3"
    CD_SWITCH_CAMPFIRE = "Cyclops Den - Switch (Campfire)"
    CD_SWITCH_TOP = "Cyclops Den - Switch (Top)"
    CD_CRYSTAL_BACKTRACK = "Cyclops Den - Crystal (Backtrack)"
    CD_CRYSTAL_START = "Cyclops Den - Crystal (Start)"
    CD_CRYSTAL_CAMPFIRE = "Cyclops Den - Crystal (Campfire)"
    CD_CRYSTAL_STEPS = "Cyclops Den - Crystal (Steps)"

    CATH_BLOCK = "Cathedral - Magic Block"
    CATH_ATTACK = "Cathedral - Attack +1"
    CATH_HP_1_TOP_LEFT = "Cathedral - Max HP +1 (Top Left)"
    CATH_HP_1_TOP_RIGHT = "Cathedral - Max HP +1 (Top Right)"
    CATH_HP_2_CLAW = "Cathedral - Max HP +2 (Left Climb)"
    CATH_HP_5_BELL = "Cathedral - Max HP +5 (Bell)"
    CATH_SWITCH_BOTTOM = "Cathedral - Switch (Bottom)"
    CATH_SWITCH_BESIDE_SHAFT = "Cathedral - Switch (Beside Shaft)"
    CATH_SWITCH_TOP_CAMPFIRE = "Cathedral - Switch (Top Campfire)"
    CATH_CRYSTAL_1ST_ROOM = "Cathedral - Crystal (1st Room)"
    CATH_CRYSTAL_SHAFT = "Cathedral - Crystal (Shaft)"
    CATH_CRYSTAL_SPIKE_PIT = "Cathedral - Crystal (Spike Pit)"
    CATH_CRYSTAL_TOP_L = "Cathedral - Crystal (Top Left)"
    CATH_CRYSTAL_TOP_R = "Cathedral - Crystal (Top Right)"
    CATH_CRYSTAL_SHAFT_ACCESS = "Cathedral - Crystal (Shaft Access)"
    CATH_CRYSTAL_ORBS = "Cathedral - Crystal (Orbs)"
    CATH_FACE_LEFT = "Cathedral - Face (Left)"
    CATH_FACE_RIGHT = "Cathedral - Face (Right)"

    SP_STAR = "Serpent Path - Morning Star"
    SP_ATTACK = "Serpent Path - Attack +1"
    SP_HP_1 = "Serpent Path - Max HP +1"
    SP_BLUE_KEY_BUBBLES = "Serpent Path - Blue Key (Bubbles)"
    SP_BLUE_KEY_STAR = "Serpent Path - Blue Key (Morning Star)"
    SP_BLUE_KEY_PAINTING = "Serpent Path - Blue Key (Painting)"
    SP_BLUE_KEY_ARIAS = "Serpent Path - Blue Key (Arias)"
    SP_SWITCH_DOUBLE_DOORS = "Serpent Path - Switch (Double Doors)"
    SP_SWITCH_BUBBLES = "Serpent Path - Switch (Bubbles)"
    SP_SWITCH_AFTER_STAR = "Serpent Path - Switch (After Star)"
    SP_CRYSTAL_BLOCKS = "Serpent Path - Crystal (Blocks)"
    SP_CRYSTAL_STAR = "Serpent Path - Crystal (Star)"

    SHOP_GIFT = "Shop - Gift"
    SHOP_KNOWLEDGE = "Shop - Knowledge"
    SHOP_MERCY = "Shop - Mercy"
    SHOP_ORB_SEEKER = "Shop - Orb Seeker"
    SHOP_MAP_REVEAL = "Shop - Map Reveal"
    SHOP_CARTOGRAPHER = "Shop - Cartographer"
    SHOP_DEATH_ORB = "Shop - Death Orb"
    SHOP_DEATH_POINT = "Shop - Death Point"
    SHOP_TITANS_EGO = "Shop - Titan's Ego"
    SHOP_ALGUS_ARCANIST = "Shop - Algus's Arcanist"
    SHOP_ALGUS_SHOCK = "Shop - Algus's Shock Field"
    SHOP_ALGUS_METEOR = "Shop - Algus's Meteor Rain"
    SHOP_ARIAS_GORGONSLAYER = "Shop - Arias's Gorgonslayer"
    SHOP_ARIAS_LAST_STAND = "Shop - Arias's Last Stand"
    SHOP_ARIAS_LIONHEART = "Shop - Arias's Lionheart"
    SHOP_KYULI_ASSASSIN = "Shop - Kyuli's Assassin Strike"
    SHOP_KYULI_BULLSEYE = "Shop - Kyuli's Bullseye"
    SHOP_KYULI_RAY = "Shop - Kyuli's Shining Ray"
    SHOP_ZEEK_JUNKYARD = "Shop - Zeek's Junkyard Hunt"
    SHOP_ZEEK_ORBS = "Shop - Zeek's Orb Monger"
    SHOP_ZEEK_LOOT = "Shop - Zeek's Bigger Loot"
    SHOP_BRAM_AXE = "Shop - Bram's Golden Axe"
    SHOP_BRAM_HUNTER = "Shop - Bram's Monster Hunter"
    SHOP_BRAM_WHIPLASH = "Shop - Bram's Whiplash"


class AstalonLocation(Location):
    game = "Astalon"


@dataclass(frozen=True)
class LocationData:
    region: RegionName
    group: LocationGroup
    area: Area


location_table: Dict[str, LocationData] = {
    LocationName.GT_GORGONHEART.value: LocationData(RegionName.GT_GORGONHEART, LocationGroup.ITEM, Area.GT),
    LocationName.GT_ANCIENTS_RING.value: LocationData(RegionName.GT_BOTTOM, LocationGroup.ITEM, Area.GT),
    LocationName.GT_SWORD.value: LocationData(RegionName.GT_SWORD, LocationGroup.ITEM, Area.GT),
    LocationName.GT_MAP.value: LocationData(RegionName.GT_BOTTOM, LocationGroup.ITEM, Area.GT),
    LocationName.GT_ASCENDANT_KEY.value: LocationData(RegionName.GT_ASCENDANT_KEY, LocationGroup.ITEM, Area.GT),
    LocationName.GT_BANISH.value: LocationData(RegionName.GT_LEFT, LocationGroup.ITEM, Area.GT),
    LocationName.GT_VOID.value: LocationData(RegionName.GT_VOID, LocationGroup.ITEM, Area.GT),
    LocationName.GT_EYE_RED.value: LocationData(RegionName.GT_BOSS, LocationGroup.ITEM, Area.GT),
    LocationName.GT_ATTACK.value: LocationData(RegionName.GT_BABY_GORGON, LocationGroup.ATTACK, Area.GT),
    LocationName.GT_HP_1_RING.value: LocationData(RegionName.GT_BOTTOM, LocationGroup.HEALTH, Area.GT),
    LocationName.GT_HP_5_KEY.value: LocationData(RegionName.GT_ASCENDANT_KEY, LocationGroup.HEALTH, Area.GT),
    LocationName.GT_WHITE_KEY_START.value: LocationData(RegionName.ENTRANCE, LocationGroup.KEY_WHITE, Area.GT),
    LocationName.GT_WHITE_KEY_RIGHT.value: LocationData(RegionName.GT_BOTTOM, LocationGroup.KEY_WHITE, Area.GT),
    LocationName.GT_WHITE_KEY_BOSS.value: LocationData(RegionName.GT_TOP_RIGHT, LocationGroup.KEY_WHITE, Area.GT),
    LocationName.GT_BLUE_KEY_BONESNAKE.value: LocationData(RegionName.GT_BOTTOM, LocationGroup.KEY_BLUE, Area.GT),
    LocationName.GT_BLUE_KEY_BUTT.value: LocationData(RegionName.GT_BUTT, LocationGroup.KEY_BLUE, Area.GT),
    LocationName.GT_BLUE_KEY_WALL.value: LocationData(RegionName.GT_BUTT, LocationGroup.KEY_BLUE, Area.GT),
    LocationName.GT_BLUE_KEY_POT.value: LocationData(RegionName.GT_UPPER_PATH, LocationGroup.KEY_BLUE, Area.GT),
    LocationName.GT_RED_KEY.value: LocationData(RegionName.GT_BOSS, LocationGroup.KEY_RED, Area.GT),
    LocationName.MECH_BOOTS.value: LocationData(RegionName.MECH_BOOTS_UPPER, LocationGroup.ITEM, Area.MECH),
    LocationName.MECH_CLOAK.value: LocationData(RegionName.MECH_CLOAK, LocationGroup.ITEM, Area.MECH),
    LocationName.MECH_EYE_BLUE.value: LocationData(RegionName.MECH_BOSS, LocationGroup.ITEM, Area.MECH),
    LocationName.MECH_ATTACK_VOLANTIS.value: LocationData(RegionName.HOTP_START, LocationGroup.ATTACK, Area.MECH),
    LocationName.MECH_ATTACK_STAR.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.ATTACK, Area.MECH),
    LocationName.MECH_HP_1_SWITCH.value: LocationData(RegionName.MECH_RIGHT, LocationGroup.HEALTH, Area.MECH),
    LocationName.MECH_HP_1_STAR.value: LocationData(RegionName.MECH_BRAM_TUNNEL, LocationGroup.HEALTH, Area.MECH),
    LocationName.MECH_HP_3_CLAW.value: LocationData(RegionName.MECH_BOTTOM_CAMPFIRE, LocationGroup.HEALTH, Area.MECH),
    LocationName.MECH_WHITE_KEY_LINUS.value: LocationData(
        RegionName.MECH_SWORD_CONNECTION, LocationGroup.KEY_WHITE, Area.MECH
    ),
    LocationName.MECH_WHITE_KEY_BK.value: LocationData(RegionName.MECH_AFTER_BK, LocationGroup.KEY_WHITE, Area.MECH),
    LocationName.MECH_WHITE_KEY_ARENA.value: LocationData(RegionName.MECH_RIGHT, LocationGroup.KEY_WHITE, Area.MECH),
    LocationName.MECH_WHITE_KEY_TOP.value: LocationData(RegionName.MECH_TOP, LocationGroup.KEY_WHITE, Area.MECH),
    LocationName.MECH_BLUE_KEY_VOID.value: LocationData(RegionName.GT_VOID, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_SNAKE.value: LocationData(RegionName.MECH_SNAKE, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_LINUS.value: LocationData(
        RegionName.MECH_LOWER_ARIAS, LocationGroup.KEY_BLUE, Area.MECH
    ),
    LocationName.MECH_BLUE_KEY_SACRIFICE.value: LocationData(
        RegionName.MECH_SACRIFICE, LocationGroup.KEY_BLUE, Area.MECH
    ),
    LocationName.MECH_BLUE_KEY_RED.value: LocationData(RegionName.MECH_START, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_ARIAS.value: LocationData(
        RegionName.MECH_ARIAS_EYEBALL, LocationGroup.KEY_BLUE, Area.MECH
    ),
    LocationName.MECH_BLUE_KEY_BLOCKS.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_TOP.value: LocationData(RegionName.MECH_SPLIT_PATH, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_OLD_MAN.value: LocationData(RegionName.MECH_RIGHT, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_SAVE.value: LocationData(RegionName.MECH_TOP, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_BLUE_KEY_POT.value: LocationData(RegionName.MECH_POTS, LocationGroup.KEY_BLUE, Area.MECH),
    LocationName.MECH_RED_KEY.value: LocationData(RegionName.MECH_LOWER_VOID, LocationGroup.KEY_RED, Area.MECH),
    LocationName.HOTP_BELL.value: LocationData(RegionName.HOTP_BELL, LocationGroup.ITEM, Area.HOTP),
    LocationName.HOTP_AMULET.value: LocationData(RegionName.HOTP_AMULET, LocationGroup.ITEM, Area.HOTP),
    LocationName.HOTP_CLAW.value: LocationData(RegionName.HOTP_CLAW, LocationGroup.ITEM, Area.HOTP),
    LocationName.HOTP_GAUNTLET.value: LocationData(RegionName.HOTP_GAUNTLET, LocationGroup.ITEM, Area.HOTP),
    LocationName.HOTP_MAIDEN_RING.value: LocationData(RegionName.HOTP_MAIDEN, LocationGroup.ITEM, Area.HOTP),
    LocationName.HOTP_HP_1_CLAW.value: LocationData(RegionName.HOTP_CLAW_LEFT, LocationGroup.HEALTH, Area.HOTP),
    LocationName.HOTP_HP_2_LADDER.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.HEALTH, Area.HOTP),
    LocationName.HOTP_HP_2_GAUNTLET.value: LocationData(RegionName.HOTP_TP_FALL_TOP, LocationGroup.HEALTH, Area.HOTP),
    LocationName.HOTP_HP_5_OLD_MAN.value: LocationData(RegionName.HOTP_ABOVE_OLD_MAN, LocationGroup.HEALTH, Area.HOTP),
    LocationName.HOTP_HP_5_MAZE.value: LocationData(RegionName.HOTP_LOWER_VOID, LocationGroup.HEALTH, Area.HOTP),
    LocationName.HOTP_HP_5_START.value: LocationData(RegionName.HOTP_START, LocationGroup.HEALTH, Area.HOTP),
    LocationName.HOTP_WHITE_KEY_LEFT.value: LocationData(
        RegionName.HOTP_START_LEFT, LocationGroup.KEY_WHITE, Area.HOTP
    ),
    LocationName.HOTP_WHITE_KEY_GHOST.value: LocationData(RegionName.HOTP_LOWER, LocationGroup.KEY_WHITE, Area.HOTP),
    LocationName.HOTP_WHITE_KEY_OLD_MAN.value: LocationData(
        RegionName.HOTP_ELEVATOR, LocationGroup.KEY_WHITE, Area.HOTP
    ),
    LocationName.HOTP_WHITE_KEY_BOSS.value: LocationData(
        RegionName.HOTP_UPPER_ARIAS, LocationGroup.KEY_WHITE, Area.HOTP
    ),
    LocationName.HOTP_BLUE_KEY_STATUE.value: LocationData(
        RegionName.HOTP_EPIMETHEUS, LocationGroup.KEY_BLUE, Area.HOTP
    ),
    LocationName.HOTP_BLUE_KEY_GOLD.value: LocationData(RegionName.HOTP_LOWER, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationName.HOTP_BLUE_KEY_AMULET.value: LocationData(
        RegionName.HOTP_AMULET_CONNECTION, LocationGroup.KEY_BLUE, Area.HOTP
    ),
    LocationName.HOTP_BLUE_KEY_LADDER.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationName.HOTP_BLUE_KEY_TELEPORTS.value: LocationData(
        RegionName.HOTP_ELEVATOR, LocationGroup.KEY_BLUE, Area.HOTP
    ),
    LocationName.HOTP_BLUE_KEY_MAZE.value: LocationData(RegionName.HOTP_TP_PUZZLE, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationName.HOTP_RED_KEY.value: LocationData(RegionName.HOTP_RED_KEY, LocationGroup.KEY_RED, Area.HOTP),
    LocationName.ROA_ICARUS.value: LocationData(RegionName.ROA_ICARUS, LocationGroup.ITEM, Area.ROA),
    LocationName.ROA_EYE_GREEN.value: LocationData(RegionName.ROA_BOSS, LocationGroup.ITEM, Area.ROA),
    LocationName.ROA_ATTACK.value: LocationData(RegionName.ROA_MIDDLE, LocationGroup.ATTACK, Area.ROA),
    LocationName.ROA_HP_1_LEFT.value: LocationData(RegionName.ROA_LEFT_ASCENT, LocationGroup.HEALTH, Area.ROA),
    LocationName.ROA_HP_2_RIGHT.value: LocationData(RegionName.ROA_RIGHT_BRANCH, LocationGroup.HEALTH, Area.ROA),
    LocationName.ROA_HP_5_SOLARIA.value: LocationData(RegionName.APEX, LocationGroup.HEALTH, Area.ROA),
    LocationName.ROA_WHITE_KEY_SAVE.value: LocationData(RegionName.ROA_WORMS, LocationGroup.KEY_WHITE, Area.ROA),
    LocationName.ROA_WHITE_KEY_REAPERS.value: LocationData(
        RegionName.ROA_LEFT_ASCENT, LocationGroup.KEY_WHITE, Area.ROA
    ),
    LocationName.ROA_WHITE_KEY_TORCHES.value: LocationData(RegionName.ROA_MIDDLE, LocationGroup.KEY_WHITE, Area.ROA),
    LocationName.ROA_WHITE_KEY_PORTAL.value: LocationData(RegionName.ROA_UPPER_VOID, LocationGroup.KEY_WHITE, Area.ROA),
    LocationName.ROA_BLUE_KEY_FACE.value: LocationData(RegionName.ROA_BOTTOM_ASCEND, LocationGroup.KEY_BLUE, Area.ROA),
    LocationName.ROA_BLUE_KEY_FLAMES.value: LocationData(
        RegionName.ROA_ARIAS_BABY_GORGON, LocationGroup.KEY_BLUE, Area.ROA
    ),
    LocationName.ROA_BLUE_KEY_BABY.value: LocationData(
        RegionName.ROA_LEFT_BABY_GORGON, LocationGroup.KEY_BLUE, Area.ROA
    ),
    LocationName.ROA_BLUE_KEY_TOP.value: LocationData(RegionName.ROA_BOSS_CONNECTION, LocationGroup.KEY_BLUE, Area.ROA),
    LocationName.ROA_BLUE_KEY_POT.value: LocationData(RegionName.ROA_TRIPLE_REAPER, LocationGroup.KEY_BLUE, Area.ROA),
    LocationName.ROA_RED_KEY.value: LocationData(RegionName.ROA_RED_KEY, LocationGroup.KEY_RED, Area.ROA),
    LocationName.DARK_HP_4.value: LocationData(RegionName.DARK_END, LocationGroup.HEALTH, Area.DARK),
    LocationName.DARK_WHITE_KEY.value: LocationData(RegionName.DARK_END, LocationGroup.KEY_WHITE, Area.DARK),
    LocationName.APEX_CHALICE.value: LocationData(RegionName.APEX_CENTAUR, LocationGroup.ITEM, Area.APEX),
    LocationName.APEX_HP_1_CHALICE.value: LocationData(RegionName.APEX, LocationGroup.HEALTH, Area.APEX),
    LocationName.APEX_HP_5_HEART.value: LocationData(RegionName.APEX_HEART, LocationGroup.HEALTH, Area.APEX),
    LocationName.APEX_BLUE_KEY.value: LocationData(RegionName.APEX, LocationGroup.KEY_BLUE, Area.APEX),
    LocationName.CATA_BOW.value: LocationData(RegionName.CATA_BOW, LocationGroup.ITEM, Area.CATA),
    LocationName.CAVES_ATTACK_RED.value: LocationData(RegionName.CAVES_ITEM_CHAIN, LocationGroup.ATTACK, Area.CAVES),
    LocationName.CAVES_ATTACK_BLUE.value: LocationData(RegionName.CAVES_ITEM_CHAIN, LocationGroup.ATTACK, Area.CAVES),
    LocationName.CAVES_ATTACK_GREEN.value: LocationData(RegionName.CAVES_ITEM_CHAIN, LocationGroup.ATTACK, Area.CAVES),
    LocationName.CATA_ATTACK_ROOT.value: LocationData(RegionName.CATA_CLIMBABLE_ROOT, LocationGroup.ATTACK, Area.CATA),
    LocationName.CATA_ATTACK_POISON.value: LocationData(RegionName.CATA_POISON_ROOTS, LocationGroup.ATTACK, Area.CATA),
    LocationName.CAVES_HP_1_START.value: LocationData(RegionName.CAVES_START, LocationGroup.HEALTH, Area.CAVES),
    LocationName.CAVES_HP_1_CYCLOPS.value: LocationData(RegionName.CAVES_ARENA, LocationGroup.HEALTH, Area.CAVES),
    LocationName.CATA_HP_1_ABOVE_POISON.value: LocationData(
        RegionName.CATA_POISON_ROOTS, LocationGroup.HEALTH, Area.CATA
    ),
    LocationName.CATA_HP_2_BEFORE_POISON.value: LocationData(
        RegionName.CATA_POISON_ROOTS, LocationGroup.HEALTH, Area.CATA
    ),
    LocationName.CATA_HP_2_AFTER_POISON.value: LocationData(
        RegionName.CATA_POISON_ROOTS, LocationGroup.HEALTH, Area.CATA
    ),
    LocationName.CATA_HP_2_GEMINI_BOTTOM.value: LocationData(
        RegionName.CATA_DOUBLE_DOOR, LocationGroup.HEALTH, Area.CATA
    ),
    LocationName.CATA_HP_2_GEMINI_TOP.value: LocationData(RegionName.CATA_CENTAUR, LocationGroup.HEALTH, Area.CATA),
    LocationName.CATA_HP_2_ABOVE_GEMINI.value: LocationData(RegionName.CATA_FLAMES, LocationGroup.HEALTH, Area.CATA),
    LocationName.CAVES_HP_5_CHAIN.value: LocationData(RegionName.CAVES_ITEM_CHAIN, LocationGroup.HEALTH, Area.CAVES),
    LocationName.CATA_WHITE_KEY_HEAD.value: LocationData(RegionName.CATA_TOP, LocationGroup.KEY_WHITE, Area.CATA),
    LocationName.CATA_WHITE_KEY_DEV_ROOM.value: LocationData(
        RegionName.CATA_DEV_ROOM_CONNECTION, LocationGroup.KEY_WHITE, Area.CATA
    ),
    LocationName.CATA_WHITE_KEY_PRISON.value: LocationData(RegionName.CATA_BOSS, LocationGroup.KEY_WHITE, Area.CATA),
    LocationName.CATA_BLUE_KEY_SLIMES.value: LocationData(
        RegionName.CATA_BOW_CAMPFIRE, LocationGroup.KEY_BLUE, Area.CATA
    ),
    LocationName.CATA_BLUE_KEY_EYEBALLS.value: LocationData(RegionName.CATA_CENTAUR, LocationGroup.KEY_BLUE, Area.CATA),
    LocationName.TR_ADORNED_KEY.value: LocationData(RegionName.TR_BOTTOM, LocationGroup.ITEM, Area.TR),
    LocationName.TR_HP_1_BOTTOM.value: LocationData(RegionName.TR_BOTTOM_LEFT, LocationGroup.HEALTH, Area.TR),
    LocationName.TR_HP_2_TOP.value: LocationData(RegionName.TR_LEFT, LocationGroup.HEALTH, Area.TR),
    LocationName.TR_RED_KEY.value: LocationData(RegionName.CATA_BOSS, LocationGroup.KEY_RED, Area.TR),
    LocationName.CD_ATTACK.value: LocationData(RegionName.CD_TOP, LocationGroup.ATTACK, Area.CD),
    LocationName.CD_HP_1.value: LocationData(RegionName.CD_TOP, LocationGroup.HEALTH, Area.CD),
    LocationName.CATH_BLOCK.value: LocationData(RegionName.CATH_TOP, LocationGroup.ITEM, Area.CATH),
    LocationName.CATH_ATTACK.value: LocationData(RegionName.CATH_UPPER_SPIKE_PIT, LocationGroup.ATTACK, Area.CATH),
    LocationName.CATH_HP_1_TOP_LEFT.value: LocationData(RegionName.CATH_TOP, LocationGroup.HEALTH, Area.CATH),
    LocationName.CATH_HP_1_TOP_RIGHT.value: LocationData(RegionName.CATH_TOP, LocationGroup.HEALTH, Area.CATH),
    LocationName.CATH_HP_2_CLAW.value: LocationData(RegionName.CATH_LEFT_SHAFT, LocationGroup.HEALTH, Area.CATH),
    LocationName.CATH_HP_5_BELL.value: LocationData(RegionName.CATH_CAMPFIRE_1, LocationGroup.HEALTH, Area.CATH),
    LocationName.SP_STAR.value: LocationData(RegionName.SP_STAR, LocationGroup.ITEM, Area.SP),
    LocationName.SP_ATTACK.value: LocationData(RegionName.SP_CAMPFIRE_2, LocationGroup.ATTACK, Area.SP),
    LocationName.SP_HP_1.value: LocationData(RegionName.SP_FROG, LocationGroup.HEALTH, Area.SP),
    LocationName.SP_BLUE_KEY_BUBBLES.value: LocationData(RegionName.SP_START, LocationGroup.KEY_BLUE, Area.SP),
    LocationName.SP_BLUE_KEY_STAR.value: LocationData(RegionName.SP_STAR_END, LocationGroup.KEY_BLUE, Area.SP),
    LocationName.SP_BLUE_KEY_PAINTING.value: LocationData(RegionName.SP_PAINTING, LocationGroup.KEY_BLUE, Area.SP),
    LocationName.SP_BLUE_KEY_ARIAS.value: LocationData(RegionName.SP_CAMPFIRE_2, LocationGroup.KEY_BLUE, Area.SP),
    LocationName.SHOP_GIFT.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_KNOWLEDGE.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_MERCY.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ORB_SEEKER.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_MAP_REVEAL.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_CARTOGRAPHER.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_DEATH_ORB.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_DEATH_POINT.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_TITANS_EGO.value: LocationData(RegionName.SHOP, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ALGUS_ARCANIST.value: LocationData(RegionName.SHOP_ALGUS, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ALGUS_SHOCK.value: LocationData(RegionName.SHOP_ALGUS, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ALGUS_METEOR.value: LocationData(RegionName.SHOP_ALGUS, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ARIAS_GORGONSLAYER.value: LocationData(RegionName.SHOP_ARIAS, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ARIAS_LAST_STAND.value: LocationData(RegionName.SHOP_ARIAS, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ARIAS_LIONHEART.value: LocationData(RegionName.SHOP_ARIAS, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_KYULI_ASSASSIN.value: LocationData(RegionName.SHOP_KYULI, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_KYULI_BULLSEYE.value: LocationData(RegionName.SHOP_KYULI, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_KYULI_RAY.value: LocationData(RegionName.SHOP_KYULI, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ZEEK_JUNKYARD.value: LocationData(RegionName.SHOP_ZEEK, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ZEEK_ORBS.value: LocationData(RegionName.SHOP_ZEEK, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_ZEEK_LOOT.value: LocationData(RegionName.SHOP_ZEEK, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_BRAM_AXE.value: LocationData(RegionName.SHOP_BRAM, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_BRAM_HUNTER.value: LocationData(RegionName.SHOP_BRAM, LocationGroup.SHOP, Area.SHOP),
    LocationName.SHOP_BRAM_WHIPLASH.value: LocationData(RegionName.SHOP_BRAM, LocationGroup.SHOP, Area.SHOP),
    LocationName.GT_ALGUS.value: LocationData(RegionName.ENTRANCE, LocationGroup.CHARACTER, Area.GT),
    LocationName.GT_ARIAS.value: LocationData(RegionName.ENTRANCE, LocationGroup.CHARACTER, Area.GT),
    LocationName.GT_KYULI.value: LocationData(RegionName.ENTRANCE, LocationGroup.CHARACTER, Area.GT),
    LocationName.MECH_ZEEK.value: LocationData(RegionName.MECH_ZEEK, LocationGroup.CHARACTER, Area.MECH),
    LocationName.TR_BRAM.value: LocationData(RegionName.TR_BRAM, LocationGroup.CHARACTER, Area.TR),
    LocationName.GT_ELEVATOR_2.value: LocationData(RegionName.GT_BOSS, LocationGroup.ELEVATOR, Area.GT),
    LocationName.GT_SWITCH_2ND_ROOM.value: LocationData(RegionName.ENTRANCE, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_1ST_CYCLOPS.value: LocationData(RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_SPIKE_TUNNEL.value: LocationData(RegionName.GT_TOP_LEFT, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_BUTT_ACCESS.value: LocationData(RegionName.GT_SPIKE_TUNNEL, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_GH.value: LocationData(RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_UPPER_PATH_BLOCKS.value: LocationData(
        RegionName.GT_UPPER_PATH_CONNECTION, LocationGroup.SWITCH, Area.GT
    ),
    LocationName.GT_SWITCH_UPPER_PATH_ACCESS.value: LocationData(
        RegionName.GT_UPPER_PATH_CONNECTION, LocationGroup.SWITCH, Area.GT
    ),
    LocationName.GT_SWITCH_CROSSES.value: LocationData(RegionName.GT_LEFT, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_GH_SHORTCUT.value: LocationData(RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_ARIAS_PATH.value: LocationData(RegionName.GT_TOP_LEFT, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_SWORD_ACCESS.value: LocationData(RegionName.GT_SWORD_FORK, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_SWORD_BACKTRACK.value: LocationData(RegionName.GT_SWORD_FORK, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_SWORD.value: LocationData(RegionName.GT_SWORD, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_SWITCH_UPPER_ARIAS.value: LocationData(
        RegionName.GT_ARIAS_SWORD_SWITCH, LocationGroup.SWITCH, Area.GT
    ),
    LocationName.GT_CRYSTAL_LADDER.value: LocationData(RegionName.GT_LADDER_SWITCH, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_CRYSTAL_ROTA.value: LocationData(RegionName.GT_UPPER_PATH, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_CRYSTAL_OLD_MAN_1.value: LocationData(RegionName.GT_OLD_MAN_FORK, LocationGroup.SWITCH, Area.GT),
    LocationName.GT_CRYSTAL_OLD_MAN_2.value: LocationData(RegionName.GT_OLD_MAN_FORK, LocationGroup.SWITCH, Area.GT),
    LocationName.MECH_ELEVATOR_1.value: LocationData(
        RegionName.MECH_ZEEK_CONNECTION, LocationGroup.ELEVATOR, Area.MECH
    ),
    LocationName.MECH_ELEVATOR_2.value: LocationData(RegionName.MECH_BOSS, LocationGroup.ELEVATOR, Area.MECH),
    LocationName.MECH_SWITCH_WATCHER.value: LocationData(RegionName.MECH_ROOTS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_CHAINS.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_BOSS_ACCESS_1.value: LocationData(
        RegionName.MECH_BOSS_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_BOSS_ACCESS_2.value: LocationData(
        RegionName.MECH_BOSS_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_SPLIT_PATH.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_SNAKE_1.value: LocationData(
        RegionName.MECH_BOTTOM_CAMPFIRE, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_BOOTS_ACCESS.value: LocationData(
        RegionName.MECH_BOOTS_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_UPPER_GT_ACCESS.value: LocationData(
        RegionName.MECH_BOTTOM_CAMPFIRE, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_UPPER_VOID_DROP.value: LocationData(
        RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_UPPER_VOID.value: LocationData(
        RegionName.MECH_UPPER_VOID, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_LINUS.value: LocationData(RegionName.MECH_LINUS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_TO_BOSS_2.value: LocationData(
        RegionName.MECH_BOSS_SWITCHES, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_POTS.value: LocationData(RegionName.MECH_POTS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_MAZE_BACKDOOR.value: LocationData(
        RegionName.HOTP_FALL_BOTTOM, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_TO_BOSS_1.value: LocationData(
        RegionName.MECH_BOSS_SWITCHES, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_BLOCK_STAIRS.value: LocationData(
        RegionName.MECH_CLOAK_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_ARIAS_CYCLOPS.value: LocationData(
        RegionName.MECH_CHARACTER_SWAPS, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_BOOTS_LOWER.value: LocationData(
        RegionName.MECH_BOOTS_LOWER, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_CHAINS_GAP.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_LOWER_KEY.value: LocationData(
        RegionName.MECH_SWORD_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_SWITCH_ARIAS.value: LocationData(RegionName.MECH_ARIAS_EYEBALL, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_SNAKE_2.value: LocationData(RegionName.MECH_SNAKE, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_KEY_BLOCKS.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_CANNON.value: LocationData(RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_EYEBALL.value: LocationData(RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_SWITCH_INVISIBLE.value: LocationData(RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_CANNON.value: LocationData(RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_LINUS.value: LocationData(RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_LOWER.value: LocationData(
        RegionName.MECH_SWORD_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_TO_BOSS_3.value: LocationData(
        RegionName.MECH_BOSS_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_TRIPLE_1.value: LocationData(
        RegionName.MECH_TRIPLE_SWITCHES, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_TRIPLE_2.value: LocationData(
        RegionName.MECH_TRIPLE_SWITCHES, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_TRIPLE_3.value: LocationData(
        RegionName.MECH_TRIPLE_SWITCHES, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_TOP.value: LocationData(RegionName.MECH_TOP, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_CLOAK.value: LocationData(
        RegionName.MECH_CLOAK_CONNECTION, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_SLIMES.value: LocationData(
        RegionName.MECH_BOSS_SWITCHES, LocationGroup.SWITCH, Area.MECH
    ),
    LocationName.MECH_CRYSTAL_TO_CD.value: LocationData(RegionName.MECH_TOP, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_CAMPFIRE.value: LocationData(RegionName.MECH_BK, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_1ST_ROOM.value: LocationData(RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_OLD_MAN.value: LocationData(RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_TOP_CHAINS.value: LocationData(RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_CRYSTAL_BK.value: LocationData(RegionName.MECH_BK, LocationGroup.SWITCH, Area.MECH),
    LocationName.MECH_FACE_ABOVE_VOLANTIS.value: LocationData(RegionName.MECH_BOSS, LocationGroup.SWITCH, Area.MECH),
    LocationName.HOTP_ELEVATOR.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.ELEVATOR, Area.HOTP),
    LocationName.HOTP_SWITCH_ROCK.value: LocationData(
        RegionName.HOTP_AMULET_CONNECTION, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_BELOW_START.value: LocationData(
        RegionName.HOTP_START_BOTTOM_MID, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_LEFT_2.value: LocationData(RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_LEFT_1.value: LocationData(RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_LOWER_SHORTCUT.value: LocationData(RegionName.HOTP_LOWER, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_BELL.value: LocationData(RegionName.HOTP_BELL, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_GHOST_BLOOD.value: LocationData(RegionName.HOTP_EYEBALL, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_TELEPORTS.value: LocationData(
        RegionName.HOTP_LOWER_ARIAS, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_WORM_PILLAR.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_TO_CLAW_1.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_TO_CLAW_2.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_CLAW_ACCESS.value: LocationData(
        RegionName.HOTP_CLAW_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_GHOSTS.value: LocationData(RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_LEFT_3.value: LocationData(RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_ABOVE_OLD_MAN.value: LocationData(
        RegionName.HOTP_ABOVE_OLD_MAN, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_TO_ABOVE_OLD_MAN.value: LocationData(
        RegionName.HOTP_TOP_LEFT, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_TP_PUZZLE.value: LocationData(RegionName.HOTP_TP_PUZZLE, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_EYEBALL_SHORTCUT.value: LocationData(
        RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_BELL_ACCESS.value: LocationData(
        RegionName.HOTP_BELL_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_SWITCH_1ST_ROOM.value: LocationData(RegionName.HOTP_START, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_SWITCH_LEFT_BACKTRACK.value: LocationData(
        RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_CRYSTAL_ROCK_ACCESS.value: LocationData(
        RegionName.HOTP_MECH_VOID_CONNECTION, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_CRYSTAL_BOTTOM.value: LocationData(
        RegionName.HOTP_MECH_VOID_CONNECTION, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_CRYSTAL_LOWER.value: LocationData(RegionName.HOTP_LOWER, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_CRYSTAL_AFTER_CLAW.value: LocationData(
        RegionName.HOTP_CLAW_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_CRYSTAL_MAIDEN_1.value: LocationData(RegionName.HOTP_MAIDEN, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_CRYSTAL_MAIDEN_2.value: LocationData(RegionName.HOTP_MAIDEN, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_CRYSTAL_BELL_ACCESS.value: LocationData(
        RegionName.HOTP_BELL_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_CRYSTAL_HEART.value: LocationData(RegionName.HOTP_BOSS_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP),
    LocationName.HOTP_CRYSTAL_BELOW_PUZZLE.value: LocationData(
        RegionName.HOTP_TP_FALL_TOP, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationName.HOTP_FACE_OLD_MAN.value: LocationData(RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationName.ROA_ELEVATOR_1.value: LocationData(RegionName.HOTP_BOSS, LocationGroup.ELEVATOR, Area.ROA),
    LocationName.ROA_ELEVATOR_2.value: LocationData(RegionName.ROA_ELEVATOR, LocationGroup.ELEVATOR, Area.ROA),
    LocationName.ROA_SWITCH_ASCEND.value: LocationData(RegionName.ROA_BOTTOM_ASCEND, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_AFTER_WORMS.value: LocationData(
        RegionName.ROA_WORMS_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_RIGHT_PATH.value: LocationData(
        RegionName.ROA_RIGHT_SWITCH_1, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_APEX_ACCESS.value: LocationData(
        RegionName.ROA_APEX_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_ICARUS.value: LocationData(RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_SHAFT_L.value: LocationData(RegionName.ROA_MIDDLE_LADDER, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_SHAFT_R.value: LocationData(RegionName.ROA_MIDDLE_LADDER, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_ELEVATOR.value: LocationData(RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_SHAFT_DOWNWARDS.value: LocationData(
        RegionName.ROA_SP_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_SPIDERS.value: LocationData(RegionName.ROA_SPIDERS_2, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_DARK_ROOM.value: LocationData(RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_ASCEND_SHORTCUT.value: LocationData(RegionName.ROA_MIDDLE, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_1ST_SHORTCUT.value: LocationData(
        RegionName.ROA_BOTTOM_ASCEND, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_SPIKE_CLIMB.value: LocationData(RegionName.ROA_SPIKE_CLIMB, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_ABOVE_CENTAUR.value: LocationData(
        RegionName.ROA_SP_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_BLOOD_POT.value: LocationData(RegionName.ROA_CENTAUR, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_WORMS.value: LocationData(RegionName.ROA_WORMS, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_TRIPLE_1.value: LocationData(RegionName.ROA_TRIPLE_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_TRIPLE_3.value: LocationData(RegionName.ROA_TRIPLE_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_BABY_GORGON.value: LocationData(RegionName.ROA_FLAMES, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_SWITCH_BOSS_ACCESS.value: LocationData(
        RegionName.ROA_BOSS_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_BLOOD_POT_L.value: LocationData(
        RegionName.ROA_BOSS_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_BLOOD_POT_R.value: LocationData(
        RegionName.ROA_BOSS_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_SWITCH_LOWER_VOID.value: LocationData(RegionName.ROA_LOWER_VOID, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_1ST_ROOM.value: LocationData(RegionName.ROA_START, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_BABY_GORGON.value: LocationData(
        RegionName.ROA_LOWER_VOID_CONNECTION, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_CRYSTAL_LADDER_R.value: LocationData(
        RegionName.ROA_RIGHT_SWITCH_2, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_CRYSTAL_LADDER_L.value: LocationData(RegionName.ROA_LEFT_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_CENTAUR.value: LocationData(RegionName.ROA_CENTAUR, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_SPIKE_BALLS.value: LocationData(RegionName.ROA_UPPER_VOID, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_LEFT_ASCEND.value: LocationData(
        RegionName.ROA_LEFT_ASCENT_CRYSTAL, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_CRYSTAL_SHAFT.value: LocationData(RegionName.ROA_SP_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_BRANCH_R.value: LocationData(RegionName.ROA_RIGHT_BRANCH, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_BRANCH_L.value: LocationData(RegionName.ROA_RIGHT_BRANCH, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_CRYSTAL_3_REAPERS.value: LocationData(
        RegionName.ROA_TRIPLE_REAPER, LocationGroup.SWITCH, Area.ROA
    ),
    LocationName.ROA_CRYSTAL_TRIPLE_2.value: LocationData(RegionName.ROA_TRIPLE_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_FACE_SPIDERS.value: LocationData(RegionName.ROA_SPIDERS_1, LocationGroup.SWITCH, Area.ROA),
    LocationName.ROA_FACE_BLUE_KEY.value: LocationData(RegionName.ROA_BOTTOM_ASCEND, LocationGroup.SWITCH, Area.ROA),
    LocationName.DARK_SWITCH.value: LocationData(RegionName.DARK_START, LocationGroup.SWITCH, Area.DARK),
    LocationName.APEX_ELEVATOR.value: LocationData(RegionName.APEX, LocationGroup.ELEVATOR, Area.APEX),
    LocationName.APEX_SWITCH.value: LocationData(RegionName.APEX, LocationGroup.SWITCH, Area.APEX),
    LocationName.CAVES_SWITCH_SKELETONS.value: LocationData(RegionName.CAVES_UPPER, LocationGroup.SWITCH, Area.CAVES),
    LocationName.CAVES_SWITCH_CATA_ACCESS_1.value: LocationData(
        RegionName.CAVES_LOWER, LocationGroup.SWITCH, Area.CAVES
    ),
    LocationName.CAVES_SWITCH_CATA_ACCESS_2.value: LocationData(
        RegionName.CAVES_LOWER, LocationGroup.SWITCH, Area.CAVES
    ),
    LocationName.CAVES_SWITCH_CATA_ACCESS_3.value: LocationData(
        RegionName.CAVES_LOWER, LocationGroup.SWITCH, Area.CAVES
    ),
    LocationName.CAVES_FACE_1ST_ROOM.value: LocationData(RegionName.CAVES_START, LocationGroup.SWITCH, Area.CAVES),
    LocationName.CATA_ELEVATOR_1.value: LocationData(RegionName.CATA_ELEVATOR, LocationGroup.ELEVATOR, Area.CATA),
    LocationName.CATA_ELEVATOR_2.value: LocationData(RegionName.CATA_BOSS, LocationGroup.ELEVATOR, Area.CATA),
    LocationName.CATA_SWITCH_ELEVATOR.value: LocationData(RegionName.CATA_TOP, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_SWITCH_SHORTCUT.value: LocationData(
        RegionName.CATA_VERTICAL_SHORTCUT, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_TOP.value: LocationData(RegionName.CATA_TOP, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_SWITCH_CLAW_1.value: LocationData(
        RegionName.CATA_SNAKE_MUSHROOMS, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_CLAW_2.value: LocationData(
        RegionName.CATA_SNAKE_MUSHROOMS, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_WATER_1.value: LocationData(
        RegionName.CATA_DOUBLE_SWITCH, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_WATER_2.value: LocationData(
        RegionName.CATA_DOUBLE_SWITCH, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_DEV_ROOM.value: LocationData(
        RegionName.CATA_DEV_ROOM_CONNECTION, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_AFTER_BLUE_DOOR.value: LocationData(
        RegionName.CATA_BLUE_EYE_DOOR, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_SHORTCUT_ACCESS.value: LocationData(
        RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_LADDER_BLOCKS.value: LocationData(
        RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_MID_SHORTCUT.value: LocationData(
        RegionName.CATA_VERTICAL_SHORTCUT, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_SWITCH_1ST_ROOM.value: LocationData(RegionName.CATA_START, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_SWITCH_FLAMES_2.value: LocationData(RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_SWITCH_FLAMES_1.value: LocationData(RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_CRYSTAL_POISON_ROOTS.value: LocationData(
        RegionName.CATA_POISON_ROOTS, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_FACE_AFTER_BOW.value: LocationData(RegionName.CATA_BOW_CAMPFIRE, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_FACE_BOW.value: LocationData(RegionName.CATA_BOW, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_FACE_X4.value: LocationData(RegionName.CATA_4_FACES, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_FACE_CAMPFIRE.value: LocationData(RegionName.CATA_BOSS, LocationGroup.SWITCH, Area.CATA),
    LocationName.CATA_FACE_DOUBLE_DOOR.value: LocationData(
        RegionName.CATA_DOUBLE_DOOR, LocationGroup.SWITCH, Area.CATA
    ),
    LocationName.CATA_FACE_BOTTOM.value: LocationData(RegionName.CATA_DOUBLE_DOOR, LocationGroup.SWITCH, Area.CATA),
    LocationName.TR_ELEVATOR.value: LocationData(RegionName.TR_START, LocationGroup.ELEVATOR, Area.TR),
    LocationName.TR_SWITCH_ADORNED_L.value: LocationData(RegionName.TR_BOTTOM, LocationGroup.SWITCH, Area.TR),
    LocationName.TR_SWITCH_ADORNED_M.value: LocationData(RegionName.TR_LEFT, LocationGroup.SWITCH, Area.TR),
    LocationName.TR_SWITCH_ADORNED_R.value: LocationData(RegionName.TR_TOP_RIGHT, LocationGroup.SWITCH, Area.TR),
    LocationName.TR_SWITCH_ELEVATOR.value: LocationData(RegionName.CATA_BOSS, LocationGroup.SWITCH, Area.TR),
    LocationName.TR_SWITCH_BOTTOM.value: LocationData(RegionName.TR_MIDDLE_RIGHT, LocationGroup.SWITCH, Area.TR),
    LocationName.TR_CRYSTAL_GOLD.value: LocationData(RegionName.TR_TOP_RIGHT, LocationGroup.SWITCH, Area.TR),
    LocationName.TR_CRYSTAL_DARK_ARIAS.value: LocationData(RegionName.TR_DARK_ARIAS, LocationGroup.SWITCH, Area.TR),
    LocationName.CD_SWITCH_1.value: LocationData(RegionName.CD_START, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_SWITCH_2.value: LocationData(RegionName.CD_2, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_SWITCH_3.value: LocationData(RegionName.CD_3, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_SWITCH_CAMPFIRE.value: LocationData(RegionName.CD_MIDDLE, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_SWITCH_TOP.value: LocationData(RegionName.CD_TOP, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_CRYSTAL_BACKTRACK.value: LocationData(RegionName.CD_2, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_CRYSTAL_START.value: LocationData(RegionName.CD_START, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_CRYSTAL_CAMPFIRE.value: LocationData(RegionName.CD_CAMPFIRE_3, LocationGroup.SWITCH, Area.CD),
    LocationName.CD_CRYSTAL_STEPS.value: LocationData(RegionName.CD_STEPS, LocationGroup.SWITCH, Area.CD),
    LocationName.CATH_SWITCH_BOTTOM.value: LocationData(RegionName.CATH_START_RIGHT, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_SWITCH_BESIDE_SHAFT.value: LocationData(
        RegionName.CATH_SHAFT_ACCESS, LocationGroup.SWITCH, Area.CATH
    ),
    LocationName.CATH_SWITCH_TOP_CAMPFIRE.value: LocationData(RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_CRYSTAL_1ST_ROOM.value: LocationData(
        RegionName.CATH_START_TOP_LEFT, LocationGroup.SWITCH, Area.CATH
    ),
    LocationName.CATH_CRYSTAL_SHAFT.value: LocationData(RegionName.CATH_LEFT_SHAFT, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_CRYSTAL_SPIKE_PIT.value: LocationData(RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_CRYSTAL_TOP_L.value: LocationData(RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_CRYSTAL_TOP_R.value: LocationData(RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_CRYSTAL_SHAFT_ACCESS.value: LocationData(
        RegionName.CATH_SHAFT_ACCESS, LocationGroup.SWITCH, Area.CATH
    ),
    LocationName.CATH_CRYSTAL_ORBS.value: LocationData(RegionName.CATH_ORB_ROOM, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_FACE_LEFT.value: LocationData(RegionName.CATH_START_LEFT, LocationGroup.SWITCH, Area.CATH),
    LocationName.CATH_FACE_RIGHT.value: LocationData(RegionName.CATH_START_LEFT, LocationGroup.SWITCH, Area.CATH),
    LocationName.SP_SWITCH_DOUBLE_DOORS.value: LocationData(RegionName.SP_HEARTS, LocationGroup.SWITCH, Area.SP),
    LocationName.SP_SWITCH_BUBBLES.value: LocationData(RegionName.SP_CAMPFIRE_1, LocationGroup.SWITCH, Area.SP),
    LocationName.SP_SWITCH_AFTER_STAR.value: LocationData(RegionName.SP_STAR_CONNECTION, LocationGroup.SWITCH, Area.SP),
    LocationName.SP_CRYSTAL_BLOCKS.value: LocationData(RegionName.SP_START, LocationGroup.SWITCH, Area.SP),
    LocationName.SP_CRYSTAL_STAR.value: LocationData(RegionName.SP_SHAFT, LocationGroup.SWITCH, Area.SP),
    LocationName.MECH_CYCLOPS.value: LocationData(RegionName.MECH_ZEEK, LocationGroup.ITEM, Area.MECH),
    LocationName.CD_CROWN.value: LocationData(RegionName.CD_BOSS, LocationGroup.ITEM, Area.CD),
    # LocationName.GT_OLD_MAN.value: LocationData(RegionName.GT_OLD_MAN, LocationGroup.FAMILIAR, Area.GT),
    # LocationName.MECH_OLD_MAN.value: LocationData(RegionName.MECH_OLD_MAN, LocationGroup.FAMILIAR, Area.MECH),
    # LocationName.HOTP_OLD_MAN.value: LocationData(RegionName.HOTP_OLD_MAN, LocationGroup.FAMILIAR, Area.HOTP),
    # LocationName.CATA_GIL.value: LocationData(RegionName.CATA_DEV_ROOM, LocationGroup.FAMILIAR, Area.CATA),
}

base_id = 333000
location_name_to_id: Dict[str, int] = {name: base_id + i for i, name in enumerate(location_table)}


def get_location_group(location_name: str) -> LocationGroup:
    return location_table[location_name].group


def get_location_area(location_name: str) -> Area:
    return location_table[location_name].area


location_name_groups: Dict[str, Set[str]] = {
    group.value: set(location for location in location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
location_name_groups.update(
    {
        group.value: set(location for location in location_names)
        for group, location_names in groupby(sorted(location_table, key=get_location_area), get_location_area)
    }
)
