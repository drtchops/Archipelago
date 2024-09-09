from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import TYPE_CHECKING, Callable, Dict, Set, Tuple, Union

from typing_extensions import TypeAlias

from BaseClasses import Item, ItemClassification

from .constants import BASE_ID, GAME_NAME

if TYPE_CHECKING:
    from . import AstalonWorld


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


ItemName: TypeAlias = Union[
    Character,
    Eye,
    Key,
    KeyItem,
    Familiar,
    Upgrade,
    Orbs,
    WhiteDoor,
    BlueDoor,
    RedDoor,
    ShopUpgrade,
    Elevator,
    Switch,
    Crystal,
    Face,
    Heal,
    Trap,
]


CHARACTERS: Tuple[Character, ...] = (
    Character.ALGUS,
    Character.ARIAS,
    Character.KYULI,
    Character.ZEEK,
    Character.BRAM,
)

EARLY_WHITE_DOORS: Tuple[WhiteDoor, ...] = (
    WhiteDoor.GT_START,
    WhiteDoor.GT_MAP,
    WhiteDoor.GT_TAUROS,
)

EARLY_BLUE_DOORS: Tuple[BlueDoor, ...] = (
    BlueDoor.GT_ASCENDANT,
    BlueDoor.CAVES,
)

EARLY_SWITCHES: Tuple[Switch, ...] = (
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

EARLY_ITEMS: Set[ItemName] = set([*EARLY_WHITE_DOORS, *EARLY_BLUE_DOORS, *EARLY_SWITCHES])

QOL_ITEMS: Tuple[ShopUpgrade, ...] = (
    ShopUpgrade.KNOWLEDGE,
    ShopUpgrade.ORB_SEEKER,
    ShopUpgrade.TITANS_EGO,
    ShopUpgrade.MAP_REVEAL,
    ShopUpgrade.GIFT,
    ShopUpgrade.CARTOGRAPHER,
)


class AstalonItem(Item):
    game = GAME_NAME


@dataclass(frozen=True)
class ItemData:
    classification: Union[ItemClassification, Callable[["AstalonWorld"], ItemClassification]]
    quantity_in_item_pool: int
    group: ItemGroup


item_table: Dict[str, ItemData] = {
    Eye.RED.value: ItemData(ItemClassification.progression, 1, ItemGroup.EYE),
    Eye.BLUE.value: ItemData(ItemClassification.progression, 1, ItemGroup.EYE),
    Eye.GREEN.value: ItemData(ItemClassification.progression, 1, ItemGroup.EYE),
    Key.WHITE.value: ItemData(ItemClassification.filler, 0, ItemGroup.KEY),
    Key.BLUE.value: ItemData(ItemClassification.filler, 0, ItemGroup.KEY),
    Key.RED.value: ItemData(ItemClassification.filler, 0, ItemGroup.KEY),
    KeyItem.GORGONHEART.value: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM),
    KeyItem.ANCIENTS_RING.value: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM),
    KeyItem.MAIDEN_RING.value: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM),
    KeyItem.SWORD.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.MAP.value: ItemData(ItemClassification.filler, 1, ItemGroup.ITEM),
    KeyItem.ASCENDANT_KEY.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.ADORNED_KEY.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.BANISH.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.VOID.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.BOOTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.CLOAK.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.BELL.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.AMULET.value: ItemData(ItemClassification.useful, 1, ItemGroup.ITEM),
    KeyItem.CLAW.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.GAUNTLET.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.ICARUS.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.CHALICE.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.BOW.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.BLOCK.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.STAR.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    Upgrade.ATTACK_1.value: ItemData(ItemClassification.useful, 12, ItemGroup.ATTACK),
    Upgrade.MAX_HP_1.value: ItemData(ItemClassification.filler, 14, ItemGroup.HEALTH),
    Upgrade.MAX_HP_2.value: ItemData(ItemClassification.useful, 10, ItemGroup.HEALTH),
    Upgrade.MAX_HP_3.value: ItemData(ItemClassification.useful, 1, ItemGroup.HEALTH),
    Upgrade.MAX_HP_4.value: ItemData(ItemClassification.useful, 1, ItemGroup.HEALTH),
    Upgrade.MAX_HP_5.value: ItemData(ItemClassification.useful, 8, ItemGroup.HEALTH),
    Orbs.ORBS_200.value: ItemData(ItemClassification.filler, 0, ItemGroup.ORBS),
    Orbs.ORBS_500.value: ItemData(ItemClassification.filler, 0, ItemGroup.ORBS),
    Orbs.ORBS_1000.value: ItemData(ItemClassification.filler, 0, ItemGroup.ORBS),
    WhiteDoor.GT_START.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.GT_MAP.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.GT_TAUROS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.MECH_2ND.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.MECH_BK.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.MECH_ARENA.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.MECH_TOP.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.HOTP_START.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.HOTP_CLAW.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.HOTP_BOSS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.ROA_WORMS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.ROA_ASCEND.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.ROA_BALLS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.ROA_SPINNERS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.ROA_SKIP.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.CATA_TOP.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.CATA_BLUE.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    WhiteDoor.CATA_PRISON.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_WHITE),
    BlueDoor.GT_HUNTER.value: ItemData(ItemClassification.useful, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.GT_RING.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.GT_ORBS.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.GT_ASCENDANT.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.GT_SWORD.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.MECH_RED.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.MECH_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.MECH_MUSIC.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.MECH_BOOTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.MECH_VOID.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.MECH_CD.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.HOTP_START.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.HOTP_STATUE.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.HOTP_MAIDEN.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.ROA_FLAMES.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.ROA_BLOOD.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.APEX.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CAVES.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_ORBS.value: ItemData(ItemClassification.useful, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_SAVE.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_BOW.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_ROOTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_PRISON_CYCLOPS.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_PRISON_LEFT.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.CATA_PRISON_RIGHT.value: ItemData(
        lambda world: ItemClassification.progression if world.options.randomize_candles else ItemClassification.filler,
        1,
        ItemGroup.DOOR_BLUE,
    ),
    BlueDoor.TR.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    BlueDoor.SP.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_BLUE),
    RedDoor.ZEEK.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    RedDoor.CATH.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    RedDoor.SP.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    RedDoor.TR.value: ItemData(ItemClassification.progression, 1, ItemGroup.DOOR_RED),
    RedDoor.DEV_ROOM.value: ItemData(ItemClassification.filler, 1, ItemGroup.DOOR_RED),
    Character.ARIAS.value: ItemData(ItemClassification.progression, 0, ItemGroup.CHARACTER),
    Character.KYULI.value: ItemData(ItemClassification.progression, 0, ItemGroup.CHARACTER),
    Character.ALGUS.value: ItemData(ItemClassification.progression, 0, ItemGroup.CHARACTER),
    Character.ZEEK.value: ItemData(ItemClassification.progression, 0, ItemGroup.CHARACTER),
    Character.BRAM.value: ItemData(ItemClassification.progression, 0, ItemGroup.CHARACTER),
    ShopUpgrade.GIFT.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.KNOWLEDGE.value: ItemData(ItemClassification.filler, 1, ItemGroup.SHOP),
    ShopUpgrade.MERCY.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.ORB_SEEKER.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.MAP_REVEAL.value: ItemData(ItemClassification.filler, 0, ItemGroup.SHOP),
    ShopUpgrade.CARTOGRAPHER.value: ItemData(ItemClassification.filler, 1, ItemGroup.SHOP),
    ShopUpgrade.DEATH_ORB.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.DEATH_POINT.value: ItemData(ItemClassification.filler, 1, ItemGroup.SHOP),
    ShopUpgrade.TITANS_EGO.value: ItemData(ItemClassification.filler, 1, ItemGroup.SHOP),
    ShopUpgrade.ALGUS_ARCANIST.value: ItemData(ItemClassification.progression, 1, ItemGroup.SHOP),
    ShopUpgrade.ALGUS_SHOCK.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.ALGUS_METEOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SHOP),
    ShopUpgrade.ARIAS_GORGONSLAYER.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.ARIAS_LAST_STAND.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.ARIAS_LIONHEART.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.KYULI_ASSASSIN.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.KYULI_BULLSEYE.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.KYULI_RAY.value: ItemData(ItemClassification.progression, 1, ItemGroup.SHOP),
    ShopUpgrade.ZEEK_JUNKYARD.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.ZEEK_ORBS.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.ZEEK_LOOT.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.BRAM_AXE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SHOP),
    ShopUpgrade.BRAM_HUNTER.value: ItemData(ItemClassification.useful, 1, ItemGroup.SHOP),
    ShopUpgrade.BRAM_WHIPLASH.value: ItemData(ItemClassification.progression, 1, ItemGroup.SHOP),
    Elevator.GT_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.MECH_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.MECH_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.HOTP.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.ROA_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.ROA_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.APEX.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.CATA_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.CATA_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Elevator.TR.value: ItemData(ItemClassification.progression, 1, ItemGroup.ELEVATOR),
    Switch.GT_2ND_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_1ST_CYCLOPS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_SPIKE_TUNNEL.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_BUTT_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_GH.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_UPPER_PATH_BLOCKS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_UPPER_PATH_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_CROSSES.value: ItemData(
        lambda world: ItemClassification.filler if world.options.open_early_doors else ItemClassification.progression,
        1,
        ItemGroup.SWITCH,
    ),
    Switch.GT_GH_SHORTCUT.value: ItemData(
        lambda world: ItemClassification.filler if world.options.open_early_doors else ItemClassification.progression,
        1,
        ItemGroup.SWITCH,
    ),
    Switch.GT_ARIAS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_SWORD_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_SWORD_BACKTRACK.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.GT_SWORD.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.GT_UPPER_ARIAS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_WATCHER.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_CHAINS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_BOSS_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_BOSS_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_SPLIT_PATH.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_SNAKE_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_BOOTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_TO_UPPER_GT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_UPPER_VOID_DROP.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_UPPER_VOID.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_LINUS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_TO_BOSS_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_POTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_MAZE_BACKDOOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_TO_BOSS_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_BLOCK_STAIRS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_ARIAS_CYCLOPS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_BOOTS_LOWER.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_CHAINS_GAP.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.MECH_LOWER_KEY.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_ARIAS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_SNAKE_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_KEY_BLOCKS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_CANNON.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_EYEBALL.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.MECH_INVISIBLE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_ROCK.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_BELOW_START.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_LEFT_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_LEFT_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_LOWER_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_BELL.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_GHOST_BLOOD.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_TELEPORTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_WORM_PILLAR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_TO_CLAW_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_TO_CLAW_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_CLAW_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_GHOSTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_LEFT_3.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_ABOVE_OLD_MAN.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_TO_ABOVE_OLD_MAN.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_TP_PUZZLE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_EYEBALL_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_BELL_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_1ST_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.HOTP_LEFT_BACKTRACK.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_ASCEND.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_AFTER_WORMS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_RIGHT_PATH.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_APEX_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_ICARUS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_SHAFT_L.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_SHAFT_R.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_ELEVATOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_SHAFT_DOWNWARDS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_SPIDERS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_DARK_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_ASCEND_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_1ST_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_SPIKE_CLIMB.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.ROA_ABOVE_CENTAUR.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.ROA_BLOOD_POT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_WORMS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_TRIPLE_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_TRIPLE_3.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_BABY_GORGON.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_BOSS_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.ROA_BLOOD_POT_L.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.ROA_BLOOD_POT_R.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.ROA_LOWER_VOID.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.DARKNESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.APEX.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.CAVES_SKELETONS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CAVES_CATA_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CAVES_CATA_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CAVES_CATA_3.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_ELEVATOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_VERTICAL_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_TOP.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_CLAW_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_CLAW_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_WATER_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_WATER_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_DEV_ROOM.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.CATA_AFTER_BLUE_DOOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_SHORTCUT_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_LADDER_BLOCKS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_MID_SHORTCUT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_1ST_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_FLAMES_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATA_FLAMES_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.TR_ADORNED_L.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.TR_ADORNED_M.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.TR_ADORNED_R.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.TR_ELEVATOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.TR_BOTTOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CD_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CD_2.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Switch.CD_3.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CD_CAMPFIRE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CD_TOP.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATH_BOTTOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATH_BESIDE_SHAFT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.CATH_TOP_CAMPFIRE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.SP_DOUBLE_DOORS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.SP_BUBBLES.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Switch.SP_AFTER_STAR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.GT_LADDER.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.GT_ROTA.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.GT_OLD_MAN_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.GT_OLD_MAN_2.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Crystal.MECH_CANNON.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_LINUS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_LOWER.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_TO_BOSS_3.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_TRIPLE_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_TRIPLE_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_TRIPLE_3.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_TOP.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_CLOAK.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_SLIMES.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_TO_CD.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_CAMPFIRE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.MECH_1ST_ROOM.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Crystal.MECH_OLD_MAN.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Crystal.MECH_TOP_CHAINS.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Crystal.MECH_BK.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_ROCK_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_BOTTOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_LOWER.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_AFTER_CLAW.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_MAIDEN_1.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_MAIDEN_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_BELL_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_HEART.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.HOTP_BELOW_PUZZLE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_1ST_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_BABY_GORGON.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_LADDER_R.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_LADDER_L.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_CENTAUR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_SPIKE_BALLS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_LEFT_ASCEND.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_SHAFT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_BRANCH_R.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_BRANCH_L.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_3_REAPERS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.ROA_TRIPLE_2.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATA_POISON_ROOTS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.TR_GOLD.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.TR_DARK_ARIAS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CD_BACKTRACK.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Crystal.CD_START.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CD_CAMPFIRE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CD_STEPS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_1ST_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_SHAFT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_SPIKE_PIT.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_TOP_L.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_TOP_R.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_SHAFT_ACCESS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.CATH_ORBS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.SP_BLOCKS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Crystal.SP_STAR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.MECH_VOLANTIS.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Face.HOTP_OLD_MAN.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Face.ROA_SPIDERS.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.ROA_BLUE_KEY.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CAVES_1ST_ROOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATA_AFTER_BOW.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATA_BOW.value: ItemData(ItemClassification.filler, 1, ItemGroup.SWITCH),
    Face.CATA_X4.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATA_CAMPFIRE.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATA_DOUBLE_DOOR.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATA_BOTTOM.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATH_L.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    Face.CATH_R.value: ItemData(ItemClassification.progression, 1, ItemGroup.SWITCH),
    KeyItem.CYCLOPS.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    KeyItem.CROWN.value: ItemData(ItemClassification.progression, 1, ItemGroup.ITEM),
    Eye.GOLD.value: ItemData(ItemClassification.progression_skip_balancing, 0, ItemGroup.EYE),
    Heal.HEAL_5.value: ItemData(ItemClassification.filler, 92, ItemGroup.HEAL),
    Trap.CUTSCENE.value: ItemData(ItemClassification.trap, 0, ItemGroup.TRAP),
    Trap.ROCKS.value: ItemData(ItemClassification.trap, 0, ItemGroup.TRAP),
}

item_name_to_id: Dict[str, int] = {name: i for i, name in enumerate(item_table, start=BASE_ID)}


def get_item_group(item_name: str):
    return item_table[item_name].group


item_name_groups: Dict[str, Set[str]] = {
    group.value: set(item for item in item_names)
    for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group)
    if group != ""
}

item_name_groups["Map Progression"] = {
    name
    for name, data in item_table.items()
    if name != Eye.GOLD.value
    and not callable(data.classification)
    and ItemClassification.progression in data.classification
}

filler_items: Tuple[str, ...] = (
    Orbs.ORBS_200.value,
    Orbs.ORBS_500.value,
    Orbs.ORBS_1000.value,
    Heal.HEAL_5.value,
)

trap_items: Tuple[str, ...] = (
    Trap.CUTSCENE.value,
    Trap.ROCKS.value,
)
