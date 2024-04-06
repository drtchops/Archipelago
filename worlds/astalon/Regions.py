from enum import Enum
from typing import Dict, Set


class Regions(str, Enum):
    MENU = "Menu"
    SHOP = "Shop"
    GT_START = "Gorgon Tomb Start"
    GT_MID = "Gorgon Tomb Mid"
    GT_LEFT = "Gorgon Tomb Left"
    GT_BOSS = "Gorgon Tomb Boss"
    GT_UPPER = "Gorgon Tomb Upper"
    MECH_LOWER = "Mechanism Lower"
    MECH_UPPER = "Mechanism Upper"
    HOTP_START = "Hall of the Phantoms Start"
    HOTP_LOWER = "Hall of the Phantoms Lower"
    HOTP_BELL = "Hall of the Phantoms Bell"
    HOTP_BOTTOM = "Hall of the Phantoms Bottom"
    HOTP_MID = "Hall of the Phantoms Mid"
    HOTP_UPPER = "Hall of the Phantoms Upper"
    ROA_LOWER = "Ruins of Ash Lower"
    ROA_MID = "Ruins of Ash Mid"
    ROA_UPPER = "Ruins of Ash Upper"
    DARK = "Darkness"
    APEX = "The Apex"
    BOSS = "Final Boss"
    CATA_UPPER = "Catacombs Upper"
    CATA_MID = "Catacombs Mid"
    CATA_ROOTS = "Catacombs Roots"
    CATA_LOWER = "Catacombs Lower"
    DEV_ROOM = "Dev Room"
    TR = "Tower Roots"
    TR_PROPER = "Tower Roots Proper"
    CD = "Cyclops Den"
    CATH = "Cathedral"
    SP = "Serpent Path"

    ENTRANCE = "ENTRANCE"
    BESTIARY = "BESTIARY"
    GT_BABY_GORGON = "GT_BABY_GORGON"
    GT_BOTTOM = "GT_BOTTOM"
    GT_VOID = "GT_VOID"
    GT_GORGONHEART = "GT_GORGONHEART"
    GT_ORBS_DOOR = "GT_ORBS_DOOR"
    GT_LEFT = "GT_LEFT"
    GT_ORBS_HEIGHT = "GT_ORBS_HEIGHT"
    GT_ASCENDANT_KEY = "GT_ASENDANT_KEY"
    GT_ARIAS = "GT_ARIAS"
    GT_TOP_LEFT = "GT_TOP_LEFT"
    GT_TOP_RIGHT = "GT_TOP_RIGHT"
    GT_SPIKE_TUNNEL = "GT_SPIKE_TUNNEL"
    GT_BUTT = "GT_BUTT"
    GT_BOSS = "GT_BOSS"
    GT_LADDER_SWITCH = "GT_LADDER_SWITCH"
    GT_UPPER_ARIAS = "GT_UPPER_ARIAS"
    GT_OLD_MAN_FORK = "GT_OLD_MAN_FORK"
    GT_OLD_MAN = "GT_OLD_MAN"
    GT_SWORD_FORK = "GT_SWORD_FORK"
    GT_SWORD = "GT_SWORD"
    GT_ARIAS_SWORD_SWITCH = "GT_ARIAS_SWORD_SWITCH"
    GT_UPPER_PATH = "GT_UPPER_PATH"
    GT_UPPER_PATH_CONNECTION = "GT_UPPER_PATH_CONNECTION"

    MECH_ENTRANCE = "MECH_ENTRANCE"
    MECH_SACRIFICE = "MECH_SACRIFICE"
    MECH_LINUS = "MECH_LINUS"
    MECH_SWORD_CONNECTION = "MECH_SWORD_CONNECTION"
    MECH_LOWER_ARIAS = "MECH_LOWER_ARIAS"
    MECH_BOOTS_CONNECTION = "MECH_BOOTS_CONNECTION"
    MECH_BOOTS_LOWER = "MECH_BOOTS_LOWER"
    MECH_BOOTS_UPPER = "MECH_BOOTS_UPPER"
    MECH_BOTTOM_CAMPFIRE = "MECH_BOTTOM_CAMPFIRE"
    MECH_SNAKE = "MECH_SNAKE"
    MECH_LOWER_VOID = "MECH_LOWER_VOID"
    MECH_ROOTS = "MECH_ROOTS"
    MECH_MUSIC = "MECH_MUSIC"
    MECH_BK = "MECH_BK"
    MECH_AFTER_BK = "MECH_AFTER_BK"
    MECH_CHAINS = "MECH_CHAINS"
    MECH_ARIAS_EYEBALL = "MECH_ARIAS_EYEBALL"
    MECH_ZEEK_CONNECTION = "MECH_ZEEK_CONNECTION"
    MECH_ZEEK = "MECH_ZEEK"
    MECH_SPLIT_PATH = "MECH_SPLIT_PATH"
    MECH_RIGHT = "MECH_RIGHT"
    MECH_OLD_MAN = "MECH_OLD_MAN"
    MECH_UPPER_VOID = "MECH_UPPER_VOID"
    MECH_POTS = "MECH_POTS"
    MECH_TOP = "MECH_TOP"
    MECH_TELEPORT_CONNECTION = "MECH_TELEPORT_CONNECTION"
    MECH_CHARACTER_SWAPS = "MECH_CHARACTER_SWAPS"
    MECH_CLOAK_CONNECTION = "MECH_CLOAK_CONNECTION"
    MECH_CLOAK = "MECH_CLOAK"
    MECH_BOSS_SWITCHES = "MECH_BOSS_SWITCHES"
    MECH_BOSS_CONNECTION = "MECH_BOSS_CONNECTION"
    MECH_BRAM_TUNNEL = "MECH_BRAM_TUNNEL"
    MECH_BOSS = "MECH_BOSS"

    HOTP_ENTRANCE = "HOTP_ENTRANCE"
    HOTP_EPIMETHEUS = "HOTP_EPIMETHEUS"

    CAVES_ENTRANCE = "CAVES_ENTRANCE"
    CAVES_STATUE = "CAVES_STATUE"

    CD_ENTRANCE = "CD_ENTRANCE"


