from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import Dict, Set

from BaseClasses import Location

from .regions import Regions


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


class LocationGroups(str, Enum):
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


class Locations(str, Enum):
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
    game = "Astalon Tears of the Earth"


@dataclass(frozen=True)
class AstalonLocationData:
    region: Regions
    group: LocationGroups
    area: Area


location_table: Dict[str, AstalonLocationData] = {
    Locations.GT_GORGONHEART.value: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.ITEM, Area.GT),
    Locations.GT_ANCIENTS_RING.value: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.ITEM, Area.GT),
    Locations.GT_SWORD.value: AstalonLocationData(Regions.GT_SWORD, LocationGroups.ITEM, Area.GT),
    Locations.GT_MAP.value: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.ITEM, Area.GT),
    Locations.GT_ASCENDANT_KEY.value: AstalonLocationData(Regions.GT_ASCENDANT_KEY, LocationGroups.ITEM, Area.GT),
    Locations.GT_BANISH.value: AstalonLocationData(Regions.GT_LEFT, LocationGroups.ITEM, Area.GT),
    Locations.GT_VOID.value: AstalonLocationData(Regions.GT_VOID, LocationGroups.ITEM, Area.GT),
    Locations.GT_EYE_RED.value: AstalonLocationData(Regions.GT_BOSS, LocationGroups.ITEM, Area.GT),
    Locations.GT_ATTACK.value: AstalonLocationData(Regions.GT_BABY_GORGON, LocationGroups.ATTACK, Area.GT),
    Locations.GT_HP_1_RING.value: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.HEALTH, Area.GT),
    Locations.GT_HP_5_KEY.value: AstalonLocationData(Regions.GT_ASCENDANT_KEY, LocationGroups.HEALTH, Area.GT),
    Locations.GT_WHITE_KEY_START.value: AstalonLocationData(Regions.ENTRANCE, LocationGroups.KEY_WHITE, Area.GT),
    Locations.GT_WHITE_KEY_RIGHT.value: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.KEY_WHITE, Area.GT),
    Locations.GT_WHITE_KEY_BOSS.value: AstalonLocationData(Regions.GT_TOP_RIGHT, LocationGroups.KEY_WHITE, Area.GT),
    Locations.GT_BLUE_KEY_BONESNAKE.value: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.KEY_BLUE, Area.GT),
    Locations.GT_BLUE_KEY_BUTT.value: AstalonLocationData(Regions.GT_BUTT, LocationGroups.KEY_BLUE, Area.GT),
    Locations.GT_BLUE_KEY_WALL.value: AstalonLocationData(Regions.GT_BUTT, LocationGroups.KEY_BLUE, Area.GT),
    Locations.GT_BLUE_KEY_POT.value: AstalonLocationData(Regions.GT_UPPER_PATH, LocationGroups.KEY_BLUE, Area.GT),
    Locations.GT_RED_KEY.value: AstalonLocationData(Regions.GT_BOSS, LocationGroups.KEY_RED, Area.GT),
    Locations.MECH_BOOTS.value: AstalonLocationData(Regions.MECH_BOOTS_UPPER, LocationGroups.ITEM, Area.MECH),
    Locations.MECH_CLOAK.value: AstalonLocationData(Regions.MECH_CLOAK, LocationGroups.ITEM, Area.MECH),
    Locations.MECH_EYE_BLUE.value: AstalonLocationData(Regions.MECH_BOSS, LocationGroups.ITEM, Area.MECH),
    Locations.MECH_ATTACK_VOLANTIS.value: AstalonLocationData(Regions.HOTP_START, LocationGroups.ATTACK, Area.MECH),
    Locations.MECH_ATTACK_STAR.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.ATTACK, Area.MECH),
    Locations.MECH_HP_1_SWITCH.value: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.HEALTH, Area.MECH),
    Locations.MECH_HP_1_STAR.value: AstalonLocationData(Regions.MECH_BRAM_TUNNEL, LocationGroups.HEALTH, Area.MECH),
    Locations.MECH_HP_3_CLAW.value: AstalonLocationData(Regions.MECH_BOTTOM_CAMPFIRE, LocationGroups.HEALTH, Area.MECH),
    Locations.MECH_WHITE_KEY_LINUS.value: AstalonLocationData(
        Regions.MECH_SWORD_CONNECTION, LocationGroups.KEY_WHITE, Area.MECH
    ),
    Locations.MECH_WHITE_KEY_BK.value: AstalonLocationData(Regions.MECH_AFTER_BK, LocationGroups.KEY_WHITE, Area.MECH),
    Locations.MECH_WHITE_KEY_ARENA.value: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.KEY_WHITE, Area.MECH),
    Locations.MECH_WHITE_KEY_TOP.value: AstalonLocationData(Regions.MECH_TOP, LocationGroups.KEY_WHITE, Area.MECH),
    Locations.MECH_BLUE_KEY_VOID.value: AstalonLocationData(Regions.GT_VOID, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_SNAKE.value: AstalonLocationData(Regions.MECH_SNAKE, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_LINUS.value: AstalonLocationData(
        Regions.MECH_LOWER_ARIAS, LocationGroups.KEY_BLUE, Area.MECH
    ),
    Locations.MECH_BLUE_KEY_SACRIFICE.value: AstalonLocationData(
        Regions.MECH_SACRIFICE, LocationGroups.KEY_BLUE, Area.MECH
    ),
    Locations.MECH_BLUE_KEY_RED.value: AstalonLocationData(Regions.MECH_START, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_ARIAS.value: AstalonLocationData(
        Regions.MECH_ARIAS_EYEBALL, LocationGroups.KEY_BLUE, Area.MECH
    ),
    Locations.MECH_BLUE_KEY_BLOCKS.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_TOP.value: AstalonLocationData(Regions.MECH_SPLIT_PATH, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_OLD_MAN.value: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_SAVE.value: AstalonLocationData(Regions.MECH_TOP, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_BLUE_KEY_POT.value: AstalonLocationData(Regions.MECH_POTS, LocationGroups.KEY_BLUE, Area.MECH),
    Locations.MECH_RED_KEY.value: AstalonLocationData(Regions.MECH_LOWER_VOID, LocationGroups.KEY_RED, Area.MECH),
    Locations.HOTP_BELL.value: AstalonLocationData(Regions.HOTP_BELL, LocationGroups.ITEM, Area.HOTP),
    Locations.HOTP_AMULET.value: AstalonLocationData(Regions.HOTP_AMULET, LocationGroups.ITEM, Area.HOTP),
    Locations.HOTP_CLAW.value: AstalonLocationData(Regions.HOTP_CLAW, LocationGroups.ITEM, Area.HOTP),
    Locations.HOTP_GAUNTLET.value: AstalonLocationData(Regions.HOTP_GAUNTLET, LocationGroups.ITEM, Area.HOTP),
    Locations.HOTP_MAIDEN_RING.value: AstalonLocationData(Regions.HOTP_MAIDEN, LocationGroups.ITEM, Area.HOTP),
    Locations.HOTP_HP_1_CLAW.value: AstalonLocationData(Regions.HOTP_CLAW_LEFT, LocationGroups.HEALTH, Area.HOTP),
    Locations.HOTP_HP_2_LADDER.value: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.HEALTH, Area.HOTP),
    Locations.HOTP_HP_2_GAUNTLET.value: AstalonLocationData(Regions.HOTP_TP_FALL_TOP, LocationGroups.HEALTH, Area.HOTP),
    Locations.HOTP_HP_5_OLD_MAN.value: AstalonLocationData(
        Regions.HOTP_ABOVE_OLD_MAN, LocationGroups.HEALTH, Area.HOTP
    ),
    Locations.HOTP_HP_5_MAZE.value: AstalonLocationData(Regions.HOTP_LOWER_VOID, LocationGroups.HEALTH, Area.HOTP),
    Locations.HOTP_HP_5_START.value: AstalonLocationData(Regions.HOTP_START, LocationGroups.HEALTH, Area.HOTP),
    Locations.HOTP_WHITE_KEY_LEFT.value: AstalonLocationData(
        Regions.HOTP_START_LEFT, LocationGroups.KEY_WHITE, Area.HOTP
    ),
    Locations.HOTP_WHITE_KEY_GHOST.value: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.KEY_WHITE, Area.HOTP),
    Locations.HOTP_WHITE_KEY_OLD_MAN.value: AstalonLocationData(
        Regions.HOTP_ELEVATOR, LocationGroups.KEY_WHITE, Area.HOTP
    ),
    Locations.HOTP_WHITE_KEY_BOSS.value: AstalonLocationData(
        Regions.HOTP_UPPER_ARIAS, LocationGroups.KEY_WHITE, Area.HOTP
    ),
    Locations.HOTP_BLUE_KEY_STATUE.value: AstalonLocationData(
        Regions.HOTP_EPIMETHEUS, LocationGroups.KEY_BLUE, Area.HOTP
    ),
    Locations.HOTP_BLUE_KEY_GOLD.value: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.KEY_BLUE, Area.HOTP),
    Locations.HOTP_BLUE_KEY_AMULET.value: AstalonLocationData(
        Regions.HOTP_AMULET_CONNECTION, LocationGroups.KEY_BLUE, Area.HOTP
    ),
    Locations.HOTP_BLUE_KEY_LADDER.value: AstalonLocationData(
        Regions.HOTP_ELEVATOR, LocationGroups.KEY_BLUE, Area.HOTP
    ),
    Locations.HOTP_BLUE_KEY_TELEPORTS.value: AstalonLocationData(
        Regions.HOTP_ELEVATOR, LocationGroups.KEY_BLUE, Area.HOTP
    ),
    Locations.HOTP_BLUE_KEY_MAZE.value: AstalonLocationData(Regions.HOTP_TP_PUZZLE, LocationGroups.KEY_BLUE, Area.HOTP),
    Locations.HOTP_RED_KEY.value: AstalonLocationData(Regions.HOTP_RED_KEY, LocationGroups.KEY_RED, Area.HOTP),
    Locations.ROA_ICARUS.value: AstalonLocationData(Regions.ROA_ICARUS, LocationGroups.ITEM, Area.ROA),
    Locations.ROA_EYE_GREEN.value: AstalonLocationData(Regions.ROA_BOSS, LocationGroups.ITEM, Area.ROA),
    Locations.ROA_ATTACK.value: AstalonLocationData(Regions.ROA_MIDDLE, LocationGroups.ATTACK, Area.ROA),
    Locations.ROA_HP_1_LEFT.value: AstalonLocationData(Regions.ROA_LEFT_ASCENT, LocationGroups.HEALTH, Area.ROA),
    Locations.ROA_HP_2_RIGHT.value: AstalonLocationData(Regions.ROA_RIGHT_BRANCH, LocationGroups.HEALTH, Area.ROA),
    Locations.ROA_HP_5_SOLARIA.value: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH, Area.ROA),
    Locations.ROA_WHITE_KEY_SAVE.value: AstalonLocationData(Regions.ROA_WORMS, LocationGroups.KEY_WHITE, Area.ROA),
    Locations.ROA_WHITE_KEY_REAPERS.value: AstalonLocationData(
        Regions.ROA_LEFT_ASCENT, LocationGroups.KEY_WHITE, Area.ROA
    ),
    Locations.ROA_WHITE_KEY_TORCHES.value: AstalonLocationData(Regions.ROA_MIDDLE, LocationGroups.KEY_WHITE, Area.ROA),
    Locations.ROA_WHITE_KEY_PORTAL.value: AstalonLocationData(
        Regions.ROA_UPPER_VOID, LocationGroups.KEY_WHITE, Area.ROA
    ),
    Locations.ROA_BLUE_KEY_FACE.value: AstalonLocationData(
        Regions.ROA_BOTTOM_ASCEND, LocationGroups.KEY_BLUE, Area.ROA
    ),
    Locations.ROA_BLUE_KEY_FLAMES.value: AstalonLocationData(
        Regions.ROA_ARIAS_BABY_GORGON, LocationGroups.KEY_BLUE, Area.ROA
    ),
    Locations.ROA_BLUE_KEY_BABY.value: AstalonLocationData(
        Regions.ROA_LEFT_BABY_GORGON, LocationGroups.KEY_BLUE, Area.ROA
    ),
    Locations.ROA_BLUE_KEY_TOP.value: AstalonLocationData(
        Regions.ROA_BOSS_CONNECTION, LocationGroups.KEY_BLUE, Area.ROA
    ),
    Locations.ROA_BLUE_KEY_POT.value: AstalonLocationData(Regions.ROA_TRIPLE_REAPER, LocationGroups.KEY_BLUE, Area.ROA),
    Locations.ROA_RED_KEY.value: AstalonLocationData(Regions.ROA_RED_KEY, LocationGroups.KEY_RED, Area.ROA),
    Locations.DARK_HP_4.value: AstalonLocationData(Regions.DARK_END, LocationGroups.HEALTH, Area.DARK),
    Locations.DARK_WHITE_KEY.value: AstalonLocationData(Regions.DARK_END, LocationGroups.KEY_WHITE, Area.DARK),
    Locations.APEX_CHALICE.value: AstalonLocationData(Regions.APEX_CENTAUR, LocationGroups.ITEM, Area.APEX),
    Locations.APEX_HP_1_CHALICE.value: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH, Area.APEX),
    Locations.APEX_HP_5_HEART.value: AstalonLocationData(Regions.APEX_HEART, LocationGroups.HEALTH, Area.APEX),
    Locations.APEX_BLUE_KEY.value: AstalonLocationData(Regions.APEX, LocationGroups.KEY_BLUE, Area.APEX),
    Locations.CATA_BOW.value: AstalonLocationData(Regions.CATA_BOW, LocationGroups.ITEM, Area.CATA),
    Locations.CAVES_ATTACK_RED.value: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.ATTACK, Area.CAVES),
    Locations.CAVES_ATTACK_BLUE.value: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.ATTACK, Area.CAVES),
    Locations.CAVES_ATTACK_GREEN.value: AstalonLocationData(
        Regions.CAVES_ITEM_CHAIN, LocationGroups.ATTACK, Area.CAVES
    ),
    Locations.CATA_ATTACK_ROOT.value: AstalonLocationData(
        Regions.CATA_CLIMBABLE_ROOT, LocationGroups.ATTACK, Area.CATA
    ),
    Locations.CATA_ATTACK_POISON.value: AstalonLocationData(
        Regions.CATA_POISON_ROOTS, LocationGroups.ATTACK, Area.CATA
    ),
    Locations.CAVES_HP_1_START.value: AstalonLocationData(Regions.CAVES_START, LocationGroups.HEALTH, Area.CAVES),
    Locations.CAVES_HP_1_CYCLOPS.value: AstalonLocationData(Regions.CAVES_ARENA, LocationGroups.HEALTH, Area.CAVES),
    Locations.CATA_HP_1_ABOVE_POISON.value: AstalonLocationData(
        Regions.CATA_POISON_ROOTS, LocationGroups.HEALTH, Area.CATA
    ),
    Locations.CATA_HP_2_BEFORE_POISON.value: AstalonLocationData(
        Regions.CATA_POISON_ROOTS, LocationGroups.HEALTH, Area.CATA
    ),
    Locations.CATA_HP_2_AFTER_POISON.value: AstalonLocationData(
        Regions.CATA_POISON_ROOTS, LocationGroups.HEALTH, Area.CATA
    ),
    Locations.CATA_HP_2_GEMINI_BOTTOM.value: AstalonLocationData(
        Regions.CATA_DOUBLE_DOOR, LocationGroups.HEALTH, Area.CATA
    ),
    Locations.CATA_HP_2_GEMINI_TOP.value: AstalonLocationData(Regions.CATA_CENTAUR, LocationGroups.HEALTH, Area.CATA),
    Locations.CATA_HP_2_ABOVE_GEMINI.value: AstalonLocationData(Regions.CATA_FLAMES, LocationGroups.HEALTH, Area.CATA),
    Locations.CAVES_HP_5_CHAIN.value: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.HEALTH, Area.CAVES),
    Locations.CATA_WHITE_KEY_HEAD.value: AstalonLocationData(Regions.CATA_TOP, LocationGroups.KEY_WHITE, Area.CATA),
    Locations.CATA_WHITE_KEY_DEV_ROOM.value: AstalonLocationData(
        Regions.CATA_DEV_ROOM_CONNECTION, LocationGroups.KEY_WHITE, Area.CATA
    ),
    Locations.CATA_WHITE_KEY_PRISON.value: AstalonLocationData(Regions.CATA_BOSS, LocationGroups.KEY_WHITE, Area.CATA),
    Locations.CATA_BLUE_KEY_SLIMES.value: AstalonLocationData(
        Regions.CATA_BOW_CAMPFIRE, LocationGroups.KEY_BLUE, Area.CATA
    ),
    Locations.CATA_BLUE_KEY_EYEBALLS.value: AstalonLocationData(
        Regions.CATA_CENTAUR, LocationGroups.KEY_BLUE, Area.CATA
    ),
    Locations.TR_ADORNED_KEY.value: AstalonLocationData(Regions.TR_BOTTOM, LocationGroups.ITEM, Area.TR),
    Locations.TR_HP_1_BOTTOM.value: AstalonLocationData(Regions.TR_BOTTOM_LEFT, LocationGroups.HEALTH, Area.TR),
    Locations.TR_HP_2_TOP.value: AstalonLocationData(Regions.TR_LEFT, LocationGroups.HEALTH, Area.TR),
    Locations.TR_RED_KEY.value: AstalonLocationData(Regions.CATA_BOSS, LocationGroups.KEY_RED, Area.TR),
    Locations.CD_ATTACK.value: AstalonLocationData(Regions.CD_TOP, LocationGroups.ATTACK, Area.CD),
    Locations.CD_HP_1.value: AstalonLocationData(Regions.CD_TOP, LocationGroups.HEALTH, Area.CD),
    Locations.CATH_BLOCK.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.ITEM, Area.CATH),
    Locations.CATH_ATTACK.value: AstalonLocationData(Regions.CATH_UPPER_SPIKE_PIT, LocationGroups.ATTACK, Area.CATH),
    Locations.CATH_HP_1_TOP_LEFT.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.HEALTH, Area.CATH),
    Locations.CATH_HP_1_TOP_RIGHT.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.HEALTH, Area.CATH),
    Locations.CATH_HP_2_CLAW.value: AstalonLocationData(Regions.CATH_LEFT_SHAFT, LocationGroups.HEALTH, Area.CATH),
    Locations.CATH_HP_5_BELL.value: AstalonLocationData(Regions.CATH_CAMPFIRE_1, LocationGroups.HEALTH, Area.CATH),
    Locations.SP_STAR.value: AstalonLocationData(Regions.SP_STAR, LocationGroups.ITEM, Area.SP),
    Locations.SP_ATTACK.value: AstalonLocationData(Regions.SP_CAMPFIRE_2, LocationGroups.ATTACK, Area.SP),
    Locations.SP_HP_1.value: AstalonLocationData(Regions.SP_FROG, LocationGroups.HEALTH, Area.SP),
    Locations.SP_BLUE_KEY_BUBBLES.value: AstalonLocationData(Regions.SP_START, LocationGroups.KEY_BLUE, Area.SP),
    Locations.SP_BLUE_KEY_STAR.value: AstalonLocationData(Regions.SP_STAR_END, LocationGroups.KEY_BLUE, Area.SP),
    Locations.SP_BLUE_KEY_PAINTING.value: AstalonLocationData(Regions.SP_PAINTING, LocationGroups.KEY_BLUE, Area.SP),
    Locations.SP_BLUE_KEY_ARIAS.value: AstalonLocationData(Regions.SP_CAMPFIRE_2, LocationGroups.KEY_BLUE, Area.SP),
    Locations.SHOP_GIFT.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_KNOWLEDGE.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_MERCY.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ORB_SEEKER.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_MAP_REVEAL.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_CARTOGRAPHER.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_DEATH_ORB.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_DEATH_POINT.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_TITANS_EGO.value: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ALGUS_ARCANIST.value: AstalonLocationData(Regions.SHOP_ALGUS, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ALGUS_SHOCK.value: AstalonLocationData(Regions.SHOP_ALGUS, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ALGUS_METEOR.value: AstalonLocationData(Regions.SHOP_ALGUS, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ARIAS_GORGONSLAYER.value: AstalonLocationData(Regions.SHOP_ARIAS, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ARIAS_LAST_STAND.value: AstalonLocationData(Regions.SHOP_ARIAS, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ARIAS_LIONHEART.value: AstalonLocationData(Regions.SHOP_ARIAS, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_KYULI_ASSASSIN.value: AstalonLocationData(Regions.SHOP_KYULI, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_KYULI_BULLSEYE.value: AstalonLocationData(Regions.SHOP_KYULI, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_KYULI_RAY.value: AstalonLocationData(Regions.SHOP_KYULI, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ZEEK_JUNKYARD.value: AstalonLocationData(Regions.SHOP_ZEEK, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ZEEK_ORBS.value: AstalonLocationData(Regions.SHOP_ZEEK, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_ZEEK_LOOT.value: AstalonLocationData(Regions.SHOP_ZEEK, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_BRAM_AXE.value: AstalonLocationData(Regions.SHOP_BRAM, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_BRAM_HUNTER.value: AstalonLocationData(Regions.SHOP_BRAM, LocationGroups.SHOP, Area.SHOP),
    Locations.SHOP_BRAM_WHIPLASH.value: AstalonLocationData(Regions.SHOP_BRAM, LocationGroups.SHOP, Area.SHOP),
    Locations.GT_ALGUS.value: AstalonLocationData(Regions.ENTRANCE, LocationGroups.CHARACTER, Area.GT),
    Locations.GT_ARIAS.value: AstalonLocationData(Regions.ENTRANCE, LocationGroups.CHARACTER, Area.GT),
    Locations.GT_KYULI.value: AstalonLocationData(Regions.ENTRANCE, LocationGroups.CHARACTER, Area.GT),
    Locations.MECH_ZEEK.value: AstalonLocationData(Regions.MECH_ZEEK, LocationGroups.CHARACTER, Area.MECH),
    Locations.TR_BRAM.value: AstalonLocationData(Regions.TR_BRAM, LocationGroups.CHARACTER, Area.TR),
    Locations.GT_ELEVATOR_2.value: AstalonLocationData(Regions.GT_BOSS, LocationGroups.ELEVATOR, Area.GT),
    Locations.GT_SWITCH_2ND_ROOM.value: AstalonLocationData(Regions.ENTRANCE, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_1ST_CYCLOPS.value: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_SPIKE_TUNNEL.value: AstalonLocationData(Regions.GT_TOP_LEFT, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_BUTT_ACCESS.value: AstalonLocationData(Regions.GT_SPIKE_TUNNEL, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_GH.value: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_UPPER_PATH_BLOCKS.value: AstalonLocationData(
        Regions.GT_UPPER_PATH_CONNECTION, LocationGroups.SWITCH, Area.GT
    ),
    Locations.GT_SWITCH_UPPER_PATH_ACCESS.value: AstalonLocationData(
        Regions.GT_UPPER_PATH_CONNECTION, LocationGroups.SWITCH, Area.GT
    ),
    Locations.GT_SWITCH_CROSSES.value: AstalonLocationData(Regions.GT_LEFT, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_GH_SHORTCUT.value: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_ARIAS_PATH.value: AstalonLocationData(Regions.GT_TOP_LEFT, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_SWORD_ACCESS.value: AstalonLocationData(Regions.GT_SWORD_FORK, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_SWORD_BACKTRACK.value: AstalonLocationData(
        Regions.GT_SWORD_FORK, LocationGroups.SWITCH, Area.GT
    ),
    Locations.GT_SWITCH_SWORD.value: AstalonLocationData(Regions.GT_SWORD, LocationGroups.SWITCH, Area.GT),
    Locations.GT_SWITCH_UPPER_ARIAS.value: AstalonLocationData(
        Regions.GT_ARIAS_SWORD_SWITCH, LocationGroups.SWITCH, Area.GT
    ),
    Locations.GT_CRYSTAL_LADDER.value: AstalonLocationData(Regions.GT_LADDER_SWITCH, LocationGroups.SWITCH, Area.GT),
    Locations.GT_CRYSTAL_ROTA.value: AstalonLocationData(Regions.GT_UPPER_PATH, LocationGroups.SWITCH, Area.GT),
    Locations.GT_CRYSTAL_OLD_MAN_1.value: AstalonLocationData(Regions.GT_OLD_MAN_FORK, LocationGroups.SWITCH, Area.GT),
    Locations.GT_CRYSTAL_OLD_MAN_2.value: AstalonLocationData(Regions.GT_OLD_MAN_FORK, LocationGroups.SWITCH, Area.GT),
    Locations.MECH_ELEVATOR_1.value: AstalonLocationData(
        Regions.MECH_ZEEK_CONNECTION, LocationGroups.ELEVATOR, Area.MECH
    ),
    Locations.MECH_ELEVATOR_2.value: AstalonLocationData(Regions.MECH_BOSS, LocationGroups.ELEVATOR, Area.MECH),
    Locations.MECH_SWITCH_WATCHER.value: AstalonLocationData(Regions.MECH_ROOTS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_CHAINS.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_BOSS_ACCESS_1.value: AstalonLocationData(
        Regions.MECH_BOSS_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_BOSS_ACCESS_2.value: AstalonLocationData(
        Regions.MECH_BOSS_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_SPLIT_PATH.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_SNAKE_1.value: AstalonLocationData(
        Regions.MECH_BOTTOM_CAMPFIRE, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_BOOTS_ACCESS.value: AstalonLocationData(
        Regions.MECH_BOOTS_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_UPPER_GT_ACCESS.value: AstalonLocationData(
        Regions.MECH_BOTTOM_CAMPFIRE, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_UPPER_VOID_DROP.value: AstalonLocationData(
        Regions.MECH_RIGHT, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_UPPER_VOID.value: AstalonLocationData(
        Regions.MECH_UPPER_VOID, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_LINUS.value: AstalonLocationData(Regions.MECH_LINUS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_TO_BOSS_2.value: AstalonLocationData(
        Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_POTS.value: AstalonLocationData(Regions.MECH_POTS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_MAZE_BACKDOOR.value: AstalonLocationData(
        Regions.HOTP_FALL_BOTTOM, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_TO_BOSS_1.value: AstalonLocationData(
        Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_BLOCK_STAIRS.value: AstalonLocationData(
        Regions.MECH_CLOAK_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_ARIAS_CYCLOPS.value: AstalonLocationData(
        Regions.MECH_CHARACTER_SWAPS, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_BOOTS_LOWER.value: AstalonLocationData(
        Regions.MECH_BOOTS_LOWER, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_CHAINS_GAP.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_LOWER_KEY.value: AstalonLocationData(
        Regions.MECH_SWORD_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_ARIAS.value: AstalonLocationData(
        Regions.MECH_ARIAS_EYEBALL, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_SWITCH_SNAKE_2.value: AstalonLocationData(Regions.MECH_SNAKE, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_KEY_BLOCKS.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_CANNON.value: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_EYEBALL.value: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_SWITCH_INVISIBLE.value: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_CANNON.value: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_LINUS.value: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_LOWER.value: AstalonLocationData(
        Regions.MECH_SWORD_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_TO_BOSS_3.value: AstalonLocationData(
        Regions.MECH_BOSS_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_TRIPLE_1.value: AstalonLocationData(
        Regions.MECH_TRIPLE_SWITCHES, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_TRIPLE_2.value: AstalonLocationData(
        Regions.MECH_TRIPLE_SWITCHES, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_TRIPLE_3.value: AstalonLocationData(
        Regions.MECH_TRIPLE_SWITCHES, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_TOP.value: AstalonLocationData(Regions.MECH_TOP, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_CLOAK.value: AstalonLocationData(
        Regions.MECH_CLOAK_CONNECTION, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_SLIMES.value: AstalonLocationData(
        Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH, Area.MECH
    ),
    Locations.MECH_CRYSTAL_TO_CD.value: AstalonLocationData(Regions.MECH_TOP, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_CAMPFIRE.value: AstalonLocationData(Regions.MECH_BK, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_1ST_ROOM.value: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_OLD_MAN.value: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_TOP_CHAINS.value: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_CRYSTAL_BK.value: AstalonLocationData(Regions.MECH_BK, LocationGroups.SWITCH, Area.MECH),
    Locations.MECH_FACE_ABOVE_VOLANTIS.value: AstalonLocationData(Regions.MECH_BOSS, LocationGroups.SWITCH, Area.MECH),
    Locations.HOTP_ELEVATOR.value: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.ELEVATOR, Area.HOTP),
    Locations.HOTP_SWITCH_ROCK.value: AstalonLocationData(
        Regions.HOTP_AMULET_CONNECTION, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_BELOW_START.value: AstalonLocationData(
        Regions.HOTP_START_BOTTOM, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_LEFT_2.value: AstalonLocationData(Regions.HOTP_START_MID, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_LEFT_1.value: AstalonLocationData(Regions.HOTP_START_MID, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_LOWER_SHORTCUT.value: AstalonLocationData(
        Regions.HOTP_LOWER, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_BELL.value: AstalonLocationData(Regions.HOTP_BELL, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_GHOST_BLOOD.value: AstalonLocationData(
        Regions.HOTP_EYEBALL, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_TELEPORTS.value: AstalonLocationData(
        Regions.HOTP_LOWER_ARIAS, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_WORM_PILLAR.value: AstalonLocationData(
        Regions.HOTP_ELEVATOR, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_TO_CLAW_1.value: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_TO_CLAW_2.value: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_CLAW_ACCESS.value: AstalonLocationData(
        Regions.HOTP_CLAW_CAMPFIRE, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_GHOSTS.value: AstalonLocationData(Regions.HOTP_START_MID, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_LEFT_3.value: AstalonLocationData(Regions.HOTP_START_MID, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_ABOVE_OLD_MAN.value: AstalonLocationData(
        Regions.HOTP_ABOVE_OLD_MAN, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_TO_ABOVE_OLD_MAN.value: AstalonLocationData(
        Regions.HOTP_TOP_LEFT, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_TP_PUZZLE.value: AstalonLocationData(
        Regions.HOTP_TP_PUZZLE, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_EYEBALL_SHORTCUT.value: AstalonLocationData(
        Regions.HOTP_ELEVATOR, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_BELL_ACCESS.value: AstalonLocationData(
        Regions.HOTP_BELL_CAMPFIRE, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_SWITCH_1ST_ROOM.value: AstalonLocationData(Regions.HOTP_START, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_SWITCH_LEFT_BACKTRACK.value: AstalonLocationData(
        Regions.HOTP_ELEVATOR, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_CRYSTAL_ROCK_ACCESS.value: AstalonLocationData(
        Regions.HOTP_MECH_VOID_CONNECTION, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_CRYSTAL_BOTTOM.value: AstalonLocationData(
        Regions.HOTP_MECH_VOID_CONNECTION, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_CRYSTAL_LOWER.value: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_CRYSTAL_AFTER_CLAW.value: AstalonLocationData(
        Regions.HOTP_CLAW_CAMPFIRE, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_CRYSTAL_MAIDEN_1.value: AstalonLocationData(Regions.HOTP_MAIDEN, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_CRYSTAL_MAIDEN_2.value: AstalonLocationData(Regions.HOTP_MAIDEN, LocationGroups.SWITCH, Area.HOTP),
    Locations.HOTP_CRYSTAL_BELL_ACCESS.value: AstalonLocationData(
        Regions.HOTP_BELL_CAMPFIRE, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_CRYSTAL_HEART.value: AstalonLocationData(
        Regions.HOTP_BOSS_CAMPFIRE, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_CRYSTAL_BELOW_PUZZLE.value: AstalonLocationData(
        Regions.HOTP_TP_FALL_TOP, LocationGroups.SWITCH, Area.HOTP
    ),
    Locations.HOTP_FACE_OLD_MAN.value: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.SWITCH, Area.HOTP),
    Locations.ROA_ELEVATOR_1.value: AstalonLocationData(Regions.HOTP_BOSS, LocationGroups.ELEVATOR, Area.ROA),
    Locations.ROA_ELEVATOR_2.value: AstalonLocationData(Regions.ROA_ELEVATOR, LocationGroups.ELEVATOR, Area.ROA),
    Locations.ROA_SWITCH_ASCEND.value: AstalonLocationData(Regions.ROA_BOTTOM_ASCEND, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_AFTER_WORMS.value: AstalonLocationData(Regions.ROA_WORMS, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_RIGHT_PATH.value: AstalonLocationData(
        Regions.ROA_RIGHT_SWITCH_1, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_APEX_ACCESS.value: AstalonLocationData(
        Regions.ROA_APEX_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_ICARUS.value: AstalonLocationData(Regions.ROA_ELEVATOR, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_SHAFT_L.value: AstalonLocationData(Regions.ROA_MIDDLE_LADDER, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_SHAFT_R.value: AstalonLocationData(Regions.ROA_MIDDLE_LADDER, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_ELEVATOR.value: AstalonLocationData(Regions.ROA_ELEVATOR, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_SHAFT_DOWNWARDS.value: AstalonLocationData(
        Regions.ROA_SP_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_SPIDERS.value: AstalonLocationData(Regions.ROA_SPIDERS_2, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_DARK_ROOM.value: AstalonLocationData(Regions.ROA_ELEVATOR, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_ASCEND_SHORTCUT.value: AstalonLocationData(
        Regions.ROA_MIDDLE, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_1ST_SHORTCUT.value: AstalonLocationData(
        Regions.ROA_BOTTOM_ASCEND, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_SPIKE_CLIMB.value: AstalonLocationData(
        Regions.ROA_SPIKE_CLIMB, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_ABOVE_CENTAUR.value: AstalonLocationData(
        Regions.ROA_SP_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_BLOOD_POT.value: AstalonLocationData(Regions.ROA_CENTAUR, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_WORMS.value: AstalonLocationData(Regions.ROA_WORMS, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_TRIPLE_1.value: AstalonLocationData(
        Regions.ROA_TRIPLE_SWITCH, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_TRIPLE_3.value: AstalonLocationData(
        Regions.ROA_TRIPLE_SWITCH, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_BABY_GORGON.value: AstalonLocationData(Regions.ROA_FLAMES, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_SWITCH_BOSS_ACCESS.value: AstalonLocationData(
        Regions.ROA_BOSS_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_BLOOD_POT_L.value: AstalonLocationData(
        Regions.ROA_BOSS_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_BLOOD_POT_R.value: AstalonLocationData(
        Regions.ROA_BOSS_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_SWITCH_LOWER_VOID.value: AstalonLocationData(Regions.ROA_LOWER_VOID, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_CRYSTAL_1ST_ROOM.value: AstalonLocationData(Regions.ROA_START, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_CRYSTAL_BABY_GORGON.value: AstalonLocationData(
        Regions.ROA_LOWER_VOID_CONNECTION, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_LADDER_R.value: AstalonLocationData(
        Regions.ROA_RIGHT_SWITCH_2, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_LADDER_L.value: AstalonLocationData(Regions.ROA_LEFT_SWITCH, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_CRYSTAL_CENTAUR.value: AstalonLocationData(Regions.ROA_CENTAUR, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_CRYSTAL_SPIKE_BALLS.value: AstalonLocationData(
        Regions.ROA_UPPER_VOID, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_LEFT_ASCEND.value: AstalonLocationData(
        Regions.ROA_LEFT_ASCENT_CRYSTAL, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_SHAFT.value: AstalonLocationData(Regions.ROA_SP_CONNECTION, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_CRYSTAL_BRANCH_R.value: AstalonLocationData(
        Regions.ROA_RIGHT_BRANCH, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_BRANCH_L.value: AstalonLocationData(
        Regions.ROA_RIGHT_BRANCH, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_3_REAPERS.value: AstalonLocationData(
        Regions.ROA_TRIPLE_REAPER, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_CRYSTAL_TRIPLE_2.value: AstalonLocationData(
        Regions.ROA_TRIPLE_SWITCH, LocationGroups.SWITCH, Area.ROA
    ),
    Locations.ROA_FACE_SPIDERS.value: AstalonLocationData(Regions.ROA_SPIDERS_1, LocationGroups.SWITCH, Area.ROA),
    Locations.ROA_FACE_BLUE_KEY.value: AstalonLocationData(Regions.ROA_BOTTOM_ASCEND, LocationGroups.SWITCH, Area.ROA),
    Locations.DARK_SWITCH.value: AstalonLocationData(Regions.DARK_START, LocationGroups.SWITCH, Area.DARK),
    Locations.APEX_ELEVATOR.value: AstalonLocationData(Regions.APEX, LocationGroups.ELEVATOR, Area.APEX),
    Locations.APEX_SWITCH.value: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH, Area.APEX),
    Locations.CAVES_SWITCH_SKELETONS.value: AstalonLocationData(Regions.CAVES_UPPER, LocationGroups.SWITCH, Area.CAVES),
    Locations.CAVES_SWITCH_CATA_ACCESS_1.value: AstalonLocationData(
        Regions.CAVES_LOWER, LocationGroups.SWITCH, Area.CAVES
    ),
    Locations.CAVES_SWITCH_CATA_ACCESS_2.value: AstalonLocationData(
        Regions.CAVES_LOWER, LocationGroups.SWITCH, Area.CAVES
    ),
    Locations.CAVES_SWITCH_CATA_ACCESS_3.value: AstalonLocationData(
        Regions.CAVES_LOWER, LocationGroups.SWITCH, Area.CAVES
    ),
    Locations.CAVES_FACE_1ST_ROOM.value: AstalonLocationData(Regions.CAVES_START, LocationGroups.SWITCH, Area.CAVES),
    Locations.CATA_ELEVATOR_1.value: AstalonLocationData(Regions.CATA_ELEVATOR, LocationGroups.ELEVATOR, Area.CATA),
    Locations.CATA_ELEVATOR_2.value: AstalonLocationData(Regions.CATA_BOSS, LocationGroups.ELEVATOR, Area.CATA),
    Locations.CATA_SWITCH_ELEVATOR.value: AstalonLocationData(Regions.CATA_TOP, LocationGroups.SWITCH, Area.CATA),
    Locations.CATA_SWITCH_SHORTCUT.value: AstalonLocationData(
        Regions.CATA_VERTICAL_SHORTCUT, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_TOP.value: AstalonLocationData(Regions.CATA_TOP, LocationGroups.SWITCH, Area.CATA),
    Locations.CATA_SWITCH_CLAW_1.value: AstalonLocationData(
        Regions.CATA_SNAKE_MUSHROOMS, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_CLAW_2.value: AstalonLocationData(
        Regions.CATA_SNAKE_MUSHROOMS, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_WATER_1.value: AstalonLocationData(
        Regions.CATA_DOUBLE_SWITCH, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_WATER_2.value: AstalonLocationData(
        Regions.CATA_DOUBLE_SWITCH, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_DEV_ROOM.value: AstalonLocationData(
        Regions.CATA_DEV_ROOM_CONNECTION, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_AFTER_BLUE_DOOR.value: AstalonLocationData(
        Regions.CATA_BLUE_EYE_DOOR, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_SHORTCUT_ACCESS.value: AstalonLocationData(
        Regions.CATA_FLAMES_FORK, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_LADDER_BLOCKS.value: AstalonLocationData(
        Regions.CATA_FLAMES_FORK, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_MID_SHORTCUT.value: AstalonLocationData(
        Regions.CATA_VERTICAL_SHORTCUT, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_1ST_ROOM.value: AstalonLocationData(Regions.CATA_START, LocationGroups.SWITCH, Area.CATA),
    Locations.CATA_SWITCH_FLAMES_2.value: AstalonLocationData(
        Regions.CATA_FLAMES_FORK, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_SWITCH_FLAMES_1.value: AstalonLocationData(
        Regions.CATA_FLAMES_FORK, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_CRYSTAL_POISON_ROOTS.value: AstalonLocationData(
        Regions.CATA_POISON_ROOTS, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_FACE_AFTER_BOW.value: AstalonLocationData(
        Regions.CATA_BOW_CAMPFIRE, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_FACE_BOW.value: AstalonLocationData(Regions.CATA_BOW, LocationGroups.SWITCH, Area.CATA),
    Locations.CATA_FACE_X4.value: AstalonLocationData(Regions.CATA_4_FACES, LocationGroups.SWITCH, Area.CATA),
    Locations.CATA_FACE_CAMPFIRE.value: AstalonLocationData(Regions.CATA_BOSS, LocationGroups.SWITCH, Area.CATA),
    Locations.CATA_FACE_DOUBLE_DOOR.value: AstalonLocationData(
        Regions.CATA_DOUBLE_DOOR, LocationGroups.SWITCH, Area.CATA
    ),
    Locations.CATA_FACE_BOTTOM.value: AstalonLocationData(Regions.CATA_DOUBLE_DOOR, LocationGroups.SWITCH, Area.CATA),
    Locations.TR_ELEVATOR.value: AstalonLocationData(Regions.TR_START, LocationGroups.ELEVATOR, Area.TR),
    Locations.TR_SWITCH_ADORNED_L.value: AstalonLocationData(Regions.TR_BOTTOM, LocationGroups.SWITCH, Area.TR),
    Locations.TR_SWITCH_ADORNED_M.value: AstalonLocationData(Regions.TR_LEFT, LocationGroups.SWITCH, Area.TR),
    Locations.TR_SWITCH_ADORNED_R.value: AstalonLocationData(Regions.TR_TOP_RIGHT, LocationGroups.SWITCH, Area.TR),
    Locations.TR_SWITCH_ELEVATOR.value: AstalonLocationData(Regions.CATA_BOSS, LocationGroups.SWITCH, Area.TR),
    Locations.TR_SWITCH_BOTTOM.value: AstalonLocationData(Regions.TR_MIDDLE_RIGHT, LocationGroups.SWITCH, Area.TR),
    Locations.TR_CRYSTAL_GOLD.value: AstalonLocationData(Regions.TR_TOP_RIGHT, LocationGroups.SWITCH, Area.TR),
    Locations.TR_CRYSTAL_DARK_ARIAS.value: AstalonLocationData(Regions.TD_DARK_ARIAS, LocationGroups.SWITCH, Area.TR),
    Locations.CD_SWITCH_1.value: AstalonLocationData(Regions.CD_START, LocationGroups.SWITCH, Area.CD),
    Locations.CD_SWITCH_2.value: AstalonLocationData(Regions.CD_2, LocationGroups.SWITCH, Area.CD),
    Locations.CD_SWITCH_3.value: AstalonLocationData(Regions.CD_3, LocationGroups.SWITCH, Area.CD),
    Locations.CD_SWITCH_CAMPFIRE.value: AstalonLocationData(Regions.CD_MIDDLE, LocationGroups.SWITCH, Area.CD),
    Locations.CD_SWITCH_TOP.value: AstalonLocationData(Regions.CD_TOP, LocationGroups.SWITCH, Area.CD),
    Locations.CD_CRYSTAL_BACKTRACK.value: AstalonLocationData(Regions.CD_2, LocationGroups.SWITCH, Area.CD),
    Locations.CD_CRYSTAL_START.value: AstalonLocationData(Regions.CD_START, LocationGroups.SWITCH, Area.CD),
    Locations.CD_CRYSTAL_CAMPFIRE.value: AstalonLocationData(Regions.CD_CAMPFIRE_3, LocationGroups.SWITCH, Area.CD),
    Locations.CD_CRYSTAL_STEPS.value: AstalonLocationData(Regions.CD_STEPS, LocationGroups.SWITCH, Area.CD),
    Locations.CATH_SWITCH_BOTTOM.value: AstalonLocationData(Regions.CATH_START_RIGHT, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_SWITCH_BESIDE_SHAFT.value: AstalonLocationData(
        Regions.CATH_SHAFT_ACCESS, LocationGroups.SWITCH, Area.CATH
    ),
    Locations.CATH_SWITCH_TOP_CAMPFIRE.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_CRYSTAL_1ST_ROOM.value: AstalonLocationData(
        Regions.CATH_START_TOP_LEFT, LocationGroups.SWITCH, Area.CATH
    ),
    Locations.CATH_CRYSTAL_SHAFT.value: AstalonLocationData(Regions.CATH_LEFT_SHAFT, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_CRYSTAL_SPIKE_PIT.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_CRYSTAL_TOP_L.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_CRYSTAL_TOP_R.value: AstalonLocationData(Regions.CATH_TOP, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_CRYSTAL_SHAFT_ACCESS.value: AstalonLocationData(
        Regions.CATH_SHAFT_ACCESS, LocationGroups.SWITCH, Area.CATH
    ),
    Locations.CATH_CRYSTAL_ORBS.value: AstalonLocationData(Regions.CATH_ORB_ROOM, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_FACE_LEFT.value: AstalonLocationData(Regions.CATH_START_LEFT, LocationGroups.SWITCH, Area.CATH),
    Locations.CATH_FACE_RIGHT.value: AstalonLocationData(Regions.CATH_START_LEFT, LocationGroups.SWITCH, Area.CATH),
    Locations.SP_SWITCH_DOUBLE_DOORS.value: AstalonLocationData(Regions.SP_HEARTS, LocationGroups.SWITCH, Area.SP),
    Locations.SP_SWITCH_BUBBLES.value: AstalonLocationData(Regions.SP_CAMPFIRE_1, LocationGroups.SWITCH, Area.SP),
    Locations.SP_SWITCH_AFTER_STAR.value: AstalonLocationData(
        Regions.SP_STAR_CONNECTION, LocationGroups.SWITCH, Area.SP
    ),
    Locations.SP_CRYSTAL_BLOCKS.value: AstalonLocationData(Regions.SP_START, LocationGroups.SWITCH, Area.SP),
    Locations.SP_CRYSTAL_STAR.value: AstalonLocationData(Regions.SP_SHAFT, LocationGroups.SWITCH, Area.SP),
    Locations.MECH_CYCLOPS.value: AstalonLocationData(Regions.MECH_ZEEK, LocationGroups.ITEM, Area.MECH),
    Locations.CD_CROWN.value: AstalonLocationData(Regions.CD_BOSS, LocationGroups.ITEM, Area.CD),
    # Locations.GT_OLD_MAN.value: AstalonLocationData(Regions.GT_OLD_MAN, LocationGroups.FAMILIAR, Area.GT),
    # Locations.MECH_OLD_MAN.value: AstalonLocationData(Regions.MECH_OLD_MAN, LocationGroups.FAMILIAR, Area.MECH),
    # Locations.HOTP_OLD_MAN.value: AstalonLocationData(Regions.HOTP_OLD_MAN, LocationGroups.FAMILIAR, Area.HOTP),
    # Locations.CATA_GIL.value: AstalonLocationData(Regions.CATA_DEV_ROOM, LocationGroups.FAMILIAR, Area.CATA),
}

base_id = 333000
location_name_to_id: Dict[str, int] = {name: base_id + i for i, name in enumerate(location_table)}


def get_location_group(location_name: str) -> LocationGroups:
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
