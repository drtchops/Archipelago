from enum import Enum, auto
from functools import cached_property, lru_cache, partial
from typing import TYPE_CHECKING, Dict, Protocol, Tuple, TypeVar, Union

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import (
    AllItems,
    BlueDoor,
    Character,
    Crystal,
    Elevator,
    Eye,
    Face,
    KeyItem,
    RedDoor,
    ShopUpgrade,
    Switch,
    WhiteDoor,
)
from .Locations import LocationGroups, location_table
from .Locations import Locations as L
from .Options import AstalonOptions, Difficulty, RandomizeCharacters
from .Regions import Regions as R

if TYPE_CHECKING:
    from . import AstalonWorld


class Events(str, Enum):
    VICTORY = "Victory"
    MET_ZEEK = "Met Zeek"
    ZEEK_JOINED = "Zeek Joined"
    BRAM_JOINED = "Bram Joined"


class Logic(Enum):
    ARIAS_JUMP = auto()
    EXTRA_HEIGHT = auto()
    COMBO_HEIGHT = auto()
    BLOCK_IN_WALL = auto()
    CRYSTAL = auto()
    BIG_MAGIC = auto()


T = TypeVar("T", bound=Enum, contravariant=True)  # noqa: PLC0105


class AstalonRule(Protocol):
    def __call__(self, rules: "AstalonRules", state: CollectionState) -> bool: ...


class Has(Protocol):
    def __call__(self, state: CollectionState, item: Union[AllItems, Events], count: int = 1) -> bool: ...


class Can(Protocol):
    def __call__(self, state: CollectionState, logic: Logic, gold_block: bool = False) -> bool: ...


class Togglable(Protocol[T]):
    def __call__(self, state: CollectionState, *items: T, disabled_case: Union[bool, AstalonRule]) -> bool: ...


