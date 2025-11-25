from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import TypeAlias

from BaseClasses import Item, ItemClassification

from .constants import BASE_ID, GAME_NAME
from .options import AstalonOptions


class ItemGroup(str, Enum):
    CHARACTER = "Characters"
    EYE = "Eyes"
    KEY = "Keys"
    ITEM = "Items"
    FAMILIAR = "Familiars"
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


class Character(str, Enum):
    ARIAS = "Arias"
    KYULI = "Kyuli"
    ALGUS = "Algus"
    ZEEK = "Zeek"
    BRAM = "Bram"


class Eye(str, Enum):
    RED = "Gorgon Eye (Red)"
    BLUE = "Gorgon Eye (Blue)"
    GREEN = "Gorgon Eye (Green)"
    GOLD = "Gorgon Eye (Gold)"


class Key(str, Enum):
    WHITE = "White Key"
    BLUE = "Blue Key"
    RED = "Red Key"


class KeyItem(str, Enum):
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


class Familiar(str, Enum):
    MONSTER = "Monster Ball"
    GIL = "Gil"


class Upgrade(str, Enum):
    ATTACK_1 = "Attack +1"
    MAX_HP_1 = "Max HP +1"
    MAX_HP_2 = "Max HP +2"
    MAX_HP_3 = "Max HP +3"
    MAX_HP_4 = "Max HP +4"
    MAX_HP_5 = "Max HP +5"


class Orbs(str, Enum):
    ORBS_200 = "200 Orbs"
    ORBS_500 = "500 Orbs"
    ORBS_1000 = "1000 Orbs"


class WhiteDoor(str, Enum):
    GT_START = "White Door (Gorgon Tomb - 1st Room)"
    GT_MAP = "White Door (Gorgon Tomb - Linus' Map)"
    GT_TAUROS = "White Door (Gorgon Tomb - Tauros)"
    MECH_2ND = "White Door (Mechanism - 2nd Room)"
    MECH_BK = "White Door (Mechanism - Black Knight)"
    MECH_ARENA = "White Door (Mechanism - Enemy Arena)"
    MECH_TOP = "White Door (Mechanism - Top)"
    HOTP_START = "White Door (Hall of the Phantoms - 1st Room)"
    HOTP_CLAW = "White Door (Hall of the Phantoms - Griffon Claw)"
    HOTP_BOSS = "White Door (Hall of the Phantoms - Boss)"
    ROA_WORMS = "White Door (Ruins of Ash - Worms)"
    ROA_ASCEND = "White Door (Ruins of Ash - Ascend)"
    ROA_BALLS = "White Door (Ruins of Ash - Spike Balls)"
    ROA_SPINNERS = "White Door (Ruins of Ash - Spike Spinners)"
    ROA_SKIP = "White Door (Ruins of Ash - Skippable)"
    CATA_TOP = "White Door (Catacombs - Top)"
    CATA_BLUE = "White Door (Catacombs - After Blue Door)"
    CATA_PRISON = "White Door (Catacombs - Prison)"


