from dataclasses import dataclass
from enum import StrEnum
from typing import Final


class RegionName(StrEnum):
    SHOP = "Shop"
    SHOP_ALGUS = "Algus Shop"
    SHOP_ARIAS = "Arias Shop"
    SHOP_KYULI = "Kyuli Shop"
    SHOP_ZEEK = "Zeek Shop"
    SHOP_BRAM = "Bram Shop"
    FINAL_BOSS = "Top of the Tower"

    GT_ENTRANCE = "GT Entrance"
    GT_BESTIARY = "GT Bestiary"
    GT_BABY_GORGON = "GT Baby Gorgon"
    GT_BOTTOM = "GT Bottom"
    GT_VOID = "GT Void"
    GT_GORGONHEART = "GT Gorgonheart"
    GT_ORBS_DOOR = "GT Blue Door Orbs"
    GT_LEFT = "GT Left"
    GT_ORBS_HEIGHT = "GT Kyuli Orbs"
    GT_ASCENDANT_KEY = "GT Ascendant Key"
    GT_TOP_LEFT = "GT Top Left"
    GT_TOP_RIGHT = "GT Top Right"
    GT_SPIKE_TUNNEL = "GT Spike Tunnel"
    GT_SPIKE_TUNNEL_SWITCH = "GT Spike Tunnel Switch"
    GT_BUTT = "GT Butt"
    GT_BOSS = "GT Boss"
    GT_LADDER_SWITCH = "GT Ladder Switch"
    GT_UPPER_ARIAS = "GT Upper Arias"
    GT_OLD_MAN_FORK = "GT Old Man Fork"
    GT_OLD_MAN = "GT Old Man"
    GT_SWORD_FORK = "GT Sword Fork"
    GT_SWORD = "GT Sword of Mirrors"
    GT_ARIAS_SWORD_SWITCH = "GT Arias Sword Switch"
    GT_UPPER_PATH = "GT Upper Path"
    GT_UPPER_PATH_CONNECTION = "GT Upper Path Connection"

    MECH_START = "Mech Start"
    MECH_SACRIFICE = "Mech Sacrifice"
    MECH_LINUS = "Mech Linus"
    MECH_SWORD_CONNECTION = "Mech Sword Connection"
    MECH_LOWER_ARIAS = "Mech Lower Arias"
    MECH_BOOTS_CONNECTION = "Mech Boots Connection"
    MECH_BOOTS_LOWER = "Mech Boots Lower"
    MECH_BOOTS_UPPER = "Mech Boots Upper"
    MECH_BOTTOM_CAMPFIRE = "Mech Bottom Campfire"
    MECH_SNAKE = "Mech Snake"
    MECH_LOWER_VOID = "Mech Lower Void"
    MECH_WATCHER = "Mech Watcher"
    MECH_ROOTS = "Mech Roots"
    MECH_MUSIC = "Mech Music"
    MECH_BK = "Mech BK"
    MECH_AFTER_BK = "Mech After BK"
    MECH_CHAINS_CANDLE = "Mech Chains Candle"
    MECH_CHAINS = "Mech Chains"
    MECH_ARIAS_EYEBALL = "Mech Arias Eyeball"
    MECH_TRIPLE_SWITCHES = "Mech Triple Switches"
    MECH_ZEEK_CONNECTION = "Mech Zeek Connection"
    MECH_ZEEK = "Mech Zeek"
    MECH_SPLIT_PATH = "Mech Split Path"
    MECH_RIGHT = "Mech Right"
    MECH_OLD_MAN = "Mech Old Man"
    MECH_UPPER_VOID = "Mech Upper Void"
    MECH_BELOW_POTS = "Mech Below Pots"
    MECH_POTS = "Mech Pots"
    MECH_TOP = "Mech Top"
    MECH_CD_ACCESS = "Mech Cyclops Den Access"
    MECH_TP_CONNECTION = "Mech Teleport Connection"
    MECH_CHARACTER_SWAPS = "Mech Character Swaps"
    MECH_CLOAK_CONNECTION = "Mech Cloak Connection"
    MECH_CLOAK = "Mech Cloak"
    MECH_BOSS_SWITCHES = "Mech Boss Switches"
    MECH_BOSS_CONNECTION = "Mech Boss Connection"
    MECH_BRAM_TUNNEL_CONNECTION = "Mech Bram Tunnel Connection"
    MECH_BRAM_TUNNEL = "Mech Bram Tunnel"
    MECH_BOSS = "Mech Boss"

    HOTP_START = "HotP Start"
    HOTP_START_MID = "HotP Start Mid"
    HOTP_LOWER_VOID_CONNECTION = "HotP Lower Void Connection"
    HOTP_LOWER_VOID = "HotP Lower Void"
    HOTP_START_LEFT = "HotP Start Left"
    HOTP_START_BOTTOM = "HotP Start Bottom"
    HOTP_START_BOTTOM_MID = "HotP Start Bottom/Mid Connection"
    HOTP_LOWER = "HotP Lower"
    HOTP_EPIMETHEUS = "HotP Epimetheus"
    HOTP_MECH_VOID_CONNECTION = "HotP Mech Void Connection"
    HOTP_AMULET_CONNECTION = "HotP Amulet Connection"
    HOTP_AMULET = "HotP Amulet of Sol"
    HOTP_TP_TUTORIAL = "HotP Teleport Tutorial"
    HOTP_BELL_CAMPFIRE = "HotP Bell Campfire"
    HOTP_RED_KEY = "HotP Red Key"
    HOTP_BELL = "HotP Bell"
    HOTP_CATH_CONNECTION = "HotP Cathedral Connection"
    HOTP_CATH_VOID = "HotP Cathedral Void"
    HOTP_LOWER_ARIAS = "HotP Lower Arias"
    HOTP_GHOST_BLOOD = "HotP Ghost Blood"
    HOTP_EYEBALL = "HotP Eyeball"
    HOTP_SPIKE_TP_SECRET = "HotP Spike Teleporters Secret"
    HOTP_WORM_SHORTCUT = "HotP Worm Pillar Shortcut"
    HOTP_ELEVATOR = "HotP Elevator"
    HOTP_OLD_MAN = "HotP Old Man"
    HOTP_CLAW_LEFT = "HotP Claw Left"
    HOTP_TOP_LEFT = "HotP Top Left"
    HOTP_ABOVE_OLD_MAN = "HotP Above Old Man"
    HOTP_CLAW_CAMPFIRE = "HotP Claw Campfire"
    HOTP_CLAW = "HotP Griffon Claw"
    HOTP_HEART = "HotP Heart"
    HOTP_UPPER_ARIAS = "HotP Upper Arias"
    HOTP_BOSS_CAMPFIRE = "HotP Boss Campfire"
    HOTP_MAIDEN = "HotP Dead Maiden"
    HOTP_TP_PUZZLE = "HotP Teleport Puzzle"
    HOTP_TP_FALL_TOP = "HotP Teleport Fall Top"
    HOTP_GAUNTLET_CONNECTION = "HotP Gauntlet Connection"
    HOTP_GAUNTLET = "HotP Boreas Gauntlet"
    HOTP_FALL_BOTTOM = "HotP Teleport Fall Bottom"
    HOTP_UPPER_VOID = "HotP Upper Void"
    HOTP_BOSS = "HotP Boss"

    ROA_START = "RoA Start"
    ROA_WORMS = "RoA Worms"
    ROA_WORMS_CONNECTION = "RoA Worms Connection"
    ROA_HEARTS = "RoA Hearts"
    ROA_SPIKE_CLIMB = "RoA Spike Climb"
    ROA_BOTTOM_ASCEND = "RoA Bottom of Ascend"
    ROA_TRIPLE_REAPER = "RoA Triple Reaper"
    ROA_ARENA = "RoA Arena"
    ROA_LOWER_VOID_CONNECTION = "RoA Lower Void Connection"
    ROA_LOWER_VOID = "RoA Lower Void"
    ROA_ARIAS_BABY_GORGON_CONNECTION = "RoA Arias Baby Gorgon Connection"
    ROA_ARIAS_BABY_GORGON = "RoA Arias Baby Gorgon"
    ROA_FLAMES_CONNECTION = "RoA Flames Connection"
    ROA_FLAMES = "RoA Flames"
    ROA_WORM_CLIMB = "RoA Worm Climb"
    ROA_RIGHT_BRANCH = "RoA Right Branch"
    ROA_LEFT_ASCENT = "RoA Left of Ascent"
    ROA_LEFT_ASCENT_CRYSTAL = "RoA Left of Ascent Crystal"
    ROA_TOP_ASCENT = "RoA Top of Ascent"
    ROA_TRIPLE_SWITCH = "RoA Triple Switch"
    ROA_MIDDLE = "RoA Middle"
    ROA_LEFT_BABY_GORGON = "RoA Left Baby Gorgon"
    ROA_LEFT_SWITCH = "RoA Left Switch"
    ROA_RIGHT_SWITCH_1 = "RoA Right Switch 1"
    ROA_RIGHT_SWITCH_2 = "RoA Right Switch 2"
    ROA_RIGHT_SWITCH_CANDLE = "RoA Right Switch Candle"
    ROA_MIDDLE_LADDER = "RoA Middle Ladder"
    ROA_UPPER_VOID = "RoA Upper Void"
    ROA_SPIKE_BALLS = "RoA Spike Balls"
    ROA_SPIKE_SPINNERS = "RoA Spike Spinners"
    ROA_SPIDERS_1 = "RoA Spiders 1"
    ROA_RED_KEY = "RoA Red Key"
    ROA_SPIDERS_2 = "RoA Spiders 2"
    ROA_BLOOD_POT_HALLWAY = "RoA Blood Pot Hallway"
    ROA_SP_CONNECTION = "RoA Serpent Path Connection"
    ROA_ELEVATOR = "RoA Elevator"
    ROA_ICARUS = "RoA Icarus Emblem"
    ROA_DARK_CONNECTION = "RoA Darkness Connection"
    ROA_DARK_EXIT = "RoA Darkness Exit"
    ROA_TOP_CENTAUR = "RoA Top Centaur"
    ROA_ABOVE_CENTAUR_L = "RoA Above Centaur Left"
    ROA_ABOVE_CENTAUR_R = "RoA Above Centaur Right"
    ROA_CRYSTAL_ABOVE_CENTAUR = "RoA Crystal Above Centaur"
    ROA_BOSS_CONNECTION = "RoA Boss Connection"
    ROA_BOSS = "RoA Boss"
    ROA_APEX_CONNECTION = "RoA The Apex Connection"

    DARK_START = "Dark Start"
    DARK_END = "Dark End"

    APEX = "Apex"
    APEX_CENTAUR_ACCESS = "Apex Centaur Access"
    APEX_CENTAUR = "Apex Centaur"
    APEX_HEART = "Apex Heart"

    CAVES_START = "Caves Start"
    CAVES_EPIMETHEUS = "Caves Epimetheus"
    CAVES_UPPER = "Caves Upper"
    CAVES_ARENA = "Caves Arena"
    CAVES_LOWER = "Caves Lower"
    CAVES_ITEM_CHAIN = "Caves Item Chain"

    CATA_START = "Cata Start"
    CATA_CLIMBABLE_ROOT = "Cata Climbable Root"
    CATA_TOP = "Cata Top"
    CATA_ELEVATOR = "Cata Elevator"
    CATA_MULTI = "Cata Orb Multiplier"
    CATA_BOW_CAMPFIRE = "Cata Bow Campfire"
    CATA_BOW_CONNECTION = "Cata Bow Connection"
    CATA_BOW = "Cata Bow"
    CATA_VERTICAL_SHORTCUT = "Cata Vertical Shortcut"
    CATA_EYEBALL_BONES = "Cata Eyeball Bones"
    CATA_SNAKE_MUSHROOMS = "Cata Snake Mushrooms"
    CATA_DEV_ROOM_CONNECTION = "Cata Dev Room Connection"
    CATA_DEV_ROOM = "Cata Dev Room"
    CATA_DOUBLE_SWITCH = "Cata Double Switch"
    CATA_ROOTS_CAMPFIRE = "Cata Roots Campfire"
    CATA_BELOW_ROOTS_CAMPFIRE = "Cata Below Roots Campfire"
    CATA_ABOVE_ROOTS = "Cata Above Roots"
    CATA_POISON_ROOTS = "Cata Poison Roots"
    CATA_BLUE_EYE_DOOR = "Cata Blue Eye Door"
    CATA_FLAMES_FORK = "Cata Flames Fork"
    CATA_FLAMES = "Cata Flames"
    CATA_CENTAUR = "Cata Centaur"
    CATA_4_FACES = "Cata 4 Faces"
    CATA_DOUBLE_DOOR = "Cata Double Door"
    CATA_VOID_R = "Cata Void Right"
    CATA_VOID_L = "Cata Void Left"
    CATA_BOSS = "Cata Boss"

    TR_START = "TR Start"
    TR_BRAM = "TR Bram"
    TR_LEFT = "TR Left"
    TR_BOTTOM_LEFT = "TR Bottom Left"
    TR_TOP_RIGHT = "TR Top Right"
    TR_GOLD = "TR Gold"
    TR_MIDDLE_RIGHT = "TR Middle Right"
    TR_DARK_ARIAS = "TR Dark Arias"
    TR_BOTTOM = "TR Bottom"

    CD_START = "CD Start"
    CD_2 = "CD 2"
    CD_3 = "CD 3"
    CD_MIDDLE = "CD Middle"
    CD_ARIAS_ROUTE = "CD Arias Route"
    CD_KYULI_ROUTE = "CD Kyuli Route"
    CD_CAMPFIRE_3 = "CD Campfire 3"
    CD_ARENA = "CD Arena"
    CD_STEPS = "CD Steps"
    CD_TOP = "CD Top"
    CD_BOSS = "CD Boss"

    CATH_START = "Cath Start"
    CATH_START_RIGHT = "Cath Start Right"
    CATH_START_TOP_LEFT = "Cath Start Top Left"
    CATH_START_LEFT = "Cath Start Left"
    CATH_TP = "Cath Teleport"
    CATH_LEFT_SHAFT = "Cath Left Shaft"
    CATH_UNDER_CAMPFIRE = "Cath Under Campfire"
    CATH_CAMPFIRE_1 = "Cath Campfire 1"
    CATH_SHAFT_ACCESS = "Cath Shaft Access"
    CATH_ORB_ROOM = "Cath Orb Room"
    CATH_GOLD_BLOCK = "Cath Gold Block"
    CATH_RIGHT_SHAFT_CONNECTION = "Cath Right Shaft Connection"
    CATH_RIGHT_SHAFT = "Cath Right Shaft"
    CATH_TOP = "Cath Top"
    CATH_CAMPFIRE_2 = "Cath Campfire 2"
    CATH_UPPER_SPIKE_PIT = "Cath Upper Spike Pit"

    SP_START = "SP Start"
    SP_CAMPFIRE_1 = "SP Campfire 1"
    SP_HEARTS = "SP Hearts"
    SP_PAINTING = "SP Painting"
    SP_SHAFT = "SP Shaft"
    SP_STAR = "SP Star"
    SP_STAR_CONNECTION = "SP Star Connection"
    SP_STAR_END = "SP Star End"
    SP_ORBS = "SP Orbs"
    SP_FROG = "SP Frog"
    SP_CAMPFIRE_2 = "SP Campfire 2"


