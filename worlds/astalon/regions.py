from enum import Enum
from typing import Dict, Optional, Set


class Regions(str, Enum):
    MENU = "Menu"
    SHOP = "Shop"
    SHOP_ALGUS = "Shop - Algus"
    SHOP_ARIAS = "Shop - Arias"
    SHOP_KYULI = "Shop - Kyuli"
    SHOP_ZEEK = "Shop - Zeek"
    SHOP_BRAM = "Shop - Bram"
    FINAL_BOSS = "Final Boss"

    ENTRANCE = "Entrance"
    BESTIARY = "Bestiary"
    GT_BABY_GORGON = "Gorgon Tomb - Baby Gorgon"
    GT_BOTTOM = "Gorgon Tomb - Bottom"
    GT_VOID = "Gorgon Tomb - Void"
    GT_GORGONHEART = "Gorgon Tomb - Gorgonheart"
    GT_ORBS_DOOR = "Gorgon Tomb - Blue Door Orbs"
    GT_LEFT = "Gorgon Tomb - Left"
    GT_ORBS_HEIGHT = "Gorgon Tomb - Kyuli Orbs"
    GT_ASCENDANT_KEY = "Gorgon Tomb - Asendant Key"
    GT_TOP_LEFT = "Gorgon Tomb - Top Left"
    GT_TOP_RIGHT = "Gorgon Tomb - Top Right"
    GT_SPIKE_TUNNEL = "Gorgon Tomb - Spike Tunnel"
    GT_BUTT = "Gorgon Tomb - Butt"
    GT_BOSS = "Gorgon Tomb - Boss"
    GT_LADDER_SWITCH = "Gorgon Tomb - Ladder Switch"
    GT_UPPER_ARIAS = "Gorgon Tomb - Upper Arias"
    GT_OLD_MAN_FORK = "Gorgon Tomb - Old Man Fork"
    GT_OLD_MAN = "Gorgon Tomb - Old Man"
    GT_SWORD_FORK = "Gorgon Tomb - Sword Fork"
    GT_SWORD = "Gorgon Tomb - Sword of Mirrors"
    GT_ARIAS_SWORD_SWITCH = "Gorgon Tomb - Arias Sword Switch"
    GT_UPPER_PATH = "Gorgon Tomb - Upper Path"
    GT_UPPER_PATH_CONNECTION = "Gorgon Tomb - Upper Path Connection"

    MECH_START = "Mechanism - Start"
    MECH_SACRIFICE = "Mechanism - Sacrifice"
    MECH_LINUS = "Mechanism - Linus"
    MECH_SWORD_CONNECTION = "Mechanism - Sword Connection"
    MECH_LOWER_ARIAS = "Mechanism - Lower Arias"
    MECH_BOOTS_CONNECTION = "Mechanism - Boots Connection"
    MECH_BOOTS_LOWER = "Mechanism - Boots Lower"
    MECH_BOOTS_UPPER = "Mechanism - Boots Upper"
    MECH_BOTTOM_CAMPFIRE = "Mechanism - Bottom Campfire"
    MECH_SNAKE = "Mechanism - Snake"
    MECH_LOWER_VOID = "Mechanism - Lower Void"
    MECH_WATCHER = "Mechanism - Watcher"
    MECH_ROOTS = "Mechanism - Roots"
    MECH_MUSIC = "Mechanism - Music"
    MECH_BK = "Mechanism - BK"
    MECH_AFTER_BK = "Mechanism - After BK"
    MECH_CHAINS = "Mechanism - Chains"
    MECH_ARIAS_EYEBALL = "Mechanism - Arias Eyeball"
    MECH_TRIPLE_SWITCHES = "Mechanism - Triple Switches"
    MECH_ZEEK_CONNECTION = "Mechanism - Zeek Connection"
    MECH_ZEEK = "Mechanism - Zeek"
    MECH_SPLIT_PATH = "Mechanism - Split Path"
    MECH_RIGHT = "Mechanism - Right"
    MECH_OLD_MAN = "Mechanism - Old Man"
    MECH_UPPER_VOID = "Mechanism - Upper Void"
    MECH_POTS = "Mechanism - Pots"
    MECH_TOP = "Mechanism - Top"
    MECH_TP_CONNECTION = "Mechanism - Teleport Connection"
    MECH_CHARACTER_SWAPS = "Mechanism - Character Swaps"
    MECH_CLOAK_CONNECTION = "Mechanism - Cloak Connection"
    MECH_CLOAK = "Mechanism - Cloak"
    MECH_BOSS_SWITCHES = "Mechanism - Boss Switches"
    MECH_BOSS_CONNECTION = "Mechanism - Boss Connection"
    MECH_BRAM_TUNNEL = "Mechanism - Bram Tunnel"
    MECH_BOSS = "Mechanism - Boss"

    HOTP_START = "Hall of the Phantoms - Start"
    HOTP_START_MID = "Hall of the Phantoms - Start Mid"
    HOTP_LOWER_VOID = "Hall of the Phantoms - Lower Void"
    HOTP_START_LEFT = "Hall of the Phantoms - Start Left"
    HOTP_START_BOTTOM = "Hall of the Phantoms - Start Bottom"
    HOTP_LOWER = "Hall of the Phantoms - Lower"
    HOTP_EPIMETHEUS = "Hall of the Phantoms - Epimetheus"
    HOTP_MECH_VOID_CONNECTION = "Hall of the Phantoms - Mech Void Connection"
    HOTP_AMULET_CONNECTION = "Hall of the Phantoms - Amulet Connection"
    HOTP_AMULET = "Hall of the Phantoms - Amulet of Sol"
    HOTP_TP_TUTORIAL = "Hall of the Phantoms - Teleport Tutorial"
    HOTP_BELL_CAMPFIRE = "Hall of the Phantoms - Bell Campfire"
    HOTP_RED_KEY = "Hall of the Phantoms - Red Key"
    HOTP_BELL = "Hall of the Phantoms - Bell"
    HOTP_CATH_CONNECTION = "Hall of the Phantoms - Cathedral Connection"
    HOTP_LOWER_ARIAS = "Hall of the Phantoms - Lower Arias"
    HOTP_EYEBALL = "Hall of the Phantoms - Eyeball"
    HOTP_ELEVATOR = "Hall of the Phantoms - Elevator"
    HOTP_OLD_MAN = "Hall of the Phantoms - Old Man"
    HOTP_CLAW_LEFT = "Hall of the Phantoms - Claw Left"
    HOTP_TOP_LEFT = "Hall of the Phantoms - Top Left"
    HOTP_ABOVE_OLD_MAN = "Hall of the Phantoms - Above Old Man"
    HOTP_CLAW_CAMPFIRE = "Hall of the Phantoms - Claw Campfire"
    HOTP_CLAW = "Hall of the Phantoms - Griffon Claw"
    HOTP_HEART = "Hall of the Phantoms - Heart"
    HOTP_UPPER_ARIAS = "Hall of the Phantoms - Upper Arias"
    HOTP_BOSS_CAMPFIRE = "Hall of the Phantoms - Boss Campfire"
    HOTP_MAIDEN = "Hall of the Phantoms - Dead Maiden"
    HOTP_TP_PUZZLE = "Hall of the Phantoms - Teleport Puzzle"
    HOTP_TP_FALL_TOP = "Hall of the Phantoms - Teleport Fall Top"
    HOTP_GAUNTLET_CONNECTION = "Hall of the Phantoms - Gauntlet Connection"
    HOTP_GAUNTLET = "Hall of the Phantoms - Boreas Gauntlet"
    HOTP_FALL_BOTTOM = "Hall of the Phantoms - Teleport Fall Bottom"
    HOTP_UPPER_VOID = "Hall of the Phantoms - Upper Void"
    HOTP_BOSS = "Hall of the Phantoms - Boss"

    ROA_START = "Ruins of Ash - Start"
    ROA_WORMS = "Ruins of Ash - Worms"
    ROA_HEARTS = "Ruins of Ash - Hearts"
    ROA_SPIKE_CLIMB = "Ruins of Ash - Spike Climb"
    ROA_BOTTOM_ASCEND = "Ruins of Ash - Bottom of Ascend"
    ROA_TRIPLE_REAPER = "Ruins of Ash - Triple Reaper"
    ROA_ARENA = "Ruins of Ash - Arena"
    ROA_LOWER_VOID_CONNECTION = "Ruins of Ash - Lower Void Connection"
    ROA_LOWER_VOID = "Ruins of Ash - Lower Void"
    ROA_ARIAS_BABY_GORGON = "Ruins of Ash - Arias Baby Gorgon"
    ROA_FLAMES_CONNECTION = "Ruins of Ash - Flames Connection"
    ROA_FLAMES = "Ruins of Ash - Flames"
    ROA_WORM_CLIMB = "Ruins of Ash - Worm Climb"
    ROA_RIGHT_BRANCH = "Ruins of Ash - Right Branch"
    ROA_LEFT_ASCENT = "Ruins of Ash - Left of Ascent"
    ROA_LEFT_ASCENT_CRYSTAL = "Ruins of Ash - Left of Ascent Crystal"
    ROA_TOP_ASCENT = "Ruins of Ash - Top of Ascent"
    ROA_TRIPLE_SWITCH = "Ruins of Ash - Triple Switch"
    ROA_MIDDLE = "Ruins of Ash - Middle"
    ROA_LEFT_BABY_GORGON = "Ruins of Ash - Left Baby Gorgon"
    ROA_LEFT_SWITCH = "Ruins of Ash - Left Switch"
    ROA_RIGHT_SWITCH_1 = "Ruins of Ash - Right Switch 1"
    ROA_RIGHT_SWITCH_2 = "Ruins of Ash - Right Switch 2"
    ROA_MIDDLE_LADDER = "Ruins of Ash - Middle Ladder"
    ROA_UPPER_VOID = "Ruins of Ash - Upper Void"
    ROA_SPIKE_BALLS = "Ruins of Ash - Spike Balls"
    ROA_SPIKE_SPINNERS = "Ruins of Ash - Spike Spinners"
    ROA_SPIDERS_1 = "Ruins of Ash - Spiders 1"
    ROA_RED_KEY = "Ruins of Ash - Red Key"
    ROA_SPIDERS_2 = "Ruins of Ash - Spiders 2"
    ROA_BLOOD_POT_HALLWAY = "Ruins of Ash - Blood Pot Hallway"
    ROA_SP_CONNECTION = "Ruins of Ash - Serpent Path Connection"
    ROA_ELEVATOR = "Ruins of Ash - Elevator"
    ROA_ICARUS = "Ruins of Ash - Icarus Emblem"
    ROA_DARK_CONNECTION = "Ruins of Ash - Darkness Connection"
    ROA_CENTAUR = "Ruins of Ash - Centaur"
    ROA_BOSS_CONNECTION = "Ruins of Ash - Boss Connection"
    ROA_BOSS = "Ruins of Ash - Boss"
    ROA_APEX_CONNECTION = "Ruins of Ash - The Apex Connection"

    DARK_START = "Darkness - Start"
    DARK_END = "Darkness - End"

    APEX = "The Apex"
    APEX_CENTAUR = "The Apex - Centaur"
    APEX_HEART = "The Apex - Heart"

    CAVES_START = "Caves - Start"
    CAVES_EPIMETHEUS = "Caves - Epimetheus"
    CAVES_UPPER = "Caves - Upper"
    CAVES_ARENA = "Caves - Arena"
    CAVES_LOWER = "Caves - Lower"
    CAVES_ITEM_CHAIN = "Caves - Item Chain"

    CATA_START = "Catacombs - Start"
    CATA_CLIMBABLE_ROOT = "Catacombs - Climbable Root"
    CATA_TOP = "Catacombs - Top"
    CATA_ELEVATOR = "Catacombs - Elevator"
    CATA_BOW_CAMPFIRE = "Catacombs - Bow Campfire"
    CATA_BOW_CONNECTION = "Catacombs - Bow Connection"
    CATA_BOW = "Catacombs - Bow"
    CATA_VERTICAL_SHORTCUT = "Catacombs - Vertical Shortcut"
    CATA_EYEBALL_BONES = "Catacombs - Eyeball Bones"
    CATA_SNAKE_MUSHROOMS = "Catacombs - Snake Mushrooms"
    CATA_DEV_ROOM_CONNECTION = "Catacombs - Dev Room Connection"
    CATA_DEV_ROOM = "Catacombs - Dev Room"
    CATA_DOUBLE_SWITCH = "Catacombs - Double Switch"
    CATA_ROOTS_CAMPFIRE = "Catacombs - Roots Campfire"
    CATA_POISON_ROOTS = "Catacombs - Poison Roots"
    CATA_BLUE_EYE_DOOR = "Catacombs - Blue Eye Door"
    CATA_FLAMES_FORK = "Catacombs - Flames Fork"
    CATA_FLAMES = "Catacombs - Flames"
    CATA_CENTAUR = "Catacombs - Centaur"
    CATA_4_FACES = "Catacombs - 4 Faces"
    CATA_DOUBLE_DOOR = "Catacombs - Double Door"
    CATA_VOID_R = "Catacombs - Void Right"
    CATA_VOID_L = "Catacombs - Void Left"
    CATA_BOSS = "Catacombs - Boss"

    TR_START = "Tower Roots - Start"
    TR_BRAM = "Tower Roots - Bram"
    TR_LEFT = "Tower Roots - Left"
    TR_BOTTOM_LEFT = "Tower Roots - Bottom Left"
    TR_TOP_RIGHT = "Tower Roots - Top Right"
    TR_GOLD = "Tower Roots - Gold"
    TR_MIDDLE_RIGHT = "Tower Roots - Middle Right"
    TD_DARK_ARIAS = "Tower Roots - Dark Arias"
    TR_BOTTOM = "Tower Roots - Bottom"

    CD_START = "Cyclops Den - Start"
    CD_2 = "Cyclops Den - 2"
    CD_3 = "Cyclops Den - 3"
    CD_MIDDLE = "Cyclops Den - Middle"
    CD_ARIAS_ROUTE = "Cyclops Den - Arias Route"
    CD_KYULI_ROUTE = "Cyclops Den - Kyuli Route"
    CD_CAMPFIRE_3 = "Cyclops Den - Campfire 3"
    CD_ARENA = "Cyclops Den - Arena"
    CD_STEPS = "Cyclops Den - Steps"
    CD_TOP = "Cyclops Den - Top"
    CD_BOSS = "Cyclops Den - Boss"

    CATH_START = "Cathedral - Start"
    CATH_START_RIGHT = "Cathedral - Start Right"
    CATH_START_TOP_LEFT = "Cathedral - Start Top Left"
    CATH_START_LEFT = "Cathedral - Start Left"
    CATH_TP = "Cathedral - Teleport"
    CATH_LEFT_SHAFT = "Cathedral - Left Shaft"
    CATH_UNDER_CAMPFIRE = "Cathedral - Under Campfire"
    CATH_CAMPFIRE_1 = "Cathedral - Campfire 1"
    CATH_SHAFT_ACCESS = "Cathedral - Shaft Access"
    CATH_ORB_ROOM = "Cathedral - Orb Room"
    CATH_GOLD_BLOCK = "Cathedral - Gold Block"
    CATH_RIGHT_SHAFT_CONNECTION = "Cathedral - Right Shaft Connection"
    CATH_RIGHT_SHAFT = "Cathedral - Right Shaft"
    CATH_TOP = "Cathedral - Top"
    CATH_CAMPFIRE_2 = "Cathedral - Campfire 2"
    CATH_UPPER_SPIKE_PIT = "Cathedral - Upper Spike Pit"

    SP_START = "Serpent Path - Start"
    SP_CAMPFIRE_1 = "Serpent Path - Campfire 1"
    SP_HEARTS = "Serpent Path - Hearts"
    SP_PAINTING = "Serpent Path - Painting"
    SP_SHAFT = "Serpent Path - Shaft"
    SP_STAR = "Serpent Path - Star"
    SP_STAR_CONNECTION = "Serpent Path - Star Connection"
    SP_STAR_END = "Serpent Path - Star End"
    SP_ORBS = "Serpent Path - Orbs"
    SP_FROG = "Serpent Path - Frog"
    SP_CAMPFIRE_2 = "Serpent Path - Campfire 2"


