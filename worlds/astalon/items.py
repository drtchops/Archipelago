from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from functools import cached_property
from itertools import groupby
from typing import TypeAlias

from BaseClasses import Item, ItemClassification

from .constants import GAME_NAME
from .options import AstalonOptions, StartingLocation


class ItemGroup(StrEnum):
    CHARACTER = "Characters"
    EYE = "Eyes"
    KEY = "Keys"
    ITEM = "Items"
    ATTACK = "Attack"
    HEALTH = "Health"
    ORBS = "Orbs"
    DOOR_WHITE = "White Doors"
    DOOR_BLUE = "Blue Doors"
    DOOR_RED = "Red Doors"
    SHOP = "Shop Upgrades"
    ELEVATOR = "Elevators"
    SWITCH = "Switches"
    HEAL = "Heal"
    TRAP = "Trap"


class Character(StrEnum):
    ARIAS = "Arias"
    KYULI = "Kyuli"
    ALGUS = "Algus"
    ZEEK = "Zeek"
    BRAM = "Bram"


class Eye(StrEnum):
    RED = "Gorgon Eye Red"
    BLUE = "Gorgon Eye Blue"
    GREEN = "Gorgon Eye Green"
    GOLD = "Gorgon Eye Gold"


class Key(StrEnum):
    WHITE = "White Key"
    BLUE = "Blue Key"
    RED = "Red Key"


class KeyItem(StrEnum):
    GORGONHEART = "Gorgonheart"
    ANCIENTS_RING = "Ring of the Ancients"
    MAIDEN_RING = "Dead Maiden's Ring"
    SWORD = "Sword of Mirrors"
    MAP = "Linus' Map"
    ASCENDANT_KEY = "Ascendant Key"
    ADORNED_KEY = "Adorned Key"
    BANISH = "Banish Spell"
    VOID = "Void Charm"
    BOOTS = "Talaria Boots"
    CLOAK = "Cloak of Levitation"
    CYCLOPS = "Cyclops Idol"
    BELL = "Athena's Bell"
    AMULET = "Amulet of Sol"
    CLAW = "Griffon Claw"
    GAUNTLET = "Boreas Gauntlet"
    ICARUS = "Icarus Emblem"
    CHALICE = "Blood Chalice"
    BOW = "Lunarian Bow"
    CROWN = "Prince's Crown"
    BLOCK = "Magic Block"
    STAR = "Morning Star"


class Upgrade(StrEnum):
    ATTACK_1 = "Attack +1"
    MAX_HP_1 = "Max HP +1"
    MAX_HP_2 = "Max HP +2"
    MAX_HP_3 = "Max HP +3"
    MAX_HP_4 = "Max HP +4"
    MAX_HP_5 = "Max HP +5"


class Orbs(StrEnum):
    ORBS_200 = "200 Orbs"
    ORBS_500 = "500 Orbs"
    ORBS_1000 = "1000 Orbs"
    ORB_MULTI = "Orb Multiplier"


class WhiteDoor(StrEnum):
    GT_START = "White Door GT 1st Room"
    GT_MAP = "White Door GT Linus' Map"
    GT_TAUROS = "White Door GT Boss"
    MECH_2ND = "White Door Mech 2nd Room"
    MECH_BK = "White Door Mech Black Knight"
    MECH_ARENA = "White Door Mech Enemy Arena"
    MECH_TOP = "White Door Mech Top"
    HOTP_START = "White Door HotP 1st Room"
    HOTP_CLAW = "White Door HotP Griffon Claw"
    HOTP_BOSS = "White Door HotP Boss"
    ROA_WORMS = "White Door RoA Worms"
    ROA_ASCEND = "White Door RoA Ascend"
    ROA_BALLS = "White Door RoA Spike Balls"
    ROA_SPINNERS = "White Door RoA Spike Spinners"
    ROA_SKIP = "White Door RoA Skippable"
    CATA_TOP = "White Door Cata Top"
    CATA_BLUE = "White Door Cata After Blue Door"
    CATA_PRISON = "White Door Cata Prison"


class BlueDoor(StrEnum):
    GT_HUNTER = "Blue Door GT Bestiary"
    GT_RING = "Blue Door GT Ring of the Ancients"
    GT_ORBS = "Blue Door GT Bonus Orbs"
    GT_ASCENDANT = "Blue Door GT Ascendant Key"
    GT_SWORD = "Blue Door GT Sword of Mirrors"
    MECH_RED = "Blue Door Mech Red Key"
    MECH_SHORTCUT = "Blue Door Mech Shortcut"
    MECH_MUSIC = "Blue Door Mech Music Test"
    MECH_BOOTS = "Blue Door Mech Talaria Boots"
    MECH_VOID = "Blue Door Mech Void Charm"
    MECH_CD = "Blue Door Mech Cyclops Den"
    HOTP_START = "Blue Door HotP Above Start"
    HOTP_STATUE = "Blue Door HotP Epimetheus"
    HOTP_MAIDEN = "Blue Door HotP Dead Maiden"
    ROA_FLAMES = "Blue Door RoA Flames"
    ROA_BLOOD = "Blue Door RoA Blood Pot"
    APEX = "Blue Door Apex"
    CAVES = "Blue Door Caves"
    CATA_ORBS = "Blue Door Cata Bonus Orbs"
    CATA_SAVE = "Blue Door Cata Checkpoint"
    CATA_BOW = "Blue Door Cata Lunarian Bow"
    CATA_ROOTS = "Blue Door Cata Poison Roots"
    CATA_PRISON_CYCLOPS = "Blue Door Cata Prison Cyclops"
    CATA_PRISON_LEFT = "Blue Door Cata Prison Left"
    CATA_PRISON_RIGHT = "Blue Door Cata Prison Right"
    TR = "Blue Door TR"
    SP = "Blue Door SP"