STARTING_REGIONS: Final[dict[int, str]] = {
    0: RegionName.GT_ENTRANCE.value,
    1: RegionName.MECH_START.value,
    2: RegionName.HOTP_BELL_CAMPFIRE.value,
    3: RegionName.ROA_START.value,
    4: RegionName.APEX.value,
    5: RegionName.CATA_BOW_CAMPFIRE.value,
    6: RegionName.TR_START.value,
}

DEFAULT_PORTALS: Final[tuple[tuple[str, str], ...]] = (
    (RegionName.GT_ENTRANCE.value, RegionName.GT_VOID.value),
    (RegionName.MECH_LOWER_VOID.value, RegionName.MECH_UPPER_VOID.value),
    (RegionName.HOTP_LOWER_VOID.value, RegionName.HOTP_UPPER_VOID.value),
    (RegionName.HOTP_CATH_VOID.value, RegionName.CATH_START.value),
    (RegionName.ROA_LOWER_VOID.value, RegionName.ROA_UPPER_VOID.value),
    (RegionName.CATA_VOID_L.value, RegionName.CATA_VOID_R.value),
)


@dataclass(frozen=True)
class RegionData:
    exits: tuple[RegionName, ...] = ()
    boss: bool = False
    campfire: bool = False
    elevator: bool = False
    multiplier: bool = False
    portal: bool = False
    statue: bool = False
    orbs: int = 0
    description: str = ""