astalon_regions: Dict[Regions, Optional[Set[Regions]]] = {
    Regions.MENU: {
        Regions.ENTRANCE,
        Regions.SHOP,
    },
    Regions.SHOP: {
        Regions.SHOP_ALGUS,
        Regions.SHOP_ARIAS,
        Regions.SHOP_KYULI,
        Regions.SHOP_ZEEK,
        Regions.SHOP_BRAM,
    },
    Regions.SHOP_ALGUS: None,
    Regions.SHOP_ARIAS: None,
    Regions.SHOP_KYULI: None,
    Regions.SHOP_ZEEK: None,
    Regions.SHOP_BRAM: None,
    Regions.FINAL_BOSS: None,
    Regions.ENTRANCE: {
        Regions.BESTIARY,
        Regions.GT_BABY_GORGON,
        Regions.GT_BOTTOM,
        Regions.GT_VOID,
        Regions.GT_GORGONHEART,
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.BESTIARY: None,
    Regions.GT_BABY_GORGON: None,
    Regions.GT_BOTTOM: {
        Regions.GT_VOID,
        Regions.GT_GORGONHEART,
        Regions.GT_UPPER_PATH,
        Regions.CAVES_START,
    },
    Regions.GT_VOID: {
        Regions.GT_BOTTOM,
        Regions.MECH_SNAKE,
    },
    Regions.GT_GORGONHEART: {
        Regions.GT_BOTTOM,
        Regions.GT_ORBS_DOOR,
        Regions.GT_LEFT,
    },
    Regions.GT_ORBS_DOOR: None,
    Regions.GT_LEFT: {
        Regions.GT_GORGONHEART,
        Regions.GT_ORBS_HEIGHT,
        Regions.GT_ASCENDANT_KEY,
        Regions.GT_TOP_LEFT,
        Regions.GT_TOP_RIGHT,
    },
    Regions.GT_ORBS_HEIGHT: None,
    Regions.GT_ASCENDANT_KEY: None,
    Regions.GT_TOP_LEFT: {
        Regions.GT_LEFT,
        Regions.GT_BUTT,
    },
    Regions.GT_TOP_RIGHT: {
        Regions.GT_LEFT,
        Regions.GT_SPIKE_TUNNEL,
    },
    Regions.GT_SPIKE_TUNNEL: {
        Regions.GT_TOP_RIGHT,
        Regions.GT_BUTT,
    },
    Regions.GT_BUTT: {
        Regions.GT_TOP_LEFT,
        Regions.GT_SPIKE_TUNNEL,
        Regions.GT_BOSS,
    },
    Regions.GT_BOSS: {
        Regions.GT_BUTT,
        Regions.MECH_START,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.GT_LADDER_SWITCH: None,
    Regions.GT_UPPER_ARIAS: {
        Regions.GT_OLD_MAN_FORK,
        Regions.MECH_SWORD_CONNECTION,
    },
    Regions.GT_OLD_MAN_FORK: {
        Regions.GT_UPPER_ARIAS,
        Regions.GT_OLD_MAN,
        Regions.GT_SWORD_FORK,
    },
    Regions.GT_OLD_MAN: None,
    Regions.GT_SWORD_FORK: {
        Regions.GT_SWORD,
        Regions.GT_ARIAS_SWORD_SWITCH,
    },
    Regions.GT_SWORD: None,
    Regions.GT_ARIAS_SWORD_SWITCH: None,
    Regions.GT_UPPER_PATH: {
        Regions.GT_BOTTOM,
        Regions.GT_UPPER_PATH_CONNECTION,
    },
    Regions.GT_UPPER_PATH_CONNECTION: {
        Regions.GT_UPPER_PATH,
        Regions.MECH_SWORD_CONNECTION,
        Regions.MECH_BOTTOM_CAMPFIRE,
    },
    Regions.MECH_START: {
        Regions.GT_BOSS,
        Regions.GT_LADDER_SWITCH,
        Regions.MECH_SACRIFICE,
        Regions.MECH_LINUS,
        Regions.MECH_LOWER_VOID,
        Regions.MECH_BK,
        Regions.MECH_WATCHER,
    },
    Regions.MECH_SACRIFICE: None,
    Regions.MECH_LINUS: {
        Regions.MECH_START,
        Regions.MECH_SWORD_CONNECTION,
    },
    Regions.MECH_SWORD_CONNECTION: {
        Regions.GT_UPPER_ARIAS,
        Regions.GT_UPPER_PATH_CONNECTION,
        Regions.MECH_LINUS,
        Regions.MECH_LOWER_ARIAS,
        Regions.MECH_BOOTS_CONNECTION,
        Regions.MECH_BOTTOM_CAMPFIRE,
    },
    Regions.MECH_LOWER_ARIAS: None,
    Regions.MECH_BOOTS_CONNECTION: {
        Regions.MECH_SWORD_CONNECTION,
        Regions.MECH_BOOTS_LOWER,
        Regions.MECH_BOTTOM_CAMPFIRE,
    },
    Regions.MECH_BOOTS_LOWER: {
        Regions.MECH_BOOTS_UPPER,
    },
    Regions.MECH_BOOTS_UPPER: None,
    Regions.MECH_BOTTOM_CAMPFIRE: {
        Regions.GT_UPPER_PATH_CONNECTION,
        Regions.MECH_SWORD_CONNECTION,
        Regions.MECH_BOOTS_CONNECTION,
        Regions.MECH_SNAKE,
    },
    Regions.MECH_SNAKE: {
        Regions.GT_VOID,
        Regions.MECH_BOTTOM_CAMPFIRE,
    },
    Regions.MECH_LOWER_VOID: {
        Regions.MECH_START,
        Regions.MECH_UPPER_VOID,
        Regions.HOTP_MECH_VOID_CONNECTION,
    },
    Regions.MECH_WATCHER: {
        Regions.MECH_START,
        Regions.MECH_ROOTS,
    },
    Regions.MECH_ROOTS: {
        Regions.MECH_WATCHER,
        Regions.MECH_MUSIC,
        Regions.MECH_BK,
        Regions.MECH_ZEEK_CONNECTION,
    },
    Regions.MECH_MUSIC: None,
    Regions.MECH_BK: {
        Regions.MECH_START,
        Regions.MECH_ROOTS,
        Regions.MECH_AFTER_BK,
        Regions.MECH_TRIPLE_SWITCHES,
    },
    Regions.MECH_AFTER_BK: {
        Regions.MECH_BK,
        Regions.MECH_CHAINS,
        Regions.HOTP_EPIMETHEUS,
    },
    Regions.MECH_CHAINS: {
        Regions.MECH_AFTER_BK,
        Regions.MECH_ARIAS_EYEBALL,
        Regions.MECH_SPLIT_PATH,
        Regions.MECH_BOSS_SWITCHES,
        Regions.MECH_BOSS_CONNECTION,
    },
    Regions.MECH_ARIAS_EYEBALL: {
        Regions.MECH_CHAINS,
        Regions.MECH_TRIPLE_SWITCHES,
        Regions.MECH_ZEEK_CONNECTION,
    },
    Regions.MECH_TRIPLE_SWITCHES: None,
    Regions.MECH_ZEEK_CONNECTION: {
        Regions.GT_BOSS,
        Regions.MECH_ROOTS,
        Regions.MECH_ARIAS_EYEBALL,
        Regions.MECH_ZEEK,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.MECH_ZEEK: None,
    Regions.MECH_SPLIT_PATH: {
        Regions.MECH_CHAINS,
        Regions.MECH_RIGHT,
    },
    Regions.MECH_RIGHT: {
        Regions.MECH_SPLIT_PATH,
        Regions.MECH_OLD_MAN,
        Regions.MECH_UPPER_VOID,
        Regions.MECH_POTS,
    },
    Regions.MECH_OLD_MAN: None,
    Regions.MECH_UPPER_VOID: {
        Regions.MECH_LOWER_VOID,
        Regions.MECH_RIGHT,
    },
    Regions.MECH_POTS: {
        Regions.MECH_RIGHT,
        Regions.MECH_TOP,
    },
    Regions.MECH_TOP: {
        Regions.MECH_TRIPLE_SWITCHES,
        Regions.MECH_POTS,
        Regions.MECH_TP_CONNECTION,
        Regions.CD_START,
    },
    Regions.MECH_TP_CONNECTION: {
        Regions.MECH_TOP,
        Regions.MECH_CHARACTER_SWAPS,
        Regions.HOTP_FALL_BOTTOM,
    },
    Regions.MECH_CHARACTER_SWAPS: {
        Regions.MECH_TP_CONNECTION,
        Regions.MECH_CLOAK_CONNECTION,
    },
    Regions.MECH_CLOAK_CONNECTION: {
        Regions.MECH_CHARACTER_SWAPS,
        Regions.MECH_CLOAK,
        Regions.MECH_BOSS_SWITCHES,
    },
    Regions.MECH_CLOAK: None,
    Regions.MECH_BOSS_SWITCHES: {
        Regions.MECH_CHAINS,
        Regions.MECH_CLOAK_CONNECTION,
        Regions.MECH_BOSS_CONNECTION,
    },
    Regions.MECH_BOSS_CONNECTION: {
        Regions.MECH_CHAINS,
        Regions.MECH_BRAM_TUNNEL,
        Regions.MECH_BOSS,
    },
    Regions.MECH_BRAM_TUNNEL: {
        Regions.MECH_BOSS_CONNECTION,
        Regions.HOTP_START_BOTTOM,
    },
    Regions.MECH_BOSS: {
        Regions.GT_BOSS,
        Regions.MECH_TRIPLE_SWITCHES,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS_CONNECTION,
        Regions.HOTP_START,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.HOTP_START: {
        Regions.MECH_BOSS,
        Regions.HOTP_START_MID,
        Regions.HOTP_START_BOTTOM,
    },
    Regions.HOTP_START_MID: {
        Regions.HOTP_START,
        Regions.HOTP_LOWER_VOID,
        Regions.HOTP_START_LEFT,
        Regions.HOTP_START_BOTTOM,
    },
    Regions.HOTP_LOWER_VOID: {
        Regions.HOTP_START_MID,
        Regions.HOTP_UPPER_VOID,
    },
    Regions.HOTP_START_LEFT: {
        Regions.HOTP_START_MID,
        Regions.HOTP_ELEVATOR,
    },
    Regions.HOTP_START_BOTTOM: {
        Regions.MECH_BRAM_TUNNEL,
        Regions.HOTP_START,
        Regions.HOTP_LOWER,
    },
    Regions.HOTP_LOWER: {
        Regions.HOTP_START_BOTTOM,
        Regions.HOTP_EPIMETHEUS,
        Regions.HOTP_MECH_VOID_CONNECTION,
        Regions.HOTP_TP_TUTORIAL,
    },
    Regions.HOTP_EPIMETHEUS: {
        Regions.MECH_AFTER_BK,
        Regions.HOTP_LOWER,
    },
    Regions.HOTP_MECH_VOID_CONNECTION: {
        Regions.MECH_LOWER_VOID,
        Regions.HOTP_LOWER,
        Regions.HOTP_AMULET_CONNECTION,
    },
    Regions.HOTP_AMULET_CONNECTION: {
        Regions.GT_BUTT,
        Regions.HOTP_MECH_VOID_CONNECTION,
        Regions.HOTP_AMULET,
    },
    Regions.HOTP_AMULET: None,
    Regions.HOTP_TP_TUTORIAL: {
        Regions.HOTP_LOWER,
        Regions.HOTP_BELL_CAMPFIRE,
    },
    Regions.HOTP_BELL_CAMPFIRE: {
        Regions.HOTP_TP_TUTORIAL,
        Regions.HOTP_RED_KEY,
        Regions.HOTP_BELL,
        Regions.HOTP_CATH_CONNECTION,
        Regions.HOTP_LOWER_ARIAS,
    },
    Regions.HOTP_RED_KEY: None,
    Regions.HOTP_BELL: None,
    Regions.HOTP_CATH_CONNECTION: {
        Regions.HOTP_BELL,
        Regions.CATH_START,
    },
    Regions.HOTP_LOWER_ARIAS: {
        Regions.HOTP_BELL_CAMPFIRE,
        Regions.HOTP_EYEBALL,
    },
    Regions.HOTP_EYEBALL: {
        Regions.HOTP_LOWER_ARIAS,
        Regions.HOTP_ELEVATOR,
    },
    Regions.HOTP_ELEVATOR: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_START_LEFT,
        Regions.HOTP_EYEBALL,
        Regions.HOTP_OLD_MAN,
        Regions.HOTP_CLAW_LEFT,
        Regions.HOTP_TOP_LEFT,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.HOTP_OLD_MAN: None,
    Regions.HOTP_CLAW_LEFT: {
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_TOP_LEFT,
        Regions.HOTP_CLAW,
    },
    Regions.HOTP_TOP_LEFT: {
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_CLAW_LEFT,
        Regions.HOTP_ABOVE_OLD_MAN,
        Regions.HOTP_CLAW_CAMPFIRE,
    },
    Regions.HOTP_ABOVE_OLD_MAN: None,
    Regions.HOTP_CLAW_CAMPFIRE: {
        Regions.HOTP_TOP_LEFT,
        Regions.HOTP_CLAW,
        Regions.HOTP_HEART,
    },
    Regions.HOTP_CLAW: {
        Regions.HOTP_CLAW_LEFT,
        Regions.HOTP_CLAW_CAMPFIRE,
    },
    Regions.HOTP_HEART: {
        Regions.HOTP_CLAW_CAMPFIRE,
        Regions.HOTP_UPPER_ARIAS,
        Regions.HOTP_BOSS_CAMPFIRE,
    },
    Regions.HOTP_UPPER_ARIAS: {
        Regions.HOTP_HEART,
        Regions.HOTP_BOSS_CAMPFIRE,
    },
    Regions.HOTP_BOSS_CAMPFIRE: {
        Regions.MECH_TRIPLE_SWITCHES,
        Regions.HOTP_HEART,
        Regions.HOTP_MAIDEN,
        Regions.HOTP_TP_PUZZLE,
        Regions.HOTP_BOSS,
    },
    Regions.HOTP_MAIDEN: None,  # may need to break this up
    Regions.HOTP_TP_PUZZLE: {
        Regions.HOTP_TP_FALL_TOP,
    },
    Regions.HOTP_TP_FALL_TOP: {
        Regions.HOTP_BOSS_CAMPFIRE,
        Regions.HOTP_TP_PUZZLE,
        Regions.HOTP_GAUNTLET_CONNECTION,
        Regions.HOTP_FALL_BOTTOM,
    },
    Regions.HOTP_GAUNTLET_CONNECTION: {
        Regions.HOTP_GAUNTLET,
    },
    Regions.HOTP_GAUNTLET: None,
    Regions.HOTP_FALL_BOTTOM: {
        Regions.MECH_TP_CONNECTION,
        Regions.HOTP_TP_FALL_TOP,
        Regions.HOTP_UPPER_VOID,
    },
    Regions.HOTP_UPPER_VOID: {
        Regions.HOTP_LOWER_VOID,
        Regions.HOTP_TP_FALL_TOP,
        Regions.HOTP_FALL_BOTTOM,
    },
    Regions.HOTP_BOSS: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS_CAMPFIRE,
        Regions.ROA_START,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.ROA_START: {
        Regions.HOTP_BOSS,
        Regions.ROA_WORMS,
    },
    Regions.ROA_WORMS: {
        Regions.ROA_START,
        Regions.ROA_HEARTS,
        Regions.ROA_LOWER_VOID_CONNECTION,
    },
    Regions.ROA_HEARTS: {
        Regions.ROA_WORMS,
        Regions.ROA_SPIKE_CLIMB,
        Regions.ROA_BOTTOM_ASCEND,
    },
    Regions.ROA_SPIKE_CLIMB: {
        Regions.ROA_HEARTS,
        Regions.ROA_BOTTOM_ASCEND,
    },
    Regions.ROA_BOTTOM_ASCEND: {
        Regions.ROA_HEARTS,
        Regions.ROA_SPIKE_CLIMB,
        Regions.ROA_TRIPLE_REAPER,
        Regions.ROA_TOP_ASCENT,
    },
    Regions.ROA_TRIPLE_REAPER: {
        Regions.ROA_BOTTOM_ASCEND,
        Regions.ROA_ARENA,
    },
    Regions.ROA_ARENA: {
        Regions.ROA_TRIPLE_REAPER,
        Regions.ROA_LOWER_VOID_CONNECTION,
        Regions.ROA_FLAMES_CONNECTION,
    },
    Regions.ROA_LOWER_VOID_CONNECTION: {
        Regions.ROA_WORMS,
        Regions.ROA_ARENA,
        Regions.ROA_LOWER_VOID,
        Regions.ROA_ARIAS_BABY_GORGON,
        Regions.ROA_FLAMES_CONNECTION,
    },
    Regions.ROA_LOWER_VOID: {
        Regions.ROA_LOWER_VOID_CONNECTION,
        Regions.ROA_UPPER_VOID,
    },
    Regions.ROA_ARIAS_BABY_GORGON: {
        Regions.ROA_LOWER_VOID_CONNECTION,
        Regions.ROA_FLAMES_CONNECTION,
        Regions.ROA_FLAMES,
    },
    Regions.ROA_FLAMES_CONNECTION: {
        Regions.ROA_ARENA,
        Regions.ROA_LOWER_VOID_CONNECTION,
        Regions.ROA_ARIAS_BABY_GORGON,
        Regions.ROA_FLAMES,
        Regions.ROA_WORM_CLIMB,
        Regions.ROA_LEFT_ASCENT,
        Regions.ROA_LEFT_ASCENT_CRYSTAL,
    },
    Regions.ROA_FLAMES: {
        Regions.ROA_ARIAS_BABY_GORGON,
    },
    Regions.ROA_WORM_CLIMB: {
        Regions.ROA_FLAMES_CONNECTION,
        Regions.ROA_RIGHT_BRANCH,
    },
    Regions.ROA_RIGHT_BRANCH: {
        Regions.ROA_WORM_CLIMB,
        Regions.ROA_MIDDLE,
    },
    Regions.ROA_LEFT_ASCENT: {
        Regions.ROA_FLAMES_CONNECTION,
        Regions.ROA_LEFT_ASCENT_CRYSTAL,
        Regions.ROA_TOP_ASCENT,
    },
    Regions.ROA_LEFT_ASCENT_CRYSTAL: None,
    Regions.ROA_TOP_ASCENT: {
        Regions.ROA_LEFT_ASCENT,
        Regions.ROA_TRIPLE_SWITCH,
    },
    Regions.ROA_TRIPLE_SWITCH: {
        Regions.ROA_TOP_ASCENT,
        Regions.ROA_MIDDLE,
    },
    Regions.ROA_MIDDLE: {
        Regions.ROA_RIGHT_BRANCH,
        Regions.ROA_TRIPLE_SWITCH,
        Regions.ROA_LEFT_BABY_GORGON,
        Regions.ROA_LEFT_SWITCH,
        Regions.ROA_RIGHT_SWITCH_1,
        Regions.ROA_MIDDLE_LADDER,
    },
    Regions.ROA_LEFT_BABY_GORGON: None,
    Regions.ROA_LEFT_SWITCH: None,
    Regions.ROA_RIGHT_SWITCH_1: {
        Regions.ROA_RIGHT_SWITCH_2,
    },
    Regions.ROA_RIGHT_SWITCH_2: None,
    Regions.ROA_MIDDLE_LADDER: {
        Regions.ROA_MIDDLE,
        Regions.ROA_UPPER_VOID,
    },
    Regions.ROA_UPPER_VOID: {
        Regions.ROA_LOWER_VOID,
        Regions.ROA_MIDDLE_LADDER,
        Regions.ROA_SPIKE_BALLS,
        Regions.ROA_SP_CONNECTION,
    },
    Regions.ROA_SPIKE_BALLS: {
        Regions.ROA_UPPER_VOID,
        Regions.ROA_SPIKE_SPINNERS,
    },
    Regions.ROA_SPIKE_SPINNERS: {
        Regions.ROA_SPIKE_BALLS,
        Regions.ROA_SPIDERS_1,
    },
    Regions.ROA_SPIDERS_1: {
        Regions.ROA_SPIKE_SPINNERS,
        Regions.ROA_RED_KEY,
        Regions.ROA_SPIDERS_2,
    },
    Regions.ROA_RED_KEY: None,
    Regions.ROA_SPIDERS_2: {
        Regions.ROA_SPIDERS_1,
        Regions.ROA_BLOOD_POT_HALLWAY,
    },
    Regions.ROA_BLOOD_POT_HALLWAY: {
        Regions.ROA_SPIDERS_2,
        Regions.ROA_SP_CONNECTION,
    },
    Regions.ROA_SP_CONNECTION: {
        Regions.ROA_UPPER_VOID,
        Regions.ROA_BLOOD_POT_HALLWAY,
        Regions.ROA_ELEVATOR,
        Regions.SP_START,
    },
    Regions.ROA_ELEVATOR: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_SP_CONNECTION,
        Regions.ROA_ICARUS,
        Regions.ROA_DARK_CONNECTION,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.ROA_ICARUS: None,
    Regions.ROA_DARK_CONNECTION: {
        Regions.ROA_ELEVATOR,
        Regions.DARK_START,
        Regions.ROA_CENTAUR,
    },
    Regions.DARK_START: {
        Regions.DARK_END,
    },
    Regions.DARK_END: {
        Regions.ROA_CENTAUR,
    },
    Regions.ROA_CENTAUR: {
        Regions.ROA_DARK_CONNECTION,
        Regions.ROA_BOSS_CONNECTION,
    },
    Regions.ROA_BOSS_CONNECTION: {
        Regions.ROA_CENTAUR,
        Regions.ROA_BOSS,
    },
    Regions.ROA_BOSS: {
        Regions.ROA_BOSS_CONNECTION,
        Regions.ROA_APEX_CONNECTION,
    },
    Regions.ROA_APEX_CONNECTION: {
        Regions.ROA_BOSS,
        Regions.APEX,
    },
    Regions.APEX: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.FINAL_BOSS,
        Regions.ROA_APEX_CONNECTION,
        Regions.APEX_CENTAUR,
        Regions.APEX_HEART,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.APEX_CENTAUR: None,
    Regions.APEX_HEART: None,
    Regions.CAVES_START: {
        Regions.GT_BOTTOM,
        Regions.CAVES_EPIMETHEUS,
    },
    Regions.CAVES_EPIMETHEUS: {
        Regions.CAVES_START,
        Regions.CAVES_UPPER,
    },
    Regions.CAVES_UPPER: {
        Regions.CAVES_EPIMETHEUS,
        Regions.CAVES_ARENA,
        Regions.CAVES_LOWER,
    },
    Regions.CAVES_ARENA: None,
    Regions.CAVES_LOWER: {
        Regions.CAVES_UPPER,
        Regions.CAVES_ITEM_CHAIN,
        Regions.CATA_START,
    },
    Regions.CAVES_ITEM_CHAIN: None,
    Regions.CATA_START: {
        Regions.CAVES_LOWER,
        Regions.CATA_CLIMBABLE_ROOT,
    },
    Regions.CATA_CLIMBABLE_ROOT: {
        Regions.CATA_TOP,
    },
    Regions.CATA_TOP: {
        Regions.CATA_CLIMBABLE_ROOT,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOW_CAMPFIRE,
    },
    Regions.CATA_ELEVATOR: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_TOP,
        Regions.CATA_BOSS,
        Regions.TR_START,
    },
    Regions.CATA_BOW_CAMPFIRE: {
        Regions.CATA_TOP,
        Regions.CATA_BOW_CONNECTION,
        Regions.CATA_EYEBALL_BONES,
    },
    Regions.CATA_BOW_CONNECTION: {
        Regions.CATA_BOW_CAMPFIRE,
        Regions.CATA_BOW,
        Regions.CATA_VERTICAL_SHORTCUT,
    },
    Regions.CATA_BOW: None,
    Regions.CATA_VERTICAL_SHORTCUT: {
        Regions.CATA_BOW_CONNECTION,
        Regions.CATA_BLUE_EYE_DOOR,
        Regions.CATA_FLAMES_FORK,
    },
    Regions.CATA_EYEBALL_BONES: {
        Regions.CATA_BOW_CAMPFIRE,
        Regions.CATA_SNAKE_MUSHROOMS,
    },
    Regions.CATA_SNAKE_MUSHROOMS: {
        Regions.CATA_EYEBALL_BONES,
        Regions.CATA_DEV_ROOM_CONNECTION,
        Regions.CATA_DOUBLE_SWITCH,
    },
    Regions.CATA_DEV_ROOM_CONNECTION: {
        Regions.CATA_DEV_ROOM,
    },
    Regions.CATA_DEV_ROOM: None,
    Regions.CATA_DOUBLE_SWITCH: {
        Regions.CATA_SNAKE_MUSHROOMS,
        Regions.CATA_ROOTS_CAMPFIRE,
    },
    Regions.CATA_ROOTS_CAMPFIRE: {
        Regions.CATA_DOUBLE_SWITCH,
        Regions.CATA_POISON_ROOTS,
        Regions.CATA_BLUE_EYE_DOOR,
    },
    Regions.CATA_POISON_ROOTS: None,
    Regions.CATA_BLUE_EYE_DOOR: {
        Regions.CATA_ROOTS_CAMPFIRE,
        Regions.CATA_FLAMES_FORK,
    },
    Regions.CATA_FLAMES_FORK: {
        Regions.CATA_VERTICAL_SHORTCUT,
        Regions.CATA_BLUE_EYE_DOOR,
        Regions.CATA_FLAMES,
        Regions.CATA_CENTAUR,
    },
    Regions.CATA_FLAMES: None,
    Regions.CATA_CENTAUR: {
        Regions.CATA_FLAMES_FORK,
        Regions.CATA_4_FACES,
        Regions.CATA_BOSS,
    },
    Regions.CATA_4_FACES: {
        Regions.CATA_CENTAUR,
        Regions.CATA_DOUBLE_DOOR,
    },
    Regions.CATA_DOUBLE_DOOR: {
        Regions.CATA_4_FACES,
        Regions.CATA_VOID_R,
    },
    Regions.CATA_VOID_R: {
        Regions.CATA_DOUBLE_DOOR,
        Regions.CATA_VOID_L,
    },
    Regions.CATA_VOID_L: {
        Regions.CATA_VOID_R,
        Regions.CATA_BOSS,
    },
    Regions.CATA_BOSS: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_CENTAUR,
        Regions.CATA_VOID_L,
        Regions.TR_START,
        Regions.TR_START,
    },
    Regions.TR_START: {
        Regions.GT_BOSS,
        Regions.MECH_ZEEK_CONNECTION,
        Regions.MECH_BOSS,
        Regions.HOTP_ELEVATOR,
        Regions.HOTP_BOSS,
        Regions.ROA_ELEVATOR,
        Regions.APEX,
        Regions.CATA_ELEVATOR,
        Regions.CATA_BOSS,
        Regions.CATA_BOSS,
        Regions.TR_BRAM,
        Regions.TR_LEFT,
    },
    Regions.TR_BRAM: None,
    Regions.TR_LEFT: {
        Regions.TR_BOTTOM_LEFT,
        Regions.TR_TOP_RIGHT,
    },
    Regions.TR_BOTTOM_LEFT: {
        Regions.TR_BOTTOM,
    },
    Regions.TR_TOP_RIGHT: {
        Regions.TR_GOLD,
        Regions.TR_MIDDLE_RIGHT,
    },
    Regions.TR_GOLD: None,
    Regions.TR_MIDDLE_RIGHT: {
        Regions.TD_DARK_ARIAS,
        Regions.TR_BOTTOM,
    },
    Regions.TD_DARK_ARIAS: None,
    Regions.TR_BOTTOM: {
        Regions.TR_BOTTOM_LEFT,
    },
    Regions.CD_START: {
        Regions.CD_2,
        Regions.CD_BOSS,
    },
    Regions.CD_2: {
        Regions.CD_3,
    },
    Regions.CD_3: {
        Regions.CD_MIDDLE,
    },
    Regions.CD_MIDDLE: {
        Regions.CD_ARIAS_ROUTE,
        Regions.CD_KYULI_ROUTE,
    },
    Regions.CD_ARIAS_ROUTE: None,
    Regions.CD_KYULI_ROUTE: {
        Regions.CD_CAMPFIRE_3,
    },
    Regions.CD_CAMPFIRE_3: {
        Regions.CD_ARENA,
    },
    Regions.CD_ARENA: {
        Regions.CD_STEPS,
    },
    Regions.CD_STEPS: {
        Regions.CD_TOP,
    },
    Regions.CD_TOP: None,
    Regions.CD_BOSS: None,
    Regions.CATH_START: {
        Regions.CATH_START_RIGHT,
        Regions.CATH_START_LEFT,
    },
    Regions.CATH_START_RIGHT: {
        Regions.CATH_START_TOP_LEFT,
    },
    Regions.CATH_START_TOP_LEFT: {
        Regions.CATH_START_LEFT,
    },
    Regions.CATH_START_LEFT: {
        Regions.CATH_TP,
    },
    Regions.CATH_TP: {
        Regions.CATH_LEFT_SHAFT,
    },
    Regions.CATH_LEFT_SHAFT: {
        Regions.CATH_UNDER_CAMPFIRE,
        Regions.CATH_SHAFT_ACCESS,
    },
    Regions.CATH_UNDER_CAMPFIRE: {
        Regions.CATH_CAMPFIRE_1,
    },
    Regions.CATH_CAMPFIRE_1: {
        Regions.CATH_SHAFT_ACCESS,
    },
    Regions.CATH_SHAFT_ACCESS: {
        Regions.CATH_ORB_ROOM,
    },
    Regions.CATH_ORB_ROOM: {
        Regions.CATH_GOLD_BLOCK,
        Regions.CATH_RIGHT_SHAFT_CONNECTION,
    },
    Regions.CATH_GOLD_BLOCK: None,
    Regions.CATH_RIGHT_SHAFT_CONNECTION: {
        Regions.CATH_RIGHT_SHAFT,
    },
    Regions.CATH_RIGHT_SHAFT: {
        Regions.CATH_TOP,
    },
    Regions.CATH_TOP: {
        Regions.CATH_CAMPFIRE_2,
        Regions.CATH_UPPER_SPIKE_PIT,
    },
    Regions.CATH_CAMPFIRE_2: None,
    Regions.CATH_UPPER_SPIKE_PIT: None,
    Regions.SP_START: {
        Regions.SP_CAMPFIRE_1,
        Regions.SP_STAR_END,
    },
    Regions.SP_CAMPFIRE_1: {
        Regions.SP_HEARTS,
    },
    Regions.SP_HEARTS: {
        Regions.SP_PAINTING,
        Regions.SP_ORBS,
        Regions.SP_FROG,
    },
    Regions.SP_PAINTING: {
        Regions.SP_SHAFT,
    },
    Regions.SP_SHAFT: {
        Regions.SP_STAR,
    },
    Regions.SP_STAR: {
        Regions.SP_STAR_CONNECTION,
    },
    Regions.SP_STAR_CONNECTION: {
        Regions.SP_STAR_END,
    },
    Regions.SP_STAR_END: None,
    Regions.SP_ORBS: None,
    Regions.SP_FROG: {
        Regions.SP_CAMPFIRE_2,
    },
    Regions.SP_CAMPFIRE_2: {
        Regions.HOTP_MAIDEN,
    },
}
