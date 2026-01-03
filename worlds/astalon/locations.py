from dataclasses import dataclass
from enum import StrEnum
from itertools import groupby

from BaseClasses import Location

from .constants import BASE_ID, GAME_NAME
from .regions import RegionName


class Area(StrEnum):
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


class LocationName(StrEnum):
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
    GT_WHITE_KEY_START = "Gorgon Tomb - White Key (1st Room)"
    GT_WHITE_KEY_RIGHT = "Gorgon Tomb - White Key (Right Side)"
    GT_WHITE_KEY_BOSS = "Gorgon Tomb - White Key (Before Boss)"
    GT_BLUE_KEY_BONESNAKE = "Gorgon Tomb - Blue Key (Bonesnakes)"
    GT_BLUE_KEY_BUTT = "Gorgon Tomb - Blue Key (Butt)"
    GT_BLUE_KEY_WALL = "Gorgon Tomb - Blue Key (Inside Wall)"
    GT_BLUE_KEY_POT = "Gorgon Tomb - Blue Key (Pot)"
    GT_RED_KEY = "Gorgon Tomb - Red Key"
    GT_ELEVATOR_1 = "Gorgon Tomb - Elevator 1"
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
    GT_CANDLE_LINUS = "Gorgon Tomb - Candle (Linus' Map)"
    GT_CANDLE_1ST_CYCLOPS = "Gorgon Tomb - Candle (1st Cyclops)"
    GT_CANDLE_BOSS = "Gorgon Tomb - Candle (Boss)"
    GT_CANDLE_BOTTOM = "Gorgon Tomb - Candle (Bottom)"

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
    MECH_SKULL_PUZZLE = "Mechanism - Skull Puzzle"
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
    MECH_CANDLE_ROOTS = "Mechanism - Candle (Roots)"
    MECH_CANDLE_BOTTOM = "Mechanism - Candle (Bottom)"
    MECH_CANDLE_CHAINS = "Mechanism - Candle (Chains)"
    MECH_CANDLE_RIGHT = "Mechanism - Candle (Right)"
    MECH_CANDLE_POTS = "Mechanism - Candle (Pots)"
    MECH_CANDLE_BOSS_1 = "Mechanism - Candle (Boss 1)"
    MECH_CANDLE_BOSS_2 = "Mechanism - Candle (Boss 2)"
    MECH_CANDLE_SLIMES = "Mechanism - Candle (Slimes)"
    MECH_CANDLE_ZEEK = "Mechanism - Candle (Zeek)"
    MECH_CANDLE_MAZE_BACKDOOR = "Mechanism - Candle (Maze Backdoor)"
    MECH_CANDLE_CD_ACCESS_1 = "Mechanism - Candle (CD Access 1)"
    MECH_CANDLE_CD_ACCESS_2 = "Mechanism - Candle (CD Access 2)"
    MECH_CANDLE_CD_ACCESS_3 = "Mechanism - Candle (CD Access 3)"
    MECH_CANDLE_1ST_ROOM = "Mechanism - Candle (1st Room)"
    MECH_CANDLE_BK = "Mechanism - Candle (Black Knight)"
    MECH_CANDLE_CAMPFIRE_R = "Mechanism - Candle (Right Campfire)"

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
    HOTP_SKULL_PUZZLE = "Hall of the Phantoms - Skull Puzzle"
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
    HOTP_CANDLE_1ST_ROOM = "Hall of the Phantoms - Candle (1st Room)"
    HOTP_CANDLE_LOWER = "Hall of the Phantoms - Candle (Lower)"
    HOTP_CANDLE_BELL = "Hall of the Phantoms - Candle (Bell)"
    HOTP_CANDLE_EYEBALL = "Hall of the Phantoms - Candle (Eyeball)"
    HOTP_CANDLE_OLD_MAN = "Hall of the Phantoms - Candle (Old Man)"
    HOTP_CANDLE_BEFORE_CLAW = "Hall of the Phantoms - Candle (Before Claw)"
    HOTP_CANDLE_CLAW_CAMPFIRE = "Hall of the Phantoms - Candle (Claw Campfire)"
    HOTP_CANDLE_TP_PUZZLE = "Hall of the Phantoms - Candle (Teleport Puzzle)"
    HOTP_CANDLE_BOSS = "Hall of the Phantoms - Candle (Boss)"
    HOTP_CANDLE_TP_FALL = "Hall of the Phantoms - Candle (Teleport Fall)"
    HOTP_CANDLE_UPPER_VOID_1 = "Hall of the Phantoms - Candle (Upper Void 1)"
    HOTP_CANDLE_UPPER_VOID_2 = "Hall of the Phantoms - Candle (Upper Void 2)"
    HOTP_CANDLE_UPPER_VOID_3 = "Hall of the Phantoms - Candle (Upper Void 3)"
    HOTP_CANDLE_UPPER_VOID_4 = "Hall of the Phantoms - Candle (Upper Void 4)"
    HOTP_CANDLE_ELEVATOR = "Hall of the Phantoms - Candle (Elevator)"

    ROA_ICARUS = "Ruins of Ash - Icarus Emblem"
    ROA_EYE_GREEN = "Ruins of Ash - Gorgon Eye (Green)"
    ROA_ATTACK = "Ruins of Ash - Attack +1"
    ROA_HP_1_LEFT = "Ruins of Ash - Max HP +1 (Left of Ascent)"
    ROA_HP_2_RIGHT = "Ruins of Ash - Max HP +2 (Right Side)"
    ROA_HP_5_SOLARIA = "Ruins of Ash - Max HP +5 (After Solaria)"
    ROA_WHITE_KEY_SAVE = "Ruins of Ash - White Key (Checkpoint)"
    ROA_WHITE_KEY_REAPERS = "Ruins of Ash - White Key (3 Reapers)"
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
    ROA_CANDLE_1ST_ROOM = "Ruins of Ash - Candle (1st Room)"
    ROA_CANDLE_3_REAPERS = "Ruins of Ash - Candle (3 Reapers)"
    ROA_CANDLE_MIDDLE_CAMPFIRE = "Ruins of Ash - Candle (Middle Campfire)"
    ROA_CANDLE_LADDER_BOTTOM = "Ruins of Ash - Candle (Ladder Bottom)"
    ROA_CANDLE_SHAFT = "Ruins of Ash - Candle (Shaft)"
    ROA_CANDLE_SHAFT_TOP = "Ruins of Ash - Candle (Shaft Top)"
    ROA_CANDLE_ABOVE_CENTAUR = "Ruins of Ash - Candle (Above Centaur)"
    ROA_CANDLE_BABY_GORGON = "Ruins of Ash - Candle (Baby Gorgon)"
    ROA_CANDLE_TOP_CENTAUR = "Ruins of Ash - Candle (Top Centaur)"
    ROA_CANDLE_HIDDEN_1 = "Ruins of Ash - Candle (Hidden 1)"
    ROA_CANDLE_HIDDEN_2 = "Ruins of Ash - Candle (Hidden 2)"
    ROA_CANDLE_HIDDEN_3 = "Ruins of Ash - Candle (Hidden 3)"
    ROA_CANDLE_HIDDEN_4 = "Ruins of Ash - Candle (Hidden 4)"
    ROA_CANDLE_HIDDEN_5 = "Ruins of Ash - Candle (Hidden 5)"
    ROA_CANDLE_BOTTOM_ASCEND = "Ruins of Ash - Candle (Bottom Ascend)"
    ROA_CANDLE_BRANCH = "Ruins of Ash - Candle (Branch)"
    ROA_CANDLE_ICARUS_1 = "Ruins of Ash - Candle (Icarus 1)"
    ROA_CANDLE_ICARUS_2 = "Ruins of Ash - Candle (Icarus 2)"
    ROA_CANDLE_ELEVATOR = "Ruins of Ash - Candle (Elevator)"
    ROA_CANDLE_ELEVATOR_CAMPFIRE = "Ruins of Ash - Candle (Elevator Campfire)"
    ROA_CANDLE_BOSS_1 = "Ruins of Ash - Candle (Boss 1)"
    ROA_CANDLE_BOSS_2 = "Ruins of Ash - Candle (Boss 2)"
    ROA_CANDLE_SPIDERS = "Ruins of Ash - Candle (Spiders)"
    ROA_CANDLE_SPIKE_BALLS = "Ruins of Ash - Candle (Spike Balls)"
    ROA_CANDLE_LADDER_R = "Ruins of Ash - Candle (Ladder Right)"
    ROA_CANDLE_ARENA = "Ruins of Ash - Candle (Enemy Arena)"

    DARK_HP_4 = "Darkness - Max HP +4"
    DARK_WHITE_KEY = "Darkness - White Key"
    DARK_SWITCH = "Darkness - Switch"

    APEX_CHALICE = "The Apex - Blood Chalice"
    APEX_HP_1_CHALICE = "The Apex - Max HP +1 (Blood Chalice)"
    APEX_HP_5_HEART = "The Apex - Max HP +5 (After Heart)"
    APEX_BLUE_KEY = "The Apex - Blue Key"
    APEX_ELEVATOR = "The Apex - Elevator"
    APEX_SWITCH = "The Apex - Switch"
    APEX_CANDLE_ELEVATOR = "The Apex - Candle (Elevator)"
    APEX_CANDLE_CHALICE_1 = "The Apex - Candle (Chalice 1)"
    APEX_CANDLE_CHALICE_2 = "The Apex - Candle (Chalice 2)"
    APEX_CANDLE_CHALICE_3 = "The Apex - Candle (Chalice 3)"
    APEX_CANDLE_GARG_1 = "The Apex - Candle (Gargoyle 1)"
    APEX_CANDLE_GARG_2 = "The Apex - Candle (Gargoyle 2)"
    APEX_CANDLE_GARG_3 = "The Apex - Candle (Gargoyle 3)"
    APEX_CANDLE_GARG_4 = "The Apex - Candle (Gargoyle 4)"

    CAVES_ATTACK_RED = "Caves - Attack +1 (Item Chain Red)"
    CAVES_ATTACK_BLUE = "Caves - Attack +1 (Item Chain Blue)"
    CAVES_ATTACK_GREEN = "Caves - Attack +1 (Item Chain Green)"
    CAVES_HP_1_START = "Caves - Max HP +1 (1st Room)"
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
    CATA_CANDLE_1ST_ROOM = "Catacombs - Candle (1st Room)"
    CATA_CANDLE_ORB_MULTI = "Catacombs - Candle (Orb Multiplier)"
    CATA_CANDLE_AFTER_BOW = "Catacombs - Candle (After Bow)"
    CATA_CANDLE_DEV_ROOM = "Catacombs - Candle (Dev Room)"
    CATA_CANDLE_GRIFFON = "Catacombs - Candle (Griffon)"
    CATA_CANDLE_SHORTCUT = "Catacombs - Candle (Vertical Shortcut)"
    CATA_CANDLE_PRISON = "Catacombs - Candle (Prison)"
    CATA_CANDLE_ABOVE_ROOTS_1 = "Catacombs - Candle (Above Roots 1)"
    CATA_CANDLE_ABOVE_ROOTS_2 = "Catacombs - Candle (Above Roots 2)"
    CATA_CANDLE_ABOVE_ROOTS_3 = "Catacombs - Candle (Above Roots 3)"
    CATA_CANDLE_ABOVE_ROOTS_4 = "Catacombs - Candle (Above Roots 4)"
    CATA_CANDLE_ABOVE_ROOTS_5 = "Catacombs - Candle (Above Roots 5)"
    CATA_CANDLE_VOID_R_1 = "Catacombs - Candle (Void Right 1)"
    CATA_CANDLE_VOID_R_2 = "Catacombs - Candle (Void Right 2)"

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
    TR_CANDLE_1ST_ROOM_1 = "Tower Roots - Candle (1st Room 1)"
    TR_CANDLE_1ST_ROOM_2 = "Tower Roots - Candle (1st Room 2)"
    TR_CANDLE_1ST_ROOM_3 = "Tower Roots - Candle (1st Room 3)"

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
    CD_CANDLE_1 = "Cyclops Den - Candle 1"
    CD_CANDLE_CAMPFIRE_2_1 = "Cyclops Den - Candle (2nd Campfire 1)"
    CD_CANDLE_CAMPFIRE_2_2 = "Cyclops Den - Candle (2nd Campfire 2)"
    CD_CANDLE_TOP_CAMPFIRE = "Cyclops Den - Candle (Top Campfire)"

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
    CATH_CANDLE_TOP_1 = "Cathedral - Candle (Top 1)"
    CATH_CANDLE_TOP_2 = "Cathedral - Candle (Top 2)"

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
    game: str = GAME_NAME


