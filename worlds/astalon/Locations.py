from dataclasses import dataclass
from enum import Enum
from itertools import groupby

from BaseClasses import Location

from .Regions import Regions


class LocationGroups(str, Enum):
    NONE = ""
    ITEMS = "items"
    FAMILIARS = "familiars"
    HEALTH = "health"
    ATTACK = "attack"
    KEYS_RED = "red keys"


class Locations(str, Enum):
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
    GT_RED_KEY = "Gorgon Tomb - Red Key"

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
    MECH_RED_KEY = "Mechanism - Red Key"

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
    HOTP_RED_KEY = "Hall of the Phantoms - Red Key"

    ROA_ICARUS = "Ruins of Ash - Icarus Emblem"
    ROA_EYE_GREEN = "Ruins of Ash - Gorgon Eye (Green)"
    ROA_ATTACK = "Ruins of Ash - Attack +1"
    ROA_HP_1_LEFT = "Ruins of Ash - Max HP +1 (Left of Ascent)"
    ROA_HP_2_RIGHT = "Ruins of Ash - Max HP +2 (Right Side)"
    ROA_HP_5_SOLARIA = "Ruins of Ash - Max HP +5 (After Solaria)"
    ROA_RED_KEY = "Ruins of Ash - Red Key"

    DARK_HP_4 = "Darkness - Max HP +4"

    APEX_CHALICE = "The Apex - Blood Chalice"
    APEX_HP_1_CHALICE = "The Apex - Max HP +1 (Blood Chalice)"
    APEX_HP_5_HEART = "The Apex - Max HP +5 (After Heart)"

    CATA_BOW = "Catacombs - Lunarian Bow"
    CATA_GIL = "Catacombs - Gil"
    CATA_ATTACK_RED = "Catacombs - Attack +1 (Item Chain Red)"
    CATA_ATTACK_BLUE = "Catacombs - Attack +1 (Item Chain Blue)"
    CATA_ATTACK_GREEN = "Catacombs - Attack +1 (Item Chain Green)"
    CATA_ATTACK_ROOT = "Catacombs - Attack +1 (Climbable Root)"
    CATA_ATTACK_POISON = "Catacombs - Attack +1 (Poison Roots)"
    CATA_HP_1_START = "Catacombs - Max HP +1 (First Room)"
    CATA_HP_1_CYCLOPS = "Catacombs - Max HP +1 (Cyclops Arena)"
    CATA_HP_1_ABOVE_POISON = "Catacombs - Max HP +1 (Above Poison Roots)"
    CATA_HP_2_BEFOER_POISON = "Catacombs - Max HP +2 (Before Poison Roots)"
    CATA_HP_2_AFTER_POISON = "Catacombs - Max HP +2 (After Poison Roots)"
    CATA_HP_2_GEMINI_BOTTOM = "Catacombs - Max HP +2 (Before Gemini Bottom)"
    CATA_HP_2_GEMINI_TOP = "Catacombs - Max HP +2 (Before Gemini Top)"
    CATA_HP_2_ABOVE_GEMINI = "Catacombs - Max HP +2 (Above Gemini)"
    CATA_HP_5_CHAIN = "Catacombs - Max HP +5 (Item Chain)"

    TR_ADORNED_KEY = "Tower Roots - Adorned Key"
    TR_HP_1_BOTTOM = "Tower Roots - Max HP +1 (Bottom)"
    TR_HP_2_TOP = "Tower Roots - Max HP +2 (Top)"
    TR_RED_KEY = "Tower Roots - Red Key"

    CD_CROWN = "Cyclops Den - Prince's Crown"
    CD_ATTACK = "Cyclops Den - Attack +1"
    CD_HP_1 = "Cyclops Den - Max HP +1"

    CATH_BLOCK = "Cathedral - Magic Block"
    CATH_ATTACK = "Cathedral - Attack +1"
    CATH_HP_1_TOP_LEFT = "Cathedral - Max HP +1 (Top Left)"
    CATH_HP_1_TOP_RIGHT = "Cathedral - Max HP +1 (Top Right)"
    CATH_HP_2_CLAW = "Cathedral - Max HP +2 (Left Climb)"
    CATH_HP_5_BELL = "Cathedral - Max HP +5 (Bell)"

    SP_STAR = "Serpent Path - Morning Star"
    SP_ATTACK = "Serpent Path - Attack +1"
    SP_HP_1 = "Serpent Path - Max HP +1"

    VICTORY = "Victory"