ENTRANCE_RULES: Dict[Tuple[R, R], AstalonRule] = {
    (R.SHOP, R.SHOP_ALGUS): lambda rules, state: rules.has(state, Character.ALGUS),
    (R.SHOP, R.SHOP_ARIAS): lambda rules, state: rules.has(state, Character.ARIAS),
    (R.SHOP, R.SHOP_KYULI): lambda rules, state: rules.has(state, Character.KYULI),
    (R.SHOP, R.SHOP_ZEEK): lambda rules, state: rules.has(state, Character.ZEEK),
    (R.SHOP, R.SHOP_BRAM): lambda rules, state: rules.has(state, Character.BRAM),
    (R.ENTRANCE, R.BESTIARY): lambda rules, state: (rules.blue_doors(state, BlueDoor.GT_HUNTER, disabled_case=True)),
    (R.ENTRANCE, R.GT_BABY_GORGON): lambda rules, state: (
        rules.has(state, Eye.GREEN)
        and (
            rules.has(state, KeyItem.CLAW)
            or (
                rules.hard
                and rules.can(state, Logic.BLOCK_IN_WALL, gold_block=True)
                and (rules.has(state, Character.KYULI, KeyItem.BELL) or rules.has(state, KeyItem.BLOCK))
            )
        )
    ),
    (R.ENTRANCE, R.GT_BOTTOM): lambda rules, state: (
        rules.switches(
            state,
            Switch.GT_2ND_ROOM,
            disabled_case=lambda rules, state: rules.white_doors(state, WhiteDoor.GT_START, disabled_case=True),
        )
    ),
    (R.ENTRANCE, R.GT_VOID): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.ENTRANCE, R.GT_GORGONHEART): lambda rules, state: (
        rules.switches(state, Switch.GT_GH_SHORTCUT, disabled_case=False)
        or rules.has_any(state, KeyItem.ICARUS, KeyItem.BOOTS)
    ),
    (R.ENTRANCE, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.ENTRANCE, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.ENTRANCE, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.ENTRANCE, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.ENTRANCE, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.ENTRANCE, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.ENTRANCE, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.ENTRANCE, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.ENTRANCE, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.ENTRANCE, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.GT_BOTTOM, R.GT_VOID): lambda rules, state: rules.has(state, Eye.RED),
    (R.GT_BOTTOM, R.GT_GORGONHEART): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.GT_MAP, disabled_case=True)
    ),
    (R.GT_BOTTOM, R.GT_UPPER_PATH): lambda rules, state: (
        rules.switches(state, Crystal.GT_ROTA, disabled_case=False)
        or rules.can(state, Logic.ARIAS_JUMP)
        or (rules.has(state, KeyItem.STAR) and rules.blue_doors(state, BlueDoor.GT_RING, disabled_case=True))
    ),
    (R.GT_BOTTOM, R.CAVES_START): lambda rules, state: (
        rules.has(state, Character.KYULI) or rules.can(state, Logic.BLOCK_IN_WALL, gold_block=True)
    ),
    (R.GT_VOID, R.GT_BOTTOM): lambda rules, state: rules.has(state, Eye.RED),
    (R.GT_VOID, R.MECH_SNAKE): lambda rules, state: (rules.switches(state, Switch.MECH_SNAKE_2, disabled_case=False)),
    (R.GT_GORGONHEART, R.GT_BOTTOM): lambda rules, state: True,
    (R.GT_GORGONHEART, R.GT_ORBS_DOOR): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.GT_ORBS, disabled_case=True)
    ),
    (R.GT_GORGONHEART, R.GT_LEFT): lambda rules, state: (
        rules.switches(state, Switch.GT_CROSSES, disabled_case=False)
        or rules.switches(state, Switch.GT_1ST_CYCLOPS, disabled_case=True)
    ),
    (R.GT_LEFT, R.GT_GORGONHEART): lambda rules, state: (
        rules.switches(state, Switch.GT_CROSSES, disabled_case=True)
        or rules.switches(state, Switch.GT_1ST_CYCLOPS, disabled_case=False)
    ),
    (R.GT_LEFT, R.GT_ORBS_HEIGHT): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.GT_LEFT, R.GT_ASCENDANT_KEY): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.GT_ASCENDANT, disabled_case=True)
    ),
    (R.GT_LEFT, R.GT_TOP_LEFT): lambda rules, state: (
        rules.switches(state, Switch.GT_ARIAS, disabled_case=False)
        or rules.has_any(state, Character.ARIAS, KeyItem.CLAW)
        or rules.has(state, KeyItem.BLOCK, Character.KYULI, KeyItem.BELL)
    ),
    (R.GT_LEFT, R.GT_TOP_RIGHT): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.GT_TOP_LEFT, R.GT_LEFT): lambda rules, state: True,
    (R.GT_TOP_LEFT, R.GT_BUTT): lambda rules, state: (
        rules.switches(
            state,
            Switch.GT_BUTT_ACCESS,
            disabled_case=lambda rules, state: rules.reachable(state, L.GT_SWITCH_BUTT_ACCESS),
        )
    ),
    (R.GT_TOP_RIGHT, R.GT_LEFT): lambda rules, state: True,
    (R.GT_TOP_RIGHT, R.GT_SPIKE_TUNNEL): lambda rules, state: (
        rules.switches(
            state,
            Switch.GT_SPIKE_TUNNEL,
            disabled_case=lambda rules, state: rules.reachable(state, L.GT_SWITCH_SPIKE_TUNNEL),
        )
    ),
    (R.GT_SPIKE_TUNNEL, R.GT_TOP_RIGHT): lambda rules, state: (
        rules.switches(state, Switch.GT_SPIKE_TUNNEL, disabled_case=False)
    ),
    (R.GT_SPIKE_TUNNEL, R.GT_BUTT): lambda rules, state: (
        rules.can(state, Logic.EXTRA_HEIGHT) and rules.has(state, KeyItem.STAR, KeyItem.BELL)
    ),
    (R.GT_BUTT, R.GT_TOP_LEFT): lambda rules, state: (
        rules.switches(state, Switch.GT_BUTT_ACCESS, disabled_case=False)
    ),
    (R.GT_BUTT, R.GT_SPIKE_TUNNEL): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.GT_BUTT, R.GT_BOSS): lambda rules, state: (rules.white_doors(state, WhiteDoor.GT_TAUROS, disabled_case=True)),
    (R.GT_BOSS, R.GT_BUTT): lambda rules, state: (rules.white_doors(state, WhiteDoor.GT_TAUROS, disabled_case=False)),
    (R.GT_BOSS, R.MECH_START): lambda rules, state: rules.has(state, Eye.RED),
    (R.GT_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.GT_BOSS, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.GT_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.GT_BOSS, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.GT_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.GT_BOSS, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.GT_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.GT_BOSS, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.GT_BOSS, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.GT_UPPER_ARIAS, R.GT_OLD_MAN_FORK): lambda rules, state: (
        rules.switches(
            state,
            Crystal.GT_LADDER,
            disabled_case=lambda rules, state: rules.reachable(state, L.GT_CRYSTAL_LADDER),
        )
    ),
    (R.GT_UPPER_ARIAS, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.has(state, Character.ARIAS)
        or rules.switches(
            state,
            Switch.GT_UPPER_ARIAS,
            disabled_case=lambda rules, state: rules.reachable(state, L.GT_SWITCH_UPPER_ARIAS),
        )
    ),
    (R.GT_OLD_MAN_FORK, R.GT_UPPER_ARIAS): lambda rules, state: (
        rules.switches(
            state,
            Crystal.GT_LADDER,
            disabled_case=lambda rules, state: rules.reachable(state, L.GT_CRYSTAL_LADDER),
        )
    ),
    (R.GT_OLD_MAN_FORK, R.GT_SWORD_FORK): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.GT_SWORD, disabled_case=True)
    ),
    (R.GT_OLD_MAN_FORK, R.GT_OLD_MAN): lambda rules, state: (
        # TODO: you don't need both switches, revisit when adding old man
        rules.has(state, KeyItem.CLAW)
        or rules.switches(
            state,
            Crystal.GT_OLD_MAN_1,
            Crystal.GT_OLD_MAN_2,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
    ),
    (R.GT_SWORD_FORK, R.GT_SWORD): lambda rules, state: (
        rules.switches(state, Switch.GT_SWORD_ACCESS, disabled_case=True)
    ),
    (R.GT_SWORD_FORK, R.GT_ARIAS_SWORD_SWITCH): lambda rules, state: (
        rules.has(state, KeyItem.SWORD) or rules.has(state, KeyItem.BOW, KeyItem.BELL)
    ),
    (R.GT_UPPER_PATH, R.GT_UPPER_PATH_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.GT_UPPER_PATH_ACCESS, disabled_case=False)
    ),
    (R.GT_UPPER_PATH, R.GT_BOTTOM): lambda rules, state: True,
    (R.GT_UPPER_PATH_CONNECTION, R.GT_UPPER_PATH): lambda rules, state: (
        rules.switches(state, Switch.GT_UPPER_PATH_ACCESS, disabled_case=True)
    ),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.MECH_START, R.GT_LADDER_SWITCH): lambda rules, state: rules.has(state, Eye.RED),
    (R.MECH_START, R.MECH_BK): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_SHORTCUT, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_START, R.MECH_WATCHER): lambda rules, state: (
        rules.switches(state, Switch.MECH_CANNON, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
        and rules.white_doors(state, WhiteDoor.MECH_2ND, disabled_case=True)
    ),
    (R.MECH_START, R.MECH_LINUS): lambda rules, state: (
        rules.switches(state, Crystal.MECH_LINUS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_START, R.MECH_LOWER_VOID): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_RED, disabled_case=True)
    ),
    (R.MECH_START, R.MECH_SACRIFICE): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.MECH_START, R.GT_BOSS): lambda rules, state: rules.has(state, Eye.RED),
    (R.MECH_LINUS, R.MECH_START): lambda rules, state: (
        rules.switches(state, Crystal.MECH_LINUS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_LINUS, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_LINUS, disabled_case=True)
    ),
    (R.MECH_SWORD_CONNECTION, R.MECH_BOOTS_CONNECTION): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_BOOTS, disabled_case=True)
        and (
            rules.switches(
                state, Crystal.MECH_LOWER, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
            )
            and (rules.has_any(state, KeyItem.CLAW, KeyItem.CLOAK) or rules.has(state, Character.KYULI, KeyItem.ICARUS))
        )
    ),
    (R.MECH_SWORD_CONNECTION, R.GT_UPPER_PATH_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.MECH_SWORD_CONNECTION, R.MECH_LOWER_ARIAS): lambda rules, state: rules.has(state, Character.ARIAS),
    (R.MECH_SWORD_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.MECH_SWORD_CONNECTION, R.MECH_LINUS): lambda rules, state: (
        rules.switches(state, Switch.MECH_LINUS, disabled_case=False)
    ),
    (R.MECH_SWORD_CONNECTION, R.GT_UPPER_ARIAS): lambda rules, state: (
        rules.has(state, Character.ARIAS) or rules.switches(state, Switch.GT_UPPER_ARIAS, disabled_case=False)
    ),
    (R.MECH_BOOTS_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_VOID, disabled_case=True)
    ),
    (R.MECH_BOOTS_CONNECTION, R.MECH_SWORD_CONNECTION): lambda rules, state: True,
    (R.MECH_BOOTS_CONNECTION, R.MECH_BOOTS_LOWER): lambda rules, state: (
        rules.switches(
            state,
            Switch.MECH_BOOTS,
            disabled_case=lambda rules, state: rules.has_any(state, Eye.RED, KeyItem.STAR),
        )
    ),
    (R.MECH_BOOTS_LOWER, R.MECH_BOOTS_UPPER): lambda rules, state: (
        rules.switches(state, Switch.MECH_BOOTS_LOWER, disabled_case=True) or rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.GT_UPPER_PATH_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_UPPER_GT, disabled_case=True)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_BOOTS_CONNECTION): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_VOID, disabled_case=True)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_SNAKE): lambda rules, state: (
        rules.switches(state, Switch.MECH_SNAKE_1, disabled_case=True)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_UPPER_GT, disabled_case=True)
    ),
    (R.MECH_SNAKE, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.switches(state, Switch.MECH_SNAKE_1, disabled_case=False)
    ),
    (R.MECH_SNAKE, R.GT_VOID): lambda rules, state: rules.switches(state, Switch.MECH_SNAKE_2, disabled_case=True),
    (R.MECH_LOWER_VOID, R.MECH_START): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_RED, disabled_case=True)
    ),
    (R.MECH_LOWER_VOID, R.MECH_UPPER_VOID): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.MECH_LOWER_VOID, R.HOTP_MECH_VOID_CONNECTION): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.MECH_WATCHER, R.MECH_START): lambda rules, state: (
        rules.switches(state, Switch.MECH_CANNON, disabled_case=False)
        and rules.white_doors(state, WhiteDoor.MECH_2ND, disabled_case=True)
    ),
    (R.MECH_WATCHER, R.MECH_ROOTS): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) or rules.switches(state, Switch.MECH_WATCHER, disabled_case=True)
    ),
    (R.MECH_ROOTS, R.MECH_WATCHER): lambda rules, state: True,
    (R.MECH_ROOTS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.has(
        state, KeyItem.CLAW, KeyItem.BLOCK, KeyItem.BELL
    ),
    (R.MECH_ROOTS, R.MECH_BK): lambda rules, state: True,
    (R.MECH_ROOTS, R.MECH_MUSIC): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_MUSIC, disabled_case=True)
    ),
    (R.MECH_BK, R.MECH_START): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.MECH_SHORTCUT, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_BK, R.MECH_AFTER_BK): lambda rules, state: (
        rules.switches(state, Crystal.MECH_BK, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_BK, R.MECH_ROOTS): lambda rules, state: (
        rules.switches(state, Crystal.MECH_CAMPFIRE, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_AFTER_BK, R.MECH_CHAINS): lambda rules, state: (
        rules.has(state, KeyItem.CLAW)
        or rules.white_doors(state, WhiteDoor.MECH_BK, disabled_case=True)
        or rules.switches(state, Switch.MECH_CHAINS, disabled_case=False)
    ),
    (R.MECH_AFTER_BK, R.MECH_BK): lambda rules, state: (
        rules.switches(state, Crystal.MECH_BK, disabled_case=(rules.hard and rules.has(state, ShopUpgrade.KYULI_RAY)))
    ),
    (R.MECH_AFTER_BK, R.HOTP_EPIMETHEUS): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.MECH_CHAINS, R.MECH_ARIAS_EYEBALL): lambda rules, state: rules.has(state, Character.ARIAS),
    (R.MECH_CHAINS, R.MECH_SPLIT_PATH): lambda rules, state: (
        rules.switches(state, Switch.MECH_SPLIT_PATH, disabled_case=True)
    ),
    (R.MECH_CHAINS, R.MECH_BOSS_SWITCHES): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_BOSS_1, disabled_case=False)
    ),
    (R.MECH_CHAINS, R.MECH_BOSS_CONNECTION): lambda rules, state: (
        rules.has(state, KeyItem.CLAW)
        or rules.switches(
            state,
            Crystal.MECH_TO_BOSS_3,
            disabled_case=(
                rules.hard and (rules.can(state, Logic.BIG_MAGIC) or rules.has(state, ShopUpgrade.KYULI_RAY))
            ),
        )
    ),
    (R.MECH_CHAINS, R.MECH_AFTER_BK): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) or rules.switches(state, Switch.MECH_CHAINS, disabled_case=True)
    ),
    (R.MECH_ARIAS_EYEBALL, R.MECH_ZEEK_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_ARIAS, disabled_case=True) or rules.has(state, KeyItem.STAR, KeyItem.BELL)
    ),
    (R.MECH_ARIAS_EYEBALL, R.MECH_CHAINS): lambda rules, state: (
        rules.has(state, Character.ARIAS, KeyItem.BELL)
        and rules.has_any(state, Character.ALGUS, ShopUpgrade.BRAM_WHIPLASH)
        and (rules.switches(state, Switch.MECH_ARIAS, disabled_case=False) or rules.has(state, KeyItem.STAR))
    ),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ARIAS_EYEBALL): lambda rules, state: (
        rules.switches(state, Switch.MECH_ARIAS, disabled_case=False) or rules.has(state, KeyItem.STAR)
    ),
    (R.MECH_ZEEK_CONNECTION, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.MECH_ZEEK_CONNECTION, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ROOTS): lambda rules, state: True,
    (R.MECH_ZEEK_CONNECTION, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.MECH_ZEEK_CONNECTION, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.MECH_ZEEK_CONNECTION, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.MECH_ZEEK_CONNECTION, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ZEEK): lambda rules, state: (
        rules.red_doors(state, RedDoor.ZEEK, disabled_case=lambda rules, state: rules.reachable(state, L.MECH_RED_KEY))
    ),
    (R.MECH_ZEEK_CONNECTION, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.MECH_ZEEK_CONNECTION, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.MECH_SPLIT_PATH, R.MECH_RIGHT): lambda rules, state: True,  # until skulls are included
    (R.MECH_SPLIT_PATH, R.MECH_CHAINS): lambda rules, state: (
        rules.switches(state, Switch.MECH_SPLIT_PATH, disabled_case=False)
    ),
    (R.MECH_RIGHT, R.MECH_OLD_MAN): lambda rules, state: (
        rules.switches(state, Crystal.MECH_OLD_MAN, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
        or rules.has(state, Character.KYULI, KeyItem.BLOCK, KeyItem.BELL)
    ),
    (R.MECH_RIGHT, R.MECH_SPLIT_PATH): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.MECH_RIGHT, R.MECH_POTS): lambda rules, state: (
        rules.switches(state, Switch.MECH_POTS, disabled_case=True)
        and (
            rules.white_doors(state, WhiteDoor.MECH_ARENA, disabled_case=True)
            or rules.switches(state, Switch.MECH_EYEBALL, disabled_case=False)
        )
    ),
    (R.MECH_RIGHT, R.MECH_UPPER_VOID): lambda rules, state: (
        rules.switches(state, Switch.MECH_UPPER_VOID, disabled_case=False)
        or (rules.has(state, KeyItem.CLAW) and rules.switches(state, Switch.MECH_UPPER_VOID_DROP, disabled_case=True))
    ),
    (R.MECH_UPPER_VOID, R.MECH_RIGHT): lambda rules, state: (
        rules.switches(state, Switch.MECH_UPPER_VOID, disabled_case=True)
    ),
    (R.MECH_UPPER_VOID, R.MECH_LOWER_VOID): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.MECH_POTS, R.MECH_RIGHT): lambda rules, state: (
        rules.switches(state, Switch.MECH_POTS, disabled_case=False)
        and (
            rules.white_doors(state, WhiteDoor.MECH_ARENA, disabled_case=True)
            or rules.switches(state, Switch.MECH_EYEBALL, disabled_case=True)
        )
    ),
    (R.MECH_POTS, R.MECH_TOP): lambda rules, state: rules.switches(state, Switch.MECH_POTS, disabled_case=True),
    (R.MECH_TOP, R.MECH_POTS): lambda rules, state: rules.switches(state, Switch.MECH_POTS, disabled_case=False),
    (R.MECH_TOP, R.MECH_TP_CONNECTION): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) or rules.white_doors(state, WhiteDoor.MECH_TOP, disabled_case=True)
    ),
    (R.MECH_TOP, R.CD_START): lambda rules, state: (
        rules.has(state, KeyItem.CYCLOPS, Eye.BLUE)
        and rules.blue_doors(state, BlueDoor.MECH_CD, disabled_case=True)
        and (
            rules.switches(
                state, Crystal.MECH_TO_CD, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
            )
            or rules.has(state, Character.KYULI, KeyItem.BLOCK, KeyItem.BELL)
        )
    ),
    (R.MECH_TP_CONNECTION, R.HOTP_FALL_BOTTOM): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) or rules.switches(state, Switch.MECH_MAZE_BACKDOOR, disabled_case=False)
    ),
    (R.MECH_TP_CONNECTION, R.MECH_TOP): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) or rules.white_doors(state, WhiteDoor.MECH_TOP, disabled_case=True)
    ),
    (R.MECH_TP_CONNECTION, R.MECH_CHARACTER_SWAPS): lambda rules, state: (
        (
            rules.has(state, Character.ARIAS)
            and (rules.white_doors(state, WhiteDoor.MECH_TOP, disabled_case=True) or rules.has(state, KeyItem.BELL))
        )
        or rules.switches(state, Switch.MECH_ARIAS_CYCLOPS, disabled_case=False)
    ),
    (R.MECH_CHARACTER_SWAPS, R.MECH_CLOAK_CONNECTION): lambda rules, state: (
        rules.switches(
            state,
            Crystal.MECH_TRIPLE_1,
            Crystal.MECH_TRIPLE_2,
            Crystal.MECH_TRIPLE_3,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
        and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_CHARACTER_SWAPS, R.MECH_TP_CONNECTION): lambda rules, state: (
        rules.has(state, Character.ARIAS) or rules.switches(state, Switch.MECH_ARIAS_CYCLOPS, disabled_case=True)
    ),
    (R.MECH_CLOAK_CONNECTION, R.MECH_BOSS_SWITCHES): lambda rules, state: True,
    (R.MECH_CLOAK_CONNECTION, R.MECH_CHARACTER_SWAPS): lambda rules, state: (
        rules.switches(
            state,
            Crystal.MECH_TRIPLE_1,
            Crystal.MECH_TRIPLE_2,
            Crystal.MECH_TRIPLE_3,
            disabled_case=False,
        )
    ),
    (R.MECH_CLOAK_CONNECTION, R.MECH_CLOAK): lambda rules, state: (
        rules.has(state, Eye.BLUE)
        and rules.switches(
            state, Crystal.MECH_CLOAK, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_BOSS_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_BOSS_1, Switch.MECH_TO_BOSS_2, disabled_case=True)
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_CLOAK_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.MECH_BLOCK_STAIRS, disabled_case=False)
        or rules.switches(
            state, Crystal.MECH_SLIMES, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_CHAINS): lambda rules, state: (
        rules.switches(state, Switch.MECH_TO_BOSS_1, disabled_case=True)
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_BOSS): lambda rules, state: (
        rules.switches(state, Switch.MECH_BOSS_2, disabled_case=True)
        or (
            rules.has(state, KeyItem.BLOCK, KeyItem.BELL)
            and (rules.has(state, Character.KYULI) or rules.can(state, Logic.ARIAS_JUMP))
        )
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_BRAM_TUNNEL): lambda rules, state: (
        rules.switches(state, Switch.MECH_BOSS_1, disabled_case=True) and rules.has(state, KeyItem.STAR)
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_CHAINS): lambda rules, state: True,
    (R.MECH_BRAM_TUNNEL, R.MECH_BOSS_CONNECTION): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.MECH_BRAM_TUNNEL, R.HOTP_START_BOTTOM): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.MECH_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.MECH_BOSS, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.MECH_BOSS, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.MECH_BOSS, R.MECH_BOSS_CONNECTION): lambda rules, state: True,
    (R.MECH_BOSS, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.MECH_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.MECH_BOSS, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.MECH_BOSS, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.MECH_BOSS, R.HOTP_START): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.MECH_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.MECH_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.HOTP_START, R.MECH_BOSS): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.HOTP_START, R.HOTP_START_BOTTOM): lambda rules, state: (
        rules.has(state, KeyItem.STAR)
        or (rules.white_doors(state, WhiteDoor.HOTP_START, disabled_case=True) and rules.has(state, Eye.BLUE))
    ),
    (R.HOTP_START, R.HOTP_START_MID): lambda rules, state: (
        rules.switches(state, Switch.HOTP_1ST_ROOM, disabled_case=True)
    ),
    (R.HOTP_START_MID, R.HOTP_START_LEFT): lambda rules, state: (
        rules.switches(state, Switch.HOTP_LEFT_3, disabled_case=True)
        or (
            rules.has(state, KeyItem.STAR)
            and rules.switches(state, Switch.HOTP_LEFT_1, Switch.HOTP_LEFT_2, disabled_case=True)
        )
    ),
    (R.HOTP_START_MID, R.HOTP_START_BOTTOM): lambda rules, state: (
        rules.has(state, KeyItem.STAR) and rules.switches(state, Switch.HOTP_GHOSTS, disabled_case=True)
    ),
    (R.HOTP_START_MID, R.HOTP_LOWER_VOID): lambda rules, state: (
        rules.has_any(state, Character.ALGUS, ShopUpgrade.BRAM_WHIPLASH)
    ),
    (R.HOTP_START_MID, R.HOTP_START): lambda rules, state: True,
    (R.HOTP_LOWER_VOID, R.HOTP_START_MID): lambda rules, state: True,
    (R.HOTP_LOWER_VOID, R.HOTP_UPPER_VOID): lambda rules, state: rules.has(state, KeyItem.VOID, KeyItem.CLAW),
    (R.HOTP_START_LEFT, R.HOTP_ELEVATOR): lambda rules, state: (
        rules.switches(state, Switch.HOTP_LEFT_BACKTRACK, disabled_case=False)
    ),
    (R.HOTP_START_LEFT, R.HOTP_START_MID): lambda rules, state: (
        rules.switches(state, Switch.HOTP_LEFT_3, disabled_case=False)
        or (
            rules.has(state, KeyItem.STAR)
            and rules.switches(state, Switch.HOTP_LEFT_1, Switch.HOTP_LEFT_2, disabled_case=True)
        )
    ),
    (R.HOTP_START_BOTTOM, R.MECH_BRAM_TUNNEL): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.HOTP_START_BOTTOM, R.HOTP_START): lambda rules, state: (
        rules.has(state, KeyItem.STAR)
        or (rules.white_doors(state, WhiteDoor.HOTP_START, disabled_case=True) and rules.has(state, Eye.BLUE))
    ),
    (R.HOTP_START_BOTTOM, R.HOTP_LOWER): lambda rules, state: (
        rules.switches(
            state,
            Switch.HOTP_BELOW_START,
            disabled_case=lambda rules, state: rules.reachable(state, L.HOTP_SWITCH_BELOW_START),
        )
    ),
    (R.HOTP_LOWER, R.HOTP_START_BOTTOM): lambda rules, state: (
        rules.switches(state, Switch.HOTP_BELOW_START, disabled_case=False)
    ),
    (R.HOTP_LOWER, R.HOTP_EPIMETHEUS): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.HOTP_STATUE, disabled_case=True)
    ),
    (R.HOTP_LOWER, R.HOTP_TP_TUTORIAL): lambda rules, state: (
        rules.switches(state, Crystal.HOTP_LOWER, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
        or rules.switches(state, Switch.HOTP_LOWER_SHORTCUT, disabled_case=False)
    ),
    (R.HOTP_LOWER, R.HOTP_MECH_VOID_CONNECTION): lambda rules, state: (
        rules.switches(
            state, Crystal.HOTP_BOTTOM, disabled_case=(rules.hard and rules.has(state, ShopUpgrade.KYULI_RAY))
        )
    ),
    (R.HOTP_EPIMETHEUS, R.MECH_AFTER_BK): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.HOTP_EPIMETHEUS, R.HOTP_LOWER): lambda rules, state: True,
    (R.HOTP_MECH_VOID_CONNECTION, R.HOTP_AMULET_CONNECTION): lambda rules, state: (
        rules.switches(
            state, Crystal.HOTP_ROCK_ACCESS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.HOTP_MECH_VOID_CONNECTION, R.MECH_LOWER_VOID): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.HOTP_MECH_VOID_CONNECTION, R.HOTP_LOWER): lambda rules, state: (
        rules.switches(state, Crystal.HOTP_BOTTOM, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.HOTP_AMULET_CONNECTION, R.HOTP_AMULET): lambda rules, state: (rules.has(state, KeyItem.CLAW, Eye.RED, Eye.BLUE)),
    (R.HOTP_AMULET_CONNECTION, R.GT_BUTT): lambda rules, state: (
        rules.switches(state, Switch.HOTP_ROCK, disabled_case=True)
    ),
    (R.HOTP_AMULET_CONNECTION, R.HOTP_MECH_VOID_CONNECTION): lambda rules, state: (
        rules.switches(
            state, Crystal.HOTP_ROCK_ACCESS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.HOTP_TP_TUTORIAL, R.HOTP_BELL_CAMPFIRE): lambda rules, state: True,  # until skulls are included
    (R.HOTP_TP_TUTORIAL, R.HOTP_LOWER): lambda rules, state: True,
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_LOWER_ARIAS): lambda rules, state: (
        rules.has(state, Character.ARIAS) and (rules.has(state, KeyItem.BELL) or rules.can(state, Logic.ARIAS_JUMP))
    ),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_RED_KEY): lambda rules, state: rules.has(state, Eye.GREEN, KeyItem.CLOAK),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_CATH_CONNECTION): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_TP_TUTORIAL): lambda rules, state: False,  # until skulls are included
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_BELL): lambda rules, state: (
        rules.switches(state, Switch.HOTP_BELL_ACCESS, disabled_case=True)
        and (
            rules.switches(
                state,
                Crystal.HOTP_BELL_ACCESS,
                disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
            )
            or (
                rules.has(state, KeyItem.BELL, KeyItem.BLOCK)
                and (rules.has(state, Character.KYULI) or rules.can(state, Logic.ARIAS_JUMP))
            )
            or (rules.hard and rules.has(state, KeyItem.CLAW))
        )
    ),
    (R.HOTP_CATH_CONNECTION, R.HOTP_BELL): lambda rules, state: True,
    (R.HOTP_CATH_CONNECTION, R.CATH_START): lambda rules, state: (
        rules.has(state, KeyItem.VOID, KeyItem.CLAW)
        and rules.red_doors(
            state, RedDoor.CATH, disabled_case=lambda rules, state: rules.reachable(state, L.HOTP_RED_KEY)
        )
    ),
    (R.HOTP_LOWER_ARIAS, R.HOTP_BELL_CAMPFIRE): lambda rules, state: rules.has(state, Character.ARIAS),
    (R.HOTP_LOWER_ARIAS, R.HOTP_EYEBALL): lambda rules, state: (
        rules.switches(state, Switch.HOTP_TELEPORTS, disabled_case=True)
        or (
            rules.has(state, KeyItem.BLOCK, KeyItem.BELL)
            and (rules.has(state, Character.KYULI) or rules.can(state, Logic.ARIAS_JUMP))
        )
    ),
    (R.HOTP_EYEBALL, R.HOTP_ELEVATOR): lambda rules, state: (
        rules.switches(state, Switch.HOTP_EYEBALL_SHORTCUT, Switch.HOTP_WORM_PILLAR, disabled_case=False)
        or rules.switches(state, Switch.HOTP_GHOST_BLOOD, disabled_case=True)
    ),
    (R.HOTP_EYEBALL, R.HOTP_LOWER_ARIAS): lambda rules, state: True,
    (R.HOTP_ELEVATOR, R.HOTP_OLD_MAN): lambda rules, state: (
        rules.has(state, KeyItem.CLOAK)
        and rules.switches(state, Face.HOTP_OLD_MAN, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    (R.HOTP_ELEVATOR, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.HOTP_ELEVATOR, R.HOTP_TOP_LEFT): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.HOTP_ELEVATOR, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.HOTP_ELEVATOR, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.HOTP_ELEVATOR, R.HOTP_START_LEFT): lambda rules, state: (
        rules.switches(state, Switch.HOTP_LEFT_BACKTRACK, disabled_case=True)
    ),
    (R.HOTP_ELEVATOR, R.HOTP_EYEBALL): lambda rules, state: (
        rules.switches(state, Switch.HOTP_EYEBALL_SHORTCUT, Switch.HOTP_WORM_PILLAR, disabled_case=True)
        and rules.switches(state, Switch.HOTP_GHOST_BLOOD, disabled_case=False)
    ),
    (R.HOTP_ELEVATOR, R.HOTP_CLAW_LEFT): lambda rules, state: (
        (rules.switches(state, Switch.HOTP_TO_CLAW_2, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT))
        or (
            rules.has(state, KeyItem.BELL)
            and (rules.has(state, KeyItem.CLAW, KeyItem.CLOAK) or rules.has(state, Character.KYULI, KeyItem.BLOCK))
        )
    ),
    (R.HOTP_ELEVATOR, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.HOTP_ELEVATOR, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.HOTP_ELEVATOR, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.HOTP_ELEVATOR, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.HOTP_ELEVATOR, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.HOTP_ELEVATOR, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.HOTP_CLAW_LEFT, R.HOTP_ELEVATOR): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.HOTP_CLAW_LEFT, R.HOTP_TOP_LEFT): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.HOTP_CLAW, disabled_case=True)
    ),
    (R.HOTP_CLAW_LEFT, R.HOTP_CLAW): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.HOTP_TOP_LEFT, R.HOTP_ELEVATOR): lambda rules, state: True,
    (R.HOTP_TOP_LEFT, R.HOTP_CLAW_CAMPFIRE): lambda rules, state: True,  # until enemy arenas are included
    (R.HOTP_TOP_LEFT, R.HOTP_CLAW_LEFT): lambda rules, state: True,
    (R.HOTP_TOP_LEFT, R.HOTP_ABOVE_OLD_MAN): lambda rules, state: (
        rules.has(state, Eye.GREEN)
        and (
            rules.switches(state, Switch.HOTP_TO_ABOVE_OLD_MAN, disabled_case=True)
            or (rules.has(state, KeyItem.BLOCK, KeyItem.BELL) and rules.can(state, Logic.ARIAS_JUMP))
        )
    ),
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_TOP_LEFT): lambda rules, state: True,
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_CLAW): lambda rules, state: (
        rules.switches(state, Switch.HOTP_CLAW_ACCESS, disabled_case=True)
        and (rules.has(state, Character.KYULI) or rules.can(state, Logic.BLOCK_IN_WALL))
    ),
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_HEART): lambda rules, state: (
        rules.switches(
            state, Crystal.HOTP_AFTER_CLAW, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.HOTP_CLAW, R.HOTP_CLAW_CAMPFIRE): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) and rules.switches(state, Switch.HOTP_CLAW_ACCESS, disabled_case=False)
    ),
    (R.HOTP_CLAW, R.HOTP_CLAW_LEFT): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.HOTP_HEART, R.HOTP_CLAW_CAMPFIRE): lambda rules, state: (
        rules.switches(
            state,
            Crystal.HOTP_AFTER_CLAW,
            disabled_case=(
                rules.hard
                and (
                    rules.has(state, KeyItem.CLOAK)
                    or rules.has(state, Character.ALGUS, KeyItem.ICARUS)
                    or rules.has(state, ShopUpgrade.KYULI_RAY)
                )
            ),
        )
    ),
    (R.HOTP_HEART, R.HOTP_UPPER_ARIAS): lambda rules, state: rules.has(state, Character.ARIAS),
    (R.HOTP_HEART, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: (
        rules.has(state, KeyItem.CLAW)
        and (
            rules.has(state, KeyItem.ICARUS)
            or rules.has(state, KeyItem.BLOCK, KeyItem.BELL)
            or rules.switches(state, Crystal.HOTP_HEART, disabled_case=False)
        )
    ),
    (R.HOTP_UPPER_ARIAS, R.HOTP_HEART): lambda rules, state: True,
    (R.HOTP_UPPER_ARIAS, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_MAIDEN): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.HOTP_MAIDEN, disabled_case=True)
        and (rules.has(state, KeyItem.SWORD) or rules.has(state, Character.KYULI, KeyItem.BLOCK, KeyItem.BELL))
    ),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_HEART): lambda rules, state: True,
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_TP_PUZZLE): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_BOSS): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.HOTP_BOSS, disabled_case=True)
    ),
    (R.HOTP_TP_PUZZLE, R.HOTP_TP_FALL_TOP): lambda rules, state: (
        rules.has(state, KeyItem.STAR) or rules.switches(state, Switch.HOTP_TP_PUZZLE, disabled_case=True)
    ),
    (R.HOTP_TP_FALL_TOP, R.HOTP_FALL_BOTTOM): lambda rules, state: rules.has(state, KeyItem.CLOAK),
    (R.HOTP_TP_FALL_TOP, R.HOTP_TP_PUZZLE): lambda rules, state: (
        rules.has(state, KeyItem.STAR) or rules.switches(state, Switch.HOTP_TP_PUZZLE, disabled_case=False)
    ),
    (R.HOTP_TP_FALL_TOP, R.HOTP_GAUNTLET_CONNECTION): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.HOTP_TP_FALL_TOP, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: (
        rules.has(state, Character.KYULI) or (rules.has(state, KeyItem.BLOCK) and rules.can(state, Logic.COMBO_HEIGHT))
    ),
    (R.HOTP_GAUNTLET_CONNECTION, R.HOTP_GAUNTLET): lambda rules, state: (
        rules.has(state, KeyItem.CLAW, KeyItem.BANISH, KeyItem.BELL)
    ),
    (R.HOTP_FALL_BOTTOM, R.HOTP_TP_FALL_TOP): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.HOTP_FALL_BOTTOM, R.MECH_TP_CONNECTION): lambda rules, state: True,
    (R.HOTP_FALL_BOTTOM, R.HOTP_UPPER_VOID): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.HOTP_UPPER_VOID, R.HOTP_FALL_BOTTOM): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.HOTP_UPPER_VOID, R.HOTP_TP_FALL_TOP): lambda rules, state: True,
    (R.HOTP_UPPER_VOID, R.HOTP_LOWER_VOID): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.HOTP_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.HOTP_BOSS, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.HOTP_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.HOTP_BOSS, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: True,
    (R.HOTP_BOSS, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.HOTP_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.HOTP_BOSS, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.HOTP_BOSS, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.HOTP_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.HOTP_BOSS, R.ROA_START): lambda rules, state: True,
    (R.HOTP_BOSS, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.ROA_START, R.HOTP_BOSS): lambda rules, state: True,
    (R.ROA_START, R.ROA_WORMS): lambda rules, state: (
        rules.switches(
            state,
            Crystal.ROA_1ST_ROOM,
            # this should be more complicated
            disabled_case=(rules.has(state, KeyItem.BELL) and rules.can(state, Logic.CRYSTAL)),
        )
    ),
    (R.ROA_WORMS, R.ROA_HEARTS): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.ROA_WORMS, disabled_case=True)
        and (rules.switches(state, Switch.ROA_AFTER_WORMS, disabled_case=True) or rules.has(state, KeyItem.STAR))
    ),
    (R.ROA_WORMS, R.ROA_START): lambda rules, state: (
        rules.switches(state, Switch.ROA_WORMS, disabled_case=True)
        or rules.switches(
            state, Crystal.ROA_1ST_ROOM, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.ROA_WORMS, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.ROA_HEARTS, R.ROA_BOTTOM_ASCEND): lambda rules, state: (
        rules.switches(state, Switch.ROA_1ST_SHORTCUT, disabled_case=False)
    ),
    (R.ROA_HEARTS, R.ROA_SPIKE_CLIMB): lambda rules, state: True,  # until enemy arenas are included
    (R.ROA_HEARTS, R.ROA_WORMS): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.ROA_WORMS, disabled_case=True)
        and (
            rules.switches(state, Switch.ROA_AFTER_WORMS, disabled_case=False)
            or (rules.has(state, KeyItem.STAR, KeyItem.BELL) and rules.can(state, Logic.EXTRA_HEIGHT))
        )
    ),
    (R.ROA_SPIKE_CLIMB, R.ROA_HEARTS): lambda rules, state: False,  # until enemy arenas are included
    (R.ROA_SPIKE_CLIMB, R.ROA_BOTTOM_ASCEND): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.ROA_BOTTOM_ASCEND, R.ROA_HEARTS): lambda rules, state: True,
    (R.ROA_BOTTOM_ASCEND, R.ROA_SPIKE_CLIMB): lambda rules, state: True,
    (R.ROA_BOTTOM_ASCEND, R.ROA_TOP_ASCENT): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.ROA_ASCEND, disabled_case=True)
    ),
    (R.ROA_BOTTOM_ASCEND, R.ROA_TRIPLE_REAPER): lambda rules, state: (
        rules.switches(state, Switch.ROA_ASCEND, disabled_case=True)
        or (rules.has(state, Character.KYULI, KeyItem.BLOCK, KeyItem.BELL))
    ),
    (R.ROA_TRIPLE_REAPER, R.ROA_BOTTOM_ASCEND): lambda rules, state: True,
    (R.ROA_TRIPLE_REAPER, R.ROA_ARENA): lambda rules, state: (
        rules.switches(state, Crystal.ROA_3_REAPERS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.ROA_ARENA, R.ROA_FLAMES_CONNECTION): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.ROA_ARENA, R.ROA_TRIPLE_REAPER): lambda rules, state: (
        rules.switches(state, Crystal.ROA_3_REAPERS, disabled_case=False)
    ),
    (R.ROA_ARENA, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: rules.has(state, Character.KYULI),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_ARIAS_BABY_GORGON): lambda rules, state: (
        rules.has(state, Character.ARIAS)
        and rules.switches(
            state, Crystal.ROA_BABY_GORGON, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_WORMS): lambda rules, state: True,
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_FLAMES_CONNECTION): lambda rules, state: (
        rules.has(state, KeyItem.STAR, KeyItem.BELL)
    ),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_LOWER_VOID): lambda rules, state: (
        rules.switches(state, Switch.ROA_LOWER_VOID, disabled_case=False)
    ),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_ARENA): lambda rules, state: False,  # until arenas are included
    (R.ROA_LOWER_VOID, R.ROA_UPPER_VOID): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.ROA_LOWER_VOID, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.ROA_LOWER_VOID, disabled_case=True)
    ),
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_FLAMES_CONNECTION): lambda rules, state: True,  # until arenas are included
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_FLAMES): lambda rules, state: (
        rules.switches(state, Switch.ROA_BABY_GORGON, disabled_case=False)
        and rules.has(state, KeyItem.BLOCK, Character.KYULI, KeyItem.BELL)
    ),
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: (
        rules.has(state, KeyItem.STAR)
        or (rules.has(state, Character.ARIAS) and rules.switches(state, Crystal.ROA_BABY_GORGON, disabled_case=False))
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_WORM_CLIMB): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.ROA_FLAMES, disabled_case=True) and rules.has(state, KeyItem.CLAW)
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_LEFT_ASCENT): lambda rules, state: (
        rules.switches(
            state,
            Crystal.ROA_LEFT_ASCEND,
            disabled_case=(rules.can(state, Logic.CRYSTAL) and rules.has(state, KeyItem.BELL)),
        )
        and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_ARIAS_BABY_GORGON): lambda rules, state: True,
    (R.ROA_FLAMES_CONNECTION, R.ROA_ARENA): lambda rules, state: True,
    (R.ROA_FLAMES_CONNECTION, R.ROA_FLAMES): lambda rules, state: (
        rules.has(state, KeyItem.GAUNTLET, KeyItem.BELL) and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.ROA_FLAMES, R.ROA_ARIAS_BABY_GORGON): lambda rules, state: (
        rules.switches(state, Switch.ROA_BABY_GORGON, disabled_case=True)
    ),
    (R.ROA_WORM_CLIMB, R.ROA_FLAMES_CONNECTION): lambda rules, state: True,
    (R.ROA_WORM_CLIMB, R.ROA_RIGHT_BRANCH): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.ROA_RIGHT_BRANCH, R.ROA_WORM_CLIMB): lambda rules, state: True,
    (R.ROA_RIGHT_BRANCH, R.ROA_MIDDLE): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.ROA_LEFT_ASCENT, R.ROA_FLAMES_CONNECTION): lambda rules, state: (
        rules.switches(
            state, Crystal.ROA_LEFT_ASCEND, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.ROA_LEFT_ASCENT, R.ROA_TOP_ASCENT): lambda rules, state: (
        rules.switches(state, Switch.ROA_ASCEND_SHORTCUT, disabled_case=False)
    ),
    (R.ROA_TOP_ASCENT, R.ROA_TRIPLE_SWITCH): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_TOP_ASCENT, R.ROA_LEFT_ASCENT): lambda rules, state: (
        rules.switches(state, Switch.ROA_ASCEND_SHORTCUT, disabled_case=False)
    ),
    (R.ROA_TRIPLE_SWITCH, R.ROA_MIDDLE): lambda rules, state: (
        rules.switches(
            state,
            Switch.ROA_TRIPLE_1,
            Switch.ROA_TRIPLE_3,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
        and rules.has(state, KeyItem.CLAW, KeyItem.BELL)
    ),
    (R.ROA_TRIPLE_SWITCH, R.ROA_TOP_ASCENT): lambda rules, state: True,
    (R.ROA_MIDDLE, R.ROA_LEFT_SWITCH): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_MIDDLE, R.ROA_RIGHT_BRANCH): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.ROA_MIDDLE, R.ROA_RIGHT_SWITCH_1): lambda rules, state: (
        rules.has(state, Character.KYULI) or rules.switches(state, Switch.ROA_RIGHT_PATH, disabled_case=False)
    ),
    (R.ROA_MIDDLE, R.ROA_MIDDLE_LADDER): lambda rules, state: (
        # this could allow more
        rules.switches(
            state,
            Crystal.ROA_LADDER_L,
            Crystal.ROA_LADDER_R,
            disabled_case=lambda rules, state: (
                rules.reachable(state, L.ROA_CRYSTAL_LADDER_L) and rules.reachable(state, L.ROA_CRYSTAL_LADDER_R)
            ),
        )
    ),
    (R.ROA_MIDDLE, R.ROA_TRIPLE_SWITCH): lambda rules, state: (
        rules.switches(state, Switch.ROA_TRIPLE_1, Switch.ROA_TRIPLE_3, disabled_case=False)
    ),
    (R.ROA_MIDDLE, R.ROA_LEFT_BABY_GORGON): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_RIGHT_SWITCH_1, R.ROA_RIGHT_SWITCH_2): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_MIDDLE_LADDER, R.ROA_MIDDLE): lambda rules, state: True,
    (R.ROA_MIDDLE_LADDER, R.ROA_UPPER_VOID): lambda rules, state: (
        rules.switches(state, Switch.ROA_SHAFT_L, Switch.ROA_SHAFT_R, disabled_case=True)
    ),
    (R.ROA_UPPER_VOID, R.ROA_MIDDLE_LADDER): lambda rules, state: True,
    (R.ROA_UPPER_VOID, R.ROA_LOWER_VOID): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.ROA_UPPER_VOID, R.ROA_SP_CONNECTION): lambda rules, state: (
        rules.switches(state, Crystal.ROA_SHAFT, Switch.ROA_SHAFT_DOWNWARDS, disabled_case=False)
    ),
    (R.ROA_UPPER_VOID, R.ROA_SPIKE_BALLS): lambda rules, state: (
        rules.switches(
            state, Crystal.ROA_SPIKE_BALLS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.ROA_SPIKE_BALLS, R.ROA_SPIKE_SPINNERS): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.ROA_BALLS, disabled_case=True)
    ),
    (R.ROA_SPIKE_BALLS, R.ROA_UPPER_VOID): lambda rules, state: True,
    (R.ROA_SPIKE_SPINNERS, R.ROA_SPIDERS_1): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.ROA_SPINNERS, disabled_case=True)
    ),
    (R.ROA_SPIKE_SPINNERS, R.ROA_SPIKE_BALLS): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.ROA_BALLS, disabled_case=True)
    ),
    (R.ROA_SPIDERS_1, R.ROA_RED_KEY): lambda rules, state: (
        rules.switches(state, Face.ROA_SPIDERS, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    (R.ROA_SPIDERS_1, R.ROA_SPIDERS_2): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_SPIDERS_1, R.ROA_SPIKE_SPINNERS): lambda rules, state: True,
    (R.ROA_SPIDERS_2, R.ROA_SPIDERS_1): lambda rules, state: True,
    (R.ROA_SPIDERS_2, R.ROA_BLOOD_POT_HALLWAY): lambda rules, state: (
        rules.switches(state, Switch.ROA_SPIDERS, disabled_case=True)
    ),
    (R.ROA_BLOOD_POT_HALLWAY, R.ROA_SP_CONNECTION): lambda rules, state: True,  # until arenas are included
    (R.ROA_BLOOD_POT_HALLWAY, R.ROA_SPIDERS_2): lambda rules, state: True,
    (R.ROA_SP_CONNECTION, R.ROA_BLOOD_POT_HALLWAY): lambda rules, state: True,
    (R.ROA_SP_CONNECTION, R.SP_START): lambda rules, state: (
        rules.red_doors(state, RedDoor.SP, disabled_case=lambda rules, state: rules.reachable(state, L.ROA_RED_KEY))
    ),
    (R.ROA_SP_CONNECTION, R.ROA_ELEVATOR): lambda rules, state: (
        # can probably make it without claw
        rules.has(state, KeyItem.CLAW) and rules.switches(state, Switch.ROA_DARK_ROOM, disabled_case=True)
    ),
    (R.ROA_SP_CONNECTION, R.ROA_UPPER_VOID): lambda rules, state: True,
    (R.ROA_ELEVATOR, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.ROA_ELEVATOR, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.ROA_ELEVATOR, R.ROA_SP_CONNECTION): lambda rules, state: True,
    (R.ROA_ELEVATOR, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.ROA_ELEVATOR, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.ROA_ELEVATOR, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.ROA_ELEVATOR, R.ROA_ICARUS): lambda rules, state: rules.switches(state, Switch.ROA_ICARUS, disabled_case=True),
    (R.ROA_ELEVATOR, R.ROA_DARK_CONNECTION): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) or rules.switches(state, Switch.ROA_ELEVATOR, disabled_case=True)
    ),
    (R.ROA_ELEVATOR, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.ROA_ELEVATOR, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.ROA_ELEVATOR, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.ROA_ELEVATOR, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.ROA_DARK_CONNECTION, R.ROA_ELEVATOR): lambda rules, state: True,
    (R.ROA_DARK_CONNECTION, R.ROA_CENTAUR): lambda rules, state: (
        rules.switches(state, Switch.ROA_BLOOD_POT, disabled_case=False)
    ),
    (R.ROA_DARK_CONNECTION, R.DARK_START): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.DARK_START, R.DARK_END): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) and rules.switches(state, Switch.DARKNESS, disabled_case=True)
    ),
    (R.DARK_END, R.ROA_CENTAUR): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.ROA_CENTAUR, R.ROA_DARK_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.ROA_BLOOD_POT, disabled_case=True)
        or rules.blue_doors(state, BlueDoor.ROA_BLOOD, disabled_case=True)
    ),
    (R.ROA_CENTAUR, R.ROA_BOSS_CONNECTION): lambda rules, state: (
        rules.switches(
            state,
            Crystal.ROA_CENTAUR,
            disabled_case=(
                rules.has(state, KeyItem.BELL, Character.ARIAS)
                and (rules.can(state, Logic.CRYSTAL) or rules.has(state, KeyItem.STAR))
            ),
        )
    ),
    (R.ROA_BOSS_CONNECTION, R.ROA_BOSS): lambda rules, state: (
        rules.switches(state, Crystal.ROA_CENTAUR, disabled_case=False)
        or (rules.has(state, KeyItem.BELL, KeyItem.STAR, Character.ARIAS) and rules.can(state, Logic.EXTRA_HEIGHT))
    ),
    (R.ROA_BOSS_CONNECTION, R.ROA_CENTAUR): lambda rules, state: (
        rules.switches(state, Switch.ROA_BOSS_ACCESS, disabled_case=False)
    ),
    (R.ROA_BOSS, R.ROA_APEX_CONNECTION): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.ROA_BOSS, R.ROA_BOSS_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.ROA_BOSS_ACCESS, disabled_case=False)
    ),
    (R.ROA_APEX_CONNECTION, R.ROA_BOSS): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.ROA_APEX_CONNECTION, R.APEX): lambda rules, state: (
        rules.switches(state, Switch.ROA_APEX_ACCESS, disabled_case=True)
    ),
    (R.APEX, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.APEX, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.APEX, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.APEX, R.FINAL_BOSS): lambda rules, state: rules.has(state, Eye.RED, Eye.BLUE, Eye.GREEN, KeyItem.BELL),
    (R.APEX, R.ROA_APEX_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.ROA_APEX_ACCESS, disabled_case=False)
    ),
    (R.APEX, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.APEX, R.APEX_HEART): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.APEX, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.APEX, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.APEX, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.APEX, R.APEX_CENTAUR): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.APEX, disabled_case=True)
        and rules.has(state, KeyItem.STAR, KeyItem.ADORNED_KEY)
    ),
    (R.APEX, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.APEX, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.CAVES_START, R.CAVES_EPIMETHEUS): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.CAVES, disabled_case=True)
    ),
    (R.CAVES_START, R.GT_BOTTOM): lambda rules, state: True,
    (R.CAVES_EPIMETHEUS, R.CAVES_UPPER): lambda rules, state: (
        rules.has(state, Character.KYULI)
        or rules.can(state, Logic.BLOCK_IN_WALL)
        or rules.can(state, Logic.COMBO_HEIGHT)
    ),
    (R.CAVES_EPIMETHEUS, R.CAVES_START): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.CAVES, disabled_case=True)
    ),
    (R.CAVES_UPPER, R.CAVES_EPIMETHEUS): lambda rules, state: True,
    (R.CAVES_UPPER, R.CAVES_ARENA): lambda rules, state: (
        rules.has_any(state, KeyItem.SWORD, ShopUpgrade.ALGUS_METEOR, ShopUpgrade.KYULI_RAY)
    ),
    (R.CAVES_UPPER, R.CAVES_LOWER): lambda rules, state: (
        rules.switches(state, Switch.CAVES_SKELETONS, disabled_case=True)
    ),
    (R.CAVES_LOWER, R.CAVES_UPPER): lambda rules, state: (
        rules.switches(state, Switch.CAVES_SKELETONS, disabled_case=False)
    ),
    (R.CAVES_LOWER, R.CAVES_ITEM_CHAIN): lambda rules, state: rules.has(state, Eye.RED),
    (R.CAVES_LOWER, R.CATA_START): lambda rules, state: (
        rules.switches(
            state,
            Switch.CAVES_CATA_1,
            Switch.CAVES_CATA_2,
            Switch.CAVES_CATA_3,
            disabled_case=True,
        )
    ),
    (R.CATA_START, R.CATA_CLIMBABLE_ROOT): lambda rules, state: (
        rules.switches(state, Switch.CATA_1ST_ROOM, disabled_case=True)
    ),
    (R.CATA_START, R.CAVES_LOWER): lambda rules, state: (
        rules.switches(
            state,
            Switch.CAVES_CATA_1,
            Switch.CAVES_CATA_2,
            Switch.CAVES_CATA_3,
            disabled_case=False,
        )
    ),
    (R.CATA_CLIMBABLE_ROOT, R.CATA_TOP): lambda rules, state: (
        rules.has(state, Eye.RED) and rules.white_doors(state, WhiteDoor.CATA_TOP, disabled_case=True)
    ),
    (R.CATA_TOP, R.CATA_CLIMBABLE_ROOT): lambda rules, state: (
        rules.has(state, Eye.RED) and rules.white_doors(state, WhiteDoor.CATA_TOP, disabled_case=True)
    ),
    (R.CATA_TOP, R.CATA_ELEVATOR): lambda rules, state: (
        rules.switches(state, Switch.CATA_ELEVATOR, disabled_case=True)
    ),
    (R.CATA_TOP, R.CATA_BOW_CAMPFIRE): lambda rules, state: (
        rules.switches(state, Switch.CATA_TOP, disabled_case=True)
    ),
    (R.CATA_ELEVATOR, R.CATA_BOSS): lambda rules, state: rules.elevator(state, Elevator.CATA_2),
    (R.CATA_ELEVATOR, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.CATA_ELEVATOR, R.TR_START): lambda rules, state: rules.elevator(state, Elevator.TR),
    (R.CATA_ELEVATOR, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.CATA_ELEVATOR, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.CATA_ELEVATOR, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.CATA_ELEVATOR, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.CATA_ELEVATOR, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.CATA_ELEVATOR, R.CATA_TOP): lambda rules, state: (
        rules.switches(state, Switch.CATA_ELEVATOR, disabled_case=False)
    ),
    (R.CATA_ELEVATOR, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.CATA_BOW_CAMPFIRE, R.CATA_TOP): lambda rules, state: (
        rules.switches(state, Switch.CATA_TOP, disabled_case=False)
    ),
    (R.CATA_BOW_CAMPFIRE, R.CATA_BOW_CONNECTION): lambda rules, state: (
        rules.has(state, Character.KYULI) and rules.blue_doors(state, BlueDoor.CATA_SAVE, disabled_case=True)
    ),
    (R.CATA_BOW_CAMPFIRE, R.CATA_EYEBALL_BONES): lambda rules, state: (
        rules.switches(state, Face.CATA_AFTER_BOW, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    (R.CATA_BOW_CONNECTION, R.CATA_BOW): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.CATA_BOW, disabled_case=True)
    ),
    (R.CATA_BOW_CONNECTION, R.CATA_BOW_CAMPFIRE): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.CATA_SAVE, disabled_case=True)
    ),
    (R.CATA_BOW_CONNECTION, R.CATA_VERTICAL_SHORTCUT): lambda rules, state: (
        rules.switches(state, Switch.CATA_VERTICAL_SHORTCUT, disabled_case=False)
    ),
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_BLUE_EYE_DOOR): lambda rules, state: True,
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_FLAMES_FORK): lambda rules, state: True,
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_BOW_CONNECTION): lambda rules, state: (
        rules.switches(state, Switch.CATA_VERTICAL_SHORTCUT, disabled_case=True)
        and (rules.switches(state, Switch.CATA_MID_SHORTCUT, disabled_case=True) or rules.has(state, Character.KYULI))
    ),
    (R.CATA_EYEBALL_BONES, R.CATA_SNAKE_MUSHROOMS): lambda rules, state: rules.has(state, Eye.RED),
    (R.CATA_EYEBALL_BONES, R.CATA_BOW_CAMPFIRE): lambda rules, state: True,
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_DEV_ROOM_CONNECTION): lambda rules, state: rules.has(
        state, KeyItem.CLAW, KeyItem.BELL, Character.ZEEK
    ),
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_EYEBALL_BONES): lambda rules, state: rules.has(state, Eye.RED),
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_DOUBLE_SWITCH): lambda rules, state: (
        rules.switches(state, Switch.CATA_CLAW_2, disabled_case=True)
        and (rules.has(state, KeyItem.CLAW) or rules.has(state, Character.KYULI, Character.ZEEK, KeyItem.BELL))
    ),
    (R.CATA_DEV_ROOM_CONNECTION, R.CATA_DEV_ROOM): lambda rules, state: (
        rules.red_doors(
            state, RedDoor.DEV_ROOM, disabled_case=lambda rules, state: rules.reachable(state, L.GT_RED_KEY)
        )
    ),
    (R.CATA_DOUBLE_SWITCH, R.CATA_SNAKE_MUSHROOMS): lambda rules, state: (
        rules.switches(state, Switch.CATA_CLAW_2, disabled_case=False)
    ),
    (R.CATA_DOUBLE_SWITCH, R.CATA_ROOTS_CAMPFIRE): lambda rules, state: (
        rules.switches(state, Switch.CATA_WATER_1, Switch.CATA_WATER_2, disabled_case=True)
    ),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_BLUE_EYE_DOOR): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_POISON_ROOTS): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.CATA_ROOTS, disabled_case=True) and rules.has(state, Character.KYULI)
    ),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_DOUBLE_SWITCH): lambda rules, state: (
        rules.switches(state, Switch.CATA_WATER_1, Switch.CATA_WATER_2, disabled_case=False)
    ),
    (R.CATA_BLUE_EYE_DOOR, R.CATA_ROOTS_CAMPFIRE): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.CATA_BLUE_EYE_DOOR, R.CATA_FLAMES_FORK): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.CATA_BLUE, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_VERTICAL_SHORTCUT): lambda rules, state: (
        rules.switches(state, Switch.CATA_SHORTCUT_ACCESS, Switch.CATA_AFTER_BLUE_DOOR, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_BLUE_EYE_DOOR): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.CATA_BLUE, disabled_case=True)
        or rules.switches(state, Switch.CATA_SHORTCUT_ACCESS, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_FLAMES): lambda rules, state: (
        rules.switches(state, Switch.CATA_FLAMES_2, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_CENTAUR): lambda rules, state: (
        rules.switches(state, Switch.CATA_LADDER_BLOCKS, disabled_case=True)
    ),
    (R.CATA_CENTAUR, R.CATA_4_FACES): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.CATA_CENTAUR, R.CATA_FLAMES_FORK): lambda rules, state: (
        rules.switches(state, Switch.CATA_LADDER_BLOCKS, disabled_case=False)
    ),
    (R.CATA_CENTAUR, R.CATA_BOSS): lambda rules, state: (
        rules.switches(state, Face.CATA_CAMPFIRE, disabled_case=False)
    ),
    (R.CATA_4_FACES, R.CATA_CENTAUR): lambda rules, state: True,
    (R.CATA_4_FACES, R.CATA_DOUBLE_DOOR): lambda rules, state: (
        rules.switches(state, Face.CATA_X4, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    (R.CATA_DOUBLE_DOOR, R.CATA_4_FACES): lambda rules, state: (
        rules.switches(state, Face.CATA_X4, disabled_case=False)
    ),
    (R.CATA_DOUBLE_DOOR, R.CATA_VOID_R): lambda rules, state: (
        rules.has(state, KeyItem.BANISH, KeyItem.BELL)
        and rules.switches(
            state, Face.CATA_DOUBLE_DOOR, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW)
        )
    ),
    (R.CATA_VOID_R, R.CATA_DOUBLE_DOOR): lambda rules, state: False,  # until arenas are included
    (R.CATA_VOID_R, R.CATA_VOID_L): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.CATA_VOID_L, R.CATA_VOID_R): lambda rules, state: rules.has(state, KeyItem.VOID),
    (R.CATA_VOID_L, R.CATA_BOSS): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.CATA_PRISON, disabled_case=True) and rules.has(state, Character.KYULI)
    ),
    (R.CATA_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.CATA_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.CATA_BOSS, R.CATA_CENTAUR): lambda rules, state: (
        rules.switches(state, Face.CATA_CAMPFIRE, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    (R.CATA_BOSS, R.CATA_VOID_L): lambda rules, state: (
        rules.white_doors(state, WhiteDoor.CATA_PRISON, disabled_case=True)
    ),
    (R.CATA_BOSS, R.TR_START): lambda rules, state: (
        rules.elevator(state, Elevator.TR) or rules.switches(state, Switch.TR_ELEVATOR, disabled_case=True)
    ),
    (R.CATA_BOSS, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.CATA_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.CATA_BOSS, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.CATA_BOSS, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.CATA_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.CATA_BOSS, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.TR_START, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.CATA_1),
    (R.TR_START, R.CATA_BOSS): lambda rules, state: (
        rules.elevator(state, Elevator.CATA_2)
        or (rules.switches(state, Switch.TR_ELEVATOR, disabled_case=False) and rules.can(state, Logic.EXTRA_HEIGHT))
    ),
    (R.TR_START, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.HOTP),
    (R.TR_START, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, Elevator.ROA_1),
    (R.TR_START, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, Elevator.ROA_2),
    (R.TR_START, R.TR_LEFT): lambda rules, state: (
        rules.blue_doors(state, BlueDoor.TR, disabled_case=True)
        and rules.red_doors(state, RedDoor.TR, disabled_case=lambda rules, state: rules.reachable(state, L.TR_RED_KEY))
    ),
    (R.TR_START, R.APEX): lambda rules, state: rules.elevator(state, Elevator.APEX),
    (R.TR_START, R.GT_BOSS): lambda rules, state: rules.elevator(state, Elevator.GT_2),
    (R.TR_START, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, Elevator.MECH_1),
    (R.TR_START, R.MECH_BOSS): lambda rules, state: rules.elevator(state, Elevator.MECH_2),
    (R.TR_START, R.TR_BRAM): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.TR_LEFT, R.TR_TOP_RIGHT): lambda rules, state: rules.has(state, KeyItem.STAR, KeyItem.BELL),
    (R.TR_LEFT, R.TR_BOTTOM_LEFT): lambda rules, state: rules.has(state, KeyItem.BANISH, KeyItem.BELL),
    (R.TR_BOTTOM_LEFT, R.TR_BOTTOM): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.TR_TOP_RIGHT, R.TR_GOLD): lambda rules, state: (
        rules.has(state, Character.ZEEK, KeyItem.BELL)
        and (rules.has_any(state, Character.KYULI, KeyItem.BLOCK) or rules.can(state, Logic.ARIAS_JUMP))
    ),
    (R.TR_TOP_RIGHT, R.TR_MIDDLE_RIGHT): lambda rules, state: (
        rules.switches(
            state,
            Crystal.TR_GOLD,
            disabled_case=(rules.has(state, KeyItem.BELL, KeyItem.CLAW) and rules.can(state, Logic.CRYSTAL)),
        )
    ),
    (R.TR_MIDDLE_RIGHT, R.TD_DARK_ARIAS): lambda rules, state: rules.has(state, Eye.GREEN),
    (R.TR_MIDDLE_RIGHT, R.TR_BOTTOM): lambda rules, state: (
        rules.switches(state, Switch.TR_BOTTOM, disabled_case=True)
    ),
    (R.TR_BOTTOM, R.TR_BOTTOM_LEFT): lambda rules, state: rules.has(state, Eye.BLUE),
    (R.CD_START, R.CD_2): lambda rules, state: rules.switches(state, Switch.CD_1, disabled_case=True),
    (R.CD_START, R.CD_BOSS): lambda rules, state: (
        rules.region(R.CD_ARIAS_ROUTE).can_reach(state) and rules.region(R.CD_TOP).can_reach(state)
    ),
    (R.CD_2, R.CD_3): lambda rules, state: True,  # until arenas are included
    (R.CD_3, R.CD_MIDDLE): lambda rules, state: rules.switches(state, Switch.CD_3, disabled_case=True),
    (R.CD_MIDDLE, R.CD_KYULI_ROUTE): lambda rules, state: (
        rules.switches(state, Switch.CD_CAMPFIRE, disabled_case=True)
    ),
    (R.CD_MIDDLE, R.CD_ARIAS_ROUTE): lambda rules, state: rules.has(state, Character.ARIAS),
    (R.CD_KYULI_ROUTE, R.CD_CAMPFIRE_3): lambda rules, state: rules.has(state, Character.KYULI),
    (R.CD_CAMPFIRE_3, R.CD_ARENA): lambda rules, state: (
        rules.switches(state, Crystal.CD_CAMPFIRE, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.CD_ARENA, R.CD_STEPS): lambda rules, state: True,  # until arenas are included
    (R.CD_STEPS, R.CD_TOP): lambda rules, state: (
        rules.switches(state, Crystal.CD_STEPS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.CATH_START, R.CATH_START_LEFT): lambda rules, state: (
        rules.switches(
            state,
            Crystal.CATH_1ST_ROOM,
            disabled_case=lambda rules, state: rules.reachable(state, L.CATH_CRYSTAL_1ST_ROOM),
        )
        and rules.has(state, KeyItem.CLAW)
    ),
    (R.CATH_START, R.CATH_START_RIGHT): lambda rules, state: True,  # until arenas are included
    (R.CATH_START_RIGHT, R.CATH_START_TOP_LEFT): lambda rules, state: (
        rules.switches(state, Switch.CATH_BOTTOM, disabled_case=True)
    ),
    (R.CATH_START_TOP_LEFT, R.CATH_START_LEFT): lambda rules, state: (
        rules.switches(state, Face.CATH_L, disabled_case=False)
    ),
    (R.CATH_START_LEFT, R.CATH_TP): lambda rules, state: (
        rules.switches(state, Face.CATH_R, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    (R.CATH_TP, R.CATH_LEFT_SHAFT): lambda rules, state: True,
    (R.CATH_LEFT_SHAFT, R.CATH_SHAFT_ACCESS): lambda rules, state: (
        rules.switches(state, Crystal.CATH_SHAFT_ACCESS, disabled_case=False) and rules.has(state, KeyItem.CLAW)
    ),
    (R.CATH_LEFT_SHAFT, R.CATH_UNDER_CAMPFIRE): lambda rules, state: (
        rules.switches(state, Crystal.CATH_SHAFT, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.CATH_UNDER_CAMPFIRE, R.CATH_CAMPFIRE_1): lambda rules, state: rules.has(state, Character.ZEEK, KeyItem.BELL),
    (R.CATH_CAMPFIRE_1, R.CATH_SHAFT_ACCESS): lambda rules, state: rules.has(state, Character.KYULI),
    (R.CATH_SHAFT_ACCESS, R.CATH_ORB_ROOM): lambda rules, state: (
        rules.switches(state, Switch.CATH_BESIDE_SHAFT, disabled_case=True)
    ),
    (R.CATH_ORB_ROOM, R.CATH_GOLD_BLOCK): lambda rules, state: (
        rules.switches(
            state,
            Crystal.CATH_ORBS,
            disabled_case=(rules.can(state, Logic.CRYSTAL) and rules.has(state, KeyItem.BELL)),
        )
    ),
    (R.CATH_ORB_ROOM, R.CATH_RIGHT_SHAFT_CONNECTION): lambda rules, state: True,  # until arenas are included
    (R.CATH_RIGHT_SHAFT_CONNECTION, R.CATH_RIGHT_SHAFT): lambda rules, state: rules.has(
        state, KeyItem.BELL, Character.ZEEK, KeyItem.BOW
    ),
    (R.CATH_RIGHT_SHAFT, R.CATH_TOP): lambda rules, state: rules.has(state, KeyItem.CLAW),
    (R.CATH_TOP, R.CATH_UPPER_SPIKE_PIT): lambda rules, state: (
        rules.switches(
            state, Crystal.CATH_SPIKE_PIT, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.CATH_TOP, R.CATH_CAMPFIRE_2): lambda rules, state: (
        rules.switches(state, Switch.CATH_TOP_CAMPFIRE, disabled_case=True)
    ),
    (R.SP_START, R.SP_STAR_END): lambda rules, state: rules.has(state, KeyItem.BLOCK, KeyItem.BELL, KeyItem.CLAW),
    (R.SP_START, R.SP_CAMPFIRE_1): lambda rules, state: (
        rules.switches(state, Crystal.SP_BLOCKS, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.SP_CAMPFIRE_1, R.SP_HEARTS): lambda rules, state: (rules.switches(state, Switch.SP_BUBBLES, disabled_case=True)),
    (R.SP_HEARTS, R.SP_ORBS): lambda rules, state: rules.has(state, KeyItem.STAR, KeyItem.BELL, Character.KYULI),
    (R.SP_HEARTS, R.SP_FROG): lambda rules, state: (rules.switches(state, Switch.SP_DOUBLE_DOORS, disabled_case=True)),
    (R.SP_HEARTS, R.SP_PAINTING): lambda rules, state: True,  # until arenas are included
    (R.SP_PAINTING, R.SP_SHAFT): lambda rules, state: (
        rules.has(state, KeyItem.CLAW) and rules.blue_doors(state, BlueDoor.SP, disabled_case=True)
    ),
    (R.SP_SHAFT, R.SP_STAR): lambda rules, state: (
        rules.has(state, KeyItem.CLAW, KeyItem.BELL)
        and rules.switches(state, Crystal.SP_STAR, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    (R.SP_STAR, R.SP_STAR_CONNECTION): lambda rules, state: rules.has(state, KeyItem.STAR),
    (R.SP_STAR_CONNECTION, R.SP_STAR_END): lambda rules, state: (
        rules.switches(
            state, Switch.SP_AFTER_STAR, disabled_case=lambda rules, state: rules.has(state, Character.ARIAS)
        )
    ),
    (R.SP_FROG, R.SP_CAMPFIRE_2): lambda rules, state: True,  # until arenas are included
    (R.SP_CAMPFIRE_2, R.HOTP_MAIDEN): lambda rules, state: True,
}

INDIRECT_CONDITIONS: Tuple[Tuple[Union[L, R], Tuple[R, R]], ...] = (
    (L.GT_SWITCH_BUTT_ACCESS, (R.GT_TOP_LEFT, R.GT_BUTT)),
    (L.GT_SWITCH_SPIKE_TUNNEL, (R.GT_TOP_RIGHT, R.GT_SPIKE_TUNNEL)),
    (L.GT_CRYSTAL_LADDER, (R.GT_UPPER_ARIAS, R.GT_OLD_MAN_FORK)),
    (L.GT_SWITCH_UPPER_ARIAS, (R.GT_UPPER_ARIAS, R.MECH_SWORD_CONNECTION)),
    (L.GT_CRYSTAL_LADDER, (R.GT_OLD_MAN_FORK, R.GT_UPPER_ARIAS)),
    (L.MECH_RED_KEY, (R.MECH_ZEEK_CONNECTION, R.MECH_ZEEK)),
    (L.HOTP_SWITCH_BELOW_START, (R.HOTP_START_BOTTOM, R.HOTP_LOWER)),
    (L.HOTP_RED_KEY, (R.HOTP_CATH_CONNECTION, R.CATH_START)),
    (L.ROA_CRYSTAL_LADDER_L, (R.ROA_MIDDLE, R.ROA_MIDDLE_LADDER)),
    (L.ROA_CRYSTAL_LADDER_R, (R.ROA_MIDDLE, R.ROA_MIDDLE_LADDER)),
    (L.ROA_RED_KEY, (R.ROA_SP_CONNECTION, R.SP_START)),
    (L.GT_RED_KEY, (R.CATA_DEV_ROOM_CONNECTION, R.CATA_DEV_ROOM)),
    (L.TR_RED_KEY, (R.TR_START, R.TR_LEFT)),
    (R.CD_ARIAS_ROUTE, (R.CD_START, R.CD_BOSS)),
    (R.CD_TOP, (R.CD_START, R.CD_BOSS)),
)

ITEM_RULES: Dict[L, AstalonRule] = {
    L.GT_GORGONHEART: lambda rules, state: (
        rules.switches(state, Switch.GT_GH, disabled_case=True)
        or rules.has_any(state, Character.KYULI, KeyItem.ICARUS, KeyItem.BLOCK, KeyItem.CLOAK, KeyItem.BOOTS)
    ),
    L.GT_ANCIENTS_RING: lambda rules, state: rules.has(state, Eye.RED),
    L.GT_BANISH: lambda rules, state: (
        rules.region(R.GT_BOTTOM).can_reach(state)
        and rules.region(R.GT_ASCENDANT_KEY).can_reach(state)
        and rules.region(R.GT_BUTT).can_reach(state)
    ),
    L.HOTP_BELL: lambda rules, state: (
        rules.switches(state, Switch.HOTP_BELL, disabled_case=True)
        or rules.has(state, Character.KYULI)
        or rules.can(state, Logic.COMBO_HEIGHT)
    ),
    L.HOTP_MAIDEN_RING: lambda rules, state: (
        rules.switches(
            state,
            Crystal.HOTP_MAIDEN_1,
            Crystal.HOTP_MAIDEN_2,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
    ),
    L.TR_ADORNED_KEY: lambda rules, state: (
        rules.switches(
            state,
            Switch.TR_ADORNED_L,
            Switch.TR_ADORNED_M,
            Switch.TR_ADORNED_R,
            disabled_case=lambda rules, state: (
                rules.reachable(state, L.TR_SWITCH_ADORNED_L)
                and rules.reachable(state, L.TR_SWITCH_ADORNED_M)
                and rules.reachable(state, L.TR_SWITCH_ADORNED_R)
            ),
        )
    ),
    L.CATH_BLOCK: lambda rules, state: (
        rules.switches(
            state,
            Crystal.CATH_TOP_L,
            Crystal.CATH_TOP_R,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
    ),
}

CHARACTER_RULES: Dict[Tuple[Character, L], AstalonRule] = {
    (Character.ZEEK, L.MECH_ZEEK): lambda rules, state: rules.has(state, KeyItem.CROWN),
}

ATTACK_RULES: Dict[L, AstalonRule] = {
    L.MECH_ATTACK_VOLANTIS: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.MECH_ATTACK_STAR: lambda rules, state: rules.has(state, KeyItem.STAR),
    L.ROA_ATTACK: lambda rules, state: rules.has(state, KeyItem.STAR),
    L.CAVES_ATTACK_RED: lambda rules, state: rules.has(state, Eye.RED),
    L.CAVES_ATTACK_BLUE: lambda rules, state: rules.has(state, Eye.RED, Eye.BLUE),
    L.CAVES_ATTACK_GREEN: lambda rules, state: (
        rules.has(state, Eye.RED, Eye.BLUE) and rules.has_any(state, Eye.GREEN, KeyItem.STAR)
    ),
    L.CD_ATTACK: lambda rules, state: (
        rules.switches(state, Switch.CD_TOP, disabled_case=True)
        or rules.has(state, KeyItem.BLOCK, KeyItem.BELL, Character.KYULI)
    ),
}

HEALTH_RULES: Dict[L, AstalonRule] = {
    L.GT_HP_1_RING: lambda rules, state: (
        rules.has(state, KeyItem.STAR)
        or (
            rules.region(R.GT_UPPER_PATH).can_reach(state)
            and rules.blue_doors(state, BlueDoor.GT_RING, disabled_case=True)
        )
    ),
    L.GT_HP_5_KEY: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.MECH_HP_1_SWITCH: lambda rules, state: rules.switches(state, Switch.MECH_INVISIBLE, disabled_case=True),
    L.MECH_HP_3_CLAW: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.HOTP_HP_2_GAUNTLET: lambda rules, state: rules.has(state, KeyItem.CLAW, Character.ZEEK, KeyItem.BELL),
    L.HOTP_HP_5_OLD_MAN: lambda rules, state: (
        rules.has(state, KeyItem.CLAW)
        and (rules.has(state, KeyItem.BELL, KeyItem.BANISH) or rules.has(state, KeyItem.CHALICE))
        and rules.switches(state, Switch.HOTP_ABOVE_OLD_MAN, disabled_case=True)
    ),
    L.HOTP_HP_5_START: lambda rules, state: (
        rules.has(state, KeyItem.CLAW) and rules.blue_doors(state, BlueDoor.HOTP_START, disabled_case=True)
    ),
    L.ROA_HP_2_RIGHT: lambda rules, state: (
        rules.has_any(state, KeyItem.GAUNTLET, KeyItem.CHALICE, KeyItem.STAR)
        and rules.has(state, KeyItem.BELL, Character.KYULI)
        and rules.switches(
            state,
            Crystal.ROA_BRANCH_L,
            Crystal.ROA_BRANCH_R,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
    ),
    L.ROA_HP_5_SOLARIA: lambda rules, state: rules.has(state, Character.KYULI),
    L.APEX_HP_1_CHALICE: lambda rules, state: rules.blue_doors(state, BlueDoor.APEX, disabled_case=True),
    L.CAVES_HP_1_START: lambda rules, state: (
        rules.has(state, KeyItem.CHALICE)
        or rules.switches(state, Face.CAVES_1ST_ROOM, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    L.CAVES_HP_1_CYCLOPS: lambda rules, state: (
        rules.has_any(state, KeyItem.SWORD, ShopUpgrade.ALGUS_METEOR, ShopUpgrade.KYULI_RAY)
    ),
    L.CATA_HP_1_ABOVE_POISON: lambda rules, state: (
        rules.has(state, Character.KYULI)
        and (
            rules.switches(
                state,
                Crystal.CATA_POISON_ROOTS,
                disabled_case=(rules.can(state, Logic.CRYSTAL) and rules.has(state, KeyItem.BELL)),
            )
            or rules.has(state, KeyItem.ICARUS, KeyItem.CLAW)
        )
    ),
    L.CATA_HP_2_GEMINI_BOTTOM: lambda rules, state: (
        rules.has(state, Character.KYULI)
        and rules.switches(state, Face.CATA_BOTTOM, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    L.CATA_HP_2_GEMINI_TOP: lambda rules, state: rules.has(state, Character.KYULI),
    L.CATA_HP_2_ABOVE_GEMINI: lambda rules, state: (
        (rules.has(state, KeyItem.CLAW) or rules.has(state, KeyItem.BLOCK, KeyItem.BELL))
        and (rules.has(state, KeyItem.GAUNTLET, KeyItem.BELL) or rules.has(state, KeyItem.CHALICE))
    ),
    L.CAVES_HP_5_CHAIN: lambda rules, state: (
        rules.has(state, Eye.RED, Eye.BLUE, KeyItem.STAR, KeyItem.CLAW, KeyItem.BELL)
    ),
    L.CD_HP_1: lambda rules, state: (
        rules.switches(state, Switch.CD_TOP, disabled_case=True)
        or rules.has(state, KeyItem.BLOCK, KeyItem.BELL, Character.KYULI)
    ),
    L.CATH_HP_1_TOP_LEFT: lambda rules, state: rules.has_any(state, KeyItem.CLOAK, KeyItem.ICARUS),
    L.CATH_HP_1_TOP_RIGHT: lambda rules, state: rules.has_any(state, KeyItem.CLOAK, KeyItem.ICARUS),
    L.CATH_HP_2_CLAW: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.CATH_HP_5_BELL: lambda rules, state: (
        rules.has_any(state, Character.KYULI, KeyItem.BLOCK, KeyItem.ICARUS, KeyItem.CLOAK)
    ),
}

WHITE_KEY_RULES: Dict[L, AstalonRule] = {
    L.MECH_WHITE_KEY_LINUS: lambda rules, state: (rules.switches(state, Switch.MECH_LOWER_KEY, disabled_case=True)),
    L.MECH_WHITE_KEY_TOP: lambda rules, state: (
        rules.switches(state, Crystal.MECH_TOP, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
        and rules.has(state, Character.KYULI)
    ),
    L.ROA_WHITE_KEY_SAVE: lambda rules, state: rules.switches(state, Switch.ROA_WORMS, disabled_case=True),
}

BLUE_KEY_RULES: Dict[L, AstalonRule] = {
    L.GT_BLUE_KEY_WALL: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.MECH_BLUE_KEY_BLOCKS: lambda rules, state: (rules.switches(state, Switch.MECH_KEY_BLOCKS, disabled_case=True)),
    L.MECH_BLUE_KEY_SAVE: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.MECH_BLUE_KEY_POT: lambda rules, state: (
        rules.has(state, Character.KYULI) or rules.can(state, Logic.COMBO_HEIGHT)
    ),
    L.HOTP_BLUE_KEY_STATUE: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.HOTP_BLUE_KEY_AMULET: lambda rules, state: (
        rules.has(state, Character.KYULI) or rules.can(state, Logic.COMBO_HEIGHT)
    ),
    L.HOTP_BLUE_KEY_LADDER: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.HOTP_BLUE_KEY_MAZE: lambda rules, state: (
        rules.switches(
            state,
            Crystal.HOTP_BELOW_PUZZLE,
            disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL),
        )
    ),
    L.ROA_BLUE_KEY_FACE: lambda rules, state: (
        rules.switches(state, Face.ROA_BLUE_KEY, disabled_case=lambda rules, state: rules.has(state, KeyItem.BOW))
    ),
    L.ROA_BLUE_KEY_FLAMES: lambda rules, state: (rules.switches(state, Switch.ROA_BABY_GORGON, disabled_case=True)),
    L.ROA_BLUE_KEY_TOP: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.SP_BLUE_KEY_ARIAS: lambda rules, state: rules.has(state, Character.ARIAS),
}

RED_KEY_RULES: Dict[L, AstalonRule] = {
    L.GT_RED_KEY: lambda rules, state: rules.has(state, Character.ZEEK, Character.KYULI),
    L.ROA_RED_KEY: lambda rules, state: rules.has(state, KeyItem.CLOAK, KeyItem.CLAW, KeyItem.BELL),
    L.TR_RED_KEY: lambda rules, state: rules.has(state, KeyItem.CLAW),
}

SHOP_RULES: Dict[L, AstalonRule] = {
    L.SHOP_GIFT: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_KNOWLEDGE: lambda rules, state: rules.cheap_shop(state),
    L.SHOP_MERCY: lambda rules, state: rules.expensive_shop(state),
    L.SHOP_ORB_SEEKER: lambda rules, state: rules.cheap_shop(state),
    # this requires way too much map completion, figure it out later
    # L.SHOP_MAP_REVEAL: lambda rules, state: (
    #     rules.region(R.TR).can_reach(state) and rules.region(R.ROA_UPPER).can_reach(state)
    # ),
    L.SHOP_CARTOGRAPHER: lambda rules, state: rules.cheap_shop(state),
    L.SHOP_DEATH_ORB: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_DEATH_POINT: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_TITANS_EGO: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_ALGUS_ARCANIST: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_ALGUS_SHOCK: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_ALGUS_METEOR: lambda rules, state: rules.expensive_shop(state),
    L.SHOP_ARIAS_GORGONSLAYER: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_ARIAS_LAST_STAND: lambda rules, state: rules.expensive_shop(state),
    L.SHOP_ARIAS_LIONHEART: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_KYULI_ASSASSIN: lambda rules, state: rules.cheap_shop(state),
    L.SHOP_KYULI_BULLSEYE: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_KYULI_RAY: lambda rules, state: rules.expensive_shop(state),
    L.SHOP_ZEEK_JUNKYARD: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_ZEEK_ORBS: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_ZEEK_LOOT: lambda rules, state: rules.cheap_shop(state),
    L.SHOP_BRAM_AXE: lambda rules, state: rules.expensive_shop(state),
    L.SHOP_BRAM_HUNTER: lambda rules, state: rules.moderate_shop(state),
    L.SHOP_BRAM_WHIPLASH: lambda rules, state: rules.moderate_shop(state),
}

SWITCH_RULES: Dict[L, AstalonRule] = {
    L.GT_SWITCH_2ND_ROOM: lambda rules, state: (rules.white_doors(state, WhiteDoor.GT_START, disabled_case=True)),
    L.GT_SWITCH_BUTT_ACCESS: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.GT_SWITCH_UPPER_PATH_ACCESS: lambda rules, state: (
        rules.switches(state, Switch.GT_UPPER_PATH_BLOCKS, disabled_case=True)
        or rules.has(state, Character.KYULI, KeyItem.BLOCK, Character.ZEEK)
    ),
    L.GT_CRYSTAL_LADDER: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.GT_CRYSTAL_ROTA: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.GT_CRYSTAL_OLD_MAN_1: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.GT_CRYSTAL_OLD_MAN_2: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_SWITCH_BOSS_ACCESS_2: lambda rules, state: (
        rules.switches(state, Switch.MECH_BOSS_1, disabled_case=True)
        or rules.region(R.MECH_BRAM_TUNNEL).can_reach(state)
    ),
    L.MECH_SWITCH_BOOTS_ACCESS: lambda rules, state: rules.has_any(state, Eye.RED, KeyItem.STAR),
    L.MECH_SWITCH_UPPER_VOID_DROP: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.MECH_SWITCH_CANNON: lambda rules, state: (
        rules.switches(state, Crystal.MECH_CANNON, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    L.MECH_SWITCH_EYEBALL: lambda rules, state: (
        rules.white_doors(state, WhiteDoor.MECH_ARENA, disabled_case=True) or rules.region(R.MECH_POTS).can_reach(state)
    ),
    L.MECH_CRYSTAL_CANNON: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_LINUS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_LOWER: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TO_BOSS_3: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TRIPLE_1: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TRIPLE_2: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TRIPLE_3: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TOP: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_CLOAK: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_SLIMES: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TO_CD: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL)
        and rules.has(state, Eye.BLUE)
        and rules.blue_doors(state, BlueDoor.MECH_CD, disabled_case=True)
    ),
    L.MECH_CRYSTAL_CAMPFIRE: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_1ST_ROOM: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_OLD_MAN: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_TOP_CHAINS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_CRYSTAL_BK: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.MECH_FACE_ABOVE_VOLANTIS: lambda rules, state: rules.has(state, KeyItem.BOW, KeyItem.CLAW),
    L.HOTP_SWITCH_BELOW_START: lambda rules, state: (rules.switches(state, Switch.HOTP_GHOSTS, disabled_case=True)),
    L.HOTP_SWITCH_LOWER_SHORTCUT: lambda rules, state: (
        rules.switches(state, Crystal.HOTP_LOWER, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    L.HOTP_SWITCH_TO_CLAW_2: lambda rules, state: (
        rules.switches(state, Switch.HOTP_TO_CLAW_1, disabled_case=True)
        or (rules.switches(state, Switch.HOTP_TO_CLAW_2, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT))
        or rules.has(state, KeyItem.CLAW)
    ),
    L.HOTP_SWITCH_CLAW_ACCESS: lambda rules, state: (
        rules.has(state, Character.KYULI) or rules.can(state, Logic.BLOCK_IN_WALL)
    ),
    L.HOTP_SWITCH_LEFT_3: lambda rules, state: (
        rules.switches(state, Switch.HOTP_LEFT_1, Switch.HOTP_LEFT_2, disabled_case=True)
        or (rules.has(state, KeyItem.STAR) and rules.region(R.HOTP_START_LEFT).can_reach(state))
    ),
    L.HOTP_SWITCH_EYEBALL_SHORTCUT: lambda rules, state: (
        rules.switches(state, Switch.HOTP_WORM_PILLAR, disabled_case=False)
    ),
    L.HOTP_CRYSTAL_ROCK_ACCESS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_BOTTOM: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_LOWER: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_AFTER_CLAW: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_MAIDEN_1: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_MAIDEN_2: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.switches(state, Crystal.HOTP_MAIDEN_1, disabled_case=True)
    ),
    L.HOTP_CRYSTAL_BELL_ACCESS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_HEART: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_CRYSTAL_BELOW_PUZZLE: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.HOTP_FACE_OLD_MAN: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.ROA_SWITCH_AFTER_WORMS: lambda rules, state: rules.white_doors(state, WhiteDoor.ROA_WORMS, disabled_case=True),
    L.ROA_SWITCH_SPIKE_CLIMB: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.ROA_SWITCH_TRIPLE_3: lambda rules, state: (
        rules.switches(state, Crystal.ROA_TRIPLE_2, disabled_case=lambda rules, state: rules.can(state, Logic.CRYSTAL))
    ),
    L.ROA_SWITCH_BABY_GORGON: lambda rules, state: (
        (
            rules.switches(state, Switch.ROA_BABY_GORGON, disabled_case=False)
            and rules.has(state, KeyItem.BELL, Character.ZEEK, Character.KYULI)
        )
        or rules.region(R.ROA_FLAMES).can_reach(state)
    ),
    L.ROA_CRYSTAL_1ST_ROOM: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.has(state, Character.KYULI, KeyItem.BELL)
    ),
    L.ROA_CRYSTAL_BABY_GORGON: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_LADDER_R: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_LADDER_L: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_CENTAUR: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.has(state, KeyItem.BELL, Character.ARIAS)
    ),
    L.ROA_CRYSTAL_SPIKE_BALLS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_LEFT_ASCEND: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_SHAFT: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_BRANCH_R: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.has(state, Character.KYULI, KeyItem.BELL)
    ),
    L.ROA_CRYSTAL_BRANCH_L: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.has(state, Character.KYULI, KeyItem.BELL)
    ),
    L.ROA_CRYSTAL_3_REAPERS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.ROA_CRYSTAL_TRIPLE_2: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.switches(state, Switch.ROA_TRIPLE_1, disabled_case=True)
    ),
    L.ROA_FACE_SPIDERS: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.ROA_FACE_BLUE_KEY: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.DARK_SWITCH: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.CAVES_FACE_1ST_ROOM: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATA_SWITCH_CLAW_2: lambda rules, state: rules.switches(state, Switch.CATA_CLAW_1, disabled_case=True),
    L.CATA_SWITCH_FLAMES_1: lambda rules, state: rules.switches(state, Switch.CATA_FLAMES_1, disabled_case=True),
    L.CATA_CRYSTAL_POISON_ROOTS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATA_FACE_AFTER_BOW: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATA_FACE_BOW: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATA_FACE_X4: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATA_FACE_CAMPFIRE: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATA_FACE_DOUBLE_DOOR: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATA_FACE_BOTTOM: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.TR_SWITCH_ADORNED_L: lambda rules, state: rules.has(state, KeyItem.CLAW),
    L.TR_SWITCH_ADORNED_M: lambda rules, state: rules.has(state, Eye.RED),
    L.TR_SWITCH_ADORNED_R: lambda rules, state: (
        rules.switches(state, Crystal.TR_DARK_ARIAS, disabled_case=True)
        and rules.has(state, Character.ZEEK, KeyItem.BELL, KeyItem.CLAW)
    ),
    L.TR_CRYSTAL_GOLD: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.has(state, KeyItem.BELL, KeyItem.CLAW)
    ),
    L.TR_CRYSTAL_DARK_ARIAS: lambda rules, state: (
        rules.can(state, Logic.CRYSTAL) and rules.has(state, Character.ZEEK, KeyItem.BELL, KeyItem.CLAW)
    ),
    L.CD_CRYSTAL_BACKTRACK: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CD_CRYSTAL_START: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CD_CRYSTAL_CAMPFIRE: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CD_CRYSTAL_STEPS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_1ST_ROOM: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_SHAFT: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_SPIKE_PIT: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_TOP_L: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_TOP_R: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_SHAFT_ACCESS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_CRYSTAL_ORBS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.CATH_FACE_LEFT: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.CATH_FACE_RIGHT: lambda rules, state: rules.has(state, KeyItem.BOW),
    L.SP_CRYSTAL_BLOCKS: lambda rules, state: rules.can(state, Logic.CRYSTAL),
    L.SP_CRYSTAL_STAR: lambda rules, state: rules.can(state, Logic.CRYSTAL),
}

EVENT_RULES: Dict[Events, AstalonRule] = {
    Events.ZEEK_JOINED: lambda rules, state: rules.has(state, KeyItem.CROWN),
}

VANILLA_CHARACTERS = {Character.ALGUS, Character.ARIAS, Character.KYULI}


class AstalonRules:
    world: "AstalonWorld"
    player: int
    options: AstalonOptions

    _has: Has
    can: Can
    white_doors: Togglable[WhiteDoor]
    blue_doors: Togglable[BlueDoor]
    red_doors: Togglable[RedDoor]
    switches: Togglable[Union[Switch, Crystal, Face]]

    def __init__(self, world: "AstalonWorld"):
        self.world = world
        self.player = world.player
        self.options = world.options

        if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
            self._has = self._vanilla_has
            self.can = self._hard_vanilla_can if self.hard else self._easy_vanilla_can
        else:
            self._has = self._rando_has
            self.can = self._hard_rando_can if self.hard else self._easy_rando_can

        self.white_doors = self._enabled_togglable if self.options.randomize_white_keys else self._disabled_togglable
        self.blue_doors = self._enabled_togglable if self.options.randomize_blue_keys else self._disabled_togglable
        self.red_doors = self._enabled_togglable if self.options.randomize_red_keys else self._disabled_togglable
        self.switches = self._enabled_togglable if self.options.randomize_switches else self._disabled_togglable

    def region(self, name: R):
        return self.world.multiworld.get_region(name.value, self.player)

    def entrance(self, from_: R, to_: R):
        return self.world.multiworld.get_entrance(f"{from_.value} -> {to_.value}", self.player)

    def location(self, name: Union[L, Events]):
        return self.world.multiworld.get_location(name.value, self.player)

    @lru_cache(maxsize=None)
    def _rando_has(self, state: CollectionState, item: Union[AllItems, Events], count: int = 1) -> bool:
        if item == KeyItem.CLOAK and not self._has(state, Character.ALGUS):
            return False
        if item in {KeyItem.SWORD, KeyItem.BOOTS} and not self._has(state, Character.ARIAS):
            return False
        if item in {KeyItem.CLAW, KeyItem.BOW} and not self._has(state, Character.KYULI):
            return False
        if item == KeyItem.BLOCK and not self._has(state, Character.ZEEK):
            return False
        if item == KeyItem.STAR and not self._has(state, Character.BRAM):
            return False
        if item == KeyItem.BANISH and not self.has_any(state, Character.ALGUS, Character.ZEEK):
            return False
        if item == KeyItem.GAUNTLET and not self.has_any(state, Character.ARIAS, Character.BRAM):
            return False

        if item in {ShopUpgrade.ALGUS_ARCANIST, ShopUpgrade.ALGUS_METEOR, ShopUpgrade.ALGUS_SHOCK} and not self._has(
            state, Character.ALGUS
        ):
            return False
        if item in {
            ShopUpgrade.ARIAS_GORGONSLAYER,
            ShopUpgrade.ARIAS_LAST_STAND,
            ShopUpgrade.ARIAS_LIONHEART,
        } and not self._has(state, Character.ARIAS):
            return False
        if item in {ShopUpgrade.KYULI_ASSASSIN, ShopUpgrade.KYULI_BULLSEYE, ShopUpgrade.KYULI_RAY} and not self._has(
            state, Character.KYULI
        ):
            return False
        if item in {ShopUpgrade.ZEEK_JUNKYARD, ShopUpgrade.ZEEK_ORBS, ShopUpgrade.ZEEK_LOOT} and not self._has(
            state, Character.ZEEK
        ):
            return False
        if item in {ShopUpgrade.BRAM_AXE, ShopUpgrade.BRAM_HUNTER, ShopUpgrade.BRAM_WHIPLASH} and not self._has(
            state, Character.BRAM
        ):
            return False

        return state.has(item.value, self.player, count=count)

    @lru_cache(maxsize=None)
    def _vanilla_has(self, state: CollectionState, item: Union[AllItems, Events], count: int = 1) -> bool:
        if item in VANILLA_CHARACTERS:
            return True
        if item == Character.ZEEK:
            return self._has(state, Events.ZEEK_JOINED)
        if item == Character.BRAM:
            return self._has(state, Events.BRAM_JOINED)

        if item == KeyItem.BLOCK and not self._has(state, Character.ZEEK):
            return False
        if item == KeyItem.STAR and not self._has(state, Character.BRAM):
            return False

        if item in {ShopUpgrade.ZEEK_JUNKYARD, ShopUpgrade.ZEEK_ORBS, ShopUpgrade.ZEEK_LOOT} and not self._has(
            state, Character.ZEEK
        ):
            return False
        if item in {ShopUpgrade.BRAM_AXE, ShopUpgrade.BRAM_HUNTER, ShopUpgrade.BRAM_WHIPLASH} and not self._has(
            state, Character.BRAM
        ):
            return False

        return state.has(item.value, self.player, count=count)

    def has(self, state: CollectionState, *items: Union[Character, Eye, KeyItem, ShopUpgrade], count: int = 1) -> bool:
        # cover extra logic instead of calling state.has_all
        for item in items:
            if not self._has(state, item, count=count):
                return False
        return True

    def has_any(self, state: CollectionState, *items: Union[Character, Eye, KeyItem, ShopUpgrade]) -> bool:
        # cover extra logic instead of calling state.has_any
        for item in items:
            if self._has(state, item):
                return True
        return False

    def _enabled_togglable(
        self, state: CollectionState, *items: AllItems, disabled_case: Union[bool, AstalonRule]
    ) -> bool:
        for item in items:
            if not self._has(state, item):
                return False
        return True

    def _disabled_togglable(
        self, state: CollectionState, *items: AllItems, disabled_case: Union[bool, AstalonRule]
    ) -> bool:
        if isinstance(disabled_case, bool):
            return disabled_case
        return disabled_case(self, state)

    def elevator(self, state: CollectionState, destination: Elevator) -> bool:
        if not self._has(state, KeyItem.ASCENDANT_KEY):
            return False
        if self.options.free_apex_elevator and destination == Elevator.APEX:
            return True
        return bool(self.options.randomize_elevator) and self._has(state, destination)

    def cheap_shop(self, state: CollectionState) -> bool:
        # TODO
        return self.region(R.GT_LEFT).can_reach(state)

    def moderate_shop(self, state: CollectionState) -> bool:
        # TODO
        return self.region(R.MECH_START).can_reach(state)

    def expensive_shop(self, state: CollectionState) -> bool:
        # TODO
        return self.region(R.ROA_START).can_reach(state)

    @lru_cache(maxsize=None)
    def _easy_rando_can(self, state: CollectionState, logic: Logic, gold_block=False) -> bool:
        if logic == Logic.ARIAS_JUMP:
            return False
        if logic == Logic.EXTRA_HEIGHT:
            return self.has_any(state, Character.KYULI, KeyItem.BLOCK) or (
                gold_block and self.has(state, Character.ZEEK)
            )
        if logic == Logic.COMBO_HEIGHT:
            return False
        if logic == Logic.BLOCK_IN_WALL:
            return False
        if logic == Logic.CRYSTAL:
            return self.has(state, Character.ALGUS) or self.has(state, Character.ZEEK, KeyItem.BANISH)
        if logic == Logic.BIG_MAGIC:
            return False

    @lru_cache(maxsize=None)
    def _hard_rando_can(self, state: CollectionState, logic: Logic, gold_block=False) -> bool:
        if logic == Logic.ARIAS_JUMP:
            return self.has(state, Character.ARIAS)
        if logic == Logic.EXTRA_HEIGHT:
            return (
                self.has_any(state, Character.KYULI, KeyItem.BLOCK)
                or (gold_block and self.has(state, Character.ZEEK))
                or self.can(state, Logic.ARIAS_JUMP)
            )
        if logic == Logic.COMBO_HEIGHT:
            return self.can(state, Logic.ARIAS_JUMP) and self.has(state, KeyItem.BELL, KeyItem.BLOCK)
        if logic == Logic.BLOCK_IN_WALL:
            return self.has(state, KeyItem.BLOCK) or (gold_block and self.has(state, Character.ZEEK))
        if logic == Logic.CRYSTAL:
            return self.has_any(state, Character.ALGUS, ShopUpgrade.KYULI_RAY, ShopUpgrade.BRAM_WHIPLASH) or self.has(
                state, Character.ZEEK, KeyItem.BANISH
            )
        if logic == Logic.BIG_MAGIC:
            return self.has(state, KeyItem.BANISH, ShopUpgrade.ALGUS_ARCANIST)

    @lru_cache(maxsize=None)
    def _easy_vanilla_can(self, state: CollectionState, logic: Logic, gold_block=False) -> bool:
        if logic == Logic.ARIAS_JUMP:
            return False
        if logic == Logic.EXTRA_HEIGHT:
            return True
        if logic == Logic.COMBO_HEIGHT:
            return False
        if logic == Logic.BLOCK_IN_WALL:
            return False
        if logic == Logic.CRYSTAL:
            return True
        if logic == Logic.BIG_MAGIC:
            return False

    @lru_cache(maxsize=None)
    def _hard_vanilla_can(self, state: CollectionState, logic: Logic, gold_block=False) -> bool:
        if logic == Logic.ARIAS_JUMP:
            return True
        if logic == Logic.EXTRA_HEIGHT:
            return True
        if logic == Logic.COMBO_HEIGHT:
            return self.has(state, KeyItem.BELL, KeyItem.BLOCK)
        if logic == Logic.BLOCK_IN_WALL:
            return self.has(state, KeyItem.BLOCK) or (gold_block and self.has(state, Character.ZEEK))
        if logic == Logic.CRYSTAL:
            return True
        if logic == Logic.BIG_MAGIC:
            return self.has(state, KeyItem.BANISH, ShopUpgrade.ALGUS_ARCANIST)

    def reachable(self, state: CollectionState, location: L) -> bool:
        data = location_table[location]
        if not self.region(data.region).can_reach(state):
            return False
        all_rules = (
            ITEM_RULES,
            ATTACK_RULES,
            HEALTH_RULES,
            WHITE_KEY_RULES,
            BLUE_KEY_RULES,
            RED_KEY_RULES,
            SHOP_RULES,
            SWITCH_RULES,
        )
        for rules in all_rules:
            if location in rules:
                return rules[location](self, state)
        return True

    def register_indirect_condition(self, dependency: Union[L, R], from_region: R, to_region: R):
        if isinstance(dependency, L):
            data = location_table[dependency]
            if data.group == LocationGroups.KEY_RED and self.options.randomize_red_keys:
                return
            if data.group == LocationGroups.SWITCH and self.options.randomize_switches:
                return
            region = self.region(data.region)
        else:
            region = self.region(dependency)

        entrance = self.entrance(from_region, to_region)
        self.world.multiworld.register_indirect_condition(region, entrance)

    @cached_property
    def easy(self):
        return self.options.difficulty >= Difficulty.option_easy

    @cached_property
    def hard(self):
        return self.options.difficulty >= Difficulty.option_hard

    def clear_cache(self):
        self.can.cache_clear()  # type: ignore
        self._has.cache_clear()  # type: ignore

    def set_region_rules(self) -> None:
        for (from_, to_), rule in ENTRANCE_RULES.items():
            set_rule(self.entrance(from_, to_), partial(rule, self))

    def set_location_rules(self) -> None:
        for location, rule in ITEM_RULES.items():
            set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_attack_pickups:
            for location, rule in ATTACK_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_health_pickups:
            for location, rule in HEALTH_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_white_keys:
            for location, rule in WHITE_KEY_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_blue_keys:
            for location, rule in BLUE_KEY_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_red_keys:
            for location, rule in RED_KEY_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_shop:
            for location, rule in SHOP_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_switches:
            for location, rule in SWITCH_RULES.items():
                set_rule(self.location(location), partial(rule, self))

        if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
            for event, rule in EVENT_RULES.items():
                set_rule(self.location(event), partial(rule, self))
        else:
            for (character, location), rule in CHARACTER_RULES.items():
                if character not in self.world.starting_characters:
                    set_rule(self.location(location), partial(rule, self))

    def set_indirect_conditions(self) -> None:
        for dependency, (from_, to_) in INDIRECT_CONDITIONS:
            self.register_indirect_condition(dependency, from_, to_)