astalon_regions: dict[RegionName, RegionData] = {
    RegionName.SHOP: RegionData(
        exits=(
            RegionName.SHOP_ALGUS,
            RegionName.SHOP_ARIAS,
            RegionName.SHOP_KYULI,
            RegionName.SHOP_ZEEK,
            RegionName.SHOP_BRAM,
        ),
        description="To access the shop, simply die. How convenient!",
    ),
    RegionName.SHOP_ALGUS: RegionData(description="Algus must be unlocked to access his shop."),
    RegionName.SHOP_ARIAS: RegionData(description="Arias must be unlocked to access his shop."),
    RegionName.SHOP_KYULI: RegionData(description="Kyuli must be unlocked to access her shop."),
    RegionName.SHOP_ZEEK: RegionData(description="Zeek must be unlocked to access his shop."),
    RegionName.SHOP_BRAM: RegionData(description="Bram must be unlocked to access his shop."),
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
            RegionName.GT_ENTRANCE,
            RegionName.GT_VOID,
            RegionName.GT_GORGONHEART,
            RegionName.GT_UPPER_PATH,
            RegionName.CAVES_START,
        ),
        campfire=True,
        description="Rooms after the first door, connecting to the caves, containing the GT Bottom campfire",
    ),
    RegionName.GT_VOID: RegionData(
        exits=(
            RegionName.GT_ENTRANCE,
            RegionName.GT_BOTTOM,
            RegionName.MECH_SNAKE,
        ),
        portal=True,
    ),
    RegionName.GT_GORGONHEART: RegionData(
        exits=(
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.HOTP_LOWER_VOID_CONNECTION,
            RegionName.HOTP_START_LEFT,
            RegionName.HOTP_START_BOTTOM_MID,
        ),
    ),
    RegionName.HOTP_LOWER_VOID_CONNECTION: RegionData(
        exits=(
            RegionName.HOTP_START_MID,
            RegionName.HOTP_LOWER_VOID,
        ),
    ),
    RegionName.HOTP_LOWER_VOID: RegionData(
        exits=(
            RegionName.HOTP_LOWER_VOID_CONNECTION,
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
            RegionName.HOTP_CATH_VOID,
        ),
    ),
    RegionName.HOTP_CATH_VOID: RegionData(
        exits=(
            RegionName.HOTP_CATH_CONNECTION,
            RegionName.CATH_START,
        ),
        portal=True,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
        exits=(RegionName.ROA_BOTTOM_ASCEND,),
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
            RegionName.ROA_LOWER_VOID,
            RegionName.ROA_ARIAS_BABY_GORGON_CONNECTION,
        ),
    ),
    RegionName.ROA_LOWER_VOID: RegionData(
        exits=(
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_UPPER_VOID,
        ),
        portal=True,
    ),
    RegionName.ROA_ARIAS_BABY_GORGON_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_ARIAS_BABY_GORGON,
            RegionName.ROA_FLAMES_CONNECTION,
        ),
    ),
    RegionName.ROA_ARIAS_BABY_GORGON: RegionData(
        exits=(
            RegionName.ROA_ARIAS_BABY_GORGON_CONNECTION,
            RegionName.ROA_FLAMES_CONNECTION,
            RegionName.ROA_FLAMES,
        ),
    ),
    RegionName.ROA_FLAMES_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_ARENA,
            RegionName.ROA_LOWER_VOID_CONNECTION,
            RegionName.ROA_ARIAS_BABY_GORGON_CONNECTION,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.ROA_TOP_CENTAUR,
        ),
    ),
    RegionName.DARK_START: RegionData(
        exits=(RegionName.DARK_END,),
    ),
    RegionName.DARK_END: RegionData(
        exits=(RegionName.ROA_DARK_EXIT,),
    ),
    RegionName.ROA_DARK_EXIT: RegionData(
        exits=(
            RegionName.ROA_TOP_CENTAUR,
            RegionName.ROA_ABOVE_CENTAUR_R,
            RegionName.ROA_CRYSTAL_ABOVE_CENTAUR,
        ),
    ),
    RegionName.ROA_TOP_CENTAUR: RegionData(
        exits=(
            RegionName.ROA_DARK_CONNECTION,
            RegionName.ROA_DARK_EXIT,
            RegionName.ROA_BOSS_CONNECTION,
        ),
    ),
    RegionName.ROA_ABOVE_CENTAUR_R: RegionData(
        exits=(
            RegionName.ROA_DARK_EXIT,
            RegionName.ROA_ABOVE_CENTAUR_L,
            RegionName.ROA_CRYSTAL_ABOVE_CENTAUR,
        )
    ),
    RegionName.ROA_ABOVE_CENTAUR_L: RegionData(
        exits=(
            RegionName.ROA_ABOVE_CENTAUR_R,
            RegionName.ROA_BOSS_CONNECTION,
            RegionName.ROA_CRYSTAL_ABOVE_CENTAUR,
        )
    ),
    RegionName.ROA_CRYSTAL_ABOVE_CENTAUR: RegionData(),
    RegionName.ROA_BOSS_CONNECTION: RegionData(
        exits=(
            RegionName.ROA_TOP_CENTAUR,
            RegionName.ROA_ABOVE_CENTAUR_L,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.GT_ENTRANCE,
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
            RegionName.HOTP_CATH_VOID,
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