class AstalonLocation(Location):
    game = "Astalon"


@dataclass
class AstalonLocationData:
    region: Regions
    item_group: LocationGroups = LocationGroups.NONE


location_table: dict[Locations, AstalonLocationData] = {
    Locations.GT_GORGONHEART: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_ANCIENTS_RING: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_SWORD: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_MAP: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_ASCENDANT_KEY: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_BANISH: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_VOID: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    Locations.GT_EYE_RED: AstalonLocationData(Regions.GT, LocationGroups.ITEMS),
    # Locations.GT_OLD_MAN: AstalonLocationData(Regions.GT, LocationGroups.FAMILIARS),
    Locations.GT_ATTACK: AstalonLocationData(Regions.GT, LocationGroups.ATTACK),
    Locations.GT_HP_1_RING: AstalonLocationData(Regions.GT, LocationGroups.HEALTH),
    Locations.GT_HP_5_KEY: AstalonLocationData(Regions.GT, LocationGroups.HEALTH),
    Locations.GT_RED_KEY: AstalonLocationData(Regions.GT, LocationGroups.KEYS_RED),
    Locations.MECH_BOOTS: AstalonLocationData(Regions.MECH, LocationGroups.ITEMS),
    Locations.MECH_CLOAK: AstalonLocationData(Regions.MECH, LocationGroups.ITEMS),
    # Locations.MECH_CYCLOPS: AstalonLocationData(Regions.MECH, LocationGroups.ITEMS),
    Locations.MECH_EYE_BLUE: AstalonLocationData(Regions.MECH, LocationGroups.ITEMS),
    # Locations.MECH_OLD_MAN: AstalonLocationData(Regions.MECH, LocationGroups.FAMILIARS),
    Locations.MECH_ATTACK_VOLANTIS: AstalonLocationData(Regions.MECH, LocationGroups.ATTACK),
    Locations.MECH_ATTACK_STAR: AstalonLocationData(Regions.MECH, LocationGroups.ATTACK),
    Locations.MECH_HP_1_SWITCH: AstalonLocationData(Regions.MECH, LocationGroups.HEALTH),
    Locations.MECH_HP_1_STAR: AstalonLocationData(Regions.MECH, LocationGroups.HEALTH),
    Locations.MECH_HP_3_CLAW: AstalonLocationData(Regions.MECH, LocationGroups.HEALTH),
    Locations.MECH_RED_KEY: AstalonLocationData(Regions.MECH, LocationGroups.KEYS_RED),
    Locations.HOTP_BELL: AstalonLocationData(Regions.HOTP, LocationGroups.ITEMS),
    Locations.HOTP_AMULET: AstalonLocationData(Regions.HOTP, LocationGroups.ITEMS),
    Locations.HOTP_CLAW: AstalonLocationData(Regions.HOTP, LocationGroups.ITEMS),
    Locations.HOTP_GAUNTLET: AstalonLocationData(Regions.HOTP, LocationGroups.ITEMS),
    Locations.HOTP_MAIDEN_RING: AstalonLocationData(Regions.HOTP, LocationGroups.ITEMS),
    # Locations.HOTP_OLD_MAN: AstalonLocationData(Regions.HOTP, LocationGroups.FAMILIARS),
    Locations.HOTP_HP_1_CLAW: AstalonLocationData(Regions.HOTP, LocationGroups.HEALTH),
    Locations.HOTP_HP_2_LADDER: AstalonLocationData(Regions.HOTP, LocationGroups.HEALTH),
    Locations.HOTP_HP_2_GAUNTLET: AstalonLocationData(Regions.HOTP, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_OLD_MAN: AstalonLocationData(Regions.HOTP, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_MAZE: AstalonLocationData(Regions.HOTP, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_START: AstalonLocationData(Regions.HOTP, LocationGroups.HEALTH),
    Locations.HOTP_RED_KEY: AstalonLocationData(Regions.HOTP, LocationGroups.KEYS_RED),
    Locations.ROA_ICARUS: AstalonLocationData(Regions.ROA, LocationGroups.ITEMS),
    Locations.ROA_EYE_GREEN: AstalonLocationData(Regions.ROA, LocationGroups.ITEMS),
    Locations.ROA_ATTACK: AstalonLocationData(Regions.ROA, LocationGroups.ATTACK),
    Locations.ROA_HP_1_LEFT: AstalonLocationData(Regions.ROA, LocationGroups.HEALTH),
    Locations.ROA_HP_2_RIGHT: AstalonLocationData(Regions.ROA, LocationGroups.HEALTH),
    # this is visually RoA but logically Apex
    Locations.ROA_HP_5_SOLARIA: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.ROA_RED_KEY: AstalonLocationData(Regions.ROA, LocationGroups.KEYS_RED),
    Locations.DARK_HP_4: AstalonLocationData(Regions.DARK, LocationGroups.HEALTH),
    Locations.APEX_CHALICE: AstalonLocationData(Regions.APEX, LocationGroups.ITEMS),
    Locations.APEX_HP_1_CHALICE: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.APEX_HP_5_HEART: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.CATA_BOW: AstalonLocationData(Regions.CATA, LocationGroups.ITEMS),
    # Locations.CATA_GIL: AstalonLocationData(Regions.CATA, LocationGroups.FAMILIARS),
    Locations.CATA_ATTACK_RED: AstalonLocationData(Regions.CATA, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_BLUE: AstalonLocationData(Regions.CATA, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_GREEN: AstalonLocationData(Regions.CATA, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_ROOT: AstalonLocationData(Regions.CATA, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_POISON: AstalonLocationData(Regions.CATA, LocationGroups.ATTACK),
    Locations.CATA_HP_1_START: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_1_CYCLOPS: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_1_ABOVE_POISON: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_2_BEFOER_POISON: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_2_AFTER_POISON: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_2_GEMINI_BOTTOM: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_2_GEMINI_TOP: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_2_ABOVE_GEMINI: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.CATA_HP_5_CHAIN: AstalonLocationData(Regions.CATA, LocationGroups.HEALTH),
    Locations.TR_ADORNED_KEY: AstalonLocationData(Regions.TR, LocationGroups.ITEMS),
    Locations.TR_HP_1_BOTTOM: AstalonLocationData(Regions.TR, LocationGroups.HEALTH),
    Locations.TR_HP_2_TOP: AstalonLocationData(Regions.TR, LocationGroups.HEALTH),
    Locations.TR_RED_KEY: AstalonLocationData(Regions.TR, LocationGroups.KEYS_RED),
    # Locations.CD_CROWN: AstalonLocationData(Regions.CD, LocationGroups.ITEMS),
    Locations.CD_ATTACK: AstalonLocationData(Regions.CD, LocationGroups.ATTACK),
    Locations.CD_HP_1: AstalonLocationData(Regions.CD, LocationGroups.HEALTH),
    Locations.CATH_BLOCK: AstalonLocationData(Regions.CATH, LocationGroups.ITEMS),
    Locations.CATH_ATTACK: AstalonLocationData(Regions.CATH, LocationGroups.ATTACK),
    Locations.CATH_HP_1_TOP_LEFT: AstalonLocationData(Regions.CATH, LocationGroups.HEALTH),
    Locations.CATH_HP_1_TOP_RIGHT: AstalonLocationData(Regions.CATH, LocationGroups.HEALTH),
    Locations.CATH_HP_2_CLAW: AstalonLocationData(Regions.CATH, LocationGroups.HEALTH),
    Locations.CATH_HP_5_BELL: AstalonLocationData(Regions.CATH, LocationGroups.HEALTH),
    Locations.SP_STAR: AstalonLocationData(Regions.SP, LocationGroups.ITEMS),
    Locations.SP_ATTACK: AstalonLocationData(Regions.SP, LocationGroups.ATTACK),
    Locations.SP_HP_1: AstalonLocationData(Regions.SP, LocationGroups.HEALTH),
}

base_id = 333000
location_name_to_id: dict[str, int] = {name.value: base_id + i for i, name in enumerate(location_table)}


def get_location_group(location_name: Locations):
    return location_table[location_name].region


location_name_groups: dict[str, set[str]] = {
    group.value: set(location.value for location in location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