class RedDoor(StrEnum):
    ZEEK = "Red Door Zeek"
    CATH = "Red Door Cath"
    SP = "Red Door SP"
    TR = "Red Door TR"
    DEV_ROOM = "Red Door Dev Room"


class ShopUpgrade(StrEnum):
    GIFT = "Gift"
    KNOWLEDGE = "Knowledge"
    MERCY = "Mercy"
    ORB_SEEKER = "Orb Seeker"
    MAP_REVEAL = "Map Reveal"
    CARTOGRAPHER = "Cartographer"
    DEATH_ORB = "Death Orb"
    DEATH_POINT = "Death Point"
    TITANS_EGO = "Titan's Ego"
    ALGUS_ARCANIST = "Arcanist"
    ALGUS_SHOCK = "Shock Field"
    ALGUS_METEOR = "Meteor Rain"
    ARIAS_GORGONSLAYER = "Gorgonslayer"
    ARIAS_LAST_STAND = "Last Stand"
    ARIAS_LIONHEART = "Lionheart"
    KYULI_ASSASSIN = "Assassin Strike"
    KYULI_BULLSEYE = "Bullseye"
    KYULI_RAY = "Shining Ray"
    ZEEK_JUNKYARD = "Junkyard Hunt"
    ZEEK_ORBS = "Orb Monger"
    ZEEK_LOOT = "Bigger Loot"
    BRAM_AXE = "Golden Axe"
    BRAM_HUNTER = "Monster Hunter"
    BRAM_WHIPLASH = "Whiplash"


class Elevator(StrEnum):
    GT_1 = "GT 1 Elevator"
    GT_2 = "GT 2 Elevator"
    MECH_1 = "Mech 1 Elevator"
    MECH_2 = "Mech 2 Elevator"
    HOTP = "HotP Elevator"
    ROA_1 = "RoA 1 Elevator"
    ROA_2 = "RoA 2 Elevator"
    APEX = "Apex Elevator"
    CATA_1 = "Cata 1 Elevator"
    CATA_2 = "Cata 2 Elevator"
    TR = "TR Elevator"