astalon_regions: Dict[Regions, Set[Regions]] = {
    Regions.MENU: {Regions.ENTRANCE, Regions.SHOP},
    Regions.SHOP: set(),
    # elevators
    Regions.ENTRANCE: {Regions.BESTIARY, Regions.GT_BABY_GORGON, Regions.GT_BOTTOM, Regions.GT_GORGONHEART},
    Regions.BESTIARY: set(),
    Regions.GT_BABY_GORGON: set(),
    Regions.GT_BOTTOM: {Regions.GT_VOID, Regions.GT_GORGONHEART, Regions.GT_UPPER_PATH, Regions.CAVES_ENTRANCE},
    Regions.GT_VOID: {Regions.GT_BOTTOM, Regions.MECH_SNAKE},
    Regions.GT_GORGONHEART: {Regions.GT_BOTTOM, Regions.GT_ORBS_DOOR, Regions.GT_LEFT},
    Regions.GT_ORBS_DOOR: set(),
    Regions.GT_LEFT: {
        Regions.GT_GORGONHEART,
        Regions.GT_ORBS_HEIGHT,
        Regions.GT_ASCENDANT_KEY,
        Regions.GT_ARIAS,
        Regions.GT_TOP_LEFT,
        Regions.GT_TOP_RIGHT,
    },
    Regions.GT_ORBS_HEIGHT: set(),
    Regions.GT_ASCENDANT_KEY: set(),
    Regions.GT_ARIAS: {Regions.GT_TOP_LEFT},
    Regions.GT_TOP_LEFT: {Regions.GT_LEFT, Regions.GT_TOP_LEFT, Regions.GT_BUTT},
    Regions.GT_TOP_RIGHT: {Regions.GT_LEFT, Regions.GT_SPIKE_TUNNEL},
    Regions.GT_SPIKE_TUNNEL: {Regions.GT_TOP_RIGHT, Regions.GT_BUTT},
    Regions.GT_BUTT: {Regions.GT_TOP_LEFT, Regions.GT_SPIKE_TUNNEL, Regions.GT_BOSS},
    # elevators
    Regions.GT_BOSS: {Regions.GT_BUTT, Regions.MECH_ENTRANCE},
    Regions.GT_LADDER_SWITCH: set(),
    Regions.GT_UPPER_ARIAS: {Regions.GT_OLD_MAN_FORK, Regions.MECH_SWORD_CONNECTION},
    Regions.GT_OLD_MAN_FORK: {Regions.GT_UPPER_ARIAS, Regions.GT_OLD_MAN, Regions.GT_SWORD_FORK},
    Regions.GT_OLD_MAN: set(),
    Regions.GT_SWORD_FORK: {Regions.GT_OLD_MAN_FORK, Regions.GT_SWORD, Regions.GT_ARIAS_SWORD_SWITCH},
    Regions.GT_SWORD: set(),
    Regions.GT_ARIAS_SWORD_SWITCH: set(),
    Regions.GT_UPPER_PATH: {Regions.GT_BOTTOM, Regions.GT_UPPER_PATH_CONNECTION},
    Regions.GT_UPPER_PATH_CONNECTION: {Regions.MECH_SWORD_CONNECTION},
    #
    Regions.MECH_ENTRANCE: {
        Regions.GT_BOSS,
        Regions.GT_LADDER_SWITCH,
        Regions.MECH_SACRIFICE,
        Regions.MECH_LINUS,
        Regions.MECH_LOWER_VOID,
        Regions.MECH_BK,
        Regions.MECH_ROOTS,
    },
    Regions.MECH_SACRIFICE: set(),
    Regions.MECH_LINUS: {Regions.MECH_ENTRANCE, Regions.MECH_SWORD_CONNECTION},
    Regions.MECH_SWORD_CONNECTION: {
        Regions.GT_UPPER_ARIAS,
        Regions.GT_UPPER_PATH_CONNECTION,
        Regions.MECH_LINUS,
        Regions.MECH_LOWER_ARIAS,
        Regions.MECH_BOOTS_CONNECTION,
        Regions.MECH_BOTTOM_CAMPFIRE,
    },
    Regions.MECH_LOWER_ARIAS: set(),
    Regions.MECH_BOOTS_CONNECTION: {
        Regions.MECH_SWORD_CONNECTION,
        Regions.MECH_BOOTS_LOWER,
        Regions.MECH_BOTTOM_CAMPFIRE,
    },
    Regions.MECH_BOOTS_LOWER: {Regions.MECH_BOOTS_UPPER},
    Regions.MECH_BOOTS_UPPER: set(),
    Regions.MECH_BOTTOM_CAMPFIRE: {Regions.MECH_SWORD_CONNECTION, Regions.MECH_BOOTS_CONNECTION, Regions.MECH_SNAKE},
    Regions.MECH_SNAKE: {Regions.GT_VOID, Regions.MECH_BOTTOM_CAMPFIRE},
    Regions.MECH_LOWER_VOID: {Regions.MECH_ENTRANCE, Regions.HOTP_SOMETHING},
    Regions.MECH_ROOTS: {Regions.MECH_ENTRANCE, Regions.MECH_MUSIC, Regions.MECH_BK, Regions.MECH_ZEEK_CONNECTION},
    Regions.MECH_MUSIC: set(),
    Regions.MECH_BK: {Regions.MECH_ENTRANCE, Regions.MECH_ROOTS, Regions.MECH_AFTER_BK},
    Regions.MECH_AFTER_BK: {Regions.MECH_BK, Regions.MECH_CHAINS, Regions.HOTP_EPIMETHEUS},
    Regions.MECH_CHAINS: {
        Regions.MECH_AFTER_BK,
        Regions.MECH_ARIAS_EYEBALL,
        Regions.MECH_SPLIT_PATH,
        Regions.MECH_BOSS_SWITCHES,
        Regions.MECH_BOSS_CONNECTION,
    },
    Regions.MECH_ARIAS_EYEBALL: {Regions.MECH_CHAINS, Regions.MECH_ZEEK_CONNECTION},
    Regions.MECH_ZEEK_CONNECTION: {Regions.MECH_ROOTS, Regions.MECH_ARIAS_EYEBALL, Regions.MECH_ZEEK},
    Regions.MECH_ZEEK: set(),
    Regions.MECH_SPLIT_PATH: {Regions.MECH_CHAINS, Regions.MECH_RIGHT},
    Regions.MECH_RIGHT: {Regions.MECH_SPLIT_PATH, Regions.MECH_OLD_MAN, Regions.MECH_UPPER_VOID, Regions.MECH_POTS},
    Regions.MECH_OLD_MAN: set(),
    Regions.MECH_UPPER_VOID: {Regions.MECH_LOWER_VOID, Regions.MECH_RIGHT},
    Regions.MECH_POTS: {Regions.MECH_RIGHT, Regions.MECH_TOP},
    Regions.MECH_TOP: {Regions.MECH_POTS, Regions.MECH_TELEPORT_CONNECTION, Regions.CD_ENTRANCE},
    Regions.MECH_TELEPORT_CONNECTION: {Regions.MECH_TOP, Regions.MECH_CHARACTER_SWAPS, Regions.HOTP_SOMETHING},
    Regions.MECH_CHARACTER_SWAPS: {Regions.MECH_TELEPORT_CONNECTION, Regions.MECH_CLOAK_CONNECTION},
    Regions.MECH_CLOAK_CONNECTION: {Regions.MECH_CHARACTER_SWAPS, Regions.MECH_CLOAK, Regions.MECH_BOSS_SWITCHES},
    Regions.MECH_CLOAK: set(),
    Regions.MECH_BOSS_SWITCHES: {Regions.MECH_CHAINS, Regions.MECH_CLOAK_CONNECTION, Regions.MECH_BOSS_CONNECTION},
    Regions.MECH_BOSS_CONNECTION: {
        Regions.MECH_CHAINS,
        Regions.MECH_BOSS_SWITCHES,
        Regions.MECH_BRAM_TUNNEL,
        Regions.MECH_BOSS,
    },
    Regions.MECH_BRAM_TUNNEL: {Regions.MECH_BOSS_CONNECTION, Regions.HOTP_SOMETHING},
    # elevators
    Regions.MECH_BOSS: {Regions.MECH_BOSS_CONNECTION, Regions.HOTP_ENTRANCE},
    #
    Regions.HOTP_EPIMETHEUS: set(),
    #
    Regions.CAVES_ENTRANCE: {Regions.GT_BOTTOM, Regions.CAVES_STATUE},
    Regions.CAVES_STATUE: set(),
    #
    Regions.GT_START: {Regions.GT_MID, Regions.GT_LEFT, Regions.APEX},
    Regions.GT_MID: {Regions.GT_LEFT, Regions.CATA_UPPER},
    Regions.GT_LEFT: {Regions.GT_BOSS, Regions.GT_MID},
    Regions.GT_BOSS: {Regions.MECH_LOWER},
    Regions.GT_UPPER: set(),
    Regions.MECH_LOWER: {Regions.MECH_UPPER, Regions.HOTP_BOTTOM, Regions.HOTP_LOWER, Regions.GT_UPPER},
    Regions.MECH_UPPER: {Regions.HOTP_START, Regions.HOTP_UPPER, Regions.CD},
    Regions.HOTP_BOTTOM: {Regions.HOTP_LOWER},
    Regions.HOTP_LOWER: {Regions.HOTP_BELL, Regions.MECH_LOWER},
    Regions.HOTP_START: {Regions.HOTP_UPPER, Regions.HOTP_LOWER, Regions.MECH_UPPER},
    Regions.HOTP_BELL: {Regions.HOTP_MID, Regions.CATH},
    Regions.HOTP_MID: {Regions.HOTP_UPPER, Regions.HOTP_BELL, Regions.HOTP_START},
    Regions.HOTP_UPPER: {Regions.ROA_LOWER, Regions.HOTP_MID, Regions.HOTP_START, Regions.MECH_UPPER},
    Regions.ROA_LOWER: {Regions.ROA_MID},
    Regions.ROA_MID: {Regions.ROA_UPPER},
    Regions.ROA_UPPER: {Regions.APEX, Regions.DARK, Regions.SP},
    Regions.DARK: set(),
    Regions.APEX: {Regions.BOSS},
    Regions.BOSS: set(),
    Regions.CATA_UPPER: {Regions.CATA_MID},
    Regions.CATA_MID: {Regions.CATA_LOWER, Regions.CATA_ROOTS, Regions.DEV_ROOM},
    Regions.CATA_ROOTS: set(),
    Regions.CATA_LOWER: {Regions.TR},
    Regions.DEV_ROOM: set(),
    Regions.TR: {Regions.TR_PROPER},
    Regions.TR_PROPER: set(),
    Regions.CD: set(),
    Regions.CATH: set(),
    Regions.SP: set(),
}
