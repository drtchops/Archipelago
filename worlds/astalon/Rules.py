from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING, Callable, Dict, Tuple, Union

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import (
    CHARACTERS,
    BlueDoors,
    Characters,
    Items,
    KeyItems,
    RedDoors,
    ShopUpgrades,
    WhiteDoors,
)
from .Locations import Locations
from .Options import AstalonOptions, Difficulty, RandomizeCharacters
from .Regions import Regions

if TYPE_CHECKING:
    from . import AstalonWorld


class Logic(Enum):
    ARIAS_JUMP = auto()
    EXTRA_HEIGHT = auto()
    COMBO_HEIGHT = auto()
    BLOCK_IN_WALL = auto()
    MAGIC_CRYSTAL = auto()
    SENT = auto()


@dataclass
class AstalonRules:
    world: "AstalonWorld"
    player: int
    options: AstalonOptions
    entrance_rules: Dict[Tuple[Regions, Regions], Callable[[CollectionState], bool]]
    item_rules: Dict[Locations, Callable[[CollectionState], bool]]
    attack_rules: Dict[Locations, Callable[[CollectionState], bool]]
    health_rules: Dict[Locations, Callable[[CollectionState], bool]]
    white_key_rules: Dict[Locations, Callable[[CollectionState], bool]]
    blue_key_rules: Dict[Locations, Callable[[CollectionState], bool]]
    red_key_rules: Dict[Locations, Callable[[CollectionState], bool]]
    shop_rules: Dict[Locations, Callable[[CollectionState], bool]]
    familiar_rules: Dict[Locations, Callable[[CollectionState], bool]]

    def __init__(self, world: "AstalonWorld"):
        self.world = world
        self.player = world.player
        self.options = world.options

        self.entrance_rules = {
            (Regions.SHOP, Regions.SHOP_ALGUS): lambda state: self.has(state, Items.ALGUS),
            (Regions.SHOP, Regions.SHOP_ARIAS): lambda state: self.has(state, Items.ARIAS),
            (Regions.SHOP, Regions.SHOP_KYULI): lambda state: self.has(state, Items.KYULI),
            (Regions.SHOP, Regions.SHOP_ZEEK): lambda state: self.has(state, Items.ZEEK),
            (Regions.SHOP, Regions.SHOP_BRAM): lambda state: self.has(state, Items.BRAM),
            (Regions.ENTRANCE, Regions.BESTIARY): lambda state: False,
            (Regions.ENTRANCE, Regions.GT_BABY_GORGON): lambda state: False,
            (Regions.ENTRANCE, Regions.GT_BOTTOM): lambda state: False,
            (Regions.ENTRANCE, Regions.GT_VOID): lambda state: False,
            (Regions.ENTRANCE, Regions.GT_GORGONHEART): lambda state: False,
            (Regions.ENTRANCE, Regions.GT_BOSS): lambda state: False,
            (Regions.ENTRANCE, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.ENTRANCE, Regions.MECH_BOSS): lambda state: False,
            (Regions.ENTRANCE, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.ENTRANCE, Regions.HOTP_BOSS): lambda state: False,
            (Regions.ENTRANCE, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.ENTRANCE, Regions.APEX): lambda state: False,
            (Regions.ENTRANCE, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.ENTRANCE, Regions.CATA_BOSS): lambda state: False,
            (Regions.ENTRANCE, Regions.TR_START): lambda state: False,
            (Regions.GT_BOTTOM, Regions.GT_VOID): lambda state: False,
            (Regions.GT_BOTTOM, Regions.GT_GORGONHEART): lambda state: False,
            (Regions.GT_BOTTOM, Regions.GT_UPPER_PATH): lambda state: False,
            (Regions.GT_BOTTOM, Regions.CAVES_START): lambda state: False,
            (Regions.GT_VOID, Regions.GT_BOTTOM): lambda state: False,
            (Regions.GT_VOID, Regions.MECH_SNAKE): lambda state: False,
            (Regions.GT_GORGONHEART, Regions.GT_BOTTOM): lambda state: False,
            (Regions.GT_GORGONHEART, Regions.GT_ORBS_DOOR): lambda state: False,
            (Regions.GT_GORGONHEART, Regions.GT_LEFT): lambda state: False,
            (Regions.GT_LEFT, Regions.GT_GORGONHEART): lambda state: False,
            (Regions.GT_LEFT, Regions.GT_ORBS_HEIGHT): lambda state: False,
            (Regions.GT_LEFT, Regions.GT_ASCENDANT_KEY): lambda state: False,
            (Regions.GT_LEFT, Regions.GT_ARIAS): lambda state: False,
            (Regions.GT_LEFT, Regions.GT_TOP_LEFT): lambda state: False,
            (Regions.GT_LEFT, Regions.GT_TOP_RIGHT): lambda state: False,
            (Regions.GT_ARIAS, Regions.GT_TOP_LEFT): lambda state: False,
            (Regions.GT_TOP_LEFT, Regions.GT_LEFT): lambda state: False,
            (Regions.GT_TOP_LEFT, Regions.GT_TOP_LEFT): lambda state: False,
            (Regions.GT_TOP_LEFT, Regions.GT_BUTT): lambda state: False,
            (Regions.GT_TOP_RIGHT, Regions.GT_LEFT): lambda state: False,
            (Regions.GT_TOP_RIGHT, Regions.GT_SPIKE_TUNNEL): lambda state: False,
            (Regions.GT_SPIKE_TUNNEL, Regions.GT_TOP_RIGHT): lambda state: False,
            (Regions.GT_SPIKE_TUNNEL, Regions.GT_BUTT): lambda state: False,
            (Regions.GT_BUTT, Regions.GT_TOP_LEFT): lambda state: False,
            (Regions.GT_BUTT, Regions.GT_SPIKE_TUNNEL): lambda state: False,
            (Regions.GT_BUTT, Regions.GT_BOSS): lambda state: False,
            (Regions.GT_BOSS, Regions.GT_BUTT): lambda state: False,
            (Regions.GT_BOSS, Regions.MECH_START): lambda state: False,
            (Regions.GT_BOSS, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.GT_BOSS, Regions.MECH_BOSS): lambda state: False,
            (Regions.GT_BOSS, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.GT_BOSS, Regions.HOTP_BOSS): lambda state: False,
            (Regions.GT_BOSS, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.GT_BOSS, Regions.APEX): lambda state: False,
            (Regions.GT_BOSS, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.GT_BOSS, Regions.CATA_BOSS): lambda state: False,
            (Regions.GT_BOSS, Regions.TR_START): lambda state: False,
            (Regions.GT_UPPER_ARIAS, Regions.GT_OLD_MAN_FORK): lambda state: False,
            (Regions.GT_UPPER_ARIAS, Regions.MECH_SWORD_CONNECTION): lambda state: False,
            (Regions.GT_OLD_MAN_FORK, Regions.GT_UPPER_ARIAS): lambda state: False,
            (Regions.GT_OLD_MAN_FORK, Regions.GT_SWORD_FORK): lambda state: False,
            (Regions.GT_OLD_MAN_FORK, Regions.GT_OLD_MAN): lambda state: False,
            (Regions.GT_SWORD_FORK, Regions.GT_SWORD): lambda state: False,
            (Regions.GT_SWORD_FORK, Regions.GT_OLD_MAN_FORK): lambda state: False,
            (Regions.GT_SWORD_FORK, Regions.GT_ARIAS_SWORD_SWITCH): lambda state: False,
            (Regions.GT_UPPER_PATH, Regions.GT_UPPER_PATH_CONNECTION): lambda state: False,
            (Regions.GT_UPPER_PATH, Regions.GT_BOTTOM): lambda state: False,
            (Regions.GT_UPPER_PATH_CONNECTION, Regions.MECH_SWORD_CONNECTION): lambda state: False,
            (Regions.MECH_START, Regions.GT_LADDER_SWITCH): lambda state: False,
            (Regions.MECH_START, Regions.MECH_BK): lambda state: False,
            (Regions.MECH_START, Regions.MECH_ROOTS): lambda state: False,
            (Regions.MECH_START, Regions.MECH_LINUS): lambda state: False,
            (Regions.MECH_START, Regions.MECH_LOWER_VOID): lambda state: False,
            (Regions.MECH_START, Regions.MECH_SACRIFICE): lambda state: False,
            (Regions.MECH_START, Regions.GT_BOSS): lambda state: False,
            (Regions.MECH_LINUS, Regions.MECH_START): lambda state: False,
            (Regions.MECH_LINUS, Regions.MECH_SWORD_CONNECTION): lambda state: False,
            (Regions.MECH_SWORD_CONNECTION, Regions.MECH_BOOTS_CONNECTION): lambda state: False,
            (Regions.MECH_SWORD_CONNECTION, Regions.GT_UPPER_PATH_CONNECTION): lambda state: False,
            (Regions.MECH_SWORD_CONNECTION, Regions.MECH_LOWER_ARIAS): lambda state: False,
            (Regions.MECH_SWORD_CONNECTION, Regions.MECH_BOTTOM_CAMPFIRE): lambda state: False,
            (Regions.MECH_SWORD_CONNECTION, Regions.MECH_LINUS): lambda state: False,
            (Regions.MECH_SWORD_CONNECTION, Regions.GT_UPPER_ARIAS): lambda state: False,
            (Regions.MECH_BOOTS_CONNECTION, Regions.MECH_BOTTOM_CAMPFIRE): lambda state: False,
            (Regions.MECH_BOOTS_CONNECTION, Regions.MECH_SWORD_CONNECTION): lambda state: False,
            (Regions.MECH_BOOTS_CONNECTION, Regions.MECH_BOOTS_LOWER): lambda state: False,
            (Regions.MECH_BOOTS_LOWER, Regions.MECH_BOOTS_UPPER): lambda state: False,
            (Regions.MECH_BOTTOM_CAMPFIRE, Regions.MECH_BOOTS_CONNECTION): lambda state: False,
            (Regions.MECH_BOTTOM_CAMPFIRE, Regions.MECH_SNAKE): lambda state: False,
            (Regions.MECH_BOTTOM_CAMPFIRE, Regions.MECH_SWORD_CONNECTION): lambda state: False,
            (Regions.MECH_SNAKE, Regions.MECH_BOTTOM_CAMPFIRE): lambda state: False,
            (Regions.MECH_SNAKE, Regions.GT_VOID): lambda state: False,
            (Regions.MECH_LOWER_VOID, Regions.MECH_START): lambda state: False,
            (Regions.MECH_LOWER_VOID, Regions.MECH_UPPER_VOID): lambda state: False,
            (Regions.MECH_LOWER_VOID, Regions.HOTP_MECH_VOID_CONNECTION): lambda state: False,
            (Regions.MECH_ROOTS, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.MECH_ROOTS, Regions.MECH_START): lambda state: False,
            (Regions.MECH_ROOTS, Regions.MECH_BK): lambda state: False,
            (Regions.MECH_ROOTS, Regions.MECH_MUSIC): lambda state: False,
            (Regions.MECH_BK, Regions.MECH_START): lambda state: False,
            (Regions.MECH_BK, Regions.MECH_AFTER_BK): lambda state: False,
            (Regions.MECH_BK, Regions.MECH_ROOTS): lambda state: False,
            (Regions.MECH_AFTER_BK, Regions.MECH_CHAINS): lambda state: False,
            (Regions.MECH_AFTER_BK, Regions.MECH_BK): lambda state: False,
            (Regions.MECH_AFTER_BK, Regions.HOTP_EPIMETHEUS): lambda state: False,
            (Regions.MECH_CHAINS, Regions.MECH_ARIAS_EYEBALL): lambda state: False,
            (Regions.MECH_CHAINS, Regions.MECH_SPLIT_PATH): lambda state: False,
            (Regions.MECH_CHAINS, Regions.MECH_BOSS_SWITCHES): lambda state: False,
            (Regions.MECH_CHAINS, Regions.MECH_BOSS_CONNECTION): lambda state: False,
            (Regions.MECH_CHAINS, Regions.MECH_AFTER_BK): lambda state: False,
            (Regions.MECH_ARIAS_EYEBALL, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.MECH_ARIAS_EYEBALL, Regions.MECH_CHAINS): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.MECH_ARIAS_EYEBALL): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.CATA_BOSS): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.MECH_ROOTS): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.TR_START): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.HOTP_BOSS): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.MECH_ZEEK): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.APEX): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.GT_BOSS): lambda state: False,
            (Regions.MECH_ZEEK_CONNECTION, Regions.MECH_BOSS): lambda state: False,
            (Regions.MECH_SPLIT_PATH, Regions.MECH_RIGHT): lambda state: False,
            (Regions.MECH_SPLIT_PATH, Regions.MECH_CHAINS): lambda state: False,
            (Regions.MECH_RIGHT, Regions.MECH_OLD_MAN): lambda state: False,
            (Regions.MECH_RIGHT, Regions.MECH_SPLIT_PATH): lambda state: False,
            (Regions.MECH_RIGHT, Regions.MECH_POTS): lambda state: False,
            (Regions.MECH_RIGHT, Regions.MECH_UPPER_VOID): lambda state: False,
            (Regions.MECH_UPPER_VOID, Regions.MECH_RIGHT): lambda state: False,
            (Regions.MECH_UPPER_VOID, Regions.MECH_LOWER_VOID): lambda state: False,
            (Regions.MECH_POTS, Regions.MECH_RIGHT): lambda state: False,
            (Regions.MECH_POTS, Regions.MECH_TOP): lambda state: False,
            (Regions.MECH_TOP, Regions.MECH_POTS): lambda state: False,
            (Regions.MECH_TOP, Regions.MECH_TP_CONNECTION): lambda state: False,
            (Regions.MECH_TOP, Regions.CD_START): lambda state: False,
            (Regions.MECH_TP_CONNECTION, Regions.HOTP_FALL_BOTTOM): lambda state: False,
            (Regions.MECH_TP_CONNECTION, Regions.MECH_TOP): lambda state: False,
            (Regions.MECH_TP_CONNECTION, Regions.MECH_CHARACTER_SWAPS): lambda state: False,
            (Regions.MECH_CHARACTER_SWAPS, Regions.MECH_CLOAK_CONNECTION): lambda state: False,
            (Regions.MECH_CHARACTER_SWAPS, Regions.MECH_TP_CONNECTION): lambda state: False,
            (Regions.MECH_CLOAK_CONNECTION, Regions.MECH_BOSS_SWITCHES): lambda state: False,
            (Regions.MECH_CLOAK_CONNECTION, Regions.MECH_CHARACTER_SWAPS): lambda state: False,
            (Regions.MECH_CLOAK_CONNECTION, Regions.MECH_CLOAK): lambda state: False,
            (Regions.MECH_BOSS_SWITCHES, Regions.MECH_BOSS_CONNECTION): lambda state: False,
            (Regions.MECH_BOSS_SWITCHES, Regions.MECH_CLOAK_CONNECTION): lambda state: False,
            (Regions.MECH_BOSS_SWITCHES, Regions.MECH_CHAINS): lambda state: False,
            (Regions.MECH_BOSS_CONNECTION, Regions.MECH_BOSS): lambda state: False,
            (Regions.MECH_BOSS_CONNECTION, Regions.MECH_BRAM_TUNNEL): lambda state: False,
            (Regions.MECH_BOSS_CONNECTION, Regions.MECH_CHAINS): lambda state: False,
            (Regions.MECH_BOSS_CONNECTION, Regions.MECH_BOSS_SWITCHES): lambda state: False,
            (Regions.MECH_BRAM_TUNNEL, Regions.MECH_BOSS_CONNECTION): lambda state: False,
            (Regions.MECH_BRAM_TUNNEL, Regions.HOTP_START_BOTTOM): lambda state: False,
            (Regions.MECH_BOSS, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.MECH_BOSS, Regions.CATA_BOSS): lambda state: False,
            (Regions.MECH_BOSS, Regions.TR_START): lambda state: False,
            (Regions.MECH_BOSS, Regions.MECH_BOSS_CONNECTION): lambda state: False,
            (Regions.MECH_BOSS, Regions.HOTP_BOSS): lambda state: False,
            (Regions.MECH_BOSS, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.MECH_BOSS, Regions.APEX): lambda state: False,
            (Regions.MECH_BOSS, Regions.GT_BOSS): lambda state: False,
            (Regions.MECH_BOSS, Regions.HOTP_START): lambda state: False,
            (Regions.MECH_BOSS, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.MECH_BOSS, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.HOTP_START, Regions.MECH_BOSS): lambda state: False,
            (Regions.HOTP_START, Regions.HOTP_START_BOTTOM): lambda state: False,
            (Regions.HOTP_START, Regions.HOTP_START_MID): lambda state: False,
            (Regions.HOTP_START_MID, Regions.HOTP_START_LEFT): lambda state: False,
            (Regions.HOTP_START_MID, Regions.HOTP_START_BOTTOM): lambda state: False,
            (Regions.HOTP_START_MID, Regions.HOTP_LOWER_VOID): lambda state: False,
            (Regions.HOTP_START_MID, Regions.HOTP_START): lambda state: False,
            (Regions.HOTP_LOWER_VOID, Regions.HOTP_START_MID): lambda state: False,
            (Regions.HOTP_LOWER_VOID, Regions.HOTP_UPPER_VOID): lambda state: False,
            (Regions.HOTP_START_LEFT, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.HOTP_START_LEFT, Regions.HOTP_START_MID): lambda state: False,
            (Regions.HOTP_START_BOTTOM, Regions.MECH_BRAM_TUNNEL): lambda state: False,
            (Regions.HOTP_START_BOTTOM, Regions.HOTP_START): lambda state: False,
            (Regions.HOTP_LOWER, Regions.HOTP_START_BOTTOM): lambda state: False,
            (Regions.HOTP_LOWER, Regions.HOTP_EPIMETHEUS): lambda state: False,
            (Regions.HOTP_LOWER, Regions.HOTP_TP_TUTORIAL): lambda state: False,
            (Regions.HOTP_LOWER, Regions.HOTP_MECH_VOID_CONNECTION): lambda state: False,
            (Regions.HOTP_EPIMETHEUS, Regions.MECH_AFTER_BK): lambda state: False,
            (Regions.HOTP_EPIMETHEUS, Regions.HOTP_LOWER): lambda state: False,
            (Regions.HOTP_MECH_VOID_CONNECTION, Regions.HOTP_AMULET_CONNECTION): lambda state: False,
            (Regions.HOTP_MECH_VOID_CONNECTION, Regions.MECH_LOWER_VOID): lambda state: False,
            (Regions.HOTP_MECH_VOID_CONNECTION, Regions.HOTP_LOWER): lambda state: False,
            (Regions.HOTP_AMULET_CONNECTION, Regions.HOTP_AMULET): lambda state: False,
            (Regions.HOTP_AMULET_CONNECTION, Regions.GT_BUTT): lambda state: False,
            (Regions.HOTP_AMULET_CONNECTION, Regions.HOTP_MECH_VOID_CONNECTION): lambda state: False,
            (Regions.HOTP_TP_TUTORIAL, Regions.HOTP_BELL_CAMPFIRE): lambda state: False,
            (Regions.HOTP_TP_TUTORIAL, Regions.HOTP_LOWER): lambda state: False,
            (Regions.HOTP_BELL_CAMPFIRE, Regions.HOTP_LOWER_ARIAS): lambda state: False,
            (Regions.HOTP_BELL_CAMPFIRE, Regions.HOTP_RED_KEY): lambda state: False,
            (Regions.HOTP_BELL_CAMPFIRE, Regions.HOTP_CATH_CONNECTION): lambda state: False,
            (Regions.HOTP_BELL_CAMPFIRE, Regions.HOTP_TP_TUTORIAL): lambda state: False,
            (Regions.HOTP_BELL_CAMPFIRE, Regions.HOTP_BELL): lambda state: False,
            (Regions.HOTP_CATH_CONNECTION, Regions.HOTP_BELL_CAMPFIRE): lambda state: False,
            (Regions.HOTP_CATH_CONNECTION, Regions.HOTP_BELL): lambda state: False,
            (Regions.HOTP_CATH_CONNECTION, Regions.CATH_START): lambda state: False,
            (Regions.HOTP_LOWER_ARIAS, Regions.HOTP_BELL_CAMPFIRE): lambda state: False,
            (Regions.HOTP_LOWER_ARIAS, Regions.HOTP_EYEBALL): lambda state: False,
            (Regions.HOTP_EYEBALL, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.HOTP_EYEBALL, Regions.HOTP_LOWER_ARIAS): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.HOTP_OLD_MAN): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.HOTP_TOP_LEFT): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.CATA_BOSS): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.TR_START): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.HOTP_START_LEFT): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.HOTP_EYEBALL): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.HOTP_CLAW_LEFT): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.HOTP_BOSS): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.APEX): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.GT_BOSS): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.HOTP_ELEVATOR, Regions.MECH_BOSS): lambda state: False,
            (Regions.HOTP_CLAW_LEFT, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.HOTP_CLAW_LEFT, Regions.HOTP_TOP_LEFT): lambda state: False,
            (Regions.HOTP_CLAW_LEFT, Regions.HOTP_CLAW): lambda state: False,
            (Regions.HOTP_TOP_LEFT, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.HOTP_TOP_LEFT, Regions.HOTP_CLAW_CAMPFIRE): lambda state: False,
            (Regions.HOTP_TOP_LEFT, Regions.HOTP_CLAW_LEFT): lambda state: False,
            (Regions.HOTP_TOP_LEFT, Regions.HOTP_ABOVE_OLD_MAN): lambda state: False,
            (Regions.HOTP_CLAW_CAMPFIRE, Regions.HOTP_TOP_LEFT): lambda state: False,
            (Regions.HOTP_CLAW_CAMPFIRE, Regions.HOTP_CLAW): lambda state: False,
            (Regions.HOTP_CLAW_CAMPFIRE, Regions.HOTP_HEART): lambda state: False,
            (Regions.HOTP_CLAW, Regions.HOTP_CLAW_CAMPFIRE): lambda state: False,
            (Regions.HOTP_CLAW, Regions.HOTP_CLAW_LEFT): lambda state: False,
            (Regions.HOTP_HEART, Regions.HOTP_CLAW_CAMPFIRE): lambda state: False,
            (Regions.HOTP_HEART, Regions.HOTP_UPPER_ARIAS): lambda state: False,
            (Regions.HOTP_HEART, Regions.HOTP_BOSS_CAMPFIRE): lambda state: False,
            (Regions.HOTP_UPPER_ARIAS, Regions.HOTP_HEART): lambda state: False,
            (Regions.HOTP_UPPER_ARIAS, Regions.HOTP_BOSS_CAMPFIRE): lambda state: False,
            (Regions.HOTP_BOSS_CAMPFIRE, Regions.HOTP_MAIDEN): lambda state: False,
            (Regions.HOTP_BOSS_CAMPFIRE, Regions.HOTP_HEART): lambda state: False,
            (Regions.HOTP_BOSS_CAMPFIRE, Regions.HOTP_TP_PUZZLE): lambda state: False,
            (Regions.HOTP_BOSS_CAMPFIRE, Regions.HOTP_BOSS): lambda state: False,
            (Regions.HOTP_TP_PUZZLE, Regions.HOTP_TP_FALL_TOP): lambda state: False,
            (Regions.HOTP_TP_FALL_TOP, Regions.HOTP_FALL_BOTTOM): lambda state: False,
            (Regions.HOTP_TP_FALL_TOP, Regions.HOTP_TP_PUZZLE): lambda state: False,
            (Regions.HOTP_TP_FALL_TOP, Regions.HOTP_GAUNTLET_CONNECTION): lambda state: False,
            (Regions.HOTP_TP_FALL_TOP, Regions.HOTP_BOSS_CAMPFIRE): lambda state: False,
            (Regions.HOTP_GAUNTLET_CONNECTION, Regions.HOTP_GAUNTLET): lambda state: False,
            (Regions.HOTP_FALL_BOTTOM, Regions.HOTP_TP_FALL_TOP): lambda state: False,
            (Regions.HOTP_FALL_BOTTOM, Regions.MECH_TP_CONNECTION): lambda state: False,
            (Regions.HOTP_UPPER_VOID, Regions.HOTP_FALL_BOTTOM): lambda state: False,
            (Regions.HOTP_UPPER_VOID, Regions.HOTP_TP_FALL_TOP): lambda state: False,
            (Regions.HOTP_UPPER_VOID, Regions.HOTP_LOWER_VOID): lambda state: False,
            (Regions.HOTP_BOSS, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.HOTP_BOSS, Regions.CATA_BOSS): lambda state: False,
            (Regions.HOTP_BOSS, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.HOTP_BOSS, Regions.HOTP_BOSS_CAMPFIRE): lambda state: False,
            (Regions.HOTP_BOSS, Regions.TR_START): lambda state: False,
            (Regions.HOTP_BOSS, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.HOTP_BOSS, Regions.APEX): lambda state: False,
            (Regions.HOTP_BOSS, Regions.GT_BOSS): lambda state: False,
            (Regions.HOTP_BOSS, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.HOTP_BOSS, Regions.ROA_START): lambda state: False,
            (Regions.HOTP_BOSS, Regions.MECH_BOSS): lambda state: False,
            (Regions.ROA_START, Regions.HOTP_BOSS): lambda state: False,
            (Regions.ROA_START, Regions.ROA_WORMS): lambda state: False,
            (Regions.ROA_WORMS, Regions.ROA_HEARTS): lambda state: False,
            (Regions.ROA_WORMS, Regions.ROA_START): lambda state: False,
            (Regions.ROA_WORMS, Regions.ROA_LOWER_VOID_CONNECTION): lambda state: False,
            (Regions.ROA_HEARTS, Regions.ROA_BOTTOM_ASCEND): lambda state: False,
            (Regions.ROA_HEARTS, Regions.ROA_SPIKE_CLIMB): lambda state: False,
            (Regions.ROA_HEARTS, Regions.ROA_WORMS): lambda state: False,
            (Regions.ROA_SPIKE_CLIMB, Regions.ROA_HEARTS): lambda state: False,
            (Regions.ROA_SPIKE_CLIMB, Regions.ROA_BOTTOM_ASCEND): lambda state: False,
            (Regions.ROA_BOTTOM_ASCEND, Regions.ROA_HEARTS): lambda state: False,
            (Regions.ROA_BOTTOM_ASCEND, Regions.ROA_ARENA): lambda state: False,
            (Regions.ROA_BOTTOM_ASCEND, Regions.ROA_SPIKE_CLIMB): lambda state: False,
            (Regions.ROA_BOTTOM_ASCEND, Regions.ROA_TOP_ASCENT): lambda state: False,
            (Regions.ROA_ARENA, Regions.ROA_FLAMES_CONNECTION): lambda state: False,
            (Regions.ROA_ARENA, Regions.ROA_BOTTOM_ASCEND): lambda state: False,
            (Regions.ROA_ARENA, Regions.ROA_LOWER_VOID_CONNECTION): lambda state: False,
            (Regions.ROA_LOWER_VOID_CONNECTION, Regions.ROA_ARIAS_BABY_GORGON): lambda state: False,
            (Regions.ROA_LOWER_VOID_CONNECTION, Regions.ROA_WORMS): lambda state: False,
            (Regions.ROA_LOWER_VOID_CONNECTION, Regions.ROA_FLAMES_CONNECTION): lambda state: False,
            (Regions.ROA_LOWER_VOID_CONNECTION, Regions.ROA_LOWER_VOID): lambda state: False,
            (Regions.ROA_LOWER_VOID_CONNECTION, Regions.ROA_ARENA): lambda state: False,
            (Regions.ROA_LOWER_VOID, Regions.ROA_UPPER_VOID): lambda state: False,
            (Regions.ROA_LOWER_VOID, Regions.ROA_LOWER_VOID_CONNECTION): lambda state: False,
            (Regions.ROA_ARIAS_BABY_GORGON, Regions.ROA_FLAMES_CONNECTION): lambda state: False,
            (Regions.ROA_ARIAS_BABY_GORGON, Regions.ROA_FLAMES): lambda state: False,
            (Regions.ROA_ARIAS_BABY_GORGON, Regions.ROA_LOWER_VOID_CONNECTION): lambda state: False,
            (Regions.ROA_FLAMES_CONNECTION, Regions.ROA_WORM_CLIMB): lambda state: False,
            (Regions.ROA_FLAMES_CONNECTION, Regions.ROA_LEFT_ASCENT): lambda state: False,
            (Regions.ROA_FLAMES_CONNECTION, Regions.ROA_ARIAS_BABY_GORGON): lambda state: False,
            (Regions.ROA_FLAMES_CONNECTION, Regions.ROA_ARENA): lambda state: False,
            (Regions.ROA_FLAMES_CONNECTION, Regions.ROA_FLAMES): lambda state: False,
            (Regions.ROA_FLAMES_CONNECTION, Regions.ROA_LOWER_VOID_CONNECTION): lambda state: False,
            (Regions.ROA_FLAMES, Regions.ROA_FLAMES_CONNECTION): lambda state: False,
            (Regions.ROA_FLAMES, Regions.ROA_ARIAS_BABY_GORGON): lambda state: False,
            (Regions.ROA_WORM_CLIMB, Regions.ROA_FLAMES_CONNECTION): lambda state: False,
            (Regions.ROA_WORM_CLIMB, Regions.ROA_RIGHT_BRANCH): lambda state: False,
            (Regions.ROA_RIGHT_BRANCH, Regions.ROA_WORM_CLIMB): lambda state: False,
            (Regions.ROA_RIGHT_BRANCH, Regions.ROA_MIDDLE): lambda state: False,
            (Regions.ROA_LEFT_ASCENT, Regions.ROA_FLAMES_CONNECTION): lambda state: False,
            (Regions.ROA_LEFT_ASCENT, Regions.ROA_TOP_ASCENT): lambda state: False,
            (Regions.ROA_TOP_ASCENT, Regions.ROA_TRIPLE_SWITCH): lambda state: False,
            (Regions.ROA_TOP_ASCENT, Regions.ROA_LEFT_ASCENT): lambda state: False,
            (Regions.ROA_TRIPLE_SWITCH, Regions.ROA_MIDDLE): lambda state: False,
            (Regions.ROA_TRIPLE_SWITCH, Regions.ROA_TOP_ASCENT): lambda state: False,
            (Regions.ROA_MIDDLE, Regions.ROA_LEFT_SWITCH): lambda state: False,
            (Regions.ROA_MIDDLE, Regions.ROA_RIGHT_BRANCH): lambda state: False,
            (Regions.ROA_MIDDLE, Regions.ROA_RIGHT_SWITCH_1): lambda state: False,
            (Regions.ROA_MIDDLE, Regions.ROA_MIDDLE_LADDER): lambda state: False,
            (Regions.ROA_MIDDLE, Regions.ROA_TRIPLE_SWITCH): lambda state: False,
            (Regions.ROA_MIDDLE, Regions.ROA_LEFT_BABY_GORGON): lambda state: False,
            (Regions.ROA_RIGHT_SWITCH_1, Regions.ROA_RIGHT_SWITCH_2): lambda state: False,
            (Regions.ROA_RIGHT_SWITCH_2, Regions.ROA_RIGHT_SWITCH_3): lambda state: False,
            (Regions.ROA_MIDDLE_LADDER, Regions.ROA_MIDDLE): lambda state: False,
            (Regions.ROA_MIDDLE_LADDER, Regions.ROA_UPPER_VOID): lambda state: False,
            (Regions.ROA_UPPER_VOID, Regions.ROA_MIDDLE_LADDER): lambda state: False,
            (Regions.ROA_UPPER_VOID, Regions.ROA_LOWER_VOID): lambda state: False,
            (Regions.ROA_UPPER_VOID, Regions.ROA_SP_CONNECTION): lambda state: False,
            (Regions.ROA_UPPER_VOID, Regions.ROA_SPIKE_BALLS): lambda state: False,
            (Regions.ROA_SPIKE_BALLS, Regions.ROA_SPIKE_SPINNERS): lambda state: False,
            (Regions.ROA_SPIKE_BALLS, Regions.ROA_UPPER_VOID): lambda state: False,
            (Regions.ROA_SPIKE_SPINNERS, Regions.ROA_SPIDERS_1): lambda state: False,
            (Regions.ROA_SPIKE_SPINNERS, Regions.ROA_SPIKE_BALLS): lambda state: False,
            (Regions.ROA_SPIDERS_1, Regions.ROA_RED_KEY): lambda state: False,
            (Regions.ROA_SPIDERS_1, Regions.ROA_SPIDERS_2): lambda state: False,
            (Regions.ROA_SPIDERS_1, Regions.ROA_SPIKE_SPINNERS): lambda state: False,
            (Regions.ROA_SPIDERS_2, Regions.ROA_SPIDERS_1): lambda state: False,
            (Regions.ROA_SPIDERS_2, Regions.ROA_BLOOD_POT_HALLWAY): lambda state: False,
            (Regions.ROA_BLOOD_POT_HALLWAY, Regions.ROA_SP_CONNECTION): lambda state: False,
            (Regions.ROA_BLOOD_POT_HALLWAY, Regions.ROA_SPIDERS_2): lambda state: False,
            (Regions.ROA_SP_CONNECTION, Regions.ROA_BLOOD_POT_HALLWAY): lambda state: False,
            (Regions.ROA_SP_CONNECTION, Regions.SP_START): lambda state: False,
            (Regions.ROA_SP_CONNECTION, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.ROA_SP_CONNECTION, Regions.ROA_UPPER_VOID): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.CATA_BOSS): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.ROA_SP_CONNECTION): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.TR_START): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.HOTP_BOSS): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.ROA_ICARUS): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.ROA_DARK_CONNECTION): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.APEX): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.GT_BOSS): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.ROA_ELEVATOR, Regions.MECH_BOSS): lambda state: False,
            (Regions.ROA_DARK_CONNECTION, Regions.ROA_DARK_CONNECTION): lambda state: False,
            (Regions.ROA_DARK_CONNECTION, Regions.ROA_CENTAUR): lambda state: False,
            (Regions.ROA_DARK_CONNECTION, Regions.DARK_START): lambda state: False,
            (Regions.DARK_START, Regions.DARK_END): lambda state: False,
            (Regions.DARK_END, Regions.ROA_CENTAUR): lambda state: False,
            (Regions.ROA_CENTAUR, Regions.ROA_DARK_CONNECTION): lambda state: False,
            (Regions.ROA_CENTAUR, Regions.ROA_BOSS_CONNECTION): lambda state: False,
            (Regions.ROA_BOSS_CONNECTION, Regions.ROA_BOSS): lambda state: False,
            (Regions.ROA_BOSS_CONNECTION, Regions.ROA_CENTAUR): lambda state: False,
            (Regions.ROA_BOSS, Regions.ROA_APEX_CONNECTION): lambda state: False,
            (Regions.ROA_BOSS, Regions.ROA_BOSS_CONNECTION): lambda state: False,
            (Regions.ROA_APEX_CONNECTION, Regions.ROA_BOSS): lambda state: False,
            (Regions.ROA_APEX_CONNECTION, Regions.APEX): lambda state: False,
            (Regions.APEX, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.APEX, Regions.CATA_BOSS): lambda state: False,
            (Regions.APEX, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.APEX, Regions.FINAL_BOSS): lambda state: False,
            (Regions.APEX, Regions.ROA_APEX_CONNECTION): lambda state: False,
            (Regions.APEX, Regions.TR_START): lambda state: False,
            (Regions.APEX, Regions.APEX_HEART): lambda state: False,
            (Regions.APEX, Regions.HOTP_BOSS): lambda state: False,
            (Regions.APEX, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.APEX, Regions.GT_BOSS): lambda state: False,
            (Regions.APEX, Regions.APEX_CENTAUR): lambda state: False,
            (Regions.APEX, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.APEX, Regions.MECH_BOSS): lambda state: False,
            (Regions.CAVES_START, Regions.CAVES_STATUE): lambda state: False,
            (Regions.CAVES_START, Regions.GT_BOTTOM): lambda state: False,
            (Regions.CAVES_STATUE, Regions.CAVES_UPPER): lambda state: False,
            (Regions.CAVES_STATUE, Regions.CAVES_START): lambda state: False,
            (Regions.CAVES_UPPER, Regions.CAVES_STATUE): lambda state: False,
            (Regions.CAVES_UPPER, Regions.CAVES_ARENA): lambda state: False,
            (Regions.CAVES_UPPER, Regions.CAVES_LOWER): lambda state: False,
            (Regions.CAVES_LOWER, Regions.CAVES_UPPER): lambda state: False,
            (Regions.CAVES_LOWER, Regions.CAVES_ITEM_CHAIN): lambda state: False,
            (Regions.CAVES_LOWER, Regions.CATA_START): lambda state: False,
            (Regions.CATA_START, Regions.CATA_CLIMBABLE_ROOT): lambda state: False,
            (Regions.CATA_START, Regions.CAVES_LOWER): lambda state: False,
            (Regions.CATA_CLIMBABLE_ROOT, Regions.CATA_TOP): lambda state: False,
            (Regions.CATA_TOP, Regions.CATA_CLIMBABLE_ROOT): lambda state: False,
            (Regions.CATA_TOP, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.CATA_TOP, Regions.CATA_BOW_CAMPFIRE): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.CATA_BOSS): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.TR_START): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.HOTP_BOSS): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.APEX): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.GT_BOSS): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.CATA_TOP): lambda state: False,
            (Regions.CATA_ELEVATOR, Regions.MECH_BOSS): lambda state: False,
            (Regions.CATA_BOW_CAMPFIRE, Regions.CATA_TOP): lambda state: False,
            (Regions.CATA_BOW_CAMPFIRE, Regions.CATA_BOW_CONNECTION): lambda state: False,
            (Regions.CATA_BOW_CAMPFIRE, Regions.CATA_EYEBALL_BONES): lambda state: False,
            (Regions.CATA_BOW_CONNECTION, Regions.CATA_BOW): lambda state: False,
            (Regions.CATA_BOW_CONNECTION, Regions.CATA_BOW_CAMPFIRE): lambda state: False,
            (Regions.CATA_BOW_CONNECTION, Regions.CATA_VERTICAL_SHORTCUT): lambda state: False,
            (Regions.CATA_VERTICAL_SHORTCUT, Regions.CATA_BLUE_EYE_DOOR): lambda state: False,
            (Regions.CATA_VERTICAL_SHORTCUT, Regions.CATA_BOW_CONNECTION): lambda state: False,
            (Regions.CATA_EYEBALL_BONES, Regions.CATA_SNAKE_MUSHROOMS): lambda state: False,
            (Regions.CATA_EYEBALL_BONES, Regions.CATA_BOW_CAMPFIRE): lambda state: False,
            (Regions.CATA_SNAKE_MUSHROOMS, Regions.CATA_DEV_ROOM_CONNECTION): lambda state: False,
            (Regions.CATA_SNAKE_MUSHROOMS, Regions.CATA_EYEBALL_BONES): lambda state: False,
            (Regions.CATA_SNAKE_MUSHROOMS, Regions.CATA_DOUBLE_SWITCH): lambda state: False,
            (Regions.CATA_DEV_ROOM_CONNECTION, Regions.CATA_DEV_ROOM): lambda state: False,
            (Regions.CATA_DOUBLE_SWITCH, Regions.CATA_SNAKE_MUSHROOMS): lambda state: False,
            (Regions.CATA_DOUBLE_SWITCH, Regions.CATA_ROOTS_CAMPFIRE): lambda state: False,
            (Regions.CATA_ROOTS_CAMPFIRE, Regions.CATA_BLUE_EYE_DOOR): lambda state: False,
            (Regions.CATA_ROOTS_CAMPFIRE, Regions.CATA_POISON_ROOTS): lambda state: False,
            (Regions.CATA_ROOTS_CAMPFIRE, Regions.CATA_DOUBLE_SWITCH): lambda state: False,
            (Regions.CATA_BLUE_EYE_DOOR, Regions.CATA_CENTAUR): lambda state: False,
            (Regions.CATA_BLUE_EYE_DOOR, Regions.CATA_FLAMES): lambda state: False,
            (Regions.CATA_BLUE_EYE_DOOR, Regions.CATA_ROOTS_CAMPFIRE): lambda state: False,
            (Regions.CATA_BLUE_EYE_DOOR, Regions.CATA_VERTICAL_SHORTCUT): lambda state: False,
            (Regions.CATA_CENTAUR, Regions.CATA_4_FACES): lambda state: False,
            (Regions.CATA_CENTAUR, Regions.CATA_BLUE_EYE_DOOR): lambda state: False,
            (Regions.CATA_CENTAUR, Regions.CATA_BOSS): lambda state: False,
            (Regions.CATA_4_FACES, Regions.CATA_CENTAUR): lambda state: False,
            (Regions.CATA_4_FACES, Regions.CATA_DOUBLE_DOOR): lambda state: False,
            (Regions.CATA_DOUBLE_DOOR, Regions.CATA_4_FACES): lambda state: False,
            (Regions.CATA_DOUBLE_DOOR, Regions.CATA_VOID): lambda state: False,
            (Regions.CATA_VOID, Regions.CATA_BOSS): lambda state: False,
            (Regions.CATA_VOID, Regions.CATA_DOUBLE_DOOR): lambda state: False,
            (Regions.CATA_BOSS, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.CATA_BOSS, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.CATA_BOSS, Regions.CATA_VOID): lambda state: False,
            (Regions.CATA_BOSS, Regions.TR_START): lambda state: False,
            (Regions.CATA_BOSS, Regions.HOTP_BOSS): lambda state: False,
            (Regions.CATA_BOSS, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.CATA_BOSS, Regions.APEX): lambda state: False,
            (Regions.CATA_BOSS, Regions.GT_BOSS): lambda state: False,
            (Regions.CATA_BOSS, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.CATA_BOSS, Regions.MECH_BOSS): lambda state: False,
            (Regions.TR_START, Regions.CATA_ELEVATOR): lambda state: False,
            (Regions.TR_START, Regions.CATA_BOSS): lambda state: False,
            (Regions.TR_START, Regions.HOTP_ELEVATOR): lambda state: False,
            (Regions.TR_START, Regions.HOTP_BOSS): lambda state: False,
            (Regions.TR_START, Regions.ROA_ELEVATOR): lambda state: False,
            (Regions.TR_START, Regions.TR_LEFT): lambda state: False,
            (Regions.TR_START, Regions.APEX): lambda state: False,
            (Regions.TR_START, Regions.GT_BOSS): lambda state: False,
            (Regions.TR_START, Regions.MECH_ZEEK_CONNECTION): lambda state: False,
            (Regions.TR_START, Regions.MECH_BOSS): lambda state: False,
            (Regions.TR_START, Regions.TR_BRAM): lambda state: False,
            (Regions.TR_LEFT, Regions.TR_TOP_RIGHT): lambda state: False,
            (Regions.TR_LEFT, Regions.TR_BOTTOM_LEFT): lambda state: False,
            (Regions.TR_BOTTOM_LEFT, Regions.TR_BOTTOM): lambda state: False,
            (Regions.TR_TOP_RIGHT, Regions.TR_GOLD): lambda state: False,
            (Regions.TR_TOP_RIGHT, Regions.TR_MIDDLE_RIGHT): lambda state: False,
            (Regions.TR_MIDDLE_RIGHT, Regions.TD_DARK_ARIAS): lambda state: False,
            (Regions.TR_MIDDLE_RIGHT, Regions.TR_BOTTOM): lambda state: False,
            (Regions.TR_BOTTOM, Regions.TR_BOTTOM_LEFT): lambda state: False,
            (Regions.CD_START, Regions.CD_2): lambda state: False,
            (Regions.CD_START, Regions.CD_BOSS): lambda state: False,
            (Regions.CD_2, Regions.CD_3): lambda state: False,
            (Regions.CD_3, Regions.CD_MIDDLE): lambda state: False,
            (Regions.CD_MIDDLE, Regions.CD_KYULI_ROUTE): lambda state: False,
            (Regions.CD_MIDDLE, Regions.CD_ARIAS_ROUTE): lambda state: False,
            (Regions.CD_KYULI_ROUTE, Regions.CD_CAMPFIRE_3): lambda state: False,
            (Regions.CD_CAMPFIRE_3, Regions.CD_ARENA): lambda state: False,
            (Regions.CD_ARENA, Regions.CD_STEPS): lambda state: False,
            (Regions.CD_STEPS, Regions.CD_TOP): lambda state: False,
            (Regions.CATH_START, Regions.CATH_START_LEFT): lambda state: False,
            (Regions.CATH_START, Regions.CATH_START_RIGHT): lambda state: False,
            (Regions.CATH_START_RIGHT, Regions.CATH_START_TOP_LEFT): lambda state: False,
            (Regions.CATH_START_TOP_LEFT, Regions.CATH_START_LEFT): lambda state: False,
            (Regions.CATH_START_LEFT, Regions.CATH_TP): lambda state: False,
            (Regions.CATH_TP, Regions.CATH_LEFT_SHAFT): lambda state: False,
            (Regions.CATH_LEFT_SHAFT, Regions.CATH_SHAFT_ACCESS): lambda state: False,
            (Regions.CATH_LEFT_SHAFT, Regions.CATH_UNDER_CAMPFIRE): lambda state: False,
            (Regions.CATH_UNDER_CAMPFIRE, Regions.CATH_CAMPFIRE_1): lambda state: False,
            (Regions.CATH_CAMPFIRE_1, Regions.CATH_SHAFT_ACCESS): lambda state: False,
            (Regions.CATH_SHAFT_ACCESS, Regions.CATH_ORB_ROOM): lambda state: False,
            (Regions.CATH_ORB_ROOM, Regions.CATH_GOLD_BLOCK): lambda state: False,
            (Regions.CATH_ORB_ROOM, Regions.CATH_RIGHT_SHAFT_CONNECTION): lambda state: False,
            (Regions.CATH_RIGHT_SHAFT_CONNECTION, Regions.CATH_RIGHT_SHAFT): lambda state: False,
            (Regions.CATH_RIGHT_SHAFT, Regions.CATH_TOP): lambda state: False,
            (Regions.CATH_TOP, Regions.CATH_UPPER_SPIKE_PIT): lambda state: False,
            (Regions.CATH_TOP, Regions.CATH_CAMPFIRE_2): lambda state: False,
            (Regions.SP_START, Regions.SP_STAR_END): lambda state: False,
            (Regions.SP_START, Regions.SP_CAMPFIRE_1): lambda state: False,
            (Regions.SP_CAMPFIRE_1, Regions.SP_HEARTS): lambda state: False,
            (Regions.SP_HEARTS, Regions.SP_ORBS): lambda state: False,
            (Regions.SP_HEARTS, Regions.SP_FROG): lambda state: False,
            (Regions.SP_HEARTS, Regions.SP_PAINTING): lambda state: False,
            (Regions.SP_PAINTING, Regions.SP_SHAFT): lambda state: False,
            (Regions.SP_SHAFT, Regions.SP_STAR): lambda state: False,
            (Regions.SP_STAR, Regions.SP_STAR_CONNECTION): lambda state: False,
            (Regions.SP_STAR_CONNECTION, Regions.SP_STAR_END): lambda state: False,
            (Regions.SP_FROG, Regions.SP_CAMPFIRE_2): lambda state: False,
        }

        self.entrance_rules = {
            (Regions.GT_START, Regions.GT_MID): lambda state: self.white_doors(state, Items.DOOR_WHITE_GT_START),
            (Regions.GT_START, Regions.GT_LEFT): lambda state: self.has_any(state, Items.ICARUS, Items.BOOTS),
            (Regions.GT_START, Regions.APEX): lambda state: (
                self.has(state, Items.ASCENDANT_KEY) if self.options.free_apex_elevator else False
            ),
            (Regions.GT_MID, Regions.GT_LEFT): lambda state: self.white_doors(state, Items.DOOR_WHITE_GT_MAP),
            (Regions.GT_MID, Regions.CATA_UPPER): lambda state: self.blue_doors(state, Items.DOOR_BLUE_CATA_START),
            (Regions.GT_LEFT, Regions.GT_BOSS): lambda state: self.white_doors(state, Items.DOOR_WHITE_GT_TAUROS),
            (Regions.GT_LEFT, Regions.GT_MID): lambda _: True,
            (Regions.GT_BOSS, Regions.MECH_LOWER): lambda state: self.has(state, Items.EYE_RED),
            (Regions.MECH_LOWER, Regions.MECH_UPPER): lambda state: (
                (
                    self.white_doors(state, Items.DOOR_WHITE_MECH_2ND)
                    or self.blue_doors(state, Items.DOOR_BLUE_MECH_SHORTCUT)
                )
                and (self.has(state, Items.CLAW) or self.white_doors(state, Items.DOOR_WHITE_MECH_BK))
            ),
            (Regions.MECH_LOWER, Regions.HOTP_BOTTOM): lambda state: (
                self.blue_doors(state, Items.DOOR_BLUE_MECH_RED) and self.has(state, Items.EYE_BLUE)
            ),
            (Regions.MECH_LOWER, Regions.HOTP_LOWER): lambda state: (
                (
                    self.white_doors(state, Items.DOOR_WHITE_MECH_2ND)
                    or self.blue_doors(state, Items.DOOR_BLUE_MECH_SHORTCUT)
                )
                and self.has(state, Items.CLAW)
            ),
            (Regions.MECH_LOWER, Regions.GT_UPPER): lambda _: True,
            (Regions.MECH_UPPER, Regions.HOTP_START): lambda state: (
                self.has_any(state, Items.EYE_BLUE, Items.STAR)
                and (
                    self.has(state, Items.CLAW)
                    or self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA, Items.DOOR_WHITE_MECH_TOP)
                )
            ),
            (Regions.MECH_UPPER, Regions.HOTP_UPPER): lambda state: (
                self.has(state, Items.CLAW) and self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA)
            ),
            (Regions.MECH_UPPER, Regions.CD): lambda state: (
                self.has(state, Items.CYCLOPS, Items.EYE_BLUE)
                and self.blue_doors(state, Items.DOOR_BLUE_MECH_CD)
                and self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA)
            ),
            (Regions.HOTP_BOTTOM, Regions.HOTP_LOWER): lambda _: True,
            (Regions.HOTP_LOWER, Regions.HOTP_BELL): lambda _: True,
            (Regions.HOTP_LOWER, Regions.MECH_LOWER): lambda state: (
                self.has(state, Items.CLAW) and self.blue_doors(state, Items.DOOR_BLUE_HOTP_STATUE)
            ),
            (Regions.HOTP_START, Regions.HOTP_UPPER): lambda state: (
                self.has(state, Items.VOID, Items.EYE_GREEN, Items.CLAW)
                and (self.has(state, Items.EYE_BLUE) or self.has(state, Items.STAR, Items.BELL))
            ),
            (Regions.HOTP_START, Regions.HOTP_LOWER): lambda state: (
                self.has(state, Items.STAR)
                or (self.has(state, Items.EYE_BLUE) and self.white_doors(state, Items.DOOR_WHITE_HOTP_START))
            ),
            (Regions.HOTP_START, Regions.MECH_UPPER): lambda state: self.has_any(state, Items.EYE_BLUE, Items.STAR),
            (Regions.HOTP_BELL, Regions.HOTP_MID): lambda state: self.has(state, Items.BELL),
            (Regions.HOTP_BELL, Regions.CATH): lambda state: (
                self.has(state, Items.EYE_GREEN, Items.BOW, Items.BELL, Items.ZEEK, Items.CLAW, Items.VOID)
                and self.red_doors(state, Items.DOOR_RED_CATH, disabled_case=self.has(state, Items.CLOAK))
            ),
            # check if door is necessary
            (Regions.HOTP_MID, Regions.HOTP_UPPER): lambda state: (
                self.has(state, Items.CLAW) or self.white_doors(state, Items.DOOR_WHITE_HOTP_CLAW)
            ),
            (Regions.HOTP_MID, Regions.HOTP_BELL): lambda _: True,
            (Regions.HOTP_MID, Regions.HOTP_START): lambda state: self.has(state, Items.STAR),
            (Regions.HOTP_UPPER, Regions.ROA_LOWER): lambda state: (
                self.has(
                    # bell not needed if kyuli has claw and beam, should redo logic once shop is in rando
                    # algus can hit the switch if he has banish and bigger projectiles, though this doesn't seem to matter checks-wise yet
                    # can bram hit it with longer whip?
                    state,
                    Items.CLAW,
                    Items.BELL,
                )
                and self.white_doors(state, Items.DOOR_WHITE_HOTP_BOSS)
            ),
            (Regions.HOTP_UPPER, Regions.HOTP_MID): lambda state: self.has_any(state, Items.CLOAK, Items.ICARUS),
            (Regions.HOTP_UPPER, Regions.HOTP_START): lambda state: (
                self.has(state, Items.EYE_GREEN, Items.CLAW, Items.CLOAK, Items.VOID)
            ),
            (Regions.HOTP_UPPER, Regions.MECH_UPPER): lambda state: (
                self.has(state, Items.EYE_GREEN, Items.CLAW, Items.CLOAK)
            ),
            (Regions.ROA_LOWER, Regions.ROA_MID): lambda state: (
                self.white_doors(state, Items.DOOR_WHITE_ROA_WORMS)
                and (
                    self.white_doors(state, Items.DOOR_WHITE_ROA_ASCEND)
                    or (self.has(state, Items.STAR) and self.blue_doors(state, Items.DOOR_BLUE_ROA_FLAMES))
                )
            ),
            (Regions.ROA_MID, Regions.ROA_UPPER): lambda state: (
                self.white_doors(state, Items.DOOR_WHITE_ROA_BALLS, Items.DOOR_WHITE_ROA_SPINNERS)
            ),
            (Regions.ROA_UPPER, Regions.APEX): lambda state: self.has(state, Items.EYE_GREEN),
            (Regions.ROA_UPPER, Regions.SP): lambda state: (
                self.red_doors(state, Items.DOOR_RED_SP, disabled_case=self.has(state, Items.CLOAK, Items.BOW))
            ),
            (Regions.APEX, Regions.FINAL_BOSS): lambda state: (
                # if difficulties are added, bell shouldn't be required on hard
                # TODO: minimum amount of hp/attack upgrades for logical completion?
                self.has(state, Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.BELL)
            ),
            (Regions.CATA_UPPER, Regions.CATA_MID): lambda state: (
                self.has(state, Items.EYE_RED) and self.white_doors(state, Items.DOOR_WHITE_CATA_TOP)
            ),
            (Regions.CATA_MID, Regions.CATA_LOWER): lambda state: (
                self.has(state, Items.BOW, Items.EYE_BLUE)
                and self.white_doors(state, Items.DOOR_WHITE_CATA_BLUE)
                and (self.has(state, Items.CLAW) or self.has(state, Items.ZEEK, Items.BELL))
            ),
            (Regions.CATA_MID, Regions.CATA_ROOTS): lambda state: (
                self.has(state, Items.BOW)
                and self.blue_doors(state, Items.DOOR_BLUE_CATA_ROOTS)
                and (self.has(state, Items.CLAW) or self.has(state, Items.ZEEK, Items.BELL))
            ),
            (Regions.CATA_MID, Regions.DEV_ROOM): lambda state: (
                self.has(
                    state, Items.BOW, Items.BELL, Items.BLOCK, Items.CLAW, Items.STAR, Items.EYE_GREEN, Items.EYE_BLUE
                )
                and self.red_doors(state, Items.DOOR_RED_DEV_ROOM)
            ),
            (Regions.CATA_LOWER, Regions.TR): lambda state: (
                self.has(state, Items.VOID, Items.CLAW, Items.BELL, Items.BANISH)
                and self.white_doors(state, Items.DOOR_WHITE_CATA_PRISON)
            ),
            (Regions.TR, Regions.TR_PROPER): lambda state: (
                self.blue_doors(state, Items.DOOR_BLUE_TR) and self.red_doors(state, Items.DOOR_RED_TR)
            ),
        }

        self.item_rules = {
            Locations.GT_GORGONHEART: lambda _: True,
            Locations.GT_ANCIENTS_RING: lambda state: self.has(state, Items.EYE_RED),
            Locations.GT_SWORD: lambda state: self.blue_doors(state, Items.DOOR_BLUE_GT_SWORD),
            Locations.GT_MAP: lambda _: True,
            Locations.GT_ASCENDANT_KEY: lambda state: self.blue_doors(state, Items.DOOR_BLUE_GT_ASCENDANT),
            Locations.GT_BANISH: lambda state: self.blue_doors(state, Items.DOOR_BLUE_GT_ASCENDANT),
            Locations.GT_VOID: lambda state: self.has(state, Items.EYE_RED),
            Locations.GT_EYE_RED: lambda _: True,
            Locations.MECH_BOOTS: lambda state: self.blue_doors(state, Items.DOOR_BLUE_MECH_BOOTS),
            Locations.MECH_CLOAK: lambda state: (
                self.has(state, Items.EYE_BLUE)
                and self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA)
                and (self.has(state, Items.CLAW) or self.white_doors(state, Items.DOOR_WHITE_MECH_TOP))
            ),
            # Locations.MECH_CYCLOPS: lambda state: self.can_reach_zeek(state),
            Locations.MECH_EYE_BLUE: lambda state: (
                self.has(state, Items.CLAW)
                or self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA, Items.DOOR_WHITE_MECH_TOP)
            ),
            Locations.HOTP_BELL: lambda _: True,
            Locations.HOTP_AMULET: lambda state: self.has(state, Items.CLAW, Items.EYE_BLUE),
            Locations.HOTP_CLAW: lambda state: (
                self.has(state, Items.CLAW) or self.white_doors(state, Items.DOOR_WHITE_HOTP_CLAW)
            ),
            Locations.HOTP_GAUNTLET: lambda state: self.has(state, Items.CLAW, Items.BELL, Items.BANISH),
            Locations.HOTP_MAIDEN_RING: lambda state: (
                self.has(state, Items.BANISH, Items.BELL, Items.CLAW)
                and (
                    self.region(Regions.SP).can_reach(state)
                    or (
                        self.blue_doors(state, Items.DOOR_BLUE_HOTP_MAIDEN)
                        and self.has_any(state, Items.SWORD, Items.BLOCK)
                    )
                )
            ),
            Locations.ROA_ICARUS: lambda _: True,
            Locations.ROA_EYE_GREEN: lambda _: True,
            Locations.APEX_CHALICE: lambda state: (
                self.has(state, Items.ADORNED_KEY, Items.STAR) and self.blue_doors(state, Items.DOOR_BLUE_APEX)
            ),
            Locations.CATA_BOW: lambda state: (
                self.blue_doors(state, Items.DOOR_BLUE_CATA_BOW, Items.DOOR_BLUE_CATA_SAVE)
            ),
            Locations.TR_ADORNED_KEY: lambda state: (
                self.has(state, Items.EYE_GREEN, Items.STAR, Items.ZEEK)
                and self.has_any(state, Items.CLOAK, Items.ICARUS, Items.BOOTS, Items.BLOCK)
            ),
            # Locations.CD_CROWN: lambda _: True,
            Locations.CATH_BLOCK: lambda _: True,
            Locations.SP_STAR: lambda state: self.blue_doors(state, Items.DOOR_BLUE_SP),
        }

        self.attack_rules = {
            Locations.GT_ATTACK: lambda state: (
                self.has(state, Items.EYE_GREEN)
                # zeek + bell should be hard logic?
                and (self.has(state, Items.CLAW) or self.has(state, Items.ZEEK, Items.BELL))
            ),
            Locations.MECH_ATTACK_VOLANTIS: lambda state: (
                self.has(state, Items.CLAW)
                and (
                    self.has(state, Items.EYE_BLUE)
                    or self.has(state, Items.EYE_GREEN, Items.VOID)
                    or self.has(state, Items.STAR, Items.BELL)
                )
            ),
            Locations.MECH_ATTACK_STAR: lambda state: self.has(state, Items.STAR),
            Locations.ROA_ATTACK: lambda state: self.has(state, Items.STAR),
            Locations.CATA_ATTACK_RED: lambda state: self.has(state, Items.EYE_RED),
            Locations.CATA_ATTACK_BLUE: lambda state: self.has(state, Items.EYE_RED, Items.EYE_BLUE),
            Locations.CATA_ATTACK_GREEN: lambda state: (
                self.has(state, Items.EYE_RED, Items.EYE_BLUE) and self.has_any(state, Items.EYE_GREEN, Items.STAR)
            ),
            Locations.CATA_ATTACK_ROOT: lambda _: True,
            Locations.CATA_ATTACK_POISON: lambda _: True,
            Locations.CD_ATTACK: lambda _: True,
            Locations.CATH_ATTACK: lambda _: True,
            Locations.SP_ATTACK: lambda _: True,
        }

        self.health_rules = {
            Locations.GT_HP_1_RING: lambda state: (
                self.has(state, Items.STAR) or self.blue_doors(state, Items.DOOR_BLUE_GT_RING)
            ),
            Locations.GT_HP_5_KEY: lambda state: (
                self.has(state, Items.CLAW) and self.blue_doors(state, Items.DOOR_BLUE_GT_ASCENDANT)
            ),
            Locations.MECH_HP_1_SWITCH: lambda _: True,
            Locations.MECH_HP_1_STAR: lambda state: (
                self.has(state, Items.STAR)
                and (
                    self.has(state, Items.CLAW)
                    or self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA, Items.DOOR_WHITE_MECH_TOP)
                )
            ),
            Locations.MECH_HP_3_CLAW: lambda state: (
                self.has(state, Items.CLAW)
                and self.blue_doors(state, Items.DOOR_BLUE_MECH_BOOTS, Items.DOOR_BLUE_MECH_VOID)
            ),
            Locations.HOTP_HP_1_CLAW: lambda _: True,
            Locations.HOTP_HP_2_LADDER: lambda _: True,
            Locations.HOTP_HP_2_GAUNTLET: lambda state: self.has(state, Items.CLAW, Items.ZEEK, Items.BELL),
            Locations.HOTP_HP_5_OLD_MAN: lambda state: (
                self.has(state, Items.EYE_GREEN, Items.CLAW)
                and (self.has(state, Items.BELL, Items.BANISH) or self.has(state, Items.CHALICE))
            ),
            Locations.HOTP_HP_5_MAZE: lambda state: (
                self.entrance(Regions.HOTP_UPPER, Regions.HOTP_START).can_reach(state)
                or self.entrance(Regions.MECH_UPPER, Regions.HOTP_START).can_reach(state)
                or self.has(state, Items.BELL)
                # bram with star and range/axe could make this without bell
            ),
            Locations.HOTP_HP_5_START: lambda state: (
                self.has(state, Items.CLAW)
                and self.blue_doors(state, Items.DOOR_BLUE_HOTP_START)
                and (
                    self.entrance(Regions.HOTP_UPPER, Regions.HOTP_START).can_reach(state)
                    or self.entrance(Regions.MECH_UPPER, Regions.HOTP_START).can_reach(state)
                    or self.has(state, Items.BELL)
                )
            ),
            Locations.ROA_HP_1_LEFT: lambda _: True,
            Locations.ROA_HP_2_RIGHT: lambda state: (
                self.has_any(state, Items.GAUNTLET, Items.CHALICE)
                and (self.has(state, Items.STAR) or self.blue_doors(state, Items.DOOR_BLUE_ROA_FLAMES))
            ),
            Locations.ROA_HP_5_SOLARIA: lambda _: True,
            Locations.DARK_HP_4: lambda _: True,
            Locations.APEX_HP_1_CHALICE: lambda state: self.blue_doors(state, Items.DOOR_BLUE_APEX),
            Locations.APEX_HP_5_HEART: lambda _: True,
            Locations.CATA_HP_1_START: lambda state: self.has_any(state, Items.BOW, Items.CHALICE),
            Locations.CATA_HP_1_CYCLOPS: lambda state: self.has(state, Items.SWORD),
            Locations.CATA_HP_1_ABOVE_POISON: lambda state: (
                self.has(state, Items.BELL) or self.has(state, Items.ICARUS, Items.CLAW)
            ),
            Locations.CATA_HP_2_BEFORE_POISON: lambda _: True,
            Locations.CATA_HP_2_AFTER_POISON: lambda _: True,
            Locations.CATA_HP_2_GEMINI_BOTTOM: lambda state: self.has(state, Items.CLAW),
            Locations.CATA_HP_2_GEMINI_TOP: lambda state: self.has(state, Items.CLAW),
            Locations.CATA_HP_2_ABOVE_GEMINI: lambda state: (
                (self.has(state, Items.CLAW) or self.has(state, Items.BLOCK, Items.BELL))
                and (self.has(state, Items.GAUNTLET, Items.BELL) or self.has(state, Items.CHALICE))
            ),
            Locations.CATA_HP_5_CHAIN: lambda state: (
                self.has(state, Items.EYE_RED, Items.EYE_BLUE, Items.STAR, Items.CLAW, Items.BELL)
            ),
            Locations.TR_HP_1_BOTTOM: lambda _: True,
            Locations.TR_HP_2_TOP: lambda _: True,
            Locations.CD_HP_1: lambda _: True,
            Locations.CATH_HP_1_TOP_LEFT: lambda _: True,
            Locations.CATH_HP_1_TOP_RIGHT: lambda _: True,
            Locations.CATH_HP_2_CLAW: lambda _: True,
            Locations.CATH_HP_5_BELL: lambda _: True,
            Locations.SP_HP_1: lambda _: True,
        }

        self.white_key_rules = {
            Locations.GT_WHITE_KEY_START: lambda _: True,
            Locations.GT_WHITE_KEY_RIGHT: lambda _: True,
            Locations.GT_WHITE_KEY_BOSS: lambda _: True,
            Locations.MECH_WHITE_KEY_LINUS: lambda _: True,
            Locations.MECH_WHITE_KEY_BK: lambda state: (
                self.white_doors(state, Items.DOOR_WHITE_MECH_2ND)
                or self.blue_doors(state, Items.DOOR_BLUE_MECH_SHORTCUT)
            ),
            Locations.MECH_WHITE_KEY_ARENA: lambda _: True,
            Locations.MECH_WHITE_KEY_TOP: lambda state: self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA),
            Locations.HOTP_WHITE_KEY_LEFT: lambda _: True,
            Locations.HOTP_WHITE_KEY_GHOST: lambda _: True,
            Locations.HOTP_WHITE_KEY_OLD_MAN: lambda _: True,
            Locations.HOTP_WHITE_KEY_BOSS: lambda _: True,
            Locations.ROA_WHITE_KEY_SAVE: lambda _: True,
            Locations.ROA_WHITE_KEY_REAPERS: lambda state: self.white_doors(state, Items.DOOR_WHITE_ROA_WORMS),
            Locations.ROA_WHITE_KEY_TORCHES: lambda _: True,
            Locations.ROA_WHITE_KEY_PORTAL: lambda _: True,
            Locations.DARK_WHITE_KEY: lambda _: True,
            Locations.CATA_WHITE_KEY_HEAD: lambda _: True,
            Locations.CATA_WHITE_KEY_DEV_ROOM: lambda state: self.has(state, Items.BOW, Items.ZEEK, Items.BELL),
            Locations.CATA_WHITE_KEY_PRISON: lambda _: True,
        }

        self.blue_key_rules = {
            Locations.GT_BLUE_KEY_BONESNAKE: lambda _: True,
            Locations.GT_BLUE_KEY_BUTT: lambda _: True,
            Locations.GT_BLUE_KEY_WALL: lambda _: True,
            Locations.GT_BLUE_KEY_POT: lambda _: True,
            Locations.MECH_BLUE_KEY_VOID: lambda state: self.has(state, Items.EYE_RED),
            Locations.MECH_BLUE_KEY_SNAKE: lambda state: (
                self.blue_doors(state, Items.DOOR_BLUE_MECH_BOOTS, Items.DOOR_BLUE_MECH_VOID)
            ),
            Locations.MECH_BLUE_KEY_LINUS: lambda _: True,
            Locations.MECH_BLUE_KEY_SACRIFICE: lambda _: True,
            Locations.MECH_BLUE_KEY_RED: lambda _: True,
            Locations.MECH_BLUE_KEY_ARIAS: lambda _: True,
            Locations.MECH_BLUE_KEY_BLOCKS: lambda _: True,
            Locations.MECH_BLUE_KEY_TOP: lambda _: True,
            Locations.MECH_BLUE_KEY_OLD_MAN: lambda _: True,
            Locations.MECH_BLUE_KEY_SAVE: lambda state: self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA),
            Locations.MECH_BLUE_KEY_POT: lambda state: self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA),
            Locations.HOTP_BLUE_KEY_STATUE: lambda state: (
                self.has(state, Items.CLAW)
                and (
                    self.white_doors(state, Items.DOOR_WHITE_MECH_2ND)
                    or self.blue_doors(state, Items.DOOR_BLUE_MECH_SHORTCUT)
                )
            ),
            Locations.HOTP_BLUE_KEY_GOLD: lambda _: True,
            Locations.HOTP_BLUE_KEY_AMULET: lambda _: True,
            Locations.HOTP_BLUE_KEY_LADDER: lambda _: True,
            Locations.HOTP_BLUE_KEY_TELEPORTS: lambda _: True,
            Locations.HOTP_BLUE_KEY_MAZE: lambda _: True,
            Locations.ROA_BLUE_KEY_FACE: lambda state: (
                self.has(state, Items.BOW) and self.white_doors(state, Items.DOOR_WHITE_ROA_WORMS)
            ),
            Locations.ROA_BLUE_KEY_FLAMES: lambda state: (
                self.has_any(state, Items.GAUNTLET, Items.BLOCK) and self.white_doors(state, Items.DOOR_WHITE_ROA_WORMS)
            ),
            Locations.ROA_BLUE_KEY_BABY: lambda _: True,
            Locations.ROA_BLUE_KEY_TOP: lambda _: True,
            Locations.ROA_BLUE_KEY_POT: lambda state: self.white_doors(state, Items.DOOR_WHITE_ROA_WORMS),
            Locations.APEX_BLUE_KEY: lambda _: True,
            Locations.CATA_BLUE_KEY_SLIMES: lambda _: True,
            Locations.CATA_BLUE_KEY_EYEBALLS: lambda _: True,
            Locations.SP_BLUE_KEY_BUBBLES: lambda _: True,
            Locations.SP_BLUE_KEY_STAR: lambda state: (
                (self.has(state, Items.STAR) and self.blue_doors(state, Items.DOOR_BLUE_SP))
                or self.has(state, Items.BLOCK)
            ),
            Locations.SP_BLUE_KEY_PAINTING: lambda _: True,
            Locations.SP_BLUE_KEY_ARIAS: lambda _: True,
        }

        self.red_key_rules = {
            Locations.GT_RED_KEY: lambda state: self.has(state, Items.ZEEK),
            Locations.MECH_RED_KEY: lambda state: self.blue_doors(state, Items.DOOR_BLUE_MECH_RED),
            Locations.HOTP_RED_KEY: lambda state: self.has(state, Items.EYE_GREEN, Items.CLOAK),
            Locations.ROA_RED_KEY: lambda state: self.has(state, Items.CLOAK, Items.BOW),
            Locations.TR_RED_KEY: lambda _: True,
        }

        self.shop_rules = {
            Locations.SHOP_GIFT: lambda state: self.moderate_shop(state),
            Locations.SHOP_KNOWLEDGE: lambda state: self.cheap_shop(state),
            Locations.SHOP_MERCY: lambda state: self.expensive_shop(state),
            Locations.SHOP_ORB_SEEKER: lambda state: self.cheap_shop(state),
            Locations.SHOP_MAP_REVEAL: lambda state: (
                self.region(Regions.TR).can_reach(state) and self.region(Regions.ROA_UPPER).can_reach(state)
            ),
            Locations.SHOP_CARTOGRAPHER: lambda state: self.cheap_shop(state),
            Locations.SHOP_DEATH_ORB: lambda state: self.moderate_shop(state),
            Locations.SHOP_DEATH_POINT: lambda state: self.moderate_shop(state),
            Locations.SHOP_TITANS_EGO: lambda state: self.moderate_shop(state),
            Locations.SHOP_ALGUS_ARCANIST: lambda state: self.moderate_shop(state) and self.has(state, Items.ALGUS),
            Locations.SHOP_ALGUS_SHOCK: lambda state: self.moderate_shop(state) and self.has(state, Items.ALGUS),
            Locations.SHOP_ALGUS_METEOR: lambda state: self.expensive_shop(state) and self.has(state, Items.ALGUS),
            Locations.SHOP_ARIAS_GORGONSLAYER: lambda state: self.moderate_shop(state) and self.has(state, Items.ARIAS),
            Locations.SHOP_ARIAS_LAST_STAND: lambda state: self.expensive_shop(state) and self.has(state, Items.ARIAS),
            Locations.SHOP_ARIAS_LIONHEART: lambda state: self.moderate_shop(state) and self.has(state, Items.ARIAS),
            Locations.SHOP_KYULI_ASSASSIN: lambda state: self.cheap_shop(state) and self.has(state, Items.KYULI),
            Locations.SHOP_KYULI_BULLSEYE: lambda state: self.moderate_shop(state) and self.has(state, Items.KYULI),
            Locations.SHOP_KYULI_RAY: lambda state: self.expensive_shop(state) and self.has(state, Items.KYULI),
            Locations.SHOP_ZEEK_JUNKYARD: lambda state: self.moderate_shop(state) and self.has(state, Items.ZEEK),
            Locations.SHOP_ZEEK_ORBS: lambda state: self.moderate_shop(state) and self.has(state, Items.ZEEK),
            Locations.SHOP_ZEEK_LOOT: lambda state: self.cheap_shop(state) and self.has(state, Items.ZEEK),
            Locations.SHOP_BRAM_AXE: lambda state: self.expensive_shop(state) and self.has(state, Items.BRAM),
            Locations.SHOP_BRAM_HUNTER: lambda state: self.moderate_shop(state) and self.has(state, Items.BRAM),
            Locations.SHOP_BRAM_WHIPLASH: lambda state: self.moderate_shop(state) and self.has(state, Items.BRAM),
        }

        self.familiar_rules = {
            Locations.GT_OLD_MAN: lambda state: self.has_any(state, Items.BELL, Items.SWORD),
            Locations.MECH_OLD_MAN: lambda _: True,
            Locations.HOTP_OLD_MAN: lambda state: self.has(state, Items.CLOAK, Items.BOW, Items.BELL),
            Locations.CATA_GIL: lambda _: True,
        }

    def region(self, name: Regions):
        return self.world.multiworld.get_region(name.value, self.player)

    def entrance(self, from_: Regions, to_: Regions):
        return self.world.multiworld.get_entrance(f"{from_.value} -> {to_.value}", self.player)

    def location(self, name: Locations):
        return self.world.multiworld.get_location(name.value, self.player)

    def can_reach_zeek(self, state: CollectionState) -> bool:
        if not self.region(Regions.MECH_UPPER).can_reach(state):
            return False
        if self.options.randomize_red_keys:
            return self.red_doors(state, Items.DOOR_RED_ZEEK)
        # can reach one of the red keys
        return (
            self.blue_doors(state, Items.DOOR_BLUE_MECH_VOID)
            or (self.region(Regions.HOTP_BELL).can_reach(state) and self.has(state, Items.EYE_GREEN, Items.CLOAK))
            or (self.region(Regions.ROA_UPPER).can_reach(state) and self.has(state, Items.BOW, Items.CLOAK))
        )

    def can_get_zeek(self, state: CollectionState) -> bool:
        return self.can_reach_zeek(state) and self.region(Regions.CD).can_reach(state)

    def can_get_bram(self, state: CollectionState) -> bool:
        return self.region(Regions.TR).can_reach(state) and self.has(state, Items.EYE_BLUE)

    def _has(self, state: CollectionState, item: Items, count: int = 1) -> bool:
        if item in CHARACTERS:
            if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
                if item in {Items.ALGUS, Items.ARIAS, Items.KYULI}:
                    return True
                elif item == Items.ZEEK:
                    return self.can_get_zeek(state)
                elif item == Items.BRAM:
                    return self.can_get_bram(state)
            else:
                return state.has(item.value, self.player)

        if item == Items.CLOAK and not self._has(state, Items.ALGUS):
            return False
        if item in {Items.SWORD, Items.BOOTS} and not self._has(state, Items.ARIAS):
            return False
        if item in {Items.CLAW, Items.BOW} and not self._has(state, Items.KYULI):
            return False
        if item == Items.BLOCK and not self._has(state, Items.ZEEK):
            return False
        if item == Items.STAR and not self._has(state, Items.BRAM):
            return False
        if item == Items.BANISH and not self.has_any(state, Items.ALGUS, Items.ZEEK):
            return False
        if item == Items.GAUNTLET and not self.has_any(state, Items.ARIAS, Items.BRAM):
            return False

        if item == Items.CYCLOPS:
            # not yet randomized
            return self.can_reach_zeek(state)

        if item in {Items.ALGUS_ARCANIST, Items.ALGUS_METEOR, Items.ALGUS_SHOCK} and not self._has(state, Items.ALGUS):
            return False
        if item in {Items.ARIAS_GORGONSLAYER, Items.ARIAS_LAST_STAND, Items.ARIAS_LIONHEART} and not self._has(
            state, Items.ARIAS
        ):
            return False
        if item in {Items.KYULI_ASSASSIN, Items.KYULI_BULLSEYE, Items.KYULI_RAY} and not self._has(state, Items.KYULI):
            return False
        if item in {Items.ZEEK_JUNKYARD, Items.ZEEK_ORBS, Items.ZEEK_LOOT} and not self._has(state, Items.ZEEK):
            return False
        if item in {Items.BRAM_AXE, Items.BRAM_HUNTER, Items.BRAM_WHIPLASH} and not self._has(state, Items.BRAM):
            return False

        return state.has(item.value, self.player, count=count)

    def has(self, state: CollectionState, *items: Union[Characters, KeyItems, ShopUpgrades], count: int = 1) -> bool:
        # cover extra logic instead of calling state.has_all
        for item in items:
            if not self._has(state, item, count=count):
                return False
        return True

    def has_any(self, state: CollectionState, *items: Union[Characters, KeyItems]) -> bool:
        # cover extra logic instead of calling state.has_any
        for item in items:
            if self._has(state, item):
                return True
        return False

    def white_doors(self, state: CollectionState, *doors: WhiteDoors, disabled_case=True) -> bool:
        if not self.options.randomize_white_keys:
            return disabled_case
        for door in doors:
            if not self._has(state, door):
                return False
        return True

    def blue_doors(self, state: CollectionState, *doors: BlueDoors, disabled_case=True) -> bool:
        if not self.options.randomize_blue_keys:
            return disabled_case
        for door in doors:
            if not self._has(state, door):
                return False
        return True

    def red_doors(self, state: CollectionState, *doors: RedDoors, disabled_case=True) -> bool:
        if not self.options.randomize_red_keys:
            return disabled_case
        for door in doors:
            if not self._has(state, door):
                return False
        return True

    def switches(self, state: CollectionState, *switches: Items, disabled_case=True) -> bool:
        return disabled_case

    def elevator(self, state: CollectionState, destination: Items) -> bool:
        return False

    def cheap_shop(self, state: CollectionState) -> bool:
        return self.region(Regions.GT_LEFT).can_reach(state)

    def moderate_shop(self, state: CollectionState) -> bool:
        return self.region(Regions.MECH_LOWER).can_reach(state)

    def expensive_shop(self, state: CollectionState) -> bool:
        return self.region(Regions.ROA_LOWER).can_reach(state)

    def can(self, state: CollectionState, logic: Logic) -> bool:
        if logic == Logic.ARIAS_JUMP:
            return self.hard and self.has(state, Items.ARIAS)
        if logic == Logic.EXTRA_HEIGHT:
            return self.has(state, Items.KYULI) or self.has(state, Items.BLOCK) or self.can(state, Logic.ARIAS_JUMP)
        if logic == Logic.COMBO_HEIGHT:
            return self.hard and self.can(state, Logic.ARIAS_JUMP) and self.has(state, Items.BELL, Items.BLOCK)
        if logic == Logic.BLOCK_IN_WALL:
            return self.hard and self.has(state, Items.ZEEK)
        if logic == Logic.MAGIC_CRYSTAL:
            if self.has(state, Items.ALGUS):
                return True
            if self.hard:
                return (
                    self.has(state, Items.ZEEK, Items.BANISH)
                    or self.has(state, Items.KYULI_RAY)
                    or self.has(state, Items.BRAM_WHIPLASH)
                )
        return False

    @property
    def easy(self):
        return self.options.difficulty >= Difficulty.option_easy

    @property
    def hard(self):
        return self.options.difficulty >= Difficulty.option_hard

    def set_region_rules(self) -> None:
        for (from_, to_), rule in self.entrance_rules.items():
            set_rule(self.entrance(from_, to_), rule)

    def set_location_rules(self) -> None:
        for location, rule in self.item_rules.items():
            set_rule(self.location(location), rule)

        if self.options.randomize_attack_pickups:
            for location, rule in self.attack_rules.items():
                set_rule(self.location(location), rule)

        if self.options.randomize_health_pickups:
            for location, rule in self.health_rules.items():
                set_rule(self.location(location), rule)

        if self.options.randomize_white_keys:
            for location, rule in self.white_key_rules.items():
                set_rule(self.location(location), rule)

        if self.options.randomize_blue_keys:
            for location, rule in self.blue_key_rules.items():
                set_rule(self.location(location), rule)

        if self.options.randomize_red_keys:
            for location, rule in self.red_key_rules.items():
                set_rule(self.location(location), rule)

        if self.options.randomize_shop:
            for location, rule in self.shop_rules.items():
                set_rule(self.location(location), rule)

        # if self.options.randomize_familiars:
        #     for location, rule in self.familiar_rules.items():
        #         set_rule(self.location(location), rule)