class Switch(StrEnum):
    GT_2ND_ROOM = "Door GT 2nd Room"
    GT_1ST_CYCLOPS = "Door GT 1st Cyclops"
    GT_SPIKE_TUNNEL = "Door GT Spike Tunnel"
    GT_BUTT_ACCESS = "Door GT Butt Access"
    GT_GH = "Blocks GT Gorgonheart"
    GT_UPPER_PATH_BLOCKS = "Blocks GT Upper Path"
    GT_UPPER_PATH_ACCESS = "Door GT Upper Path"
    GT_CROSSES = "Door GT Crosses"
    GT_GH_SHORTCUT = "Blocks GT Gorgonheart Shortcut"
    GT_ARIAS = "Blocks GT Arias Path"
    GT_SWORD_ACCESS = "Switch GT Sword Access"
    GT_SWORD_BACKTRACK = "Switch GT Sword Backtrack"
    GT_SWORD = "Switch GT Sword"
    GT_UPPER_ARIAS = "Switch GT Upper Arias"
    MECH_WATCHER = "Door Mech Watcher"
    MECH_CHAINS = "Door Mech Chains"
    MECH_BOSS_1 = "Door Mech Boss Lower"
    MECH_BOSS_2 = "Door Mech Boss Upper"
    MECH_SPLIT_PATH = "Door Mech Split Path"
    MECH_SNAKE_1 = "Door Mech Snake Upper"
    MECH_BOOTS = "Door Mech Boots"
    MECH_TO_UPPER_GT = "Door Mech to Upper GT"
    MECH_UPPER_VOID_DROP = "Switch Mech Upper Void Drop"
    MECH_UPPER_VOID = "Switch Mech Upper Void"
    MECH_LINUS = "Door Mech Linus Lower"
    MECH_TO_BOSS_2 = "Switch Mech To Boss 2"
    MECH_POTS = "Switch Mech Pots"
    MECH_MAZE_BACKDOOR = "Switch Mech Maze Backdoor"
    MECH_TO_BOSS_1 = "Switch Mech To Boss 1"
    MECH_BLOCK_STAIRS = "Switch Mech Block Stairs"
    MECH_ARIAS_CYCLOPS = "Switch Mech Arias Cyclops"
    MECH_BOOTS_LOWER = "Switch Mech Boots Lower"
    MECH_CHAINS_GAP = "Switch Mech Chains Gap"
    MECH_LOWER_KEY = "Switch Mech Lower Key"
    MECH_ARIAS = "Switch Mech Arias"
    MECH_SNAKE_2 = "Door Mech Snake Lower"
    MECH_KEY_BLOCKS = "Switch Mech Key Blocks"
    MECH_CANNON = "Door Mech Cannon Upper"
    MECH_EYEBALL = "Switch Mech Eyeball"
    MECH_INVISIBLE = "Switch Mech Invisible"
    MECH_SKULL_PUZZLE = "Switch Mech Skull Puzzle"
    HOTP_ROCK = "Rockfall HotP"
    HOTP_BELOW_START = "Door HotP Below Start"
    HOTP_LEFT_2 = "Door HotP Left 2"
    HOTP_LEFT_1 = "Door HotP Left 1"
    HOTP_LOWER_SHORTCUT = "Switch HotP Lower Shortcut"
    HOTP_BELL = "Switch HotP Bell"
    HOTP_GHOST_BLOOD = "Switch HotP Ghost Blood"
    HOTP_TELEPORTS = "Switch HotP Teleports"
    HOTP_WORM_PILLAR = "Switch HotP Worm Pillar"
    HOTP_TO_CLAW_1 = "Switch HotP To Claw 1"
    HOTP_TO_CLAW_2 = "Switch HotP To Claw 2"
    HOTP_CLAW_ACCESS = "Switch HotP Claw Access"
    HOTP_GHOSTS = "Switch HotP Ghosts"
    HOTP_LEFT_3 = "Blocks HotP Left"
    HOTP_ABOVE_OLD_MAN = "Switch HotP Above Old Man"
    HOTP_TO_ABOVE_OLD_MAN = "Switch HotP To Above Old Man"
    HOTP_TP_PUZZLE = "Switch HotP TP Puzzle"
    HOTP_EYEBALL_SHORTCUT = "Switch HotP Eyeball Shortcut"
    HOTP_BELL_ACCESS = "Switch HotP Bell Access"
    HOTP_1ST_ROOM = "Switch HotP 1st Room"
    HOTP_LEFT_BACKTRACK = "Switch HotP Left Backtrack"
    HOTP_SKULL_PUZZLE = "Switch HotP Skull Puzzle"
    ROA_ASCEND = "Switch RoA Ascend"
    ROA_AFTER_WORMS = "Switch RoA After Worms"
    ROA_RIGHT_PATH = "Switch RoA Right Path"
    ROA_APEX_ACCESS = "Switch RoA Apex Access"
    ROA_ICARUS = "Switch RoA Icarus"
    ROA_SHAFT_L = "Switch RoA Shaft Left"
    ROA_SHAFT_R = "Switch RoA Shaft Right"
    ROA_ELEVATOR = "Switch RoA Elevator"
    ROA_SHAFT_DOWNWARDS = "Switch RoA Shaft Downwards"
    ROA_SPIDERS = "Switch RoA Spiders"
    ROA_DARK_ROOM = "Switch RoA Dark Room"
    ROA_ASCEND_SHORTCUT = "Switch RoA Ascend Shortcut"
    ROA_1ST_SHORTCUT = "Switch RoA 1st Shortcut"
    ROA_SPIKE_CLIMB = "Switch RoA Spike Climb"
    ROA_ABOVE_CENTAUR = "Switch RoA Above Centaur"
    ROA_BLOOD_POT = "Switch RoA Blood Pot"
    ROA_WORMS = "Switch RoA Worms"
    ROA_TRIPLE_1 = "Switch RoA Triple 1"
    ROA_TRIPLE_3 = "Switch RoA Triple 3"
    ROA_BABY_GORGON = "Switch RoA Baby Gorgon"
    ROA_BOSS_ACCESS = "Switch RoA Boss Access"
    ROA_BLOOD_POT_L = "Switch RoA Blood Pot Left"
    ROA_BLOOD_POT_R = "Switch RoA Blood Pot Right"
    ROA_LOWER_VOID = "Switch RoA Lower Void"
    DARKNESS = "Switch Dark"
    APEX = "Switch Apex"
    CAVES_SKELETONS = "Switch Caves Skeletons)"
    CAVES_CATA_1 = "Switch Caves Cata Access 1)"
    CAVES_CATA_2 = "Switch Caves Cata Access 2)"
    CAVES_CATA_3 = "Switch Caves Cata Access 3)"
    CATA_ELEVATOR = "Switch Cata Elevator"
    CATA_VERTICAL_SHORTCUT = "Switch Cata Vertical Shortcut"
    CATA_TOP = "Switch Cata Top"
    CATA_CLAW_1 = "Switch Cata Claw 1"
    CATA_CLAW_2 = "Switch Cata Claw 2"
    CATA_WATER_1 = "Switch Cata Water 1"
    CATA_WATER_2 = "Switch Cata Water 2"
    CATA_DEV_ROOM = "Switch Cata Dev Room"
    CATA_AFTER_BLUE_DOOR = "Switch Cata After Blue Door"
    CATA_SHORTCUT_ACCESS = "Switch Cata Shortcut Access"
    CATA_LADDER_BLOCKS = "Switch Cata Ladder Blocks"
    CATA_MID_SHORTCUT = "Switch Cata Mid Shortcut"
    CATA_1ST_ROOM = "Switch Cata 1st Room"
    CATA_FLAMES_2 = "Switch Cata Flames 2"
    CATA_FLAMES_1 = "Switch Cata Flames 1"
    TR_ADORNED_L = "Switch TR Adorned Left"
    TR_ADORNED_M = "Switch TR Adorned Middle"
    TR_ADORNED_R = "Switch TR Adorned Right"
    TR_ELEVATOR = "Switch TR Elevator"
    TR_BOTTOM = "Switch TR Bottom"
    CD_1 = "Switch CD 1"
    CD_2 = "Switch CD 2"
    CD_3 = "Switch CD 3"
    CD_CAMPFIRE = "Switch CD Campfire"
    CD_TOP = "Switch CD Top"
    CATH_BOTTOM = "Switch Cath Bottom"
    CATH_BESIDE_SHAFT = "Switch Cath Beside Shaft"
    CATH_TOP_CAMPFIRE = "Switch Cath Top Campfire"
    SP_DOUBLE_DOORS = "Switch SP Double Doors"
    SP_BUBBLES = "Switch SP Bubbles"
    SP_AFTER_STAR = "Switch SP After Star"


