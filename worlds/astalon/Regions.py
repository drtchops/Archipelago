from enum import Enum


class Regions(str, Enum):
    MENU = "Menu"
    GT = "Gorgon Tomb"
    MECH = "Mechanism"
    HOTP = "Hall of the Phantoms"
    ROA = "Ruins of Ash"
    DARK = "Darkness"
    APEX = "The Apex"
    BOSS = "Final Boss"
    CATA = "Catacombs"
    TR = "Tower Roots"
    CD = "Cyclops Den"
    CATH = "Cathedral"
    SP = "Serpent Path"


astalon_regions: dict[Regions, set[Regions]] = {
    Regions.MENU: {Regions.GT},
    Regions.GT: {Regions.MECH, Regions.APEX, Regions.CATA},
    Regions.MECH: {Regions.HOTP, Regions.CD},
    Regions.HOTP: {Regions.ROA, Regions.CATH},
    Regions.ROA: {Regions.DARK, Regions.APEX, Regions.SP},
    Regions.DARK: set(),
    Regions.APEX: {Regions.BOSS},
    Regions.BOSS: set(),
    Regions.CATA: {Regions.TR},
    Regions.TR: set(),
    Regions.CD: set(),
    Regions.CATH: set(),
    Regions.SP: set(),
}
