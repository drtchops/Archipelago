from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import Dict, Set

from BaseClasses import Location

from .Regions import Regions


class LocationGroups(str, Enum):
    NONE = ""
    CHARACTERS = "characters"
    ITEMS = "items"
    FAMILIARS = "familiars"
    HEALTH = "health"
    ATTACK = "attack"
    KEYS_WHITE = "white keys"
    KEYS_BLUE = "blue keys"
    KEYS_RED = "red keys"
    SHOP = "shop upgrades"


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
    GT_WHITE_KEY_START = "Gorgon Tomb - White Key (First Room)"
    GT_WHITE_KEY_RIGHT = "Gorgon Tomb - White Key (Right Side)"
    GT_WHITE_KEY_BOSS = "Gorgon Tomb - White Key (Before Boss)"
    GT_BLUE_KEY_BONESNAKE = "Gorgon Tomb - Blue Key (Bonesnakes)"
    GT_BLUE_KEY_BUTT = "Gorgon Tomb - Blue Key (Butt)"
    GT_BLUE_KEY_WALL = "Gorgon Tomb - Blue Key (Inside Wall)"
    GT_BLUE_KEY_POT = "Gorgon Tomb - Blue Key (Pot)"
    GT_RED_KEY = "Gorgon Tomb - Red Key"

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

    DARK_HP_4 = "Darkness - Max HP +4"
    DARK_WHITE_KEY = "Darkness - White Key"

    APEX_CHALICE = "The Apex - Blood Chalice"
    APEX_HP_1_CHALICE = "The Apex - Max HP +1 (Blood Chalice)"
    APEX_HP_5_HEART = "The Apex - Max HP +5 (After Heart)"
    APEX_BLUE_KEY = "The Apex - Blue Key"

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
    CATA_WHITE_KEY_HEAD = "Catacombs - White Key (On Head)"
    CATA_WHITE_KEY_DEV_ROOM = "Catacombs - White Key (Dev Room)"
    CATA_WHITE_KEY_PRISON = "Catacombs - White Key (Prison)"
    CATA_BLUE_KEY_SLIMES = "Catacombs - Blue Key (Slime Water)"
    CATA_BLUE_KEY_EYEBALLS = "Catacombs - Blue Key (Eyeballs)"

    TR_BRAM = "Tower Roots - Bram"
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
    SP_BLUE_KEY_BUBBLES = "Serpent Path - Blue Key (Bubbles)"
    SP_BLUE_KEY_STAR = "Serpent Path - Blue Key (Morning Star)"
    SP_BLUE_KEY_PAINTING = "Serpent Path - Blue Key (Painting)"
    SP_BLUE_KEY_ARIAS = "Serpent Path - Blue Key (Arias)"

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
    Locations.GT_GORGONHEART: AstalonLocationData(Regions.GT_LEFT, LocationGroups.ITEMS),
    Locations.GT_ANCIENTS_RING: AstalonLocationData(Regions.GT_MID, LocationGroups.ITEMS),
    Locations.GT_SWORD: AstalonLocationData(Regions.GT_UPPER, LocationGroups.ITEMS),
    Locations.GT_MAP: AstalonLocationData(Regions.GT_MID, LocationGroups.ITEMS),
    Locations.GT_ASCENDANT_KEY: AstalonLocationData(Regions.GT_LEFT, LocationGroups.ITEMS),
    Locations.GT_BANISH: AstalonLocationData(Regions.GT_LEFT, LocationGroups.ITEMS),
    Locations.GT_VOID: AstalonLocationData(Regions.GT_MID, LocationGroups.ITEMS),
    Locations.GT_EYE_RED: AstalonLocationData(Regions.GT_BOSS, LocationGroups.ITEMS),
    Locations.GT_ATTACK: AstalonLocationData(Regions.GT_START, LocationGroups.ATTACK),
    Locations.GT_HP_1_RING: AstalonLocationData(Regions.GT_MID, LocationGroups.HEALTH),
    Locations.GT_HP_5_KEY: AstalonLocationData(Regions.GT_LEFT, LocationGroups.HEALTH),
    Locations.GT_WHITE_KEY_START: AstalonLocationData(Regions.GT_START, LocationGroups.KEYS_WHITE),
    Locations.GT_WHITE_KEY_RIGHT: AstalonLocationData(Regions.GT_MID, LocationGroups.KEYS_WHITE),
    Locations.GT_WHITE_KEY_BOSS: AstalonLocationData(Regions.GT_LEFT, LocationGroups.KEYS_WHITE),
    Locations.GT_BLUE_KEY_BONESNAKE: AstalonLocationData(Regions.GT_MID, LocationGroups.KEYS_BLUE),
    Locations.GT_BLUE_KEY_BUTT: AstalonLocationData(Regions.GT_LEFT, LocationGroups.KEYS_BLUE),
    Locations.GT_BLUE_KEY_WALL: AstalonLocationData(Regions.GT_LEFT, LocationGroups.KEYS_BLUE),
    Locations.GT_BLUE_KEY_POT: AstalonLocationData(Regions.GT_MID, LocationGroups.KEYS_BLUE),
    Locations.GT_RED_KEY: AstalonLocationData(Regions.GT_BOSS, LocationGroups.KEYS_RED),
    Locations.MECH_BOOTS: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.ITEMS),
    Locations.MECH_CLOAK: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.ITEMS),
    Locations.MECH_EYE_BLUE: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.ITEMS),
    Locations.MECH_ATTACK_VOLANTIS: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.ATTACK),
    Locations.MECH_ATTACK_STAR: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.ATTACK),
    Locations.MECH_HP_1_SWITCH: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.HEALTH),
    Locations.MECH_HP_1_STAR: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.HEALTH),
    Locations.MECH_HP_3_CLAW: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.HEALTH),
    Locations.MECH_WHITE_KEY_LINUS: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_WHITE),
    Locations.MECH_WHITE_KEY_BK: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_WHITE),
    Locations.MECH_WHITE_KEY_ARENA: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_WHITE),
    Locations.MECH_WHITE_KEY_TOP: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_WHITE),
    Locations.MECH_BLUE_KEY_VOID: AstalonLocationData(Regions.GT_MID, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_SNAKE: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_LINUS: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_SACRIFICE: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_RED: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_ARIAS: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_BLOCKS: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_TOP: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_OLD_MAN: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_SAVE: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_BLUE),
    Locations.MECH_BLUE_KEY_POT: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.KEYS_BLUE),
    Locations.MECH_RED_KEY: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_RED),
    Locations.HOTP_BELL: AstalonLocationData(Regions.HOTP_BELL, LocationGroups.ITEMS),
    Locations.HOTP_AMULET: AstalonLocationData(Regions.HOTP_BOTTOM, LocationGroups.ITEMS),
    Locations.HOTP_CLAW: AstalonLocationData(Regions.HOTP_MID, LocationGroups.ITEMS),
    Locations.HOTP_GAUNTLET: AstalonLocationData(Regions.HOTP_UPPER, LocationGroups.ITEMS),
    Locations.HOTP_MAIDEN_RING: AstalonLocationData(Regions.HOTP_UPPER, LocationGroups.ITEMS),
    Locations.HOTP_HP_1_CLAW: AstalonLocationData(Regions.HOTP_MID, LocationGroups.HEALTH),
    Locations.HOTP_HP_2_LADDER: AstalonLocationData(Regions.HOTP_MID, LocationGroups.HEALTH),
    Locations.HOTP_HP_2_GAUNTLET: AstalonLocationData(Regions.HOTP_UPPER, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_OLD_MAN: AstalonLocationData(Regions.HOTP_MID, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_MAZE: AstalonLocationData(Regions.HOTP_START, LocationGroups.HEALTH),
    Locations.HOTP_HP_5_START: AstalonLocationData(Regions.HOTP_START, LocationGroups.HEALTH),
    Locations.HOTP_WHITE_KEY_LEFT: AstalonLocationData(Regions.HOTP_START, LocationGroups.KEYS_WHITE),
    Locations.HOTP_WHITE_KEY_GHOST: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.KEYS_WHITE),
    Locations.HOTP_WHITE_KEY_OLD_MAN: AstalonLocationData(Regions.HOTP_MID, LocationGroups.KEYS_WHITE),
    Locations.HOTP_WHITE_KEY_BOSS: AstalonLocationData(Regions.HOTP_UPPER, LocationGroups.KEYS_WHITE),
    Locations.HOTP_BLUE_KEY_STATUE: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.KEYS_BLUE),
    Locations.HOTP_BLUE_KEY_GOLD: AstalonLocationData(Regions.HOTP_LOWER, LocationGroups.KEYS_BLUE),
    Locations.HOTP_BLUE_KEY_AMULET: AstalonLocationData(Regions.HOTP_BOTTOM, LocationGroups.KEYS_BLUE),
    Locations.HOTP_BLUE_KEY_LADDER: AstalonLocationData(Regions.HOTP_MID, LocationGroups.KEYS_BLUE),
    Locations.HOTP_BLUE_KEY_TELEPORTS: AstalonLocationData(Regions.HOTP_MID, LocationGroups.KEYS_BLUE),
    Locations.HOTP_BLUE_KEY_MAZE: AstalonLocationData(Regions.HOTP_UPPER, LocationGroups.KEYS_BLUE),
    Locations.HOTP_RED_KEY: AstalonLocationData(Regions.HOTP_BELL, LocationGroups.KEYS_RED),
    Locations.ROA_ICARUS: AstalonLocationData(Regions.ROA_UPPER, LocationGroups.ITEMS),
    Locations.ROA_EYE_GREEN: AstalonLocationData(Regions.ROA_UPPER, LocationGroups.ITEMS),
    Locations.ROA_ATTACK: AstalonLocationData(Regions.ROA_MID, LocationGroups.ATTACK),
    Locations.ROA_HP_1_LEFT: AstalonLocationData(Regions.ROA_MID, LocationGroups.HEALTH),
    Locations.ROA_HP_2_RIGHT: AstalonLocationData(Regions.ROA_MID, LocationGroups.HEALTH),
    Locations.ROA_HP_5_SOLARIA: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.ROA_WHITE_KEY_SAVE: AstalonLocationData(Regions.ROA_LOWER, LocationGroups.KEYS_WHITE),
    Locations.ROA_WHITE_KEY_REAPERS: AstalonLocationData(Regions.ROA_LOWER, LocationGroups.KEYS_WHITE),
    Locations.ROA_WHITE_KEY_TORCHES: AstalonLocationData(Regions.ROA_MID, LocationGroups.KEYS_WHITE),
    Locations.ROA_WHITE_KEY_PORTAL: AstalonLocationData(Regions.ROA_MID, LocationGroups.KEYS_WHITE),
    Locations.ROA_BLUE_KEY_FACE: AstalonLocationData(Regions.ROA_LOWER, LocationGroups.KEYS_BLUE),
    Locations.ROA_BLUE_KEY_FLAMES: AstalonLocationData(Regions.ROA_LOWER, LocationGroups.KEYS_BLUE),
    Locations.ROA_BLUE_KEY_BABY: AstalonLocationData(Regions.ROA_MID, LocationGroups.KEYS_BLUE),
    Locations.ROA_BLUE_KEY_TOP: AstalonLocationData(Regions.ROA_UPPER, LocationGroups.KEYS_BLUE),
    Locations.ROA_BLUE_KEY_POT: AstalonLocationData(Regions.ROA_LOWER, LocationGroups.KEYS_BLUE),
    Locations.ROA_RED_KEY: AstalonLocationData(Regions.ROA_UPPER, LocationGroups.KEYS_RED),
    Locations.DARK_HP_4: AstalonLocationData(Regions.DARK, LocationGroups.HEALTH),
    Locations.DARK_WHITE_KEY: AstalonLocationData(Regions.DARK, LocationGroups.KEYS_WHITE),
    Locations.APEX_CHALICE: AstalonLocationData(Regions.APEX, LocationGroups.ITEMS),
    Locations.APEX_HP_1_CHALICE: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.APEX_HP_5_HEART: AstalonLocationData(Regions.APEX, LocationGroups.HEALTH),
    Locations.APEX_BLUE_KEY: AstalonLocationData(Regions.APEX, LocationGroups.KEYS_BLUE),
    Locations.CATA_BOW: AstalonLocationData(Regions.CATA_MID, LocationGroups.ITEMS),
    Locations.CATA_ATTACK_RED: AstalonLocationData(Regions.CATA_UPPER, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_BLUE: AstalonLocationData(Regions.CATA_UPPER, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_GREEN: AstalonLocationData(Regions.CATA_UPPER, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_ROOT: AstalonLocationData(Regions.CATA_UPPER, LocationGroups.ATTACK),
    Locations.CATA_ATTACK_POISON: AstalonLocationData(Regions.CATA_ROOTS, LocationGroups.ATTACK),
    Locations.CATA_HP_1_START: AstalonLocationData(Regions.GT_MID, LocationGroups.HEALTH),
    Locations.CATA_HP_1_CYCLOPS: AstalonLocationData(Regions.CATA_UPPER, LocationGroups.HEALTH),
    Locations.CATA_HP_1_ABOVE_POISON: AstalonLocationData(Regions.CATA_ROOTS, LocationGroups.HEALTH),
    Locations.CATA_HP_2_BEFOER_POISON: AstalonLocationData(Regions.CATA_ROOTS, LocationGroups.HEALTH),
    Locations.CATA_HP_2_AFTER_POISON: AstalonLocationData(Regions.CATA_ROOTS, LocationGroups.HEALTH),
    Locations.CATA_HP_2_GEMINI_BOTTOM: AstalonLocationData(Regions.CATA_LOWER, LocationGroups.HEALTH),
    Locations.CATA_HP_2_GEMINI_TOP: AstalonLocationData(Regions.CATA_LOWER, LocationGroups.HEALTH),
    Locations.CATA_HP_2_ABOVE_GEMINI: AstalonLocationData(Regions.CATA_LOWER, LocationGroups.HEALTH),
    Locations.CATA_HP_5_CHAIN: AstalonLocationData(Regions.CATA_UPPER, LocationGroups.HEALTH),
    Locations.CATA_WHITE_KEY_HEAD: AstalonLocationData(Regions.CATA_MID, LocationGroups.KEYS_WHITE),
    Locations.CATA_WHITE_KEY_DEV_ROOM: AstalonLocationData(Regions.CATA_MID, LocationGroups.KEYS_WHITE),
    Locations.CATA_WHITE_KEY_PRISON: AstalonLocationData(Regions.TR, LocationGroups.KEYS_WHITE),
    Locations.CATA_BLUE_KEY_SLIMES: AstalonLocationData(Regions.CATA_MID, LocationGroups.KEYS_BLUE),
    Locations.CATA_BLUE_KEY_EYEBALLS: AstalonLocationData(Regions.CATA_LOWER, LocationGroups.KEYS_BLUE),
    Locations.TR_ADORNED_KEY: AstalonLocationData(Regions.TR_PROPER, LocationGroups.ITEMS),
    Locations.TR_HP_1_BOTTOM: AstalonLocationData(Regions.TR_PROPER, LocationGroups.HEALTH),
    Locations.TR_HP_2_TOP: AstalonLocationData(Regions.TR_PROPER, LocationGroups.HEALTH),
    Locations.TR_RED_KEY: AstalonLocationData(Regions.TR, LocationGroups.KEYS_RED),
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
    Locations.SP_BLUE_KEY_BUBBLES: AstalonLocationData(Regions.SP, LocationGroups.KEYS_BLUE),
    Locations.SP_BLUE_KEY_STAR: AstalonLocationData(Regions.SP, LocationGroups.KEYS_BLUE),
    Locations.SP_BLUE_KEY_PAINTING: AstalonLocationData(Regions.SP, LocationGroups.KEYS_BLUE),
    Locations.SP_BLUE_KEY_ARIAS: AstalonLocationData(Regions.SP, LocationGroups.KEYS_BLUE),
    Locations.SHOP_GIFT: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_KNOWLEDGE: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_MERCY: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ORB_SEEKER: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_MAP_REVEAL: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_CARTOGRAPHER: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_DEATH_ORB: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_DEATH_POINT: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_TITANS_EGO: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ALGUS_ARCANIST: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ALGUS_SHOCK: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ALGUS_METEOR: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ARIAS_GORGONSLAYER: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ARIAS_LAST_STAND: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ARIAS_LIONHEART: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_KYULI_ASSASSIN: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_KYULI_BULLSEYE: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_KYULI_RAY: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ZEEK_JUNKYARD: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ZEEK_ORBS: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_ZEEK_LOOT: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_BRAM_AXE: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_BRAM_HUNTER: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    Locations.SHOP_BRAM_WHIPLASH: AstalonLocationData(Regions.SHOP, LocationGroups.SHOP),
    # Locations.MECH_ZEEK: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.CHARACTERS),
    # Locations.TR_BRAM: AstalonLocationData(Regions.TR, LocationGroups.CHARACTERS),
    # Locations.GT_OLD_MAN: AstalonLocationData(Regions.GT_UPPER, LocationGroups.FAMILIARS),
    # Locations.MECH_OLD_MAN: AstalonLocationData(Regions.MECH_UPPER, LocationGroups.FAMILIARS),
    # Locations.HOTP_OLD_MAN: AstalonLocationData(Regions.HOTP_MID, LocationGroups.FAMILIARS),
    # Locations.CATA_GIL: AstalonLocationData(Regions.DEV_ROOM, LocationGroups.FAMILIARS),
    # Locations.MECH_CYCLOPS: AstalonLocationData(Regions.MECH_LOWER, LocationGroups.ITEMS),
    # Locations.CD_CROWN: AstalonLocationData(Regions.CD, LocationGroups.ITEMS),
}

base_id = 333000
location_name_to_id: Dict[str, int] = {name.value: base_id + i for i, name in enumerate(location_table)}


def get_location_group(location_name: Locations):
    return location_table[location_name].region


location_name_groups: Dict[str, Set[str]] = {
    group.value: set(location.value for location in location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