class Crystal(StrEnum):
    GT_LADDER = "Door GT Ladder"
    GT_ROTA = "Door GT RotA"
    GT_OLD_MAN_1 = "Crystal GT Old Man 1"
    GT_OLD_MAN_2 = "Crystal GT Old Man 2"
    MECH_CANNON = "Door Mech Cannon Lower"
    MECH_LINUS = "Door Mech Linus Upper"
    MECH_LOWER = "Crystal Mech Lower"
    MECH_TO_BOSS_3 = "Crystal Mech To Boss 3"
    MECH_TRIPLE_1 = "Crystal Mech Triple 1"
    MECH_TRIPLE_2 = "Crystal Mech Triple 2"
    MECH_TRIPLE_3 = "Crystal Mech Triple 3"
    MECH_TOP = "Crystal Mech Top"
    MECH_CLOAK = "Crystal Mech Cloak"
    MECH_SLIMES = "Crystal Mech Slimes"
    MECH_TO_CD = "Crystal Mech To CD"
    MECH_CAMPFIRE = "Crystal Mech Campfire"
    MECH_1ST_ROOM = "Blocks Mech 1st Room"
    MECH_OLD_MAN = "Crystal Mech Old Man"
    MECH_TOP_CHAINS = "Passage Mech Top Chains"
    MECH_BK = "Crystal Mech BK"
    HOTP_ROCK_ACCESS = "Door HotP Rock"
    HOTP_BOTTOM = "Crystal HotP Bottom"
    HOTP_LOWER = "Crystal HotP Lower"
    HOTP_AFTER_CLAW = "Crystal HotP After Claw"
    HOTP_MAIDEN_1 = "Crystal HotP Maiden 1"
    HOTP_MAIDEN_2 = "Crystal HotP Maiden 2"
    HOTP_BELL_ACCESS = "Crystal HotP Bell Access"
    HOTP_HEART = "Crystal HotP Heart"
    HOTP_BELOW_PUZZLE = "Crystal HotP Below Puzzle"
    ROA_1ST_ROOM = "Crystal RoA 1st Room"
    ROA_BABY_GORGON = "Crystal RoA Baby Gorgon"
    ROA_LADDER_R = "Crystal RoA Ladder Right"
    ROA_LADDER_L = "Crystal RoA Ladder Left"
    ROA_CENTAUR = "Crystal RoA Centaur"
    ROA_SPIKE_BALLS = "Crystal RoA Spike Balls"
    ROA_LEFT_ASCEND = "Crystal RoA Left Ascend"
    ROA_SHAFT = "Crystal RoA Shaft"
    ROA_BRANCH_R = "Crystal RoA Branch Right"
    ROA_BRANCH_L = "Crystal RoA Branch Left"
    ROA_3_REAPERS = "Crystal RoA 3 Reapers"
    ROA_TRIPLE_2 = "Crystal RoA Triple 2"
    CATA_POISON_ROOTS = "Crystal Cata Poison Roots"
    TR_GOLD = "Crystal TR Gold"
    TR_DARK_ARIAS = "Crystal TR Dark Arias"
    CD_BACKTRACK = "Crystal CD Backtrack"
    CD_START = "Crystal CD Start"
    CD_CAMPFIRE = "Crystal CD Campfire"
    CD_STEPS = "Crystal CD Steps"
    CATH_1ST_ROOM = "Crystal Cath 1st Room"
    CATH_SHAFT = "Crystal Cath Shaft"
    CATH_SPIKE_PIT = "Crystal Cath Spike Pit"
    CATH_TOP_L = "Crystal Cath Top Left"
    CATH_TOP_R = "Crystal Cath Top Right"
    CATH_SHAFT_ACCESS = "Crystal Cath Shaft Access"
    CATH_ORBS = "Crystal Cath Orbs"
    SP_BLOCKS = "Crystal SP Blocks"
    SP_STAR = "Crystal SP Star"