class BlueDoor(str, Enum):
    GT_HUNTER = "Blue Door (Gorgon Tomb - Bestiary)"
    GT_RING = "Blue Door (Gorgon Tomb - Ring of the Ancients)"
    GT_ORBS = "Blue Door (Gorgon Tomb - Bonus Orbs)"
    GT_ASCENDANT = "Blue Door (Gorgon Tomb - Ascendant Key)"
    GT_SWORD = "Blue Door (Gorgon Tomb - Sword of Mirrors)"
    MECH_RED = "Blue Door (Mechanism - Red Key)"
    MECH_SHORTCUT = "Blue Door (Mechanism - Shortcut)"
    MECH_MUSIC = "Blue Door (Mechanism - Music Test)"
    MECH_BOOTS = "Blue Door (Mechanism - Talaria Boots)"
    MECH_VOID = "Blue Door (Mechanism - Void Charm)"
    MECH_CD = "Blue Door (Mechanism - Cyclops Den)"
    HOTP_START = "Blue Door (Hall of the Phantoms - Above Start)"
    HOTP_STATUE = "Blue Door (Hall of the Phantoms - Epimetheus)"
    HOTP_MAIDEN = "Blue Door (Hall of the Phantoms - Dead Maiden)"
    ROA_FLAMES = "Blue Door (Ruins of Ash - Flames)"
    ROA_BLOOD = "Blue Door (Ruins of Ash - Blood Pot)"
    APEX = "Blue Door (The Apex)"
    CAVES = "Blue Door (Caves)"
    CATA_ORBS = "Blue Door (Catacombs - Bonus Orbs)"
    CATA_SAVE = "Blue Door (Catacombs - Checkpoint)"
    CATA_BOW = "Blue Door (Catacombs - Lunarian Bow)"
    CATA_ROOTS = "Blue Door (Catacombs - Poison Roots)"
    CATA_PRISON_CYCLOPS = "Blue Door (Catacombs - Prison Cyclops)"
    CATA_PRISON_LEFT = "Blue Door (Catacombs - Prison Left)"
    CATA_PRISON_RIGHT = "Blue Door (Catacombs - Prison Right)"
    TR = "Blue Door (Tower Roots)"
    SP = "Blue Door (Serpent Path)"


class RedDoor(str, Enum):
    ZEEK = "Red Door (Zeek)"
    CATH = "Red Door (Cathedral)"
    SP = "Red Door (Serpent Path)"
    TR = "Red Door (Tower Roots)"
    DEV_ROOM = "Red Door (Dev Room)"


class ShopUpgrade(str, Enum):
    GIFT = "Gift"
    KNOWLEDGE = "Knowledge"
    MERCY = "Mercy"
    ORB_SEEKER = "Orb Seeker"
    MAP_REVEAL = "Map Reveal"
    CARTOGRAPHER = "Cartographer"
    DEATH_ORB = "Death Orb"
    DEATH_POINT = "Death Point"
    TITANS_EGO = "Titan's Ego"
    ALGUS_ARCANIST = "Algus's Arcanist"
    ALGUS_SHOCK = "Algus's Shock Field"
    ALGUS_METEOR = "Algus's Meteor Rain"
    ARIAS_GORGONSLAYER = "Arias's Gorgonslayer"
    ARIAS_LAST_STAND = "Arias's Last Stand"
    ARIAS_LIONHEART = "Arias's Lionheart"
    KYULI_ASSASSIN = "Kyuli's Assassin Strike"
    KYULI_BULLSEYE = "Kyuli's Bullseye"
    KYULI_RAY = "Kyuli's Shining Ray"
    ZEEK_JUNKYARD = "Zeek's Junkyard Hunt"
    ZEEK_ORBS = "Zeek's Orb Monger"
    ZEEK_LOOT = "Zeek's Bigger Loot"
    BRAM_AXE = "Bram's Golden Axe"
    BRAM_HUNTER = "Bram's Monster Hunter"
    BRAM_WHIPLASH = "Bram's Whiplash"


class Elevator(str, Enum):
    GT_2 = "Gorgon Tomb 2 Elevator"
    MECH_1 = "Mechanism 1 Elevator"
    MECH_2 = "Mechanism 2 Elevator"
    HOTP = "Hall of the Phantoms Elevator"
    ROA_1 = "Ruins of Ash 1 Elevator"
    ROA_2 = "Ruins of Ash 2 Elevator"
    APEX = "The Apex Elevator"
    CATA_1 = "Catacombs 1 Elevator"
    CATA_2 = "Catacombs 2 Elevator"
    TR = "Tower Roots Elevator"


