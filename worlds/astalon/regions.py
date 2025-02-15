from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple


class RegionName(str, Enum):
    MENU = "Menu"
    SHOP = "Shop"
    SHOP_ALGUS = "Shop - Algus"
    SHOP_ARIAS = "Shop - Arias"
    SHOP_KYULI = "Shop - Kyuli"
    SHOP_ZEEK = "Shop - Zeek"
    SHOP_BRAM = "Shop - Bram"
    FINAL_BOSS = "Final Boss"

    GT_ENTRANCE = "Gorgon Tomb - Entrance"
    GT_BESTIARY = "Gorgon Tomb - Bestiary"
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
    GT_SPIKE_TUNNEL_SWITCH = "Gorgon Tomb - Spike Tunnel Switch"
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
    MECH_CHAINS_CANDLE = "Mechanism - Chains Candle"
    MECH_CHAINS = "Mechanism - Chains"
    MECH_ARIAS_EYEBALL = "Mechanism - Arias Eyeball"
    MECH_TRIPLE_SWITCHES = "Mechanism - Triple Switches"
    MECH_ZEEK_CONNECTION = "Mechanism - Zeek Connection"
    MECH_ZEEK = "Mechanism - Zeek"
    MECH_SPLIT_PATH = "Mechanism - Split Path"
    MECH_RIGHT = "Mechanism - Right"
    MECH_OLD_MAN = "Mechanism - Old Man"
    MECH_UPPER_VOID = "Mechanism - Upper Void"
    MECH_BELOW_POTS = "Mechanism - Below Pots"
    MECH_POTS = "Mechanism - Pots"
    MECH_TOP = "Mechanism - Top"
    MECH_CD_ACCESS = "Mechanism - Cyclops Den Access"
    MECH_TP_CONNECTION = "Mechanism - Teleport Connection"
    MECH_CHARACTER_SWAPS = "Mechanism - Character Swaps"
    MECH_CLOAK_CONNECTION = "Mechanism - Cloak Connection"
    MECH_CLOAK = "Mechanism - Cloak"
    MECH_BOSS_SWITCHES = "Mechanism - Boss Switches"
    MECH_BOSS_CONNECTION = "Mechanism - Boss Connection"
    MECH_BRAM_TUNNEL_CONNECTION = "Mechanism - Bram Tunnel Connection"
    MECH_BRAM_TUNNEL = "Mechanism - Bram Tunnel"
    MECH_BOSS = "Mechanism - Boss"

    HOTP_START = "Hall of the Phantoms - Start"
    HOTP_START_MID = "Hall of the Phantoms - Start Mid"
    HOTP_LOWER_VOID = "Hall of the Phantoms - Lower Void"
    HOTP_START_LEFT = "Hall of the Phantoms - Start Left"
    HOTP_START_BOTTOM = "Hall of the Phantoms - Start Bottom"
    HOTP_START_BOTTOM_MID = "Hall of the Phantoms - Start Bottom/Mid Connection"
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
    HOTP_GHOST_BLOOD = "Hall of the Phantoms - Ghost Blood"
    HOTP_EYEBALL = "Hall of the Phantoms - Eyeball"
    HOTP_SPIKE_TP_SECRET = "Hall of the Phantoms - Spike Teleporters Secret"
    HOTP_WORM_SHORTCUT = "Hall of the Phantoms - Worm Pillar Shortcut"
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
    HOTP_MAIDEN = "Hall of the Phantoms - Dead Maiden"  # may need to break this up
    HOTP_TP_PUZZLE = "Hall of the Phantoms - Teleport Puzzle"
    HOTP_TP_FALL_TOP = "Hall of the Phantoms - Teleport Fall Top"
    HOTP_GAUNTLET_CONNECTION = "Hall of the Phantoms - Gauntlet Connection"
    HOTP_GAUNTLET = "Hall of the Phantoms - Boreas Gauntlet"
    HOTP_FALL_BOTTOM = "Hall of the Phantoms - Teleport Fall Bottom"
    HOTP_UPPER_VOID = "Hall of the Phantoms - Upper Void"
    HOTP_BOSS = "Hall of the Phantoms - Boss"

    ROA_START = "Ruins of Ash - Start"
    ROA_WORMS = "Ruins of Ash - Worms"
    ROA_WORMS_CONNECTION = "Ruins of Ash - Worms Connection"
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
    ROA_RIGHT_SWITCH_CANDLE = "Ruins of Ash - Right Switch Candle"
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
    APEX_CENTAUR_ACCESS = "The Apex - Centaur Access"
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
    CATA_MULTI = "Catacombs - Orb Multiplier"
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
    CATA_BELOW_ROOTS_CAMPFIRE = "Catacombs - Below Roots Campfire"
    CATA_ABOVE_ROOTS = "Catacombs - Above Roots"
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
    TR_DARK_ARIAS = "Tower Roots - Dark Arias"
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


@dataclass(frozen=True)
class RegionData:
    exits: Tuple[RegionName, ...] = ()
    boss: bool = False
    campfire: bool = False
    elevator: bool = False
    multiplier: bool = False
    portal: bool = False
    statue: bool = False
    orbs: int = 0