class Face(StrEnum):
    MECH_VOLANTIS = "Face Mech Volantis"
    HOTP_OLD_MAN = "Face HotP Old Man"
    ROA_SPIDERS = "Face RoA Spiders"
    ROA_BLUE_KEY = "Face RoA Blue Key"
    CAVES_1ST_ROOM = "Face Caves 1st Room"
    CATA_AFTER_BOW = "Face Cata After Bow"
    CATA_BOW = "Face Cata Bow"
    CATA_X4 = "Face Cata x4"
    CATA_CAMPFIRE = "Face Cata Campfire"
    CATA_DOUBLE_DOOR = "Face Cata Double Door"
    CATA_BOTTOM = "Face Cata Bottom"
    CATH_L = "Door Cath Left"
    CATH_R = "Door Cath Right"


class Heal(StrEnum):
    HEAL_5 = "Heal HP +5"


class Trap(StrEnum):
    CUTSCENE = "Cutscene Trap"
    ROCKS = "Rocks Trap"


ItemName: TypeAlias = (
    Character
    | Eye
    | Key
    | KeyItem
    | Upgrade
    | Orbs
    | WhiteDoor
    | BlueDoor
    | RedDoor
    | ShopUpgrade
    | Elevator
    | Switch
    | Crystal
    | Face
    | Heal
    | Trap
)


CHARACTERS: tuple[Character, ...] = (
    Character.ALGUS,
    Character.ARIAS,
    Character.KYULI,
    Character.ZEEK,
    Character.BRAM,
)

QOL_ITEMS: tuple[ShopUpgrade, ...] = (
    ShopUpgrade.KNOWLEDGE,
    ShopUpgrade.ORB_SEEKER,
    ShopUpgrade.TITANS_EGO,
    ShopUpgrade.MAP_REVEAL,
    ShopUpgrade.GIFT,
    ShopUpgrade.CARTOGRAPHER,
)


@dataclass(frozen=True)
class EarlyItems:
    white_doors: tuple[WhiteDoor, ...] = ()
    blue_doors: tuple[BlueDoor, ...] = ()
    switches: tuple[Switch, ...] = ()

    @cached_property
    def all(self) -> set[ItemName]:
        return set(self.white_doors + self.blue_doors + self.switches)


EARLY_ITEMS = {
    0: EarlyItems(
        white_doors=(
            WhiteDoor.GT_START,
            WhiteDoor.GT_MAP,
            WhiteDoor.GT_TAUROS,
        ),
        blue_doors=(
            BlueDoor.GT_ASCENDANT,
            BlueDoor.CAVES,
        ),
        switches=(
            Switch.GT_2ND_ROOM,
            Switch.GT_1ST_CYCLOPS,
            Switch.GT_SPIKE_TUNNEL,
            Switch.GT_BUTT_ACCESS,
            Switch.GT_GH,
            Switch.GT_ARIAS,
            Switch.CAVES_SKELETONS,
            Switch.CAVES_CATA_1,
            Switch.CAVES_CATA_2,
            Switch.CAVES_CATA_3,
        ),
    ),
    1: EarlyItems(),
    2: EarlyItems(),
    3: EarlyItems(),
    4: EarlyItems(),
    5: EarlyItems(),
    6: EarlyItems(),
}


class Events(StrEnum):
    VICTORY = "Victory"
    EYE_RED = Eye.RED.value
    EYE_BLUE = Eye.BLUE.value
    EYE_GREEN = Eye.GREEN.value
    SWORD = KeyItem.SWORD.value
    ASCENDANT_KEY = KeyItem.ASCENDANT_KEY.value
    ADORNED_KEY = KeyItem.ADORNED_KEY.value
    BANISH = KeyItem.BANISH.value
    VOID = KeyItem.VOID.value
    BOOTS = KeyItem.BOOTS.value
    CLOAK = KeyItem.CLOAK.value
    CYCLOPS = KeyItem.CYCLOPS.value
    BELL = KeyItem.BELL.value
    CLAW = KeyItem.CLAW.value
    GAUNTLET = KeyItem.GAUNTLET.value
    ICARUS = KeyItem.ICARUS.value
    CHALICE = KeyItem.CHALICE.value
    BOW = KeyItem.BOW.value
    CROWN = KeyItem.CROWN.value
    BLOCK = KeyItem.BLOCK.value
    STAR = KeyItem.STAR.value
    ZEEK = Character.ZEEK.value
    BRAM = Character.BRAM.value
    FAKE_OOL_ITEM = "Hard Logic"