class Switch(str, Enum):
    GT_2ND_ROOM = "Switch (Gorgon Tomb - 2nd Room)"
    GT_1ST_CYCLOPS = "Switch (Gorgon Tomb - 1st Cyclops)"
    GT_SPIKE_TUNNEL = "Switch (Gorgon Tomb - Spike Tunnel)"
    GT_BUTT_ACCESS = "Switch (Gorgon Tomb - Butt Access)"
    GT_GH = "Switch (Gorgon Tomb - Gorgonheart)"
    GT_UPPER_PATH_BLOCKS = "Switch (Gorgon Tomb - Upper Path Blocks)"
    GT_UPPER_PATH_ACCESS = "Switch (Gorgon Tomb - Upper Path Access)"
    GT_CROSSES = "Switch (Gorgon Tomb - Crosses)"
    GT_GH_SHORTCUT = "Switch (Gorgon Tomb - GH Shortcut)"
    GT_ARIAS = "Switch (Gorgon Tomb - Arias)"
    GT_SWORD_ACCESS = "Switch (Gorgon Tomb - Sword Access)"
    GT_SWORD_BACKTRACK = "Switch (Gorgon Tomb - Sword Backtrack)"
    GT_SWORD = "Switch (Gorgon Tomb - Sword)"
    GT_UPPER_ARIAS = "Switch (Gorgon Tomb - Upper Arias)"
    MECH_WATCHER = "Switch (Mechanism - Watcher)"
    MECH_CHAINS = "Switch (Mechanism - Chains)"
    MECH_BOSS_1 = "Switch (Mechanism - Boss 1)"
    MECH_BOSS_2 = "Switch (Mechanism - Boss 2)"
    MECH_SPLIT_PATH = "Switch (Mechanism - Split Path)"
    MECH_SNAKE_1 = "Switch (Mechanism - Snake 1)"
    MECH_BOOTS = "Switch (Mechanism - Boots)"
    MECH_TO_UPPER_GT = "Switch (Mechanism - to Upper GT)"
    MECH_UPPER_VOID_DROP = "Switch (Mechanism - Upper Void Drop)"
    MECH_UPPER_VOID = "Switch (Mechanism - Upper Void)"
    MECH_LINUS = "Switch (Mechanism - Linus)"
    MECH_TO_BOSS_2 = "Switch (Mechanism - To Boss 2)"
    MECH_POTS = "Switch (Mechanism - Pots)"
    MECH_MAZE_BACKDOOR = "Switch (Mechanism - Maze Backdoor)"
    MECH_TO_BOSS_1 = "Switch (Mechanism - To Boss 1)"
    MECH_BLOCK_STAIRS = "Switch (Mechanism - Block Stairs)"
    MECH_ARIAS_CYCLOPS = "Switch (Mechanism - Arias Cyclops)"
    MECH_BOOTS_LOWER = "Switch (Mechanism - Boots Lower)"
    MECH_CHAINS_GAP = "Switch (Mechanism - Chains Gap)"
    MECH_LOWER_KEY = "Switch (Mechanism - Lower Key)"
    MECH_ARIAS = "Switch (Mechanism - Arias)"
    MECH_SNAKE_2 = "Switch (Mechanism - Snake 2)"
    MECH_KEY_BLOCKS = "Switch (Mechanism - Key Blocks)"
    MECH_CANNON = "Switch (Mechanism - Cannon)"
    MECH_EYEBALL = "Switch (Mechanism - Eyeball)"
    MECH_INVISIBLE = "Switch (Mechanism - Invisible)"
    HOTP_ROCK = "Switch (Hall of the Phantoms - Rock)"
    HOTP_BELOW_START = "Switch (Hall of the Phantoms - Below Start)"
    HOTP_LEFT_2 = "Switch (Hall of the Phantoms - Left 2)"
    HOTP_LEFT_1 = "Switch (Hall of the Phantoms - Left 1)"
    HOTP_LOWER_SHORTCUT = "Switch (Hall of the Phantoms - Lower Shortcut)"
    HOTP_BELL = "Switch (Hall of the Phantoms - Bell)"
    HOTP_GHOST_BLOOD = "Switch (Hall of the Phantoms - Ghost Blood)"
    HOTP_TELEPORTS = "Switch (Hall of the Phantoms - Teleports)"
    HOTP_WORM_PILLAR = "Switch (Hall of the Phantoms - Worm Pillar)"
    HOTP_TO_CLAW_1 = "Switch (Hall of the Phantoms - To Claw 1)"
    HOTP_TO_CLAW_2 = "Switch (Hall of the Phantoms - To Claw 2)"
    HOTP_CLAW_ACCESS = "Switch (Hall of the Phantoms - Claw Access)"
    HOTP_GHOSTS = "Switch (Hall of the Phantoms - Ghosts)"
    HOTP_LEFT_3 = "Switch (Hall of the Phantoms - Left 3)"
    HOTP_ABOVE_OLD_MAN = "Switch (Hall of the Phantoms - Above Old Man)"
    HOTP_TO_ABOVE_OLD_MAN = "Switch (Hall of the Phantoms - To Above Old Man)"
    HOTP_TP_PUZZLE = "Switch (Hall of the Phantoms - TP Puzzle)"
    HOTP_EYEBALL_SHORTCUT = "Switch (Hall of the Phantoms - Eyeball Shortcut)"
    HOTP_BELL_ACCESS = "Switch (Hall of the Phantoms - Bell Access)"
    HOTP_1ST_ROOM = "Switch (Hall of the Phantoms - 1st Room)"
    HOTP_LEFT_BACKTRACK = "Switch (Hall of the Phantoms - Left Backtrack)"
    ROA_ASCEND = "Switch (Ruins of Ash - Ascend)"
    ROA_AFTER_WORMS = "Switch (Ruins of Ash - After Worms)"
    ROA_RIGHT_PATH = "Switch (Ruins of Ash - Right Path)"
    ROA_APEX_ACCESS = "Switch (Ruins of Ash - Apex Access)"
    ROA_ICARUS = "Switch (Ruins of Ash - Icarus)"
    ROA_SHAFT_L = "Switch (Ruins of Ash - Shaft Left)"
    ROA_SHAFT_R = "Switch (Ruins of Ash - Shaft Right)"
    ROA_ELEVATOR = "Switch (Ruins of Ash - Elevator)"
    ROA_SHAFT_DOWNWARDS = "Switch (Ruins of Ash - Shaft Downwards)"
    ROA_SPIDERS = "Switch (Ruins of Ash - Spiders)"
    ROA_DARK_ROOM = "Switch (Ruins of Ash - Dark Room)"
    ROA_ASCEND_SHORTCUT = "Switch (Ruins of Ash - Ascend Shortcut)"
    ROA_1ST_SHORTCUT = "Switch (Ruins of Ash - 1st Shortcut)"
    ROA_SPIKE_CLIMB = "Switch (Ruins of Ash - Spike Climb)"
    ROA_ABOVE_CENTAUR = "Switch (Ruins of Ash - Above Centaur)"
    ROA_BLOOD_POT = "Switch (Ruins of Ash - Blood Pot)"
    ROA_WORMS = "Switch (Ruins of Ash - Worms)"
    ROA_TRIPLE_1 = "Switch (Ruins of Ash - Triple 1)"
    ROA_TRIPLE_3 = "Switch (Ruins of Ash - Triple 3)"
    ROA_BABY_GORGON = "Switch (Ruins of Ash - Baby Gorgon)"
    ROA_BOSS_ACCESS = "Switch (Ruins of Ash - Boss Access)"
    ROA_BLOOD_POT_L = "Switch (Ruins of Ash - Blood Pot Left)"
    ROA_BLOOD_POT_R = "Switch (Ruins of Ash - Blood Pot Right)"
    ROA_LOWER_VOID = "Switch (Ruins of Ash - Lower Void)"
    DARKNESS = "Switch (Darkness)"
    APEX = "Switch (The Apex)"
    CAVES_SKELETONS = "Switch (Caves - Skeletons)"
    CAVES_CATA_1 = "Switch (Caves - Catacombs Access 1)"
    CAVES_CATA_2 = "Switch (Caves - Catacombs Access 2)"
    CAVES_CATA_3 = "Switch (Caves - Catacombs Access 3)"
    CATA_ELEVATOR = "Switch (Catacombs - Elevator)"
    CATA_VERTICAL_SHORTCUT = "Switch (Catacombs - Vertical Shortcut)"
    CATA_TOP = "Switch (Catacombs - Top)"
    CATA_CLAW_1 = "Switch (Catacombs - Claw 1)"
    CATA_CLAW_2 = "Switch (Catacombs - Claw 2)"
    CATA_WATER_1 = "Switch (Catacombs - Water 1)"
    CATA_WATER_2 = "Switch (Catacombs - Water 2)"
    CATA_DEV_ROOM = "Switch (Catacombs - Dev Room)"
    CATA_AFTER_BLUE_DOOR = "Switch (Catacombs - After Blue Door)"
    CATA_SHORTCUT_ACCESS = "Switch (Catacombs - Shortcut Access)"
    CATA_LADDER_BLOCKS = "Switch (Catacombs - Ladder Blocks)"
    CATA_MID_SHORTCUT = "Switch (Catacombs - Mid Shortcut)"
    CATA_1ST_ROOM = "Switch (Catacombs - 1st Room)"
    CATA_FLAMES_2 = "Switch (Catacombs - Flames 2)"
    CATA_FLAMES_1 = "Switch (Catacombs - Flames 1)"
    TR_ADORNED_L = "Switch (Tower Roots - Adorned Left)"
    TR_ADORNED_M = "Switch (Tower Roots - Adorned Middle)"
    TR_ADORNED_R = "Switch (Tower Roots - Adorned Right)"
    TR_ELEVATOR = "Switch (Tower Roots - Elevator)"
    TR_BOTTOM = "Switch (Tower Roots - Bottom)"
    CD_1 = "Switch (Cyclops Den - 1)"
    CD_2 = "Switch (Cyclops Den - 2)"
    CD_3 = "Switch (Cyclops Den - 3)"
    CD_CAMPFIRE = "Switch (Cyclops Den - Campfire)"
    CD_TOP = "Switch (Cyclops Den - Top)"
    CATH_BOTTOM = "Switch (Cathedral - Bottom)"
    CATH_BESIDE_SHAFT = "Switch (Cathedral - Beside Shaft)"
    CATH_TOP_CAMPFIRE = "Switch (Cathedral - Top Campfire)"
    SP_DOUBLE_DOORS = "Switch (Serpent Path - Double Doors)"
    SP_BUBBLES = "Switch (Serpent Path - Bubbles)"
    SP_AFTER_STAR = "Switch (Serpent Path - After Star)"


