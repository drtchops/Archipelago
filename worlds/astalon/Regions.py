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


astalon_regions: Dict[Regions, Set[Regions]] = {
    Regions.MENU: {Regions.GT_START, Regions.SHOP},
    Regions.SHOP: set(),
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
