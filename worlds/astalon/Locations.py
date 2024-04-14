from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import Dict, Set

from BaseClasses import Location

from .Regions import Regions


class LocationGroups(str, Enum):
    NONE = ""
    CHARACTER = "characters"
    ITEM = "items"
    FAMILIAR = "familiars"
    HEALTH = "health"
    ATTACK = "attack"
    KEY_WHITE = "white keys"
    KEY_BLUE = "blue keys"
    KEY_RED = "red keys"
    SHOP = "shop upgrades"
    SWITCH = "switches"


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
    GT_SWITCH_2ND_ROOM = "Gorgon Tomb - Switch (2nd Room)"
    GT_SWITCH_1ST_CYCLOPS = "Gorgon Tomb - Switch (1st Cyclops)"
    GT_SWITCH_SPIKE_TUNNEL = "Gorgon Tomb - Switch (Spike Tunnel Access)"
    GT_SWITCH_BUTT_ACCESS = "Gorgon Tomb - Switch (Butt Access)"
    GT_SWITCH_GH = "Gorgon Tomb - Switch (Gorgonheart)"
    GT_SWITCH_ROTA = "Gorgon Tomb - Switch (Ring of the Ancients)"
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
    HOTP_SWITCH_ROCK = "Hall of the Phantoms - Switch (Rock)"
    HOTP_SWITCH_BELOW_START = "Hall of the Phantoms - Switch (Below Start)"
    HOTP_SWITCH_ROCK_ACCESS = "Hall of the Phantoms - Switch (Rock Access)"
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
    HOTP_SWITCH_MAIDEN_ACCESS = "Hall of the Phantoms - Switch (Dead Maiden Access)"
    HOTP_SWITCH_MAZE_PUZZLE = "Hall of the Phantoms - Switch (Maze Puzzle)"
    HOTP_SWITCH_EYEBALL_SHORTCUT = "Hall of the Phantoms - Switch (Eyeball Shortcut)"
    HOTP_SWITCH_BELL_ACCESS = "Hall of the Phantoms - Switch (Bell Access)"
    HOTP_SWITCH_1ST_ROOM = "Hall of the Phantoms - Switch (1st Room)"
    HOTP_SWITCH_LEFT_BACKTRACK = "Hall of the Phantoms - Switch (Left Backtrack)"
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
    ROA_SWITCH_ASCEND = "Ruins of Ash - Switch (Ascend)"
    ROA_SWITCH_AFTER_WORMS = "Ruins of Ash - Switch (After Worms)"
    ROA_SWITCH_RIGHT_PATH = "Ruins of Ash - Switch (Right Path)"
    ROA_SWITCH_APEX_ACCESS = "Ruins of Ash - Switch (Apex Access)"
    ROA_SWITCH_ICARUS = "Ruins of Ash - Switch (Icarus Emblem)"
    ROA_SWITCH_SHAFT_L = "Ruins of Ash - Switch (Shaft Left)"
    ROA_SWITCH_SHAFT_R = "Ruins of Ash - Switch (Shaft Right)"
    ROA_SWITCH_ELEVATOR = "Ruins of Ash - Switch (Elevator)"
    ROA_SWITCH_SHAFT_DOWNWARDS = "Ruins of Ash - Switch (Shaft Downwards)"
    ROA_SWITCH_SPIDERS_T = "Ruins of Ash - Switch (Spiders Top)"
    ROA_SWITCH_SPIDERS_B = "Ruins of Ash - Switch (Spiders Bottom)"
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
    ROA_FACE_BLUE_KEY = "Ruins of Ash - Face (Blue Key)"

    DARK_HP_4 = "Darkness - Max HP +4"
    DARK_WHITE_KEY = "Darkness - White Key"
    DARK_SWITCH = "Darkness - Switch"

    APEX_CHALICE = "The Apex - Blood Chalice"
    APEX_HP_1_CHALICE = "The Apex - Max HP +1 (Blood Chalice)"
    APEX_HP_5_HEART = "The Apex - Max HP +5 (After Heart)"
    APEX_BLUE_KEY = "The Apex - Blue Key"
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
    CD_CRYSTAL_STAIRS = "Cyclops Den - Crystal (Stairs)"

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

    VICTORY = "Victory"


class AstalonLocation(Location):
    game = "Astalon"


@dataclass
class AstalonLocationData:
    region: Regions
    item_group: LocationGroups = LocationGroups.NONE