class Crystal(str, Enum):
    GT_LADDER = "Crystal (Gorgon Tomb - Ladder)"
    GT_ROTA = "Crystal (Gorgon Tomb - RotA)"
    GT_OLD_MAN_1 = "Crystal (Gorgon Tomb - Old Man 1)"
    GT_OLD_MAN_2 = "Crystal (Gorgon Tomb - Old Man 2)"
    MECH_CANNON = "Crystal (Mechanism - Cannon)"
    MECH_LINUS = "Crystal (Mechanism - Linus)"
    MECH_LOWER = "Crystal (Mechanism - Lower)"
    MECH_TO_BOSS_3 = "Crystal (Mechanism - To Boss 3)"
    MECH_TRIPLE_1 = "Crystal (Mechanism - Triple 1)"
    MECH_TRIPLE_2 = "Crystal (Mechanism - Triple 2)"
    MECH_TRIPLE_3 = "Crystal (Mechanism - Triple 3)"
    MECH_TOP = "Crystal (Mechanism - Top)"
    MECH_CLOAK = "Crystal (Mechanism - Cloak)"
    MECH_SLIMES = "Crystal (Mechanism - Slimes)"
    MECH_TO_CD = "Crystal (Mechanism - To CD)"
    MECH_CAMPFIRE = "Crystal (Mechanism - Campfire)"
    MECH_1ST_ROOM = "Crystal (Mechanism - 1st Room)"
    MECH_OLD_MAN = "Crystal (Mechanism - Old Man)"
    MECH_TOP_CHAINS = "Crystal (Mechanism - Top Chains)"
    MECH_BK = "Crystal (Mechanism - BK)"
    HOTP_ROCK_ACCESS = "Crystal (Hall of the Phantoms - Rock Access)"
    HOTP_BOTTOM = "Crystal (Hall of the Phantoms - Bottom)"
    HOTP_LOWER = "Crystal (Hall of the Phantoms - Lower)"
    HOTP_AFTER_CLAW = "Crystal (Hall of the Phantoms - After Claw)"
    HOTP_MAIDEN_1 = "Crystal (Hall of the Phantoms - Maiden 1)"
    HOTP_MAIDEN_2 = "Crystal (Hall of the Phantoms - Maiden 2)"
    HOTP_BELL_ACCESS = "Crystal (Hall of the Phantoms - Bell Access)"
    HOTP_HEART = "Crystal (Hall of the Phantoms - Heart)"
    HOTP_BELOW_PUZZLE = "Crystal (Hall of the Phantoms - Below Puzzle)"
    ROA_1ST_ROOM = "Crystal (Ruins of Ash - 1st Room)"
    ROA_BABY_GORGON = "Crystal (Ruins of Ash - Baby Gorgon)"
    ROA_LADDER_R = "Crystal (Ruins of Ash - Ladder Right)"
    ROA_LADDER_L = "Crystal (Ruins of Ash - Ladder Left)"
    ROA_CENTAUR = "Crystal (Ruins of Ash - Centaur)"
    ROA_SPIKE_BALLS = "Crystal (Ruins of Ash - Spike Balls)"
    ROA_LEFT_ASCEND = "Crystal (Ruins of Ash - Left Ascend)"
    ROA_SHAFT = "Crystal (Ruins of Ash - Shaft)"
    ROA_BRANCH_R = "Crystal (Ruins of Ash - Branch Right)"
    ROA_BRANCH_L = "Crystal (Ruins of Ash - Branch Left)"
    ROA_3_REAPERS = "Crystal (Ruins of Ash - 3 Reapers)"
    ROA_TRIPLE_2 = "Crystal (Ruins of Ash - Triple 2)"
    CATA_POISON_ROOTS = "Crystal (Catacombs - Poison Roots)"
    TR_GOLD = "Crystal (Tower Roots - Gold)"
    TR_DARK_ARIAS = "Crystal (Tower Roots - Dark Arias)"
    CD_BACKTRACK = "Crystal (Cyclops Den - Backtrack)"
    CD_START = "Crystal (Cyclops Den - Start)"
    CD_CAMPFIRE = "Crystal (Cyclops Den - Campfire)"
    CD_STEPS = "Crystal (Cyclops Den - Steps)"
    CATH_1ST_ROOM = "Crystal (Cathedral - 1st Room)"
    CATH_SHAFT = "Crystal (Cathedral - Shaft)"
    CATH_SPIKE_PIT = "Crystal (Cathedral - Spike Pit)"
    CATH_TOP_L = "Crystal (Cathedral - Top Left)"
    CATH_TOP_R = "Crystal (Cathedral - Top Right)"
    CATH_SHAFT_ACCESS = "Crystal (Cathedral - Shaft Access)"
    CATH_ORBS = "Crystal (Cathedral - Orbs)"
    SP_BLOCKS = "Crystal (Serpent Path - Blocks)"
    SP_STAR = "Crystal (Serpent Path - Star)"