@dataclass(frozen=True)
class LocationData:
    name: LocationName
    region: RegionName
    group: LocationGroup
    area: Area
    description: str = ""
    room: str = ""


ALL_LOCATIONS: tuple[LocationData, ...] = (
    LocationData(LocationName.GT_GORGONHEART, RegionName.GT_GORGONHEART, LocationGroup.ITEM, Area.GT),
    LocationData(LocationName.GT_ANCIENTS_RING, RegionName.GT_BOTTOM, LocationGroup.ITEM, Area.GT),
    LocationData(LocationName.GT_SWORD, RegionName.GT_SWORD, LocationGroup.ITEM, Area.GT),
    LocationData(LocationName.GT_MAP, RegionName.GT_BOTTOM, LocationGroup.ITEM, Area.GT),
    LocationData(LocationName.GT_ASCENDANT_KEY, RegionName.GT_ASCENDANT_KEY, LocationGroup.ITEM, Area.GT),
    LocationData(LocationName.GT_BANISH, RegionName.GT_LEFT, LocationGroup.ITEM, Area.GT),
    LocationData(LocationName.GT_VOID, RegionName.GT_VOID, LocationGroup.ITEM, Area.GT),
    LocationData(
        LocationName.GT_EYE_RED,
        RegionName.GT_BOSS,
        LocationGroup.ITEM,
        Area.GT,
        description="Default Tauros, the boss of Gorgon Tomb",
    ),
    LocationData(LocationName.GT_ATTACK, RegionName.GT_BABY_GORGON, LocationGroup.ATTACK, Area.GT),
    LocationData(LocationName.GT_HP_1_RING, RegionName.GT_BOTTOM, LocationGroup.HEALTH, Area.GT),
    LocationData(LocationName.GT_HP_5_KEY, RegionName.GT_ASCENDANT_KEY, LocationGroup.HEALTH, Area.GT),
    LocationData(LocationName.GT_WHITE_KEY_START, RegionName.GT_ENTRANCE, LocationGroup.KEY_WHITE, Area.GT),
    LocationData(LocationName.GT_WHITE_KEY_RIGHT, RegionName.GT_BOTTOM, LocationGroup.KEY_WHITE, Area.GT),
    LocationData(LocationName.GT_WHITE_KEY_BOSS, RegionName.GT_TOP_RIGHT, LocationGroup.KEY_WHITE, Area.GT),
    LocationData(LocationName.GT_BLUE_KEY_BONESNAKE, RegionName.GT_BOTTOM, LocationGroup.KEY_BLUE, Area.GT),
    LocationData(LocationName.GT_BLUE_KEY_BUTT, RegionName.GT_BUTT, LocationGroup.KEY_BLUE, Area.GT),
    LocationData(LocationName.GT_BLUE_KEY_WALL, RegionName.GT_BUTT, LocationGroup.KEY_BLUE, Area.GT),
    LocationData(LocationName.GT_BLUE_KEY_POT, RegionName.GT_UPPER_PATH, LocationGroup.KEY_BLUE, Area.GT),
    LocationData(LocationName.GT_RED_KEY, RegionName.GT_BOSS, LocationGroup.KEY_RED, Area.GT),
    LocationData(LocationName.MECH_BOOTS, RegionName.MECH_BOOTS_UPPER, LocationGroup.ITEM, Area.MECH),
    LocationData(LocationName.MECH_CLOAK, RegionName.MECH_CLOAK, LocationGroup.ITEM, Area.MECH),
    LocationData(
        LocationName.MECH_EYE_BLUE,
        RegionName.MECH_BOSS,
        LocationGroup.ITEM,
        Area.MECH,
        description="Defeat Volantis, the boss of Mechanism",
    ),
    LocationData(LocationName.MECH_ATTACK_VOLANTIS, RegionName.HOTP_START, LocationGroup.ATTACK, Area.MECH),
    LocationData(LocationName.MECH_ATTACK_STAR, RegionName.MECH_CHAINS, LocationGroup.ATTACK, Area.MECH),
    LocationData(LocationName.MECH_HP_1_SWITCH, RegionName.MECH_RIGHT, LocationGroup.HEALTH, Area.MECH),
    LocationData(LocationName.MECH_HP_1_STAR, RegionName.MECH_BRAM_TUNNEL, LocationGroup.HEALTH, Area.MECH),
    LocationData(LocationName.MECH_HP_3_CLAW, RegionName.MECH_BOTTOM_CAMPFIRE, LocationGroup.HEALTH, Area.MECH),
    LocationData(
        LocationName.MECH_WHITE_KEY_LINUS,
        RegionName.MECH_SWORD_CONNECTION,
        LocationGroup.KEY_WHITE,
        Area.MECH,
    ),
    LocationData(LocationName.MECH_WHITE_KEY_BK, RegionName.MECH_AFTER_BK, LocationGroup.KEY_WHITE, Area.MECH),
    LocationData(LocationName.MECH_WHITE_KEY_ARENA, RegionName.MECH_RIGHT, LocationGroup.KEY_WHITE, Area.MECH),
    LocationData(LocationName.MECH_WHITE_KEY_TOP, RegionName.MECH_TOP, LocationGroup.KEY_WHITE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_VOID, RegionName.GT_VOID, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_SNAKE, RegionName.MECH_SNAKE, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_LINUS, RegionName.MECH_LOWER_ARIAS, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_SACRIFICE, RegionName.MECH_SACRIFICE, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_RED, RegionName.MECH_START, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_ARIAS, RegionName.MECH_ARIAS_EYEBALL, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_BLOCKS, RegionName.MECH_CHAINS, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_TOP, RegionName.MECH_SPLIT_PATH, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_OLD_MAN, RegionName.MECH_RIGHT, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_SAVE, RegionName.MECH_TOP, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_BLUE_KEY_POT, RegionName.MECH_POTS, LocationGroup.KEY_BLUE, Area.MECH),
    LocationData(LocationName.MECH_RED_KEY, RegionName.MECH_LOWER_VOID, LocationGroup.KEY_RED, Area.MECH),
    LocationData(LocationName.HOTP_BELL, RegionName.HOTP_BELL, LocationGroup.ITEM, Area.HOTP),
    LocationData(LocationName.HOTP_AMULET, RegionName.HOTP_AMULET, LocationGroup.ITEM, Area.HOTP),
    LocationData(LocationName.HOTP_CLAW, RegionName.HOTP_CLAW, LocationGroup.ITEM, Area.HOTP),
    LocationData(LocationName.HOTP_GAUNTLET, RegionName.HOTP_GAUNTLET, LocationGroup.ITEM, Area.HOTP),
    LocationData(LocationName.HOTP_MAIDEN_RING, RegionName.HOTP_MAIDEN, LocationGroup.ITEM, Area.HOTP),
    LocationData(LocationName.HOTP_HP_1_CLAW, RegionName.HOTP_CLAW_LEFT, LocationGroup.HEALTH, Area.HOTP),
    LocationData(LocationName.HOTP_HP_2_LADDER, RegionName.HOTP_ELEVATOR, LocationGroup.HEALTH, Area.HOTP),
    LocationData(LocationName.HOTP_HP_2_GAUNTLET, RegionName.HOTP_TP_FALL_TOP, LocationGroup.HEALTH, Area.HOTP),
    LocationData(LocationName.HOTP_HP_5_OLD_MAN, RegionName.HOTP_ABOVE_OLD_MAN, LocationGroup.HEALTH, Area.HOTP),
    LocationData(LocationName.HOTP_HP_5_MAZE, RegionName.HOTP_LOWER_VOID, LocationGroup.HEALTH, Area.HOTP),
    LocationData(LocationName.HOTP_HP_5_START, RegionName.HOTP_START, LocationGroup.HEALTH, Area.HOTP),
    LocationData(LocationName.HOTP_WHITE_KEY_LEFT, RegionName.HOTP_START_LEFT, LocationGroup.KEY_WHITE, Area.HOTP),
    LocationData(LocationName.HOTP_WHITE_KEY_GHOST, RegionName.HOTP_LOWER, LocationGroup.KEY_WHITE, Area.HOTP),
    LocationData(LocationName.HOTP_WHITE_KEY_OLD_MAN, RegionName.HOTP_ELEVATOR, LocationGroup.KEY_WHITE, Area.HOTP),
    LocationData(LocationName.HOTP_WHITE_KEY_BOSS, RegionName.HOTP_UPPER_ARIAS, LocationGroup.KEY_WHITE, Area.HOTP),
    LocationData(LocationName.HOTP_BLUE_KEY_STATUE, RegionName.HOTP_EPIMETHEUS, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationData(LocationName.HOTP_BLUE_KEY_GOLD, RegionName.HOTP_LOWER, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationData(
        LocationName.HOTP_BLUE_KEY_AMULET,
        RegionName.HOTP_AMULET_CONNECTION,
        LocationGroup.KEY_BLUE,
        Area.HOTP,
    ),
    LocationData(LocationName.HOTP_BLUE_KEY_LADDER, RegionName.HOTP_ELEVATOR, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationData(
        LocationName.HOTP_BLUE_KEY_TELEPORTS,
        RegionName.HOTP_SPIKE_TP_SECRET,
        LocationGroup.KEY_BLUE,
        Area.HOTP,
    ),
    LocationData(LocationName.HOTP_BLUE_KEY_MAZE, RegionName.HOTP_TP_FALL_TOP, LocationGroup.KEY_BLUE, Area.HOTP),
    LocationData(LocationName.HOTP_RED_KEY, RegionName.HOTP_RED_KEY, LocationGroup.KEY_RED, Area.HOTP),
    LocationData(LocationName.ROA_ICARUS, RegionName.ROA_ICARUS, LocationGroup.ITEM, Area.ROA),
    LocationData(
        LocationName.ROA_EYE_GREEN,
        RegionName.ROA_BOSS,
        LocationGroup.ITEM,
        Area.ROA,
        description="Defeat Solaria, the boss of Ruins of Ash",
    ),
    LocationData(LocationName.ROA_ATTACK, RegionName.ROA_MIDDLE, LocationGroup.ATTACK, Area.ROA),
    LocationData(LocationName.ROA_HP_1_LEFT, RegionName.ROA_LEFT_ASCENT, LocationGroup.HEALTH, Area.ROA),
    LocationData(LocationName.ROA_HP_2_RIGHT, RegionName.ROA_RIGHT_BRANCH, LocationGroup.HEALTH, Area.ROA),
    LocationData(LocationName.ROA_HP_5_SOLARIA, RegionName.APEX, LocationGroup.HEALTH, Area.ROA),
    LocationData(LocationName.ROA_WHITE_KEY_SAVE, RegionName.ROA_WORMS, LocationGroup.KEY_WHITE, Area.ROA),
    LocationData(LocationName.ROA_WHITE_KEY_REAPERS, RegionName.ROA_LEFT_ASCENT, LocationGroup.KEY_WHITE, Area.ROA),
    LocationData(LocationName.ROA_WHITE_KEY_TORCHES, RegionName.ROA_MIDDLE, LocationGroup.KEY_WHITE, Area.ROA),
    LocationData(LocationName.ROA_WHITE_KEY_PORTAL, RegionName.ROA_UPPER_VOID, LocationGroup.KEY_WHITE, Area.ROA),
    LocationData(LocationName.ROA_BLUE_KEY_FACE, RegionName.ROA_BOTTOM_ASCEND, LocationGroup.KEY_BLUE, Area.ROA),
    LocationData(LocationName.ROA_BLUE_KEY_FLAMES, RegionName.ROA_ARIAS_BABY_GORGON, LocationGroup.KEY_BLUE, Area.ROA),
    LocationData(LocationName.ROA_BLUE_KEY_BABY, RegionName.ROA_LEFT_BABY_GORGON, LocationGroup.KEY_BLUE, Area.ROA),
    LocationData(LocationName.ROA_BLUE_KEY_TOP, RegionName.ROA_ABOVE_CENTAUR_L, LocationGroup.KEY_BLUE, Area.ROA),
    LocationData(LocationName.ROA_BLUE_KEY_POT, RegionName.ROA_TRIPLE_REAPER, LocationGroup.KEY_BLUE, Area.ROA),
    LocationData(LocationName.ROA_RED_KEY, RegionName.ROA_RED_KEY, LocationGroup.KEY_RED, Area.ROA),
    LocationData(LocationName.DARK_HP_4, RegionName.DARK_END, LocationGroup.HEALTH, Area.DARK),
    LocationData(LocationName.DARK_WHITE_KEY, RegionName.DARK_END, LocationGroup.KEY_WHITE, Area.DARK),
    LocationData(LocationName.APEX_CHALICE, RegionName.APEX_CENTAUR, LocationGroup.ITEM, Area.APEX),
    LocationData(LocationName.APEX_HP_1_CHALICE, RegionName.APEX, LocationGroup.HEALTH, Area.APEX),
    LocationData(LocationName.APEX_HP_5_HEART, RegionName.APEX_HEART, LocationGroup.HEALTH, Area.APEX),
    LocationData(LocationName.APEX_BLUE_KEY, RegionName.APEX, LocationGroup.KEY_BLUE, Area.APEX),
    LocationData(LocationName.CATA_BOW, RegionName.CATA_BOW, LocationGroup.ITEM, Area.CATA),
    LocationData(LocationName.CAVES_ATTACK_RED, RegionName.CAVES_ITEM_CHAIN, LocationGroup.ATTACK, Area.CAVES),
    LocationData(LocationName.CAVES_ATTACK_BLUE, RegionName.CAVES_ITEM_CHAIN, LocationGroup.ATTACK, Area.CAVES),
    LocationData(LocationName.CAVES_ATTACK_GREEN, RegionName.CAVES_ITEM_CHAIN, LocationGroup.ATTACK, Area.CAVES),
    LocationData(LocationName.CATA_ATTACK_ROOT, RegionName.CATA_CLIMBABLE_ROOT, LocationGroup.ATTACK, Area.CATA),
    LocationData(LocationName.CATA_ATTACK_POISON, RegionName.CATA_POISON_ROOTS, LocationGroup.ATTACK, Area.CATA),
    LocationData(LocationName.CAVES_HP_1_START, RegionName.CAVES_START, LocationGroup.HEALTH, Area.CAVES),
    LocationData(LocationName.CAVES_HP_1_CYCLOPS, RegionName.CAVES_ARENA, LocationGroup.HEALTH, Area.CAVES),
    LocationData(LocationName.CATA_HP_1_ABOVE_POISON, RegionName.CATA_POISON_ROOTS, LocationGroup.HEALTH, Area.CATA),
    LocationData(LocationName.CATA_HP_2_BEFORE_POISON, RegionName.CATA_POISON_ROOTS, LocationGroup.HEALTH, Area.CATA),
    LocationData(LocationName.CATA_HP_2_AFTER_POISON, RegionName.CATA_POISON_ROOTS, LocationGroup.HEALTH, Area.CATA),
    LocationData(LocationName.CATA_HP_2_GEMINI_BOTTOM, RegionName.CATA_DOUBLE_DOOR, LocationGroup.HEALTH, Area.CATA),
    LocationData(LocationName.CATA_HP_2_GEMINI_TOP, RegionName.CATA_CENTAUR, LocationGroup.HEALTH, Area.CATA),
    LocationData(LocationName.CATA_HP_2_ABOVE_GEMINI, RegionName.CATA_FLAMES, LocationGroup.HEALTH, Area.CATA),
    LocationData(LocationName.CAVES_HP_5_CHAIN, RegionName.CAVES_ITEM_CHAIN, LocationGroup.HEALTH, Area.CAVES),
    LocationData(LocationName.CATA_WHITE_KEY_HEAD, RegionName.CATA_TOP, LocationGroup.KEY_WHITE, Area.CATA),
    LocationData(
        LocationName.CATA_WHITE_KEY_DEV_ROOM,
        RegionName.CATA_DEV_ROOM_CONNECTION,
        LocationGroup.KEY_WHITE,
        Area.CATA,
    ),
    LocationData(LocationName.CATA_WHITE_KEY_PRISON, RegionName.CATA_BOSS, LocationGroup.KEY_WHITE, Area.CATA),
    LocationData(LocationName.CATA_BLUE_KEY_SLIMES, RegionName.CATA_BOW_CAMPFIRE, LocationGroup.KEY_BLUE, Area.CATA),
    LocationData(LocationName.CATA_BLUE_KEY_EYEBALLS, RegionName.CATA_CENTAUR, LocationGroup.KEY_BLUE, Area.CATA),
    LocationData(LocationName.TR_ADORNED_KEY, RegionName.TR_BOTTOM, LocationGroup.ITEM, Area.TR),
    LocationData(LocationName.TR_HP_1_BOTTOM, RegionName.TR_BOTTOM_LEFT, LocationGroup.HEALTH, Area.TR),
    LocationData(LocationName.TR_HP_2_TOP, RegionName.TR_LEFT, LocationGroup.HEALTH, Area.TR),
    LocationData(LocationName.TR_RED_KEY, RegionName.CATA_BOSS, LocationGroup.KEY_RED, Area.TR),
    LocationData(LocationName.CD_ATTACK, RegionName.CD_TOP, LocationGroup.ATTACK, Area.CD),
    LocationData(LocationName.CD_HP_1, RegionName.CD_TOP, LocationGroup.HEALTH, Area.CD),
    LocationData(LocationName.CATH_BLOCK, RegionName.CATH_TOP, LocationGroup.ITEM, Area.CATH),
    LocationData(LocationName.CATH_ATTACK, RegionName.CATH_UPPER_SPIKE_PIT, LocationGroup.ATTACK, Area.CATH),
    LocationData(LocationName.CATH_HP_1_TOP_LEFT, RegionName.CATH_TOP, LocationGroup.HEALTH, Area.CATH),
    LocationData(LocationName.CATH_HP_1_TOP_RIGHT, RegionName.CATH_TOP, LocationGroup.HEALTH, Area.CATH),
    LocationData(LocationName.CATH_HP_2_CLAW, RegionName.CATH_LEFT_SHAFT, LocationGroup.HEALTH, Area.CATH),
    LocationData(LocationName.CATH_HP_5_BELL, RegionName.CATH_CAMPFIRE_1, LocationGroup.HEALTH, Area.CATH),
    LocationData(LocationName.SP_STAR, RegionName.SP_STAR, LocationGroup.ITEM, Area.SP),
    LocationData(LocationName.SP_ATTACK, RegionName.SP_CAMPFIRE_2, LocationGroup.ATTACK, Area.SP),
    LocationData(LocationName.SP_HP_1, RegionName.SP_FROG, LocationGroup.HEALTH, Area.SP),
    LocationData(LocationName.SP_BLUE_KEY_BUBBLES, RegionName.SP_START, LocationGroup.KEY_BLUE, Area.SP),
    LocationData(LocationName.SP_BLUE_KEY_STAR, RegionName.SP_STAR_END, LocationGroup.KEY_BLUE, Area.SP),
    LocationData(LocationName.SP_BLUE_KEY_PAINTING, RegionName.SP_PAINTING, LocationGroup.KEY_BLUE, Area.SP),
    LocationData(LocationName.SP_BLUE_KEY_ARIAS, RegionName.SP_CAMPFIRE_2, LocationGroup.KEY_BLUE, Area.SP),
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
    LocationData(LocationName.GT_ALGUS, RegionName.GT_ENTRANCE, LocationGroup.CHARACTER, Area.GT),
    LocationData(LocationName.GT_ARIAS, RegionName.GT_ENTRANCE, LocationGroup.CHARACTER, Area.GT),
    LocationData(LocationName.GT_KYULI, RegionName.GT_ENTRANCE, LocationGroup.CHARACTER, Area.GT),
    LocationData(LocationName.MECH_ZEEK, RegionName.MECH_ZEEK, LocationGroup.CHARACTER, Area.MECH),
    LocationData(LocationName.TR_BRAM, RegionName.TR_BRAM, LocationGroup.CHARACTER, Area.TR),
    LocationData(LocationName.GT_ELEVATOR_2, RegionName.GT_BOSS, LocationGroup.ELEVATOR, Area.GT),
    LocationData(LocationName.GT_SWITCH_2ND_ROOM, RegionName.GT_ENTRANCE, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_1ST_CYCLOPS, RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_SPIKE_TUNNEL, RegionName.GT_TOP_LEFT, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_BUTT_ACCESS, RegionName.GT_SPIKE_TUNNEL_SWITCH, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_GH, RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT),
    LocationData(
        LocationName.GT_SWITCH_UPPER_PATH_BLOCKS,
        RegionName.GT_UPPER_PATH_CONNECTION,
        LocationGroup.SWITCH,
        Area.GT,
    ),
    LocationData(
        LocationName.GT_SWITCH_UPPER_PATH_ACCESS,
        RegionName.GT_UPPER_PATH_CONNECTION,
        LocationGroup.SWITCH,
        Area.GT,
    ),
    LocationData(LocationName.GT_SWITCH_CROSSES, RegionName.GT_LEFT, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_GH_SHORTCUT, RegionName.GT_GORGONHEART, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_ARIAS_PATH, RegionName.GT_TOP_LEFT, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_SWORD_ACCESS, RegionName.GT_SWORD_FORK, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_SWORD_BACKTRACK, RegionName.GT_SWORD_FORK, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_SWORD, RegionName.GT_SWORD, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_SWITCH_UPPER_ARIAS, RegionName.GT_ARIAS_SWORD_SWITCH, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_CRYSTAL_LADDER, RegionName.GT_LADDER_SWITCH, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_CRYSTAL_ROTA, RegionName.GT_UPPER_PATH, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_CRYSTAL_OLD_MAN_1, RegionName.GT_OLD_MAN_FORK, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.GT_CRYSTAL_OLD_MAN_2, RegionName.GT_OLD_MAN_FORK, LocationGroup.SWITCH, Area.GT),
    LocationData(LocationName.MECH_ELEVATOR_1, RegionName.MECH_ZEEK_CONNECTION, LocationGroup.ELEVATOR, Area.MECH),
    LocationData(LocationName.MECH_ELEVATOR_2, RegionName.MECH_BOSS, LocationGroup.ELEVATOR, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_WATCHER, RegionName.MECH_ROOTS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_CHAINS, RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationData(
        LocationName.MECH_SWITCH_BOSS_ACCESS_1,
        RegionName.MECH_BOSS_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
    ),
    LocationData(
        LocationName.MECH_SWITCH_BOSS_ACCESS_2,
        RegionName.MECH_BRAM_TUNNEL_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
    ),
    LocationData(LocationName.MECH_SWITCH_SPLIT_PATH, RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_SNAKE_1, RegionName.MECH_BOTTOM_CAMPFIRE, LocationGroup.SWITCH, Area.MECH),
    LocationData(
        LocationName.MECH_SWITCH_BOOTS_ACCESS,
        RegionName.MECH_BOOTS_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
    ),
    LocationData(
        LocationName.MECH_SWITCH_UPPER_GT_ACCESS,
        RegionName.MECH_BOTTOM_CAMPFIRE,
        LocationGroup.SWITCH,
        Area.MECH,
    ),
    LocationData(LocationName.MECH_SWITCH_UPPER_VOID_DROP, RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_UPPER_VOID, RegionName.MECH_UPPER_VOID, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_LINUS, RegionName.MECH_LINUS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_TO_BOSS_2, RegionName.MECH_BOSS_SWITCHES, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_POTS, RegionName.MECH_BELOW_POTS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_MAZE_BACKDOOR, RegionName.HOTP_FALL_BOTTOM, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_TO_BOSS_1, RegionName.MECH_BOSS_SWITCHES, LocationGroup.SWITCH, Area.MECH),
    LocationData(
        LocationName.MECH_SWITCH_BLOCK_STAIRS,
        RegionName.MECH_CLOAK_CONNECTION,
        LocationGroup.SWITCH,
        Area.MECH,
    ),
    LocationData(
        LocationName.MECH_SWITCH_ARIAS_CYCLOPS,
        RegionName.MECH_CHARACTER_SWAPS,
        LocationGroup.SWITCH,
        Area.MECH,
    ),
    LocationData(LocationName.MECH_SWITCH_BOOTS_LOWER, RegionName.MECH_BOOTS_LOWER, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_CHAINS_GAP, RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_LOWER_KEY, RegionName.MECH_SWORD_CONNECTION, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_ARIAS, RegionName.MECH_ARIAS_EYEBALL, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_SNAKE_2, RegionName.MECH_SNAKE, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_KEY_BLOCKS, RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_CANNON, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_EYEBALL, RegionName.MECH_BELOW_POTS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_SWITCH_INVISIBLE, RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_CANNON, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_LINUS, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_LOWER, RegionName.MECH_SWORD_CONNECTION, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TO_BOSS_3, RegionName.MECH_BOSS_CONNECTION, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TRIPLE_1, RegionName.MECH_TRIPLE_SWITCHES, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TRIPLE_2, RegionName.MECH_TRIPLE_SWITCHES, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TRIPLE_3, RegionName.MECH_TRIPLE_SWITCHES, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TOP, RegionName.MECH_TOP, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_CLOAK, RegionName.MECH_CLOAK_CONNECTION, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_SLIMES, RegionName.MECH_BOSS_SWITCHES, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TO_CD, RegionName.MECH_TOP, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_CAMPFIRE, RegionName.MECH_BK, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_1ST_ROOM, RegionName.MECH_START, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_OLD_MAN, RegionName.MECH_RIGHT, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_TOP_CHAINS, RegionName.MECH_CHAINS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_CRYSTAL_BK, RegionName.MECH_BK, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.MECH_FACE_ABOVE_VOLANTIS, RegionName.MECH_BOSS, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.HOTP_ELEVATOR, RegionName.HOTP_ELEVATOR, LocationGroup.ELEVATOR, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_ROCK, RegionName.HOTP_AMULET_CONNECTION, LocationGroup.SWITCH, Area.HOTP),
    LocationData(
        LocationName.HOTP_SWITCH_BELOW_START,
        RegionName.HOTP_START_BOTTOM_MID,
        LocationGroup.SWITCH,
        Area.HOTP,
    ),
    LocationData(LocationName.HOTP_SWITCH_LEFT_2, RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_LEFT_1, RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_LOWER_SHORTCUT, RegionName.HOTP_LOWER, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_BELL, RegionName.HOTP_BELL, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_GHOST_BLOOD, RegionName.HOTP_GHOST_BLOOD, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_TELEPORTS, RegionName.HOTP_LOWER_ARIAS, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_WORM_PILLAR, RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_TO_CLAW_1, RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_TO_CLAW_2, RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_CLAW_ACCESS, RegionName.HOTP_CLAW_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_GHOSTS, RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_LEFT_3, RegionName.HOTP_START_MID, LocationGroup.SWITCH, Area.HOTP),
    LocationData(
        LocationName.HOTP_SWITCH_ABOVE_OLD_MAN, RegionName.HOTP_ABOVE_OLD_MAN, LocationGroup.SWITCH, Area.HOTP
    ),
    LocationData(LocationName.HOTP_SWITCH_TO_ABOVE_OLD_MAN, RegionName.HOTP_TOP_LEFT, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_TP_PUZZLE, RegionName.HOTP_TP_PUZZLE, LocationGroup.SWITCH, Area.HOTP),
    LocationData(
        LocationName.HOTP_SWITCH_EYEBALL_SHORTCUT,
        RegionName.HOTP_WORM_SHORTCUT,
        LocationGroup.SWITCH,
        Area.HOTP,
    ),
    LocationData(LocationName.HOTP_SWITCH_BELL_ACCESS, RegionName.HOTP_BELL_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_1ST_ROOM, RegionName.HOTP_START, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_SWITCH_LEFT_BACKTRACK, RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationData(
        LocationName.HOTP_CRYSTAL_ROCK_ACCESS,
        RegionName.HOTP_MECH_VOID_CONNECTION,
        LocationGroup.SWITCH,
        Area.HOTP,
    ),
    LocationData(
        LocationName.HOTP_CRYSTAL_BOTTOM,
        RegionName.HOTP_MECH_VOID_CONNECTION,
        LocationGroup.SWITCH,
        Area.HOTP,
    ),
    LocationData(LocationName.HOTP_CRYSTAL_LOWER, RegionName.HOTP_LOWER, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_CRYSTAL_AFTER_CLAW, RegionName.HOTP_CLAW_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_CRYSTAL_MAIDEN_1, RegionName.HOTP_MAIDEN, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_CRYSTAL_MAIDEN_2, RegionName.HOTP_MAIDEN, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_CRYSTAL_BELL_ACCESS, RegionName.HOTP_BELL_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_CRYSTAL_HEART, RegionName.HOTP_BOSS_CAMPFIRE, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_CRYSTAL_BELOW_PUZZLE, RegionName.HOTP_TP_FALL_TOP, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.HOTP_FACE_OLD_MAN, RegionName.HOTP_ELEVATOR, LocationGroup.SWITCH, Area.HOTP),
    LocationData(LocationName.ROA_ELEVATOR_1, RegionName.HOTP_BOSS, LocationGroup.ELEVATOR, Area.ROA),
    LocationData(LocationName.ROA_ELEVATOR_2, RegionName.ROA_ELEVATOR, LocationGroup.ELEVATOR, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_ASCEND, RegionName.ROA_BOTTOM_ASCEND, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_AFTER_WORMS, RegionName.ROA_WORMS_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_RIGHT_PATH, RegionName.ROA_RIGHT_SWITCH_1, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_APEX_ACCESS, RegionName.ROA_APEX_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_ICARUS, RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_SHAFT_L, RegionName.ROA_MIDDLE_LADDER, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_SHAFT_R, RegionName.ROA_MIDDLE_LADDER, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_ELEVATOR, RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_SHAFT_DOWNWARDS, RegionName.ROA_SP_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_SPIDERS, RegionName.ROA_SPIDERS_2, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_DARK_ROOM, RegionName.ROA_ELEVATOR, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_ASCEND_SHORTCUT, RegionName.ROA_MIDDLE, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_1ST_SHORTCUT, RegionName.ROA_BOTTOM_ASCEND, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_SPIKE_CLIMB, RegionName.ROA_SPIKE_CLIMB, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_ABOVE_CENTAUR, RegionName.ROA_SP_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_BLOOD_POT, RegionName.ROA_TOP_CENTAUR, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_WORMS, RegionName.ROA_WORMS, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_TRIPLE_1, RegionName.ROA_TRIPLE_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_TRIPLE_3, RegionName.ROA_TRIPLE_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_BABY_GORGON, RegionName.ROA_FLAMES, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_BOSS_ACCESS, RegionName.ROA_BOSS_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_BLOOD_POT_L, RegionName.ROA_BOSS_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_BLOOD_POT_R, RegionName.ROA_BOSS_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_SWITCH_LOWER_VOID, RegionName.ROA_LOWER_VOID, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_CRYSTAL_1ST_ROOM, RegionName.ROA_START, LocationGroup.SWITCH, Area.ROA),
    LocationData(
        LocationName.ROA_CRYSTAL_BABY_GORGON,
        RegionName.ROA_LOWER_VOID_CONNECTION,
        LocationGroup.SWITCH,
        Area.ROA,
    ),
    LocationData(LocationName.ROA_CRYSTAL_LADDER_R, RegionName.ROA_RIGHT_SWITCH_2, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_CRYSTAL_LADDER_L, RegionName.ROA_LEFT_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationData(
        LocationName.ROA_CRYSTAL_CENTAUR, RegionName.ROA_CRYSTAL_ABOVE_CENTAUR, LocationGroup.SWITCH, Area.ROA
    ),
    LocationData(LocationName.ROA_CRYSTAL_SPIKE_BALLS, RegionName.ROA_UPPER_VOID, LocationGroup.SWITCH, Area.ROA),
    LocationData(
        LocationName.ROA_CRYSTAL_LEFT_ASCEND,
        RegionName.ROA_LEFT_ASCENT_CRYSTAL,
        LocationGroup.SWITCH,
        Area.ROA,
    ),
    LocationData(LocationName.ROA_CRYSTAL_SHAFT, RegionName.ROA_SP_CONNECTION, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_CRYSTAL_BRANCH_R, RegionName.ROA_RIGHT_BRANCH, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_CRYSTAL_BRANCH_L, RegionName.ROA_RIGHT_BRANCH, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_CRYSTAL_3_REAPERS, RegionName.ROA_TRIPLE_REAPER, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_CRYSTAL_TRIPLE_2, RegionName.ROA_TRIPLE_SWITCH, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_FACE_SPIDERS, RegionName.ROA_SPIDERS_1, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.ROA_FACE_BLUE_KEY, RegionName.ROA_BOTTOM_ASCEND, LocationGroup.SWITCH, Area.ROA),
    LocationData(LocationName.DARK_SWITCH, RegionName.DARK_START, LocationGroup.SWITCH, Area.DARK),
    LocationData(LocationName.APEX_ELEVATOR, RegionName.APEX, LocationGroup.ELEVATOR, Area.APEX),
    LocationData(LocationName.APEX_SWITCH, RegionName.APEX, LocationGroup.SWITCH, Area.APEX),
    LocationData(LocationName.CAVES_SWITCH_SKELETONS, RegionName.CAVES_UPPER, LocationGroup.SWITCH, Area.CAVES),
    LocationData(LocationName.CAVES_SWITCH_CATA_ACCESS_1, RegionName.CAVES_LOWER, LocationGroup.SWITCH, Area.CAVES),
    LocationData(LocationName.CAVES_SWITCH_CATA_ACCESS_2, RegionName.CAVES_LOWER, LocationGroup.SWITCH, Area.CAVES),
    LocationData(LocationName.CAVES_SWITCH_CATA_ACCESS_3, RegionName.CAVES_LOWER, LocationGroup.SWITCH, Area.CAVES),
    LocationData(LocationName.CAVES_FACE_1ST_ROOM, RegionName.CAVES_START, LocationGroup.SWITCH, Area.CAVES),
    LocationData(LocationName.CATA_ELEVATOR_1, RegionName.CATA_ELEVATOR, LocationGroup.ELEVATOR, Area.CATA),
    LocationData(LocationName.CATA_ELEVATOR_2, RegionName.CATA_BOSS, LocationGroup.ELEVATOR, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_ELEVATOR, RegionName.CATA_TOP, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_SHORTCUT, RegionName.CATA_VERTICAL_SHORTCUT, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_TOP, RegionName.CATA_TOP, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_CLAW_1, RegionName.CATA_SNAKE_MUSHROOMS, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_CLAW_2, RegionName.CATA_SNAKE_MUSHROOMS, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_WATER_1, RegionName.CATA_DOUBLE_SWITCH, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_WATER_2, RegionName.CATA_DOUBLE_SWITCH, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_DEV_ROOM, RegionName.CATA_SNAKE_MUSHROOMS, LocationGroup.SWITCH, Area.CATA),
    LocationData(
        LocationName.CATA_SWITCH_AFTER_BLUE_DOOR,
        RegionName.CATA_BLUE_EYE_DOOR,
        LocationGroup.SWITCH,
        Area.CATA,
    ),
    LocationData(
        LocationName.CATA_SWITCH_SHORTCUT_ACCESS, RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA
    ),
    LocationData(LocationName.CATA_SWITCH_LADDER_BLOCKS, RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA),
    LocationData(
        LocationName.CATA_SWITCH_MID_SHORTCUT,
        RegionName.CATA_VERTICAL_SHORTCUT,
        LocationGroup.SWITCH,
        Area.CATA,
    ),
    LocationData(LocationName.CATA_SWITCH_1ST_ROOM, RegionName.CATA_START, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_FLAMES_2, RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_SWITCH_FLAMES_1, RegionName.CATA_FLAMES_FORK, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_CRYSTAL_POISON_ROOTS, RegionName.CATA_POISON_ROOTS, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_FACE_AFTER_BOW, RegionName.CATA_BOW_CAMPFIRE, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_FACE_BOW, RegionName.CATA_BOW, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_FACE_X4, RegionName.CATA_4_FACES, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_FACE_CAMPFIRE, RegionName.CATA_BOSS, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_FACE_DOUBLE_DOOR, RegionName.CATA_DOUBLE_DOOR, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.CATA_FACE_BOTTOM, RegionName.CATA_DOUBLE_DOOR, LocationGroup.SWITCH, Area.CATA),
    LocationData(LocationName.TR_ELEVATOR, RegionName.TR_START, LocationGroup.ELEVATOR, Area.TR),
    LocationData(LocationName.TR_SWITCH_ADORNED_L, RegionName.TR_BOTTOM, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.TR_SWITCH_ADORNED_M, RegionName.TR_LEFT, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.TR_SWITCH_ADORNED_R, RegionName.TR_DARK_ARIAS, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.TR_SWITCH_ELEVATOR, RegionName.CATA_BOSS, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.TR_SWITCH_BOTTOM, RegionName.TR_MIDDLE_RIGHT, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.TR_CRYSTAL_GOLD, RegionName.TR_TOP_RIGHT, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.TR_CRYSTAL_DARK_ARIAS, RegionName.TR_DARK_ARIAS, LocationGroup.SWITCH, Area.TR),
    LocationData(LocationName.CD_SWITCH_1, RegionName.CD_START, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_SWITCH_2, RegionName.CD_2, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_SWITCH_3, RegionName.CD_3, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_SWITCH_CAMPFIRE, RegionName.CD_MIDDLE, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_SWITCH_TOP, RegionName.CD_TOP, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_CRYSTAL_BACKTRACK, RegionName.CD_2, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_CRYSTAL_START, RegionName.CD_START, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_CRYSTAL_CAMPFIRE, RegionName.CD_CAMPFIRE_3, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CD_CRYSTAL_STEPS, RegionName.CD_STEPS, LocationGroup.SWITCH, Area.CD),
    LocationData(LocationName.CATH_SWITCH_BOTTOM, RegionName.CATH_START_RIGHT, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_SWITCH_BESIDE_SHAFT, RegionName.CATH_SHAFT_ACCESS, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_SWITCH_TOP_CAMPFIRE, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_1ST_ROOM, RegionName.CATH_START_TOP_LEFT, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_SHAFT, RegionName.CATH_LEFT_SHAFT, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_SPIKE_PIT, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_TOP_L, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_TOP_R, RegionName.CATH_TOP, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_SHAFT_ACCESS, RegionName.CATH_SHAFT_ACCESS, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_CRYSTAL_ORBS, RegionName.CATH_ORB_ROOM, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_FACE_LEFT, RegionName.CATH_START_LEFT, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.CATH_FACE_RIGHT, RegionName.CATH_START_LEFT, LocationGroup.SWITCH, Area.CATH),
    LocationData(LocationName.SP_SWITCH_DOUBLE_DOORS, RegionName.SP_HEARTS, LocationGroup.SWITCH, Area.SP),
    LocationData(LocationName.SP_SWITCH_BUBBLES, RegionName.SP_CAMPFIRE_1, LocationGroup.SWITCH, Area.SP),
    LocationData(LocationName.SP_SWITCH_AFTER_STAR, RegionName.SP_STAR_CONNECTION, LocationGroup.SWITCH, Area.SP),
    LocationData(LocationName.SP_CRYSTAL_BLOCKS, RegionName.SP_START, LocationGroup.SWITCH, Area.SP),
    LocationData(LocationName.SP_CRYSTAL_STAR, RegionName.SP_SHAFT, LocationGroup.SWITCH, Area.SP),
    LocationData(LocationName.MECH_CYCLOPS, RegionName.MECH_ZEEK, LocationGroup.ITEM, Area.MECH),
    LocationData(LocationName.CD_CROWN, RegionName.CD_BOSS, LocationGroup.ITEM, Area.CD),
    LocationData(LocationName.GT_CANDLE_LINUS, RegionName.GT_BOTTOM, LocationGroup.CANDLE, Area.GT),
    LocationData(LocationName.GT_CANDLE_1ST_CYCLOPS, RegionName.GT_LEFT, LocationGroup.CANDLE, Area.GT),
    LocationData(LocationName.GT_CANDLE_BOSS, RegionName.GT_BOSS, LocationGroup.CANDLE, Area.GT),
    LocationData(LocationName.GT_CANDLE_BOTTOM, RegionName.GT_BOTTOM, LocationGroup.CANDLE, Area.GT),
    LocationData(LocationName.MECH_CANDLE_ROOTS, RegionName.MECH_ROOTS, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_BOTTOM, RegionName.MECH_BOTTOM_CAMPFIRE, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_CHAINS, RegionName.MECH_CHAINS_CANDLE, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_RIGHT, RegionName.MECH_SPLIT_PATH, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_POTS, RegionName.MECH_BELOW_POTS, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_BOSS_1, RegionName.MECH_BOSS_CONNECTION, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_BOSS_2, RegionName.MECH_BOSS, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_SLIMES, RegionName.MECH_CLOAK_CONNECTION, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_ZEEK, RegionName.MECH_ZEEK_CONNECTION, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_MAZE_BACKDOOR, RegionName.HOTP_FALL_BOTTOM, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_CD_ACCESS_1, RegionName.MECH_CD_ACCESS, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_CD_ACCESS_2, RegionName.MECH_CD_ACCESS, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_CD_ACCESS_3, RegionName.MECH_CD_ACCESS, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_1ST_ROOM, RegionName.MECH_START, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_BK, RegionName.MECH_BK, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.MECH_CANDLE_CAMPFIRE_R, RegionName.MECH_RIGHT, LocationGroup.CANDLE, Area.MECH),
    LocationData(LocationName.HOTP_CANDLE_1ST_ROOM, RegionName.HOTP_START, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_LOWER, RegionName.HOTP_LOWER, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_BELL, RegionName.HOTP_BELL_CAMPFIRE, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_EYEBALL, RegionName.HOTP_EYEBALL, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_OLD_MAN, RegionName.HOTP_ELEVATOR, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_BEFORE_CLAW, RegionName.HOTP_TOP_LEFT, LocationGroup.CANDLE, Area.HOTP),
    LocationData(
        LocationName.HOTP_CANDLE_CLAW_CAMPFIRE, RegionName.HOTP_CLAW_CAMPFIRE, LocationGroup.CANDLE, Area.HOTP
    ),
    LocationData(LocationName.HOTP_CANDLE_TP_PUZZLE, RegionName.HOTP_BOSS_CAMPFIRE, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_BOSS, RegionName.HOTP_BOSS_CAMPFIRE, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_TP_FALL, RegionName.HOTP_TP_FALL_TOP, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_UPPER_VOID_1, RegionName.HOTP_UPPER_VOID, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_UPPER_VOID_2, RegionName.HOTP_UPPER_VOID, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_UPPER_VOID_3, RegionName.HOTP_UPPER_VOID, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_UPPER_VOID_4, RegionName.HOTP_UPPER_VOID, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.HOTP_CANDLE_ELEVATOR, RegionName.HOTP_ELEVATOR, LocationGroup.CANDLE, Area.HOTP),
    LocationData(LocationName.ROA_CANDLE_1ST_ROOM, RegionName.ROA_START, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_3_REAPERS, RegionName.ROA_LEFT_ASCENT, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_MIDDLE_CAMPFIRE, RegionName.ROA_MIDDLE, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_LADDER_BOTTOM, RegionName.ROA_MIDDLE, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_SHAFT, RegionName.ROA_UPPER_VOID, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_SHAFT_TOP, RegionName.ROA_SP_CONNECTION, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_ABOVE_CENTAUR, RegionName.ROA_SP_CONNECTION, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_BABY_GORGON, RegionName.ROA_ELEVATOR, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_TOP_CENTAUR, RegionName.ROA_TOP_CENTAUR, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_HIDDEN_1, RegionName.ROA_MIDDLE_LADDER, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_HIDDEN_2, RegionName.ROA_MIDDLE_LADDER, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_HIDDEN_3, RegionName.ROA_MIDDLE_LADDER, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_HIDDEN_4, RegionName.ROA_MIDDLE_LADDER, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_HIDDEN_5, RegionName.ROA_MIDDLE_LADDER, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_BOTTOM_ASCEND, RegionName.ROA_BOTTOM_ASCEND, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_BRANCH, RegionName.ROA_RIGHT_BRANCH, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_ICARUS_1, RegionName.ROA_ICARUS, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_ICARUS_2, RegionName.ROA_ICARUS, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_ELEVATOR, RegionName.ROA_ELEVATOR, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_ELEVATOR_CAMPFIRE, RegionName.ROA_ELEVATOR, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_BOSS_1, RegionName.ROA_BOSS, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_BOSS_2, RegionName.ROA_BOSS, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_SPIDERS, RegionName.ROA_SPIDERS_1, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_SPIKE_BALLS, RegionName.ROA_UPPER_VOID, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_LADDER_R, RegionName.ROA_RIGHT_SWITCH_CANDLE, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.ROA_CANDLE_ARENA, RegionName.ROA_ARENA, LocationGroup.CANDLE, Area.ROA),
    LocationData(LocationName.APEX_CANDLE_ELEVATOR, RegionName.APEX, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_CHALICE_1, RegionName.APEX_CENTAUR_ACCESS, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_CHALICE_2, RegionName.APEX_CENTAUR_ACCESS, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_CHALICE_3, RegionName.APEX_CENTAUR_ACCESS, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_GARG_1, RegionName.APEX, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_GARG_2, RegionName.APEX, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_GARG_3, RegionName.APEX, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.APEX_CANDLE_GARG_4, RegionName.APEX, LocationGroup.CANDLE, Area.APEX),
    LocationData(LocationName.CATA_CANDLE_1ST_ROOM, RegionName.CATA_START, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_ORB_MULTI, RegionName.CATA_MULTI, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_AFTER_BOW, RegionName.CATA_EYEBALL_BONES, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_DEV_ROOM, RegionName.CATA_SNAKE_MUSHROOMS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_GRIFFON, RegionName.CATA_DOUBLE_SWITCH, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_SHORTCUT, RegionName.CATA_VERTICAL_SHORTCUT, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_PRISON, RegionName.CATA_BOSS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_ABOVE_ROOTS_1, RegionName.CATA_ABOVE_ROOTS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_ABOVE_ROOTS_2, RegionName.CATA_ABOVE_ROOTS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_ABOVE_ROOTS_3, RegionName.CATA_ABOVE_ROOTS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_ABOVE_ROOTS_4, RegionName.CATA_ABOVE_ROOTS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_ABOVE_ROOTS_5, RegionName.CATA_ABOVE_ROOTS, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_VOID_R_1, RegionName.CATA_VOID_R, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.CATA_CANDLE_VOID_R_2, RegionName.CATA_VOID_R, LocationGroup.CANDLE, Area.CATA),
    LocationData(LocationName.TR_CANDLE_1ST_ROOM_1, RegionName.TR_START, LocationGroup.CANDLE, Area.TR),
    LocationData(LocationName.TR_CANDLE_1ST_ROOM_2, RegionName.TR_START, LocationGroup.CANDLE, Area.TR),
    LocationData(LocationName.TR_CANDLE_1ST_ROOM_3, RegionName.TR_START, LocationGroup.CANDLE, Area.TR),
    LocationData(LocationName.CD_CANDLE_1, RegionName.CD_START, LocationGroup.CANDLE, Area.CD),
    LocationData(LocationName.CD_CANDLE_CAMPFIRE_2_1, RegionName.CD_MIDDLE, LocationGroup.CANDLE, Area.CD),
    LocationData(LocationName.CD_CANDLE_CAMPFIRE_2_2, RegionName.CD_MIDDLE, LocationGroup.CANDLE, Area.CD),
    LocationData(LocationName.CD_CANDLE_TOP_CAMPFIRE, RegionName.CD_TOP, LocationGroup.CANDLE, Area.CD),
    LocationData(LocationName.CATH_CANDLE_TOP_1, RegionName.CATH_TOP, LocationGroup.CANDLE, Area.CATH),
    LocationData(LocationName.CATH_CANDLE_TOP_2, RegionName.CATH_TOP, LocationGroup.CANDLE, Area.CATH),
    LocationData(LocationName.GT_ELEVATOR_1, RegionName.GT_ENTRANCE, LocationGroup.ELEVATOR, Area.GT),
    LocationData(LocationName.MECH_SKULL_PUZZLE, RegionName.MECH_SPLIT_PATH, LocationGroup.SWITCH, Area.MECH),
    LocationData(LocationName.HOTP_SKULL_PUZZLE, RegionName.HOTP_TP_TUTORIAL, LocationGroup.SWITCH, Area.MECH),
)

location_table = {location.name.value: location for location in ALL_LOCATIONS}
location_name_to_id: dict[str, int] = {data.name.value: i for i, data in enumerate(ALL_LOCATIONS, start=BASE_ID)}


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