location_table: Dict[Locations, AstalonLocationData] = {
    Locations.GT_GORGONHEART: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.ITEM),
    Locations.GT_ANCIENTS_RING: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.ITEM),
    Locations.GT_SWORD: AstalonLocationData(Regions.GT_SWORD, LocationGroups.ITEM),
    Locations.GT_MAP: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.ITEM),
    Locations.GT_ASCENDANT_KEY: AstalonLocationData(Regions.GT_ASCENDANT_KEY, LocationGroups.ITEM),
    Locations.GT_BANISH: AstalonLocationData(Regions.GT_LEFT, LocationGroups.ITEM),
    Locations.GT_VOID: AstalonLocationData(Regions.GT_VOID, LocationGroups.ITEM),
    Locations.GT_EYE_RED: AstalonLocationData(Regions.GT_BOSS, LocationGroups.ITEM),
    Locations.GT_ATTACK: AstalonLocationData(Regions.GT_BABY_GORGON, LocationGroups.ATTACK),
    Locations.GT_HP_1_RING: AstalonLocationData(Regions.GT_UPPER_PATH, LocationGroups.HEALTH),
    Locations.GT_HP_5_KEY: AstalonLocationData(Regions.GT_ASCENDANT_KEY, LocationGroups.HEALTH),
    Locations.GT_WHITE_KEY_START: AstalonLocationData(Regions.ENTRANCE, LocationGroups.KEY_WHITE),
    Locations.GT_WHITE_KEY_RIGHT: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.KEY_WHITE),
    Locations.GT_WHITE_KEY_BOSS: AstalonLocationData(Regions.GT_TOP_RIGHT, LocationGroups.KEY_WHITE),
    Locations.GT_BLUE_KEY_BONESNAKE: AstalonLocationData(Regions.GT_BOTTOM, LocationGroups.KEY_BLUE),
    Locations.GT_BLUE_KEY_BUTT: AstalonLocationData(Regions.GT_BUTT, LocationGroups.KEY_BLUE),
    Locations.GT_BLUE_KEY_WALL: AstalonLocationData(Regions.GT_BUTT, LocationGroups.KEY_BLUE),
    Locations.GT_BLUE_KEY_POT: AstalonLocationData(Regions.GT_UPPER_PATH, LocationGroups.KEY_BLUE),
    Locations.GT_RED_KEY: AstalonLocationData(Regions.GT_BOSS, LocationGroups.KEY_RED),
    Locations.MECH_BOOTS: AstalonLocationData(Regions.MECH_BOOTS_UPPER, LocationGroups.ITEM),
    Locations.MECH_CLOAK: AstalonLocationData(Regions.MECH_CLOAK, LocationGroups.ITEM),
    Locations.MECH_EYE_BLUE: AstalonLocationData(Regions.MECH_BOSS, LocationGroups.ITEM),
    Locations.MECH_ATTACK_VOLANTIS: AstalonLocationData(Regions.HOTP_START, LocationGroups.ATTACK),
    Locations.MECH_ATTACK_STAR: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.ATTACK),
    Locations.MECH_HP_1_SWITCH: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.HEALTH),
    Locations.MECH_HP_1_STAR: AstalonLocationData(Regions.MECH_BRAM_TUNNEL, LocationGroups.HEALTH),
    Locations.MECH_HP_3_CLAW: AstalonLocationData(Regions.MECH_BOTTOM_CAMPFIRE, LocationGroups.HEALTH),
    Locations.MECH_WHITE_KEY_LINUS: AstalonLocationData(Regions.MECH_SWORD_CONNECTION, LocationGroups.KEY_WHITE),
    Locations.MECH_WHITE_KEY_BK: AstalonLocationData(Regions.MECH_AFTER_BK, LocationGroups.KEY_WHITE),
    Locations.MECH_WHITE_KEY_ARENA: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.KEY_WHITE),
    Locations.MECH_WHITE_KEY_TOP: AstalonLocationData(Regions.MECH_TOP, LocationGroups.KEY_WHITE),
    Locations.MECH_BLUE_KEY_VOID: AstalonLocationData(Regions.GT_VOID, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_SNAKE: AstalonLocationData(Regions.MECH_SNAKE, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_LINUS: AstalonLocationData(Regions.MECH_LOWER_ARIAS, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_SACRIFICE: AstalonLocationData(Regions.MECH_SACRIFICE, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_RED: AstalonLocationData(Regions.MECH_LOWER_VOID, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_ARIAS: AstalonLocationData(Regions.MECH_ARIAS_EYEBALL, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_BLOCKS: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_TOP: AstalonLocationData(Regions.MECH_SPLIT_PATH, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_OLD_MAN: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_SAVE: AstalonLocationData(Regions.MECH_TOP, LocationGroups.KEY_BLUE),
    Locations.MECH_BLUE_KEY_POT: AstalonLocationData(Regions.MECH_POTS, LocationGroups.KEY_BLUE),
    Locations.MECH_RED_KEY: AstalonLocationData(Regions.MECH_LOWER_VOID, LocationGroups.KEY_RED),
    Locations.HOTP_BELL: AstalonLocationData(Regions.HOTP_BELL, LocationGroups.ITEM),
    Locations.HOTP_AMULET: AstalonLocationData(Regions.HOTP_AMULET, LocationGroups.ITEM),
    Locations.HOTP_CLAW: AstalonLocationData(Regions.HOTP_CLAW, LocationGroups.ITEM),
    Locations.HOTP_GAUNTLET: AstalonLocationData(Regions.HOTP_GAUNTLET, LocationGroups.ITEM),
    Locations.HOTP_MAIDEN_RING: AstalonLocationData(Regions.HOTP_MAIDEN, LocationGroups.ITEM),
    Locations.HOTP_HP_1_CLAW: AstalonLocationData(Regions.HOTP_CLAW_LEFT, LocationGroups.HEALTH),
    Locations.HOTP_HP_2_LADDER: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.HEALTH),
    Locations.HOTP_HP_2_GAUNTLET: AstalonLocationData(Regions.HOTP_TP_FALL_TOP, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_OLD_MAN: AstalonLocationData(Regions.HOTP_ABOVE_OLD_MAN, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_MAZE: AstalonLocationData(Regions.HOTP_LOWER_VOID, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_START: AstalonLocationData(Regions.HOTP_START, LocationGroups.HEALTH),
    Locations.HOTP_WHITE_KEY_LEFT: AstalonLocationData(Regions.HOTP_START_LEFT, LocationGroups.KEY_WHITE),
    Locations.HOTP_WHITE_KEY_GHOST: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.KEY_WHITE),
    Locations.HOTP_WHITE_KEY_OLD_MAN: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.KEY_WHITE),
    Locations.HOTP_WHITE_KEY_BOSS: AstalonLocationData(Regions.HOTP_UPPER_ARIAS, LocationGroups.KEY_WHITE),
    Locations.HOTP_BLUE_KEY_STATUE: AstalonLocationData(Regions.HOTP_EPIMETHEUS, LocationGroups.KEY_BLUE),
    Locations.HOTP_BLUE_KEY_GOLD: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.KEY_BLUE),
    Locations.HOTP_BLUE_KEY_AMULET: AstalonLocationData(Regions.HOTP_AMULET_CONNECTION, LocationGroups.KEY_BLUE),
    Locations.HOTP_BLUE_KEY_LADDER: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.KEY_BLUE),
    Locations.HOTP_BLUE_KEY_TELEPORTS: AstalonLocationData(Regions.HOTP_ELEVATOR, LocationGroups.KEY_BLUE),
    Locations.HOTP_BLUE_KEY_MAZE: AstalonLocationData(Regions.HOTP_TP_PUZZLE, LocationGroups.KEY_BLUE),
    Locations.HOTP_RED_KEY: AstalonLocationData(Regions.HOTP_RED_KEY, LocationGroups.KEY_RED),
    Locations.ROA_ICARUS: AstalonLocationData(Regions.ROA_ICARUS, LocationGroups.ITEM),
    Locations.ROA_EYE_GREEN: AstalonLocationData(Regions.ROA_BOSS, LocationGroups.ITEM),
    Locations.ROA_ATTACK: AstalonLocationData(Regions.ROA_MIDDLE, LocationGroups.ATTACK),
    Locations.ROA_HP_1_LEFT: AstalonLocationData(Regions.ROA_LEFT_ASCENT, LocationGroups.HEALTH),
    Locations.ROA_HP_2_RIGHT: AstalonLocationData(Regions.ROA_RIGHT_BRANCH, LocationGroups.HEALTH),
    Locations.ROA_HP_5_SOLARIA: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.ROA_WHITE_KEY_SAVE: AstalonLocationData(Regions.ROA_WORMS, LocationGroups.KEY_WHITE),
    Locations.ROA_WHITE_KEY_REAPERS: AstalonLocationData(Regions.ROA_LEFT_ASCENT, LocationGroups.KEY_WHITE),
    Locations.ROA_WHITE_KEY_TORCHES: AstalonLocationData(Regions.ROA_MIDDLE, LocationGroups.KEY_WHITE),
    Locations.ROA_WHITE_KEY_PORTAL: AstalonLocationData(Regions.ROA_UPPER_VOID, LocationGroups.KEY_WHITE),
    Locations.ROA_BLUE_KEY_FACE: AstalonLocationData(Regions.ROA_BOTTOM_ASCEND, LocationGroups.KEY_BLUE),
    Locations.ROA_BLUE_KEY_FLAMES: AstalonLocationData(Regions.ROA_FLAMES, LocationGroups.KEY_BLUE),
    Locations.ROA_BLUE_KEY_BABY: AstalonLocationData(Regions.ROA_LEFT_BABY_GORGON, LocationGroups.KEY_BLUE),
    Locations.ROA_BLUE_KEY_TOP: AstalonLocationData(Regions.ROA_CENTAUR, LocationGroups.KEY_BLUE),
    Locations.ROA_BLUE_KEY_POT: AstalonLocationData(Regions.ROA_BOTTOM_ASCEND, LocationGroups.KEY_BLUE),
    Locations.ROA_RED_KEY: AstalonLocationData(Regions.ROA_RED_KEY, LocationGroups.KEY_RED),
    Locations.DARK_HP_4: AstalonLocationData(Regions.DARK_END, LocationGroups.HEALTH),
    Locations.DARK_WHITE_KEY: AstalonLocationData(Regions.DARK_END, LocationGroups.KEY_WHITE),
    Locations.APEX_CHALICE: AstalonLocationData(Regions.APEX_CENTAUR, LocationGroups.ITEM),
    Locations.APEX_HP_1_CHALICE: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.APEX_HP_5_HEART: AstalonLocationData(Regions.APEX_HEART, LocationGroups.HEALTH),
    Locations.APEX_BLUE_KEY: AstalonLocationData(Regions.APEX, LocationGroups.KEY_BLUE),
    Locations.CATA_BOW: AstalonLocationData(Regions.CATA_BOW, LocationGroups.ITEM),
    Locations.CAVES_ATTACK_RED: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.ATTACK),
    Locations.CAVES_ATTACK_BLUE: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.ATTACK),
    Locations.CAVES_ATTACK_GREEN: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_ROOT: AstalonLocationData(Regions.CATA_CLIMBABLE_ROOT, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_POISON: AstalonLocationData(Regions.CATA_POISON_ROOTS, LocationGroups.ATTACK),
    Locations.CAVES_HP_1_START: AstalonLocationData(Regions.CAVES_START, LocationGroups.HEALTH),
    Locations.CAVES_HP_1_CYCLOPS: AstalonLocationData(Regions.CAVES_ARENA, LocationGroups.HEALTH),
    Locations.CATA_HP_1_ABOVE_POISON: AstalonLocationData(Regions.CATA_POISON_ROOTS, LocationGroups.HEALTH),
    Locations.CATA_HP_2_BEFORE_POISON: AstalonLocationData(Regions.CATA_POISON_ROOTS, LocationGroups.HEALTH),
    Locations.CATA_HP_2_AFTER_POISON: AstalonLocationData(Regions.CATA_POISON_ROOTS, LocationGroups.HEALTH),
    Locations.CATA_HP_2_GEMINI_BOTTOM: AstalonLocationData(Regions.CATA_DOUBLE_DOOR, LocationGroups.HEALTH),
    Locations.CATA_HP_2_GEMINI_TOP: AstalonLocationData(Regions.CATA_CENTAUR, LocationGroups.HEALTH),
    Locations.CATA_HP_2_ABOVE_GEMINI: AstalonLocationData(Regions.CATA_FLAMES, LocationGroups.HEALTH),
    Locations.CAVES_HP_5_CHAIN: AstalonLocationData(Regions.CAVES_ITEM_CHAIN, LocationGroups.HEALTH),
    Locations.CATA_WHITE_KEY_HEAD: AstalonLocationData(Regions.CATA_TOP, LocationGroups.KEY_WHITE),
    Locations.CATA_WHITE_KEY_DEV_ROOM: AstalonLocationData(Regions.CATA_DEV_ROOM_CONNECTION, LocationGroups.KEY_WHITE),
    Locations.CATA_WHITE_KEY_PRISON: AstalonLocationData(Regions.CATA_BOSS, LocationGroups.KEY_WHITE),
    Locations.CATA_BLUE_KEY_SLIMES: AstalonLocationData(Regions.CATA_BOW_CAMPFIRE, LocationGroups.KEY_BLUE),
    Locations.CATA_BLUE_KEY_EYEBALLS: AstalonLocationData(Regions.CATA_CENTAUR, LocationGroups.KEY_BLUE),
    Locations.TR_ADORNED_KEY: AstalonLocationData(Regions.TR_BOTTOM, LocationGroups.ITEM),
    Locations.TR_HP_1_BOTTOM: AstalonLocationData(Regions.TR_BOTTOM_LEFT, LocationGroups.HEALTH),
    Locations.TR_HP_2_TOP: AstalonLocationData(Regions.TR_LEFT, LocationGroups.HEALTH),
    Locations.TR_RED_KEY: AstalonLocationData(Regions.TR_START, LocationGroups.KEY_RED),
    Locations.CD_ATTACK: AstalonLocationData(Regions.CD_TOP, LocationGroups.ATTACK),
    Locations.CD_HP_1: AstalonLocationData(Regions.CD_TOP, LocationGroups.HEALTH),
    Locations.CATH_BLOCK: AstalonLocationData(Regions.CATH_TOP, LocationGroups.ITEM),
    Locations.CATH_ATTACK: AstalonLocationData(Regions.CATH_UPPER_SPIKE_PIT, LocationGroups.ATTACK),
    Locations.CATH_HP_1_TOP_LEFT: AstalonLocationData(Regions.CATH_TOP, LocationGroups.HEALTH),
    Locations.CATH_HP_1_TOP_RIGHT: AstalonLocationData(Regions.CATH_TOP, LocationGroups.HEALTH),
    Locations.CATH_HP_2_CLAW: AstalonLocationData(Regions.CATH_LEFT_SHAFT, LocationGroups.HEALTH),
    Locations.CATH_HP_5_BELL: AstalonLocationData(Regions.CATH_CAMPFIRE_1, LocationGroups.HEALTH),
    Locations.SP_STAR: AstalonLocationData(Regions.SP_STAR, LocationGroups.ITEM),
    Locations.SP_ATTACK: AstalonLocationData(Regions.SP_CAMPFIRE_2, LocationGroups.ATTACK),
    Locations.SP_HP_1: AstalonLocationData(Regions.SP_FROG, LocationGroups.HEALTH),
    Locations.SP_BLUE_KEY_BUBBLES: AstalonLocationData(Regions.SP_START, LocationGroups.KEY_BLUE),
    Locations.SP_BLUE_KEY_STAR: AstalonLocationData(Regions.SP_STAR_END, LocationGroups.KEY_BLUE),
    Locations.SP_BLUE_KEY_PAINTING: AstalonLocationData(Regions.SP_PAINTING, LocationGroups.KEY_BLUE),
    Locations.SP_BLUE_KEY_ARIAS: AstalonLocationData(Regions.SP_CAMPFIRE_2, LocationGroups.KEY_BLUE),
    Locations.SHOP_GIFT: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_KNOWLEDGE: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_MERCY: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ORB_SEEKER: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_MAP_REVEAL: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_CARTOGRAPHER: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_DEATH_ORB: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_DEATH_POINT: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_TITANS_EGO: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ALGUS_ARCANIST: AstalonLocationData(Regions.SHOP_ALGUS, LocationGroups.SHOP),
    Locations.SHOP_ALGUS_SHOCK: AstalonLocationData(Regions.SHOP_ALGUS, LocationGroups.SHOP),
    Locations.SHOP_ALGUS_METEOR: AstalonLocationData(Regions.SHOP_ALGUS, LocationGroups.SHOP),
    Locations.SHOP_ARIAS_GORGONSLAYER: AstalonLocationData(Regions.SHOP_ARIAS, LocationGroups.SHOP),
    Locations.SHOP_ARIAS_LAST_STAND: AstalonLocationData(Regions.SHOP_ARIAS, LocationGroups.SHOP),
    Locations.SHOP_ARIAS_LIONHEART: AstalonLocationData(Regions.SHOP_ARIAS, LocationGroups.SHOP),
    Locations.SHOP_KYULI_ASSASSIN: AstalonLocationData(Regions.SHOP_KYULI, LocationGroups.SHOP),
    Locations.SHOP_KYULI_BULLSEYE: AstalonLocationData(Regions.SHOP_KYULI, LocationGroups.SHOP),
    Locations.SHOP_KYULI_RAY: AstalonLocationData(Regions.SHOP_KYULI, LocationGroups.SHOP),
    Locations.SHOP_ZEEK_JUNKYARD: AstalonLocationData(Regions.SHOP_ZEEK, LocationGroups.SHOP),
    Locations.SHOP_ZEEK_ORBS: AstalonLocationData(Regions.SHOP_ZEEK, LocationGroups.SHOP),
    Locations.SHOP_ZEEK_LOOT: AstalonLocationData(Regions.SHOP_ZEEK, LocationGroups.SHOP),
    Locations.SHOP_BRAM_AXE: AstalonLocationData(Regions.SHOP_BRAM, LocationGroups.SHOP),
    Locations.SHOP_BRAM_HUNTER: AstalonLocationData(Regions.SHOP_BRAM, LocationGroups.SHOP),
    Locations.SHOP_BRAM_WHIPLASH: AstalonLocationData(Regions.SHOP_BRAM, LocationGroups.SHOP),
    Locations.GT_ALGUS: AstalonLocationData(Regions.ENTRANCE, LocationGroups.CHARACTER),
    Locations.GT_ARIAS: AstalonLocationData(Regions.ENTRANCE, LocationGroups.CHARACTER),
    Locations.GT_KYULI: AstalonLocationData(Regions.ENTRANCE, LocationGroups.CHARACTER),
    Locations.MECH_ZEEK: AstalonLocationData(Regions.MECH_ZEEK, LocationGroups.CHARACTER),
    Locations.TR_BRAM: AstalonLocationData(Regions.TR_BRAM, LocationGroups.CHARACTER),
    Locations.GT_SWITCH_2ND_ROOM: AstalonLocationData(Regions.ENTRANCE, LocationGroups.SWITCH),
    Locations.GT_SWITCH_1ST_CYCLOPS: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.SWITCH),
    Locations.GT_SWITCH_SPIKE_TUNNEL: AstalonLocationData(Regions.GT_TOP_LEFT, LocationGroups.SWITCH),
    Locations.GT_SWITCH_BUTT_ACCESS: AstalonLocationData(Regions.GT_SPIKE_TUNNEL, LocationGroups.SWITCH),
    Locations.GT_SWITCH_GH: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.SWITCH),
    Locations.GT_SWITCH_ROTA: AstalonLocationData(Regions.GT_UPPER_PATH, LocationGroups.SWITCH),
    Locations.GT_SWITCH_UPPER_PATH_BLOCKS: AstalonLocationData(Regions.GT_UPPER_PATH_CONNECTION, LocationGroups.SWITCH),
    Locations.GT_SWITCH_UPPER_PATH_ACCESS: AstalonLocationData(Regions.GT_UPPER_PATH_CONNECTION, LocationGroups.SWITCH),
    Locations.GT_SWITCH_CROSSES: AstalonLocationData(Regions.GT_LEFT, LocationGroups.SWITCH),
    Locations.GT_SWITCH_GH_SHORTCUT: AstalonLocationData(Regions.GT_GORGONHEART, LocationGroups.SWITCH),
    Locations.GT_SWITCH_ARIAS_PATH: AstalonLocationData(Regions.GT_TOP_LEFT, LocationGroups.SWITCH),
    Locations.GT_SWITCH_SWORD_ACCESS: AstalonLocationData(Regions.GT_SWORD_FORK, LocationGroups.SWITCH),
    Locations.GT_SWITCH_SWORD_BACKTRACK: AstalonLocationData(Regions.GT_SWORD_FORK, LocationGroups.SWITCH),
    Locations.GT_SWITCH_SWORD: AstalonLocationData(Regions.GT_SWORD, LocationGroups.SWITCH),
    Locations.GT_SWITCH_UPPER_ARIAS: AstalonLocationData(Regions.GT_ARIAS_SWORD_SWITCH, LocationGroups.SWITCH),
    Locations.GT_CRYSTAL_LADDER: AstalonLocationData(Regions.GT_LADDER_SWITCH, LocationGroups.SWITCH),
    Locations.GT_CRYSTAL_OLD_MAN_1: AstalonLocationData(Regions.GT_OLD_MAN_FORK, LocationGroups.SWITCH),
    Locations.GT_CRYSTAL_OLD_MAN_2: AstalonLocationData(Regions.GT_OLD_MAN_FORK, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_WATCHER: AstalonLocationData(Regions.MECH_ROOTS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_CHAINS: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_BOSS_ACCESS_1: AstalonLocationData(Regions.MECH_BOSS_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_BOSS_ACCESS_2: AstalonLocationData(Regions.MECH_BOSS_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_SPLIT_PATH: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_SNAKE_1: AstalonLocationData(Regions.MECH_BOTTOM_CAMPFIRE, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_BOOTS_ACCESS: AstalonLocationData(Regions.MECH_BOOTS_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_UPPER_GT_ACCESS: AstalonLocationData(Regions.MECH_BOTTOM_CAMPFIRE, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_UPPER_VOID_DROP: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_UPPER_VOID: AstalonLocationData(Regions.MECH_UPPER_VOID, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_LINUS: AstalonLocationData(Regions.MECH_LINUS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_TO_BOSS_2: AstalonLocationData(Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_POTS: AstalonLocationData(Regions.MECH_POTS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_MAZE_BACKDOOR: AstalonLocationData(Regions.MECH_TP_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_TO_BOSS_1: AstalonLocationData(Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_BLOCK_STAIRS: AstalonLocationData(Regions.MECH_CLOAK_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_ARIAS_CYCLOPS: AstalonLocationData(Regions.MECH_CHARACTER_SWAPS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_BOOTS_LOWER: AstalonLocationData(Regions.MECH_BOOTS_LOWER, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_CHAINS_GAP: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_LOWER_KEY: AstalonLocationData(Regions.MECH_SWORD_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_ARIAS: AstalonLocationData(Regions.MECH_ARIAS_EYEBALL, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_SNAKE_2: AstalonLocationData(Regions.MECH_SNAKE, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_KEY_BLOCKS: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_CANNON: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_EYEBALL: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH),
    Locations.MECH_SWITCH_INVISIBLE: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_CANNON: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_LINUS: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_LOWER: AstalonLocationData(Regions.MECH_SWORD_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TO_BOSS_3: AstalonLocationData(Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TRIPLE_1: AstalonLocationData(Regions.MECH_CHARACTER_SWAPS, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TRIPLE_2: AstalonLocationData(Regions.MECH_CHARACTER_SWAPS, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TRIPLE_3: AstalonLocationData(Regions.MECH_CHARACTER_SWAPS, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TOP: AstalonLocationData(Regions.MECH_TOP, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_CLOAK: AstalonLocationData(Regions.MECH_CLOAK_CONNECTION, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_SLIMES: AstalonLocationData(Regions.MECH_BOSS_SWITCHES, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TO_CD: AstalonLocationData(Regions.MECH_TOP, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_CAMPFIRE: AstalonLocationData(Regions.MECH_BK, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_1ST_ROOM: AstalonLocationData(Regions.MECH_START, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_OLD_MAN: AstalonLocationData(Regions.MECH_RIGHT, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_TOP_CHAINS: AstalonLocationData(Regions.MECH_CHAINS, LocationGroups.SWITCH),
    Locations.MECH_CRYSTAL_BK: AstalonLocationData(Regions.MECH_BK, LocationGroups.SWITCH),
    Locations.MECH_FACE_ABOVE_VOLANTIS: AstalonLocationData(Regions.MECH_BOSS, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_ROCK: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_BELOW_START: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_ROCK_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_LEFT_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_LEFT_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_LOWER_SHORTCUT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_BELL: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_GHOST_BLOOD: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_TELEPORTS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_WORM_PILLAR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_TO_CLAW_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_TO_CLAW_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_CLAW_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_GHOSTS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_LEFT_3: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_ABOVE_OLD_MAN: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_MAIDEN_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_MAZE_PUZZLE: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_EYEBALL_SHORTCUT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_BELL_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_1ST_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_SWITCH_LEFT_BACKTRACK: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_BOTTOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_LOWER: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_AFTER_CLAW: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_MAIDEN_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_MAIDEN_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_BELL_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_HEART: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_CRYSTAL_BELOW_PUZZLE: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.HOTP_FACE_OLD_MAN: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_ASCEND: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_AFTER_WORMS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_RIGHT_PATH: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_APEX_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_ICARUS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_SHAFT_L: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_SHAFT_R: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_ELEVATOR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_SHAFT_DOWNWARDS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_SPIDERS_T: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_SPIDERS_B: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_DARK_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_ASCEND_SHORTCUT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_1ST_SHORTCUT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_SPIKE_CLIMB: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_ABOVE_CENTAUR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_BLOOD_POT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_WORMS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_TRIPLE_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_TRIPLE_3: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_BABY_GORGON: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_BOSS_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_BLOOD_POT_L: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_BLOOD_POT_R: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_SWITCH_LOWER_VOID: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_1ST_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_BABY_GORGON: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_LADDER_R: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_LADDER_L: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_CENTAUR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_SPIKE_BALLS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_LEFT_ASCEND: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_SHAFT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_BRANCH_R: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_BRANCH_L: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_3_REAPERS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_CRYSTAL_TRIPLE_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.ROA_FACE_BLUE_KEY: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.DARK_SWITCH: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.APEX_SWITCH: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CAVES_SWITCH_SKELETONS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CAVES_SWITCH_CATA_ACCESS_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CAVES_SWITCH_CATA_ACCESS_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CAVES_SWITCH_CATA_ACCESS_3: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CAVES_FACE_1ST_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_ELEVATOR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_SHORTCUT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_TOP: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_CLAW_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_CLAW_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_WATER_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_WATER_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_DEV_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_AFTER_BLUE_DOOR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_SHORTCUT_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_LADDER_BLOCKS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_MID_SHORTCUT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_1ST_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_FLAMES_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_SWITCH_FLAMES_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_CRYSTAL_POISON_ROOTS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_FACE_AFTER_BOW: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_FACE_BOW: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_FACE_X4: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_FACE_CAMPFIRE: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_FACE_DOUBLE_DOOR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATA_FACE_BOTTOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_SWITCH_ADORNED_L: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_SWITCH_ADORNED_M: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_SWITCH_ADORNED_R: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_SWITCH_ELEVATOR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_SWITCH_BOTTOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_CRYSTAL_GOLD: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.TR_CRYSTAL_DARK_ARIAS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_SWITCH_1: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_SWITCH_2: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_SWITCH_3: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_SWITCH_CAMPFIRE: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_SWITCH_TOP: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_CRYSTAL_BACKTRACK: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_CRYSTAL_START: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_CRYSTAL_CAMPFIRE: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CD_CRYSTAL_STAIRS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_SWITCH_BOTTOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_SWITCH_BESIDE_SHAFT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_SWITCH_TOP_CAMPFIRE: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_1ST_ROOM: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_SHAFT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_SPIKE_PIT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_TOP_L: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_TOP_R: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_SHAFT_ACCESS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_CRYSTAL_ORBS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_FACE_LEFT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.CATH_FACE_RIGHT: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.SP_SWITCH_DOUBLE_DOORS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.SP_SWITCH_BUBBLES: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.SP_SWITCH_AFTER_STAR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.SP_CRYSTAL_BLOCKS: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    Locations.SP_CRYSTAL_STAR: AstalonLocationData(Regions.APEX, LocationGroups.SWITCH),
    # Locations.GT_OLD_MAN: AstalonLocationData(Regions.GT_OLD_MAN, LocationGroups.FAMILIARS),
    # Locations.MECH_OLD_MAN: AstalonLocationData(Regions.MECH_OLD_MAN, LocationGroups.FAMILIARS),
    # Locations.HOTP_OLD_MAN: AstalonLocationData(Regions.HOTP_OLD_MAN, LocationGroups.FAMILIARS),
    # Locations.CATA_GIL: AstalonLocationData(Regions.CATA_DEV_ROOM, LocationGroups.FAMILIARS),
    # Locations.MECH_CYCLOPS: AstalonLocationData(Regions.MECH_ZEEK, LocationGroups.ITEMS),
    # Locations.CD_CROWN: AstalonLocationData(Regions.CD_BOSS, LocationGroups.ITEMS),
}

base_id = 333000
location_name_to_id: Dict[str, int] = {name.value: base_id + i for i, name in enumerate(location_table)}


def get_location_group(location_name: Locations):
    return location_table[location_name].region


location_name_groups: Dict[str, Set[str]] = {
    group.value: set(location.value for location in location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