astalon_regions: Dict[RegionName, RegionData] = {
    RegionName.MENU: RegionData(
        exits=(
            RegionName.GT_ENTRANCE,
            RegionName.SHOP,
        ),
    ),
    RegionName.SHOP: RegionData(
        exits=(
            RegionName.SHOP_ALGUS,
            RegionName.SHOP_ARIAS,
            RegionName.SHOP_KYULI,
            RegionName.SHOP_ZEEK,
            RegionName.SHOP_BRAM,
        ),
    ),
    RegionName.SHOP_ALGUS: RegionData(),
    RegionName.SHOP_ARIAS: RegionData(),
    RegionName.SHOP_KYULI: RegionData(),
    RegionName.SHOP_ZEEK: RegionData(),
    RegionName.SHOP_BRAM: RegionData(),
    RegionName.FINAL_BOSS: RegionData(boss=True),
    RegionName.GT_ENTRANCE: RegionData(
        exits=(
            RegionName.GT_BESTIARY,
            RegionName.GT_BABY_GORGON,
            RegionName.GT_BOTTOM,
            RegionName.GT_VOID,
            RegionName.GT_GORGONHEART,
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        campfire=True,
        elevator=True,
        multiplier=True,
        portal=True,
    ),
    RegionName.GT_BESTIARY: RegionData(),
    RegionName.GT_BABY_GORGON: RegionData(),
    RegionName.GT_BOTTOM: RegionData(
        exits=(
            RegionName.GT_VOID,
            RegionName.GT_GORGONHEART,
            RegionName.GT_UPPER_PATH,
            RegionName.CAVES_START,
        ),
        campfire=True,
    ),
    RegionName.GT_VOID: RegionData(
        exits=(
            RegionName.GT_BOTTOM,
            RegionName.MECH_SNAKE,
        ),
        portal=True,
    ),
    RegionName.GT_GORGONHEART: RegionData(
        exits=(
            RegionName.GT_BOTTOM,
            RegionName.GT_ORBS_DOOR,
            RegionName.GT_LEFT,
        ),
    ),
    RegionName.GT_ORBS_DOOR: RegionData(),
    RegionName.GT_LEFT: RegionData(
        exits=(
            RegionName.GT_GORGONHEART,
            RegionName.GT_ORBS_HEIGHT,
            RegionName.GT_ASCENDANT_KEY,
            RegionName.GT_TOP_LEFT,
            RegionName.GT_TOP_RIGHT,
        ),
        campfire=True,
    ),
    RegionName.GT_ORBS_HEIGHT: RegionData(),
    RegionName.GT_ASCENDANT_KEY: RegionData(),
    RegionName.GT_TOP_LEFT: RegionData(
        exits=(
            RegionName.GT_LEFT,
            RegionName.GT_BUTT,
        ),
    ),
    RegionName.GT_TOP_RIGHT: RegionData(
        exits=(
            RegionName.GT_LEFT,
            RegionName.GT_SPIKE_TUNNEL,
        ),
    ),
    RegionName.GT_SPIKE_TUNNEL: RegionData(
        exits=(
            RegionName.GT_TOP_RIGHT,
            RegionName.GT_SPIKE_TUNNEL_SWITCH,
        ),
    ),
    RegionName.GT_SPIKE_TUNNEL_SWITCH: RegionData(
        exits=(
            RegionName.GT_SPIKE_TUNNEL,
            RegionName.GT_BUTT,
        ),
    ),
    RegionName.GT_BUTT: RegionData(
        exits=(
            RegionName.GT_TOP_LEFT,
            RegionName.GT_SPIKE_TUNNEL_SWITCH,
            RegionName.GT_BOSS,
        ),
    ),
    RegionName.GT_BOSS: RegionData(
        exits=(
            RegionName.GT_BUTT,
            RegionName.MECH_START,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        boss=True,
        campfire=True,
        elevator=True,
    ),
    RegionName.GT_LADDER_SWITCH: RegionData(),
    RegionName.GT_UPPER_ARIAS: RegionData(
        exits=(
            RegionName.GT_OLD_MAN_FORK,
            RegionName.MECH_SWORD_CONNECTION,
        ),
    ),
    RegionName.GT_OLD_MAN_FORK: RegionData(
        exits=(
            RegionName.GT_UPPER_ARIAS,
            RegionName.GT_OLD_MAN,
            RegionName.GT_SWORD_FORK,
        ),
    ),
    RegionName.GT_OLD_MAN: RegionData(),
    RegionName.GT_SWORD_FORK: RegionData(
        exits=(
            RegionName.GT_SWORD,
            RegionName.GT_ARIAS_SWORD_SWITCH,
        ),
    ),
    RegionName.GT_SWORD: RegionData(),
    RegionName.GT_ARIAS_SWORD_SWITCH: RegionData(),
    RegionName.GT_UPPER_PATH: RegionData(
        exits=(
            RegionName.GT_BOTTOM,
            RegionName.GT_UPPER_PATH_CONNECTION,
        ),
    ),
    RegionName.GT_UPPER_PATH_CONNECTION: RegionData(
        exits=(
            RegionName.GT_UPPER_PATH,
            RegionName.MECH_SWORD_CONNECTION,
            RegionName.MECH_BOTTOM_CAMPFIRE,
        ),
    ),
    RegionName.MECH_START: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.GT_LADDER_SWITCH,
            RegionName.MECH_SACRIFICE,
            RegionName.MECH_LINUS,
            RegionName.MECH_LOWER_VOID,
            RegionName.MECH_BK,
            RegionName.MECH_WATCHER,
        ),
        campfire=True,
    ),
    RegionName.MECH_SACRIFICE: RegionData(),
    RegionName.MECH_LINUS: RegionData(
        exits=(
            RegionName.MECH_START,
            RegionName.MECH_SWORD_CONNECTION,
        ),
    ),
    RegionName.MECH_SWORD_CONNECTION: RegionData(
        exits=(
            RegionName.GT_UPPER_ARIAS,
            RegionName.GT_UPPER_PATH_CONNECTION,
            RegionName.MECH_LINUS,
            RegionName.MECH_LOWER_ARIAS,
            RegionName.MECH_BOOTS_CONNECTION,
            RegionName.MECH_BOTTOM_CAMPFIRE,
        ),
        campfire=True,
    ),
    RegionName.MECH_LOWER_ARIAS: RegionData(),
    RegionName.MECH_BOOTS_CONNECTION: RegionData(
        exits=(
            RegionName.MECH_SWORD_CONNECTION,
            RegionName.MECH_BOOTS_LOWER,
            RegionName.MECH_BOTTOM_CAMPFIRE,
        ),
    ),
    RegionName.MECH_BOOTS_LOWER: RegionData(
        exits=(RegionName.MECH_BOOTS_UPPER,),
    ),
    RegionName.MECH_BOOTS_UPPER: RegionData(),
    RegionName.MECH_BOTTOM_CAMPFIRE: RegionData(
        exits=(
            RegionName.GT_UPPER_PATH_CONNECTION,
            RegionName.MECH_SWORD_CONNECTION,
            RegionName.MECH_BOOTS_CONNECTION,
            RegionName.MECH_SNAKE,
        ),
        campfire=True,
    ),
    RegionName.MECH_SNAKE: RegionData(
        exits=(
            RegionName.GT_VOID,
            RegionName.MECH_BOTTOM_CAMPFIRE,
        ),
    ),
    RegionName.MECH_LOWER_VOID: RegionData(
        exits=(
            RegionName.MECH_START,
            RegionName.MECH_UPPER_VOID,
            RegionName.HOTP_MECH_VOID_CONNECTION,
        ),
        portal=True,
    ),
    RegionName.MECH_WATCHER: RegionData(
        exits=(
            RegionName.MECH_START,
            RegionName.MECH_ROOTS,
        ),
    ),
    RegionName.MECH_ROOTS: RegionData(
        exits=(
            RegionName.MECH_WATCHER,
            RegionName.MECH_MUSIC,
            RegionName.MECH_BK,
            RegionName.MECH_ZEEK_CONNECTION,
        ),
    ),
    RegionName.MECH_MUSIC: RegionData(),
    RegionName.MECH_BK: RegionData(
        exits=(
            RegionName.MECH_START,
            RegionName.MECH_ROOTS,
            RegionName.MECH_AFTER_BK,
            RegionName.MECH_TRIPLE_SWITCHES,
        ),
        boss=True,
        campfire=True,
    ),
    RegionName.MECH_AFTER_BK: RegionData(
        exits=(
            RegionName.MECH_BK,
            RegionName.MECH_CHAINS_CANDLE,
            RegionName.MECH_CHAINS,
            RegionName.HOTP_EPIMETHEUS,
        ),
        multiplier=True,
        statue=True,
    ),
    RegionName.MECH_CHAINS_CANDLE: RegionData(
        exits=(
            RegionName.MECH_AFTER_BK,
            RegionName.MECH_CHAINS,
        ),
    ),
    RegionName.MECH_CHAINS: RegionData(
        exits=(
            RegionName.MECH_AFTER_BK,
            RegionName.MECH_CHAINS_CANDLE,
            RegionName.MECH_ARIAS_EYEBALL,
            RegionName.MECH_SPLIT_PATH,
            RegionName.MECH_BOSS_SWITCHES,
            RegionName.MECH_BOSS_CONNECTION,
        ),
    ),
    RegionName.MECH_ARIAS_EYEBALL: RegionData(
        exits=(
            RegionName.MECH_CHAINS,
            RegionName.MECH_ZEEK_CONNECTION,
        ),
    ),
    RegionName.MECH_TRIPLE_SWITCHES: RegionData(),
    RegionName.MECH_ZEEK_CONNECTION: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ROOTS,
            RegionName.MECH_ARIAS_EYEBALL,
            RegionName.MECH_ZEEK,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        elevator=True,
    ),
    RegionName.MECH_ZEEK: RegionData(),
    RegionName.MECH_SPLIT_PATH: RegionData(
        exits=(
            RegionName.MECH_CHAINS,
            RegionName.MECH_RIGHT,
        ),
    ),
    RegionName.MECH_RIGHT: RegionData(
        exits=(
            RegionName.MECH_TRIPLE_SWITCHES,
            RegionName.MECH_SPLIT_PATH,
            RegionName.MECH_OLD_MAN,
            RegionName.MECH_UPPER_VOID,
            RegionName.MECH_BELOW_POTS,
        ),
        campfire=True,
    ),
    RegionName.MECH_OLD_MAN: RegionData(),
    RegionName.MECH_UPPER_VOID: RegionData(
        exits=(
            RegionName.MECH_LOWER_VOID,
            RegionName.MECH_RIGHT,
        ),
        portal=True,
    ),
    RegionName.MECH_BELOW_POTS: RegionData(
        exits=(
            RegionName.MECH_RIGHT,
            RegionName.MECH_POTS,
        ),
    ),
    RegionName.MECH_POTS: RegionData(
        exits=(
            RegionName.MECH_BELOW_POTS,
            RegionName.MECH_TOP,
        ),
    ),
    RegionName.MECH_TOP: RegionData(
        exits=(
            RegionName.MECH_TRIPLE_SWITCHES,
            RegionName.MECH_POTS,
            RegionName.MECH_TP_CONNECTION,
            RegionName.MECH_CD_ACCESS,
        ),
        campfire=True,
    ),
    RegionName.MECH_CD_ACCESS: RegionData(
        exits=(RegionName.CD_START,),
    ),
    RegionName.MECH_TP_CONNECTION: RegionData(
        exits=(
            RegionName.MECH_TOP,
            RegionName.MECH_CHARACTER_SWAPS,
            RegionName.HOTP_FALL_BOTTOM,
        ),
    ),
    RegionName.MECH_CHARACTER_SWAPS: RegionData(
        exits=(
            RegionName.MECH_TP_CONNECTION,
            RegionName.MECH_CLOAK_CONNECTION,
        ),
    ),
    RegionName.MECH_CLOAK_CONNECTION: RegionData(
        exits=(
            RegionName.MECH_CHARACTER_SWAPS,
            RegionName.MECH_CLOAK,
            RegionName.MECH_BOSS_SWITCHES,
        ),
    ),
    RegionName.MECH_CLOAK: RegionData(),
    RegionName.MECH_BOSS_SWITCHES: RegionData(
        exits=(
            RegionName.MECH_CHAINS,
            RegionName.MECH_CLOAK_CONNECTION,
            RegionName.MECH_BOSS_CONNECTION,
        ),
    ),
    RegionName.MECH_BOSS_CONNECTION: RegionData(
        exits=(
            RegionName.MECH_CHAINS,
            RegionName.MECH_BRAM_TUNNEL_CONNECTION,
            RegionName.MECH_BOSS,
        ),
    ),
    RegionName.MECH_BRAM_TUNNEL_CONNECTION: RegionData(
        exits=(
            RegionName.MECH_BOSS_CONNECTION,
            RegionName.MECH_BRAM_TUNNEL,
        )
    ),
    RegionName.MECH_BRAM_TUNNEL: RegionData(
        exits=(
            RegionName.MECH_BRAM_TUNNEL_CONNECTION,
            RegionName.HOTP_START_BOTTOM,
        ),
    ),
    RegionName.MECH_BOSS: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_TRIPLE_SWITCHES,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS_CONNECTION,
            RegionName.HOTP_START,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        boss=True,
        campfire=True,
        elevator=True,
    ),
    RegionName.HOTP_START: RegionData(
        exits=(
            RegionName.MECH_BOSS,
            RegionName.HOTP_START_MID,
            RegionName.HOTP_START_BOTTOM,
        ),
    ),
    RegionName.HOTP_START_MID: RegionData(
        exits=(
            RegionName.HOTP_START,
            RegionName.HOTP_LOWER_VOID,
            RegionName.HOTP_START_LEFT,
            RegionName.HOTP_START_BOTTOM_MID,
        ),
    ),
    RegionName.HOTP_LOWER_VOID: RegionData(
        exits=(
            RegionName.HOTP_START_MID,
            RegionName.HOTP_UPPER_VOID,
        ),
        portal=True,
    ),
    RegionName.HOTP_START_LEFT: RegionData(
        exits=(
            RegionName.HOTP_START_MID,
            RegionName.HOTP_ELEVATOR,
        ),
    ),
    RegionName.HOTP_START_BOTTOM: RegionData(
        exits=(
            RegionName.MECH_BRAM_TUNNEL,
            RegionName.HOTP_START,
            RegionName.HOTP_START_BOTTOM_MID,
            RegionName.HOTP_LOWER,
        ),
    ),
    RegionName.HOTP_START_BOTTOM_MID: RegionData(
        exits=(
            RegionName.HOTP_START_MID,
            RegionName.HOTP_START_BOTTOM,
        ),
    ),
    RegionName.HOTP_LOWER: RegionData(
        exits=(
            RegionName.HOTP_START_BOTTOM,
            RegionName.HOTP_EPIMETHEUS,
            RegionName.HOTP_MECH_VOID_CONNECTION,
            RegionName.HOTP_TP_TUTORIAL,
        ),
    ),
    RegionName.HOTP_EPIMETHEUS: RegionData(
        exits=(
            RegionName.MECH_AFTER_BK,
            RegionName.HOTP_LOWER,
        ),
        campfire=True,
    ),
    RegionName.HOTP_MECH_VOID_CONNECTION: RegionData(
        exits=(
            RegionName.MECH_LOWER_VOID,
            RegionName.HOTP_LOWER,
            RegionName.HOTP_AMULET_CONNECTION,
        ),
    ),
    RegionName.HOTP_AMULET_CONNECTION: RegionData(
        exits=(
            RegionName.GT_BUTT,
            RegionName.HOTP_MECH_VOID_CONNECTION,
            RegionName.HOTP_AMULET,
        ),
    ),
    RegionName.HOTP_AMULET: RegionData(),
    RegionName.HOTP_TP_TUTORIAL: RegionData(
        exits=(
            RegionName.HOTP_LOWER,
            RegionName.HOTP_BELL_CAMPFIRE,
        ),
    ),
    RegionName.HOTP_BELL_CAMPFIRE: RegionData(
        exits=(
            RegionName.HOTP_TP_TUTORIAL,
            RegionName.HOTP_RED_KEY,
            RegionName.HOTP_BELL,
            RegionName.HOTP_CATH_CONNECTION,
            RegionName.HOTP_LOWER_ARIAS,
        ),
        campfire=True,
    ),
    RegionName.HOTP_RED_KEY: RegionData(),
    RegionName.HOTP_BELL: RegionData(),
    RegionName.HOTP_CATH_CONNECTION: RegionData(
        exits=(
            RegionName.HOTP_BELL,
            RegionName.CATH_START,
        ),
    ),
    RegionName.HOTP_LOWER_ARIAS: RegionData(
        exits=(
            RegionName.HOTP_BELL_CAMPFIRE,
            RegionName.HOTP_GHOST_BLOOD,
        ),
    ),
    RegionName.HOTP_GHOST_BLOOD: RegionData(
        exits=(
            RegionName.HOTP_LOWER_ARIAS,
            RegionName.HOTP_EYEBALL,
            RegionName.HOTP_WORM_SHORTCUT,
        ),
    ),
    RegionName.HOTP_EYEBALL: RegionData(
        exits=(
            RegionName.HOTP_SPIKE_TP_SECRET,
            RegionName.HOTP_ELEVATOR,
        ),
    ),
    RegionName.HOTP_SPIKE_TP_SECRET: RegionData(),
    RegionName.HOTP_WORM_SHORTCUT: RegionData(
        exits=(
            RegionName.HOTP_GHOST_BLOOD,
            RegionName.HOTP_ELEVATOR,
        ),
    ),
    RegionName.HOTP_ELEVATOR: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_START_LEFT,
            RegionName.HOTP_SPIKE_TP_SECRET,
            RegionName.HOTP_WORM_SHORTCUT,
            RegionName.HOTP_OLD_MAN,
            RegionName.HOTP_CLAW_LEFT,
            RegionName.HOTP_TOP_LEFT,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        elevator=True,
    ),
    RegionName.HOTP_OLD_MAN: RegionData(),
    RegionName.HOTP_CLAW_LEFT: RegionData(
        exits=(
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_TOP_LEFT,
            RegionName.HOTP_CLAW,
        ),
    ),
    RegionName.HOTP_TOP_LEFT: RegionData(
        exits=(
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_CLAW_LEFT,
            RegionName.HOTP_ABOVE_OLD_MAN,
            RegionName.HOTP_CLAW_CAMPFIRE,
        ),
    ),
    RegionName.HOTP_ABOVE_OLD_MAN: RegionData(),
    RegionName.HOTP_CLAW_CAMPFIRE: RegionData(
        exits=(
            RegionName.HOTP_TOP_LEFT,
            RegionName.HOTP_CLAW,
            RegionName.HOTP_HEART,
        ),
        campfire=True,
    ),
    RegionName.HOTP_CLAW: RegionData(
        exits=(
            RegionName.HOTP_CLAW_LEFT,
            RegionName.HOTP_CLAW_CAMPFIRE,
        ),
    ),
    RegionName.HOTP_HEART: RegionData(
        exits=(
            RegionName.HOTP_CLAW_CAMPFIRE,
            RegionName.HOTP_UPPER_ARIAS,
            RegionName.HOTP_BOSS_CAMPFIRE,
        ),
    ),
    RegionName.HOTP_UPPER_ARIAS: RegionData(
        exits=(
            RegionName.HOTP_HEART,
            RegionName.HOTP_BOSS_CAMPFIRE,
        ),
    ),
    RegionName.HOTP_BOSS_CAMPFIRE: RegionData(
        exits=(
            RegionName.MECH_TRIPLE_SWITCHES,
            RegionName.HOTP_HEART,
            RegionName.HOTP_MAIDEN,
            RegionName.HOTP_TP_PUZZLE,
            RegionName.HOTP_BOSS,
        ),
        campfire=True,
    ),
    RegionName.HOTP_MAIDEN: RegionData(statue=True),
    RegionName.HOTP_TP_PUZZLE: RegionData(
        exits=(RegionName.HOTP_TP_FALL_TOP,),
    ),
    RegionName.HOTP_TP_FALL_TOP: RegionData(
        exits=(
            RegionName.HOTP_BOSS_CAMPFIRE,
            RegionName.HOTP_TP_PUZZLE,
            RegionName.HOTP_GAUNTLET_CONNECTION,
            RegionName.HOTP_FALL_BOTTOM,
        ),
    ),
    RegionName.HOTP_GAUNTLET_CONNECTION: RegionData(
        exits=(RegionName.HOTP_GAUNTLET,),
    ),
    RegionName.HOTP_GAUNTLET: RegionData(),
    RegionName.HOTP_FALL_BOTTOM: RegionData(
        exits=(
            RegionName.MECH_TP_CONNECTION,
            RegionName.HOTP_TP_FALL_TOP,
            RegionName.HOTP_UPPER_VOID,
        ),
    ),
    RegionName.HOTP_UPPER_VOID: RegionData(
        exits=(
            RegionName.HOTP_LOWER_VOID,
            RegionName.HOTP_TP_FALL_TOP,
            RegionName.HOTP_FALL_BOTTOM,
        ),
        portal=True,
    ),
    RegionName.HOTP_BOSS: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS_CAMPFIRE,
            RegionName.ROA_START,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        boss=True,
        elevator=True,
    ),
    RegionName.ROA_START: RegionData(
        exits=(
            RegionName.HOTP_BOSS,
            RegionName.ROA_WORMS,
        ),
        campfire=True,
    ),
    RegionName.ROA_WORMS: RegionData(
        exits=(
            RegionName.ROA_START,
            RegionName.ROA_WORMS_CONNECTION,
            RegionName.ROA_LOWER_VOID_CONNECTION,
        ),
    ),
    RegionName.ROA_WORMS_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_WORMS,
            RegionName.ROA_HEARTS,
        ),
    ),
    RegionName.ROA_HEARTS: RegionData(
        exits=(
            RegionName.ROA_WORMS_CONNECTION,
            RegionName.ROA_SPIKE_CLIMB,
            RegionName.ROA_BOTTOM_ASCEND,
        ),
    ),
    RegionName.ROA_SPIKE_CLIMB: RegionData(
        exits=(
            RegionName.ROA_HEARTS,
            RegionName.ROA_BOTTOM_ASCEND,
        ),
    ),
    RegionName.ROA_BOTTOM_ASCEND: RegionData(
        exits=(
            RegionName.ROA_HEARTS,
            RegionName.ROA_SPIKE_CLIMB,
            RegionName.ROA_TRIPLE_REAPER,
            RegionName.ROA_TOP_ASCENT,
        ),
    ),
    RegionName.ROA_TRIPLE_REAPER: RegionData(
        exits=(
            RegionName.ROA_BOTTOM_ASCEND,
            RegionName.ROA_ARENA,
        ),
    ),
    RegionName.ROA_ARENA: RegionData(
        exits=(
            RegionName.ROA_TRIPLE_REAPER,
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_FLAMES_CONNECTION,
        ),
    ),
    RegionName.ROA_LOWER_VOID_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_WORMS,
            RegionName.ROA_ARENA,
            RegionName.ROA_LOWER_VOID,
            RegionName.ROA_ARIAS_BABY_GORGON,
            RegionName.ROA_FLAMES_CONNECTION,
        ),
    ),
    RegionName.ROA_LOWER_VOID: RegionData(
        exits=(
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_UPPER_VOID,
        ),
        portal=True,
    ),
    RegionName.ROA_ARIAS_BABY_GORGON: RegionData(
        exits=(
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_FLAMES_CONNECTION,
            RegionName.ROA_FLAMES,
        ),
    ),
    RegionName.ROA_FLAMES_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_ARENA,
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_ARIAS_BABY_GORGON,
            RegionName.ROA_FLAMES,
            RegionName.ROA_WORM_CLIMB,
            RegionName.ROA_LEFT_ASCENT,
            RegionName.ROA_LEFT_ASCENT_CRYSTAL,
        ),
    ),
    RegionName.ROA_FLAMES: RegionData(
        exits=(RegionName.ROA_ARIAS_BABY_GORGON,),
    ),
    RegionName.ROA_WORM_CLIMB: RegionData(
        exits=(
            RegionName.ROA_FLAMES_CONNECTION,
            RegionName.ROA_RIGHT_BRANCH,
        ),
    ),
    RegionName.ROA_RIGHT_BRANCH: RegionData(
        exits=(
            RegionName.ROA_WORM_CLIMB,
            RegionName.ROA_MIDDLE,
        ),
    ),
    RegionName.ROA_LEFT_ASCENT: RegionData(
        exits=(
            RegionName.ROA_FLAMES_CONNECTION,
            RegionName.ROA_LEFT_ASCENT_CRYSTAL,
            RegionName.ROA_TOP_ASCENT,
        ),
        campfire=True,
    ),
    RegionName.ROA_LEFT_ASCENT_CRYSTAL: RegionData(),
    RegionName.ROA_TOP_ASCENT: RegionData(
        exits=(
            RegionName.ROA_LEFT_ASCENT,
            RegionName.ROA_TRIPLE_SWITCH,
            RegionName.ROA_MIDDLE,
        ),
    ),
    RegionName.ROA_TRIPLE_SWITCH: RegionData(
        exits=(
            RegionName.ROA_TOP_ASCENT,
            RegionName.ROA_MIDDLE,
        ),
    ),
    RegionName.ROA_MIDDLE: RegionData(
        exits=(
            RegionName.ROA_RIGHT_BRANCH,
            RegionName.ROA_TOP_ASCENT,
            RegionName.ROA_TRIPLE_SWITCH,
            RegionName.ROA_LEFT_BABY_GORGON,
            RegionName.ROA_LEFT_SWITCH,
            RegionName.ROA_RIGHT_SWITCH_1,
            RegionName.ROA_MIDDLE_LADDER,
        ),
        campfire=True,
    ),
    RegionName.ROA_LEFT_BABY_GORGON: RegionData(),
    RegionName.ROA_LEFT_SWITCH: RegionData(),
    RegionName.ROA_RIGHT_SWITCH_1: RegionData(
        exits=(RegionName.ROA_RIGHT_SWITCH_2,),
    ),
    RegionName.ROA_RIGHT_SWITCH_2: RegionData(
        exits=(RegionName.ROA_RIGHT_SWITCH_CANDLE,),
    ),
    RegionName.ROA_RIGHT_SWITCH_CANDLE: RegionData(),
    RegionName.ROA_MIDDLE_LADDER: RegionData(
        exits=(
            RegionName.ROA_MIDDLE,
            RegionName.ROA_RIGHT_SWITCH_CANDLE,
            RegionName.ROA_UPPER_VOID,
        ),
    ),
    RegionName.ROA_UPPER_VOID: RegionData(
        exits=(
            RegionName.ROA_LOWER_VOID,
            RegionName.ROA_MIDDLE_LADDER,
            RegionName.ROA_SPIKE_BALLS,
            RegionName.ROA_SP_CONNECTION,
        ),
        portal=True,
    ),
    RegionName.ROA_SPIKE_BALLS: RegionData(
        exits=(
            RegionName.ROA_UPPER_VOID,
            RegionName.ROA_SPIKE_SPINNERS,
        ),
    ),
    RegionName.ROA_SPIKE_SPINNERS: RegionData(
        exits=(
            RegionName.ROA_SPIKE_BALLS,
            RegionName.ROA_SPIDERS_1,
        ),
    ),
    RegionName.ROA_SPIDERS_1: RegionData(
        exits=(
            RegionName.ROA_SPIKE_SPINNERS,
            RegionName.ROA_RED_KEY,
            RegionName.ROA_SPIDERS_2,
        ),
    ),
    RegionName.ROA_RED_KEY: RegionData(),
    RegionName.ROA_SPIDERS_2: RegionData(
        exits=(
            RegionName.ROA_SPIDERS_1,
            RegionName.ROA_BLOOD_POT_HALLWAY,
        ),
    ),
    RegionName.ROA_BLOOD_POT_HALLWAY: RegionData(
        exits=(
            RegionName.ROA_SPIDERS_2,
            RegionName.ROA_SP_CONNECTION,
        ),
    ),
    RegionName.ROA_SP_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_UPPER_VOID,
            RegionName.ROA_BLOOD_POT_HALLWAY,
            RegionName.ROA_ELEVATOR,
            RegionName.SP_START,
        ),
    ),
    RegionName.ROA_ELEVATOR: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_SP_CONNECTION,
            RegionName.ROA_ICARUS,
            RegionName.ROA_DARK_CONNECTION,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        campfire=True,
        elevator=True,
    ),
    RegionName.ROA_ICARUS: RegionData(),
    RegionName.ROA_DARK_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_ELEVATOR,
            RegionName.DARK_START,
            RegionName.ROA_CENTAUR,
        ),
    ),
    RegionName.DARK_START: RegionData(
        exits=(RegionName.DARK_END,),
    ),
    RegionName.DARK_END: RegionData(
        exits=(RegionName.ROA_CENTAUR,),
    ),
    RegionName.ROA_CENTAUR: RegionData(
        exits=(
            RegionName.ROA_DARK_CONNECTION,
            RegionName.ROA_BOSS_CONNECTION,
        ),
    ),
    RegionName.ROA_BOSS_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_CENTAUR,
            RegionName.ROA_BOSS,
        ),
    ),
    RegionName.ROA_BOSS: RegionData(
        exits=(
            RegionName.ROA_BOSS_CONNECTION,
            RegionName.ROA_APEX_CONNECTION,
        ),
        boss=True,
        campfire=True,
    ),
    RegionName.ROA_APEX_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_BOSS,
            RegionName.APEX,
        ),
    ),
    RegionName.APEX: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.FINAL_BOSS,
            RegionName.ROA_APEX_CONNECTION,
            RegionName.APEX_CENTAUR_ACCESS,
            RegionName.APEX_HEART,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        campfire=True,
        elevator=True,
        statue=True,
    ),
    RegionName.APEX_CENTAUR_ACCESS: RegionData(
        exits=(RegionName.APEX_CENTAUR,),
    ),
    RegionName.APEX_CENTAUR: RegionData(boss=True),
    RegionName.APEX_HEART: RegionData(),
    RegionName.CAVES_START: RegionData(
        exits=(
            RegionName.GT_BOTTOM,
            RegionName.CAVES_EPIMETHEUS,
        ),
    ),
    RegionName.CAVES_EPIMETHEUS: RegionData(
        exits=(
            RegionName.CAVES_START,
            RegionName.CAVES_UPPER,
        ),
        statue=True,
    ),
    RegionName.CAVES_UPPER: RegionData(
        exits=(
            RegionName.CAVES_EPIMETHEUS,
            RegionName.CAVES_ARENA,
            RegionName.CAVES_LOWER,
        ),
    ),
    RegionName.CAVES_ARENA: RegionData(),
    RegionName.CAVES_LOWER: RegionData(
        exits=(
            RegionName.CAVES_UPPER,
            RegionName.CAVES_ITEM_CHAIN,
            RegionName.CATA_START,
        ),
        campfire=True,
    ),
    RegionName.CAVES_ITEM_CHAIN: RegionData(),
    RegionName.CATA_START: RegionData(
        exits=(
            RegionName.CAVES_LOWER,
            RegionName.CATA_CLIMBABLE_ROOT,
        ),
    ),
    RegionName.CATA_CLIMBABLE_ROOT: RegionData(
        exits=(RegionName.CATA_TOP,),
    ),
    RegionName.CATA_TOP: RegionData(
        exits=(
            RegionName.CATA_CLIMBABLE_ROOT,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOW_CAMPFIRE,
        ),
    ),
    RegionName.CATA_ELEVATOR: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_TOP,
            RegionName.CATA_MULTI,
            RegionName.CATA_BOSS,
            RegionName.TR_START,
        ),
        elevator=True,
    ),
    RegionName.CATA_MULTI: RegionData(multiplier=True),
    RegionName.CATA_BOW_CAMPFIRE: RegionData(
        exits=(
            RegionName.CATA_TOP,
            RegionName.CATA_BOW_CONNECTION,
            RegionName.CATA_EYEBALL_BONES,
        ),
        campfire=True,
    ),
    RegionName.CATA_BOW_CONNECTION: RegionData(
        exits=(
            RegionName.CATA_BOW_CAMPFIRE,
            RegionName.CATA_BOW,
            RegionName.CATA_VERTICAL_SHORTCUT,
        ),
    ),
    RegionName.CATA_BOW: RegionData(),
    RegionName.CATA_VERTICAL_SHORTCUT: RegionData(
        exits=(
            RegionName.CATA_BOW_CONNECTION,
            RegionName.CATA_BLUE_EYE_DOOR,
            RegionName.CATA_FLAMES_FORK,
        ),
    ),
    RegionName.CATA_EYEBALL_BONES: RegionData(
        exits=(
            RegionName.CATA_BOW_CAMPFIRE,
            RegionName.CATA_SNAKE_MUSHROOMS,
        ),
    ),
    RegionName.CATA_SNAKE_MUSHROOMS: RegionData(
        exits=(
            RegionName.CATA_EYEBALL_BONES,
            RegionName.CATA_DEV_ROOM_CONNECTION,
            RegionName.CATA_DOUBLE_SWITCH,
        ),
    ),
    RegionName.CATA_DEV_ROOM_CONNECTION: RegionData(
        exits=(RegionName.CATA_DEV_ROOM,),
    ),
    RegionName.CATA_DEV_ROOM: RegionData(
        campfire=True,
        statue=True,
    ),
    RegionName.CATA_DOUBLE_SWITCH: RegionData(
        exits=(
            RegionName.CATA_SNAKE_MUSHROOMS,
            RegionName.CATA_ROOTS_CAMPFIRE,
        ),
    ),
    RegionName.CATA_ROOTS_CAMPFIRE: RegionData(
        exits=(
            RegionName.CATA_DOUBLE_SWITCH,
            RegionName.CATA_BELOW_ROOTS_CAMPFIRE,
        ),
        campfire=True,
    ),
    RegionName.CATA_BELOW_ROOTS_CAMPFIRE: RegionData(
        exits=(
            RegionName.CATA_ROOTS_CAMPFIRE,
            RegionName.CATA_ABOVE_ROOTS,
            RegionName.CATA_POISON_ROOTS,
            RegionName.CATA_BLUE_EYE_DOOR,
        )
    ),
    RegionName.CATA_ABOVE_ROOTS: RegionData(),
    RegionName.CATA_POISON_ROOTS: RegionData(),
    RegionName.CATA_BLUE_EYE_DOOR: RegionData(
        exits=(
            RegionName.CATA_BELOW_ROOTS_CAMPFIRE,
            RegionName.CATA_FLAMES_FORK,
        ),
    ),
    RegionName.CATA_FLAMES_FORK: RegionData(
        exits=(
            RegionName.CATA_VERTICAL_SHORTCUT,
            RegionName.CATA_BLUE_EYE_DOOR,
            RegionName.CATA_FLAMES,
            RegionName.CATA_CENTAUR,
        ),
    ),
    RegionName.CATA_FLAMES: RegionData(),
    RegionName.CATA_CENTAUR: RegionData(
        exits=(
            RegionName.CATA_FLAMES_FORK,
            RegionName.CATA_4_FACES,
            RegionName.CATA_BOSS,
        ),
    ),
    RegionName.CATA_4_FACES: RegionData(
        exits=(
            RegionName.CATA_CENTAUR,
            RegionName.CATA_DOUBLE_DOOR,
        ),
    ),
    RegionName.CATA_DOUBLE_DOOR: RegionData(
        exits=(
            RegionName.CATA_4_FACES,
            RegionName.CATA_VOID_R,
        ),
    ),
    RegionName.CATA_VOID_R: RegionData(
        exits=(
            RegionName.CATA_DOUBLE_DOOR,
            RegionName.CATA_VOID_L,
        ),
        portal=True,
    ),
    RegionName.CATA_VOID_L: RegionData(
        exits=(
            RegionName.CATA_VOID_R,
            RegionName.CATA_BOSS,
        ),
        portal=True,
    ),
    RegionName.CATA_BOSS: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_CENTAUR,
            RegionName.CATA_VOID_L,
            RegionName.TR_START,
        ),
        boss=True,
        campfire=True,
        elevator=True,
    ),
    RegionName.TR_START: RegionData(
        exits=(
            RegionName.GT_BOSS,
            RegionName.MECH_ZEEK_CONNECTION,
            RegionName.MECH_BOSS,
            RegionName.HOTP_ELEVATOR,
            RegionName.HOTP_BOSS,
            RegionName.ROA_ELEVATOR,
            RegionName.APEX,
            RegionName.CATA_ELEVATOR,
            RegionName.CATA_BOSS,
            RegionName.TR_BRAM,
            RegionName.TR_LEFT,
        ),
        campfire=True,
        elevator=True,
    ),
    RegionName.TR_BRAM: RegionData(),
    RegionName.TR_LEFT: RegionData(
        exits=(
            RegionName.TR_BOTTOM_LEFT,
            RegionName.TR_TOP_RIGHT,
        ),
    ),
    RegionName.TR_BOTTOM_LEFT: RegionData(
        exits=(RegionName.TR_BOTTOM,),
    ),
    RegionName.TR_TOP_RIGHT: RegionData(
        exits=(
            RegionName.TR_GOLD,
            RegionName.TR_MIDDLE_RIGHT,
        ),
    ),
    RegionName.TR_GOLD: RegionData(),
    RegionName.TR_MIDDLE_RIGHT: RegionData(
        exits=(
            RegionName.TR_DARK_ARIAS,
            RegionName.TR_BOTTOM,
        ),
    ),
    RegionName.TR_DARK_ARIAS: RegionData(boss=True),
    RegionName.TR_BOTTOM: RegionData(
        exits=(RegionName.TR_BOTTOM_LEFT,),
    ),
    RegionName.CD_START: RegionData(
        exits=(
            RegionName.CD_2,
            RegionName.CD_BOSS,
        ),
        campfire=True,
    ),
    RegionName.CD_2: RegionData(
        exits=(RegionName.CD_3,),
    ),
    RegionName.CD_3: RegionData(
        exits=(RegionName.CD_MIDDLE,),
    ),
    RegionName.CD_MIDDLE: RegionData(
        exits=(
            RegionName.CD_ARIAS_ROUTE,
            RegionName.CD_KYULI_ROUTE,
        ),
        campfire=True,
    ),
    RegionName.CD_ARIAS_ROUTE: RegionData(),
    RegionName.CD_KYULI_ROUTE: RegionData(
        exits=(RegionName.CD_CAMPFIRE_3,),
    ),
    RegionName.CD_CAMPFIRE_3: RegionData(
        exits=(RegionName.CD_ARENA,),
        campfire=True,
    ),
    RegionName.CD_ARENA: RegionData(
        exits=(RegionName.CD_STEPS,),
    ),
    RegionName.CD_STEPS: RegionData(
        exits=(RegionName.CD_TOP,),
    ),
    RegionName.CD_TOP: RegionData(campfire=True),
    RegionName.CD_BOSS: RegionData(boss=True),
    RegionName.CATH_START: RegionData(
        exits=(
            RegionName.CATH_START_RIGHT,
            RegionName.CATH_START_LEFT,
        ),
        portal=True,
    ),
    RegionName.CATH_START_RIGHT: RegionData(
        exits=(RegionName.CATH_START_TOP_LEFT,),
    ),
    RegionName.CATH_START_TOP_LEFT: RegionData(
        exits=(RegionName.CATH_START_LEFT,),
    ),
    RegionName.CATH_START_LEFT: RegionData(
        exits=(RegionName.CATH_TP,),
    ),
    RegionName.CATH_TP: RegionData(
        exits=(RegionName.CATH_LEFT_SHAFT,),
    ),
    RegionName.CATH_LEFT_SHAFT: RegionData(
        exits=(
            RegionName.CATH_UNDER_CAMPFIRE,
            RegionName.CATH_SHAFT_ACCESS,
        ),
    ),
    RegionName.CATH_UNDER_CAMPFIRE: RegionData(
        exits=(RegionName.CATH_CAMPFIRE_1,),
    ),
    RegionName.CATH_CAMPFIRE_1: RegionData(
        exits=(RegionName.CATH_SHAFT_ACCESS,),
        campfire=True,
    ),
    RegionName.CATH_SHAFT_ACCESS: RegionData(
        exits=(RegionName.CATH_ORB_ROOM,),
    ),
    RegionName.CATH_ORB_ROOM: RegionData(
        exits=(
            RegionName.CATH_GOLD_BLOCK,
            RegionName.CATH_RIGHT_SHAFT_CONNECTION,
        ),
    ),
    RegionName.CATH_GOLD_BLOCK: RegionData(),
    RegionName.CATH_RIGHT_SHAFT_CONNECTION: RegionData(
        exits=(RegionName.CATH_RIGHT_SHAFT,),
    ),
    RegionName.CATH_RIGHT_SHAFT: RegionData(
        exits=(RegionName.CATH_TOP,),
    ),
    RegionName.CATH_TOP: RegionData(
        exits=(
            RegionName.CATH_CAMPFIRE_2,
            RegionName.CATH_UPPER_SPIKE_PIT,
        ),
    ),
    RegionName.CATH_CAMPFIRE_2: RegionData(campfire=True),
    RegionName.CATH_UPPER_SPIKE_PIT: RegionData(),
    RegionName.SP_START: RegionData(
        exits=(
            RegionName.SP_CAMPFIRE_1,
            RegionName.SP_STAR_END,
        ),
    ),
    RegionName.SP_CAMPFIRE_1: RegionData(
        exits=(RegionName.SP_HEARTS,),
        campfire=True,
    ),
    RegionName.SP_HEARTS: RegionData(
        exits=(
            RegionName.SP_CAMPFIRE_1,
            RegionName.SP_PAINTING,
            RegionName.SP_ORBS,
            RegionName.SP_FROG,
        ),
    ),
    RegionName.SP_PAINTING: RegionData(
        exits=(
            RegionName.SP_HEARTS,
            RegionName.SP_SHAFT,
        ),
    ),
    RegionName.SP_SHAFT: RegionData(
        exits=(
            RegionName.SP_PAINTING,
            RegionName.SP_STAR,
        ),
    ),
    RegionName.SP_STAR: RegionData(
        exits=(
            RegionName.SP_SHAFT,
            RegionName.SP_STAR_CONNECTION,
        ),
    ),
    RegionName.SP_STAR_CONNECTION: RegionData(
        exits=(
            RegionName.SP_STAR,
            RegionName.SP_STAR_END,
        ),
    ),
    RegionName.SP_STAR_END: RegionData(
        exits=(RegionName.SP_STAR_CONNECTION,),
    ),
    RegionName.SP_ORBS: RegionData(),
    RegionName.SP_FROG: RegionData(
        exits=(RegionName.SP_CAMPFIRE_2,),
    ),
    RegionName.SP_CAMPFIRE_2: RegionData(
        exits=(RegionName.HOTP_MAIDEN,),
        campfire=True,
    ),
}