class AstalonItem(Item):
    game = GAME_NAME


@dataclass(frozen=True)
class ItemData:
    name: ItemName
    classification: ItemClassification | Callable[[AstalonOptions], ItemClassification]
    quantity_in_item_pool: int
    group: ItemGroup
    description: str = ""


ALL_ITEMS: tuple[ItemData, ...] = (
    ItemData(Eye.RED, ItemClassification.progression, 1, ItemGroup.EYE),
    ItemData(Eye.BLUE, ItemClassification.progression, 1, ItemGroup.EYE),
    ItemData(Eye.GREEN, ItemClassification.progression, 1, ItemGroup.EYE),
    ItemData(Key.WHITE, ItemClassification.filler, 0, ItemGroup.KEY),
    ItemData(Key.BLUE, ItemClassification.filler, 0, ItemGroup.KEY),
    ItemData(Key.RED, ItemClassification.filler, 0, ItemGroup.KEY),
    ItemData(KeyItem.GORGONHEART, ItemClassification.filler, 1, ItemGroup.ITEM),
    ItemData(KeyItem.ANCIENTS_RING, ItemClassification.filler, 1, ItemGroup.ITEM),
    ItemData(KeyItem.MAIDEN_RING, ItemClassification.filler, 1, ItemGroup.ITEM),
    ItemData(KeyItem.SWORD, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.MAP, ItemClassification.filler, 1, ItemGroup.ITEM),
    ItemData(KeyItem.ASCENDANT_KEY, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.ADORNED_KEY, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BANISH, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.VOID, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BOOTS, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.CLOAK, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BELL, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.AMULET, ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(
        KeyItem.CLAW,
        ItemClassification.progression | ItemClassification.useful,
        1,
        ItemGroup.ITEM,
        description="Lets Kyuli jump up walls. Very useful!",
    ),
    ItemData(KeyItem.GAUNTLET, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.ICARUS, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.CHALICE, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BOW, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BLOCK, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(KeyItem.STAR, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(Upgrade.ATTACK_1, ItemClassification.useful, 12, ItemGroup.ATTACK),
    ItemData(Upgrade.MAX_HP_1, ItemClassification.filler, 14, ItemGroup.HEALTH),
    ItemData(Upgrade.MAX_HP_2, ItemClassification.useful, 10, ItemGroup.HEALTH),
    ItemData(Upgrade.MAX_HP_3, ItemClassification.useful, 1, ItemGroup.HEALTH),
    ItemData(Upgrade.MAX_HP_4, ItemClassification.useful, 1, ItemGroup.HEALTH),
    ItemData(Upgrade.MAX_HP_5, ItemClassification.useful, 8, ItemGroup.HEALTH),
    ItemData(Orbs.ORBS_200, ItemClassification.filler, 0, ItemGroup.ORBS),
    ItemData(Orbs.ORBS_500, ItemClassification.filler, 0, ItemGroup.ORBS),
    ItemData(Orbs.ORBS_1000, ItemClassification.filler, 0, ItemGroup.ORBS),
    ItemData(WhiteDoor.GT_START, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.GT_MAP, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.GT_TAUROS, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.MECH_2ND, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.MECH_BK, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.MECH_ARENA, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.MECH_TOP, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.HOTP_START, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.HOTP_CLAW, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.HOTP_BOSS, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.ROA_WORMS, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.ROA_ASCEND, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.ROA_BALLS, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.ROA_SPINNERS, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.ROA_SKIP, ItemClassification.filler, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.CATA_TOP, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.CATA_BLUE, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(WhiteDoor.CATA_PRISON, ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    ItemData(BlueDoor.GT_HUNTER, ItemClassification.useful, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.GT_RING, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.GT_ORBS, ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.GT_ASCENDANT, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.GT_SWORD, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.MECH_RED, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.MECH_SHORTCUT, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.MECH_MUSIC, ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.MECH_BOOTS, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.MECH_VOID, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.MECH_CD, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.HOTP_START, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.HOTP_STATUE, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.HOTP_MAIDEN, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.ROA_FLAMES, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.ROA_BLOOD, ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.APEX, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.CAVES, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(
        BlueDoor.CATA_ORBS,
        lambda options: (
            ItemClassification.progression
            if options.randomize_candles or options.randomize_orb_multipliers
            else ItemClassification.useful
        ),
        1,
        ItemGroup.DOOR_BLUE,
    ),
    ItemData(BlueDoor.CATA_SAVE, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.CATA_BOW, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.CATA_ROOTS, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.CATA_PRISON_CYCLOPS, ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.CATA_PRISON_LEFT, ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    ItemData(
        BlueDoor.CATA_PRISON_RIGHT,
        lambda options: ItemClassification.progression if options.randomize_candles else ItemClassification.filler,
        1,
        ItemGroup.DOOR_BLUE,
    ),
    ItemData(BlueDoor.TR, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(BlueDoor.SP, ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    ItemData(RedDoor.ZEEK, ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    ItemData(RedDoor.CATH, ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    ItemData(RedDoor.SP, ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    ItemData(RedDoor.TR, ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    ItemData(RedDoor.DEV_ROOM, ItemClassification.filler, 1, ItemGroup.DOOR_RED),
    ItemData(Character.ARIAS, ItemClassification.progression | ItemClassification.useful, 0, ItemGroup.CHARACTER),
    ItemData(Character.KYULI, ItemClassification.progression | ItemClassification.useful, 0, ItemGroup.CHARACTER),
    ItemData(Character.ALGUS, ItemClassification.progression | ItemClassification.useful, 0, ItemGroup.CHARACTER),
    ItemData(Character.ZEEK, ItemClassification.progression | ItemClassification.useful, 0, ItemGroup.CHARACTER),
    ItemData(Character.BRAM, ItemClassification.progression | ItemClassification.useful, 0, ItemGroup.CHARACTER),
    ItemData(ShopUpgrade.GIFT, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.KNOWLEDGE, ItemClassification.filler, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.MERCY, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ORB_SEEKER, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.MAP_REVEAL, ItemClassification.filler, 0, ItemGroup.SHOP),
    ItemData(ShopUpgrade.CARTOGRAPHER, ItemClassification.filler, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.DEATH_ORB, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.DEATH_POINT, ItemClassification.filler, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.TITANS_EGO, ItemClassification.filler, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ALGUS_ARCANIST, ItemClassification.progression, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ALGUS_SHOCK, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ALGUS_METEOR, ItemClassification.progression, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ARIAS_GORGONSLAYER, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ARIAS_LAST_STAND, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ARIAS_LIONHEART, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.KYULI_ASSASSIN, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.KYULI_BULLSEYE, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.KYULI_RAY, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ZEEK_JUNKYARD, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ZEEK_ORBS, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ZEEK_LOOT, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.BRAM_AXE, ItemClassification.progression, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.BRAM_HUNTER, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.BRAM_WHIPLASH, ItemClassification.progression | ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(Elevator.GT_2, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.MECH_1, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.MECH_2, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.HOTP, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.ROA_1, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.ROA_2, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.APEX, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.CATA_1, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.CATA_2, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Elevator.TR, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Switch.GT_2ND_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_1ST_CYCLOPS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_SPIKE_TUNNEL, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_BUTT_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_GH, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_UPPER_PATH_BLOCKS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_UPPER_PATH_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(
        Switch.GT_CROSSES,
        lambda options: (
            ItemClassification.filler
            if options.open_early_doors and options.starting_location == StartingLocation.option_gorgon_tomb
            else ItemClassification.progression
        ),
        1,
        ItemGroup.SWITCH,
    ),
    ItemData(
        Switch.GT_GH_SHORTCUT,
        lambda options: (
            ItemClassification.filler
            if options.open_early_doors and options.starting_location == StartingLocation.option_gorgon_tomb
            else ItemClassification.progression
        ),
        1,
        ItemGroup.SWITCH,
    ),
    ItemData(Switch.GT_ARIAS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_SWORD_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_SWORD_BACKTRACK, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_SWORD, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.GT_UPPER_ARIAS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_WATCHER, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_CHAINS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_BOSS_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_BOSS_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_SPLIT_PATH, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_SNAKE_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_BOOTS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_TO_UPPER_GT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_UPPER_VOID_DROP, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_UPPER_VOID, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_LINUS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_TO_BOSS_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_POTS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_MAZE_BACKDOOR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_TO_BOSS_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_BLOCK_STAIRS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_ARIAS_CYCLOPS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_BOOTS_LOWER, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_CHAINS_GAP, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_LOWER_KEY, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_ARIAS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_SNAKE_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_KEY_BLOCKS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_CANNON, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_EYEBALL, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.MECH_INVISIBLE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_ROCK, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_BELOW_START, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_LEFT_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_LEFT_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_LOWER_SHORTCUT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_BELL, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_GHOST_BLOOD, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_TELEPORTS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_WORM_PILLAR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_TO_CLAW_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_TO_CLAW_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_CLAW_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_GHOSTS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_LEFT_3, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_ABOVE_OLD_MAN, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_TO_ABOVE_OLD_MAN, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_TP_PUZZLE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_EYEBALL_SHORTCUT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_BELL_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_1ST_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_LEFT_BACKTRACK, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_ASCEND, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_AFTER_WORMS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_RIGHT_PATH, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_APEX_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_ICARUS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_SHAFT_L, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_SHAFT_R, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_ELEVATOR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_SHAFT_DOWNWARDS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_SPIDERS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_DARK_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_ASCEND_SHORTCUT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_1ST_SHORTCUT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_SPIKE_CLIMB, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_ABOVE_CENTAUR, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_BLOOD_POT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_WORMS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_TRIPLE_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_TRIPLE_3, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_BABY_GORGON, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_BOSS_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_BLOOD_POT_L, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_BLOOD_POT_R, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.ROA_LOWER_VOID, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.DARKNESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.APEX, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.CAVES_SKELETONS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CAVES_CATA_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CAVES_CATA_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CAVES_CATA_3, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_ELEVATOR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_VERTICAL_SHORTCUT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_TOP, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_CLAW_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_CLAW_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_WATER_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_WATER_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_DEV_ROOM, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_AFTER_BLUE_DOOR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_SHORTCUT_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_LADDER_BLOCKS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_MID_SHORTCUT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_1ST_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_FLAMES_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATA_FLAMES_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.TR_ADORNED_L, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.TR_ADORNED_M, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.TR_ADORNED_R, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.TR_ELEVATOR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.TR_BOTTOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CD_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CD_2, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Switch.CD_3, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CD_CAMPFIRE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CD_TOP, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATH_BOTTOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATH_BESIDE_SHAFT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.CATH_TOP_CAMPFIRE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.SP_DOUBLE_DOORS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.SP_BUBBLES, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.SP_AFTER_STAR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.GT_LADDER, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.GT_ROTA, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.GT_OLD_MAN_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.GT_OLD_MAN_2, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_CANNON, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_LINUS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_LOWER, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TO_BOSS_3, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TRIPLE_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TRIPLE_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TRIPLE_3, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TOP, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_CLOAK, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_SLIMES, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TO_CD, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_CAMPFIRE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_1ST_ROOM, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_OLD_MAN, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_TOP_CHAINS, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Crystal.MECH_BK, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_ROCK_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_BOTTOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_LOWER, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_AFTER_CLAW, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_MAIDEN_1, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_MAIDEN_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_BELL_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_HEART, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.HOTP_BELOW_PUZZLE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_1ST_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_BABY_GORGON, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_LADDER_R, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_LADDER_L, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_CENTAUR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_SPIKE_BALLS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_LEFT_ASCEND, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_SHAFT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_BRANCH_R, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_BRANCH_L, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_3_REAPERS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.ROA_TRIPLE_2, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATA_POISON_ROOTS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.TR_GOLD, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.TR_DARK_ARIAS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CD_BACKTRACK, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CD_START, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CD_CAMPFIRE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CD_STEPS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_1ST_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_SHAFT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_SPIKE_PIT, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_TOP_L, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_TOP_R, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_SHAFT_ACCESS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.CATH_ORBS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.SP_BLOCKS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Crystal.SP_STAR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.MECH_VOLANTIS, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Face.HOTP_OLD_MAN, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Face.ROA_SPIDERS, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.ROA_BLUE_KEY, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CAVES_1ST_ROOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATA_AFTER_BOW, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATA_BOW, ItemClassification.filler, 1, ItemGroup.SWITCH),
    ItemData(Face.CATA_X4, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATA_CAMPFIRE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATA_DOUBLE_DOOR, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATA_BOTTOM, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATH_L, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Face.CATH_R, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(KeyItem.CYCLOPS, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.CROWN, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(Eye.GOLD, ItemClassification.progression_skip_balancing, 0, ItemGroup.EYE),
    ItemData(Heal.HEAL_5, ItemClassification.filler, 92, ItemGroup.HEAL),
    ItemData(Trap.CUTSCENE, ItemClassification.trap, 0, ItemGroup.TRAP),
    ItemData(Trap.ROCKS, ItemClassification.trap, 0, ItemGroup.TRAP),
    ItemData(Elevator.GT_1, ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    ItemData(Switch.MECH_SKULL_PUZZLE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Switch.HOTP_SKULL_PUZZLE, ItemClassification.progression, 1, ItemGroup.SWITCH),
    ItemData(Orbs.ORB_MULTI, ItemClassification.useful, 3, ItemGroup.ORBS),
)

item_table: dict[str, ItemData] = {item.name.value: item for item in ALL_ITEMS}
item_name_to_id: dict[str, int] = {data.name.value: i for i, data in enumerate(ALL_ITEMS, start=1)}


def get_item_group(item_name: str) -> ItemGroup:
    return item_table[item_name].group


item_name_groups: dict[str, set[str]] = {
    group.value: set(item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
}

item_name_groups["Map Progression"] = {
    name
    for name, data in item_table.items()
    if name != Eye.GOLD.value
    and not callable(data.classification)
    and ItemClassification.progression in data.classification
}

filler_items: tuple[str, ...] = (
    Orbs.ORBS_200.value,
    Orbs.ORBS_500.value,
    Orbs.ORBS_1000.value,
    Heal.HEAL_5.value,
)

trap_items: tuple[str, ...] = (
    Trap.CUTSCENE.value,
    Trap.ROCKS.value,
)