class Face(str, Enum):
    MECH_VOLANTIS = "Face (Mechanism - Volantis)"
    HOTP_OLD_MAN = "Face (Hall of the Phantoms - Old Man)"
    ROA_SPIDERS = "Face (Ruins of Ash - Spiders)"
    ROA_BLUE_KEY = "Face (Ruins of Ash - Blue Key)"
    CAVES_1ST_ROOM = "Face (Caves - 1st Room)"
    CATA_AFTER_BOW = "Face (Catacombs - After Bow)"
    CATA_BOW = "Face (Catacombs - Bow)"
    CATA_X4 = "Face (Catacombs - x4)"
    CATA_CAMPFIRE = "Face (Catacombs - Campfire)"
    CATA_DOUBLE_DOOR = "Face (Catacombs - Double Door)"
    CATA_BOTTOM = "Face (Catacombs - Bottom)"
    CATH_L = "Face (Cathedral - Left)"
    CATH_R = "Face (Cathedral - Right)"


class Heal(str, Enum):
    HEAL_5 = "Heal HP +5"


class Trap(str, Enum):
    CUTSCENE = "Cutscene Trap"
    ROCKS = "Rocks Trap"


ItemName: TypeAlias = (
    Character
    | Eye
    | Key
    | KeyItem
    | Familiar
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


ProgressionItem: TypeAlias = Character | Eye | KeyItem | ShopUpgrade

CHARACTERS: tuple[Character, ...] = (
    Character.ALGUS,
    Character.ARIAS,
    Character.KYULI,
    Character.ZEEK,
    Character.BRAM,
)

EARLY_WHITE_DOORS: tuple[WhiteDoor, ...] = (
    WhiteDoor.GT_START,
    WhiteDoor.GT_MAP,
    WhiteDoor.GT_TAUROS,
)

EARLY_BLUE_DOORS: tuple[BlueDoor, ...] = (
    BlueDoor.GT_ASCENDANT,
    BlueDoor.CAVES,
)

EARLY_SWITCHES: tuple[Switch, ...] = (
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
)

EARLY_ITEMS: set[ItemName] = {*EARLY_WHITE_DOORS, *EARLY_BLUE_DOORS, *EARLY_SWITCHES}

QOL_ITEMS: tuple[ShopUpgrade, ...] = (
    ShopUpgrade.KNOWLEDGE,
    ShopUpgrade.ORB_SEEKER,
    ShopUpgrade.TITANS_EGO,
    ShopUpgrade.MAP_REVEAL,
    ShopUpgrade.GIFT,
    ShopUpgrade.CARTOGRAPHER,
)


class Events(str, Enum):
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
    game: str = GAME_NAME


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
    ItemData(KeyItem.ASCENDANT_KEY, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.ADORNED_KEY, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BANISH, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.VOID, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BOOTS, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.CLOAK, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BELL, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.AMULET, ItemClassification.useful, 1, ItemGroup.ITEM),
    ItemData(
        KeyItem.CLAW,
        ItemClassification.progression,
        1,
        ItemGroup.ITEM,
        description="Lets Kyuli jump up walls. Very useful!",
    ),
    ItemData(KeyItem.GAUNTLET, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.ICARUS, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.CHALICE, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BOW, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.BLOCK, ItemClassification.progression, 1, ItemGroup.ITEM),
    ItemData(KeyItem.STAR, ItemClassification.progression, 1, ItemGroup.ITEM),
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
        lambda options: ItemClassification.progression if options.randomize_candles else ItemClassification.useful,
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
    ItemData(Character.ARIAS, ItemClassification.progression, 0, ItemGroup.CHARACTER),
    ItemData(Character.KYULI, ItemClassification.progression, 0, ItemGroup.CHARACTER),
    ItemData(Character.ALGUS, ItemClassification.progression, 0, ItemGroup.CHARACTER),
    ItemData(Character.ZEEK, ItemClassification.progression, 0, ItemGroup.CHARACTER),
    ItemData(Character.BRAM, ItemClassification.progression, 0, ItemGroup.CHARACTER),
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
    ItemData(ShopUpgrade.KYULI_RAY, ItemClassification.progression, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ZEEK_JUNKYARD, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ZEEK_ORBS, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.ZEEK_LOOT, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.BRAM_AXE, ItemClassification.progression, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.BRAM_HUNTER, ItemClassification.useful, 1, ItemGroup.SHOP),
    ItemData(ShopUpgrade.BRAM_WHIPLASH, ItemClassification.progression, 1, ItemGroup.SHOP),
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
        lambda options: ItemClassification.filler if options.open_early_doors else ItemClassification.progression,
        1,
        ItemGroup.SWITCH,
    ),
    ItemData(
        Switch.GT_GH_SHORTCUT,
        lambda options: ItemClassification.filler if options.open_early_doors else ItemClassification.progression,
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
)

item_table = {item.name.value: item for item in ALL_ITEMS}
item_name_to_id: dict[str, int] = {data.name.value: i for i, data in enumerate(ALL_ITEMS, start=BASE_ID)}


def get_item_group(item_name: str):
    return item_table[item_name].group


item_name_groups: dict[str, set[str]] = {
    group.value: set(item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group
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
