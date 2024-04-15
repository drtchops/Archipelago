from enum import Enum, auto
from functools import partial
from typing import TYPE_CHECKING, Callable, Dict, Tuple, Union

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import (
    CHARACTERS,
    BlueDoors,
    Characters,
    Elevators,
    KeyItems,
    RedDoors,
    ShopUpgrades,
    Switches,
    WhiteDoors,
)
from .Items import Items as I
from .Locations import Locations as L
from .Locations import location_table
from .Options import AstalonOptions, Difficulty, RandomizeCharacters
from .Regions import Regions as R

if TYPE_CHECKING:
    from . import AstalonWorld


class Logic(Enum):
    ARIAS_JUMP = auto()
    EXTRA_HEIGHT = auto()
    COMBO_HEIGHT = auto()
    BLOCK_IN_WALL = auto()
    CRYSTAL = auto()
    BIG_MAGIC = auto()


ENTRANCE_RULES: Dict[Tuple[R, R], Callable[["AstalonRules", CollectionState], bool]] = {
    (R.SHOP, R.SHOP_ALGUS): lambda rules, state: rules.has(state, I.ALGUS),
    (R.SHOP, R.SHOP_ARIAS): lambda rules, state: rules.has(state, I.ARIAS),
    (R.SHOP, R.SHOP_KYULI): lambda rules, state: rules.has(state, I.KYULI),
    (R.SHOP, R.SHOP_ZEEK): lambda rules, state: rules.has(state, I.ZEEK),
    (R.SHOP, R.SHOP_BRAM): lambda rules, state: rules.has(state, I.BRAM),
    (R.ENTRANCE, R.BESTIARY): lambda rules, state: rules.blue_doors(state, I.DOOR_BLUE_GT_HUNTER, disabled_case=True),
    (R.ENTRANCE, R.GT_BABY_GORGON): lambda rules, state: (
        rules.has(state, I.EYE_GREEN)
        and (
            rules.has(state, I.CLAW)
            or (
                rules.hard
                and rules.can(state, Logic.BLOCK_IN_WALL, gold_block=True)
                and (rules.has(state, I.KYULI, I.BELL) or rules.has(state, I.BLOCK))
            )
        )
    ),
    (R.ENTRANCE, R.GT_BOTTOM): lambda rules, state: (
        rules.switches(
            state,
            I.SWITCH_GT_2ND_ROOM,
            disabled_case=rules.white_doors(state, I.DOOR_WHITE_GT_START, disabled_case=True),
        )
    ),
    (R.ENTRANCE, R.GT_VOID): lambda rules, state: rules.has(state, I.VOID),
    (R.ENTRANCE, R.GT_GORGONHEART): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_GH_SHORTCUT, disabled_case=False) or rules.has_any(state, I.ICARUS, I.BOOTS)
    ),
    (R.ENTRANCE, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.ENTRANCE, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.ENTRANCE, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.ENTRANCE, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.ENTRANCE, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.ENTRANCE, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.ENTRANCE, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.ENTRANCE, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.ENTRANCE, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.ENTRANCE, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.GT_BOTTOM, R.GT_VOID): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.GT_BOTTOM, R.GT_GORGONHEART): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_GT_MAP, disabled_case=True)
    ),
    (R.GT_BOTTOM, R.GT_UPPER_PATH): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_ROTA, disabled_case=False)
        or rules.can(state, Logic.ARIAS_JUMP)
        or (rules.has(state, I.STAR) and rules.blue_doors(state, I.DOOR_BLUE_GT_RING, disabled_case=True))
    ),
    (R.GT_BOTTOM, R.CAVES_START): lambda rules, state: (
        rules.has(state, I.KYULI) or rules.can(state, Logic.BLOCK_IN_WALL, gold_block=True)
    ),
    (R.GT_VOID, R.GT_BOTTOM): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.GT_VOID, R.MECH_SNAKE): lambda rules, state: rules.switches(state, I.SWITCH_MECH_SNAKE_2, disabled_case=False),
    (R.GT_GORGONHEART, R.GT_BOTTOM): lambda *_: True,
    (R.GT_GORGONHEART, R.GT_ORBS_DOOR): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_GT_ORBS, disabled_case=True)
    ),
    (R.GT_GORGONHEART, R.GT_LEFT): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_CROSSES, disabled_case=False)
        or rules.switches(state, I.SWITCH_GT_1ST_CYCLOPS, disabled_case=True)
    ),
    (R.GT_LEFT, R.GT_GORGONHEART): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_CROSSES, disabled_case=True)
        or rules.switches(state, I.SWITCH_GT_1ST_CYCLOPS, disabled_case=False)
    ),
    (R.GT_LEFT, R.GT_ORBS_HEIGHT): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.GT_LEFT, R.GT_ASCENDANT_KEY): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_GT_ASCENDANT, disabled_case=True)
    ),
    (R.GT_LEFT, R.GT_TOP_LEFT): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_ARIAS, disabled_case=False)
        or rules.has_any(state, I.ARIAS, I.CLAW)
        or rules.has(state, I.BLOCK, I.KYULI, I.BELL)
    ),
    (R.GT_LEFT, R.GT_TOP_RIGHT): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.GT_TOP_LEFT, R.GT_LEFT): lambda *_: True,
    (R.GT_TOP_LEFT, R.GT_BUTT): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_BUTT_ACCESS, disabled_case=rules.reachable(state, L.GT_SWITCH_BUTT_ACCESS))
    ),
    (R.GT_TOP_RIGHT, R.GT_LEFT): lambda *_: True,
    (R.GT_TOP_RIGHT, R.GT_SPIKE_TUNNEL): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_SPIKE_TUNNEL, disabled_case=rules.reachable(L.GT_SWITCH_SPIKE_TUNNEL))
    ),
    (R.GT_SPIKE_TUNNEL, R.GT_TOP_RIGHT): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_SPIKE_TUNNEL, disabled_case=False)
    ),
    (R.GT_SPIKE_TUNNEL, R.GT_BUTT): lambda rules, state: (
        rules.can(state, Logic.EXTRA_HEIGHT) and rules.has(state, I.STAR, I.BELL)
    ),
    (R.GT_BUTT, R.GT_TOP_LEFT): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_BUTT_ACCESS, disabled_case=False)
    ),
    (R.GT_BUTT, R.GT_SPIKE_TUNNEL): lambda rules, state: rules.has(state, I.STAR),
    (R.GT_BUTT, R.GT_BOSS): lambda rules, state: rules.white_doors(state, I.DOOR_WHITE_GT_TAUROS, disabled_case=True),
    (R.GT_BOSS, R.GT_BUTT): lambda rules, state: rules.white_doors(state, I.DOOR_WHITE_GT_TAUROS, disabled_case=False),
    (R.GT_BOSS, R.MECH_START): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.GT_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.GT_BOSS, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.GT_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.GT_BOSS, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.GT_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.GT_BOSS, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.GT_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.GT_BOSS, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.GT_BOSS, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.GT_UPPER_ARIAS, R.GT_OLD_MAN_FORK): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_GT_LADDER, disabled_case=rules.reachable(L.GT_CRYSTAL_LADDER))
    ),
    (R.GT_UPPER_ARIAS, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.has(state, I.ARIAS)
        or rules.switches(state, I.SWITCH_GT_UPPER_ARIAS, disabled_case=rules.reachable(L.GT_SWITCH_UPPER_ARIAS))
    ),
    (R.GT_OLD_MAN_FORK, R.GT_UPPER_ARIAS): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_GT_LADDER, disabled_case=rules.reachable(L.GT_CRYSTAL_LADDER))
    ),
    (R.GT_OLD_MAN_FORK, R.GT_SWORD_FORK): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_GT_SWORD, disabled_case=True)
    ),
    (R.GT_OLD_MAN_FORK, R.GT_OLD_MAN): lambda rules, state: (
        # TODO: you don't need both switches, revist when adding old man
        rules.has(state, I.CLAW)
        or rules.switches(
            state, I.CRYSTAL_GT_OLD_MAN_1, I.CRYSTAL_GT_OLD_MAN_2, disabled_case=rules.can(state, Logic.CRYSTAL)
        )
    ),
    (R.GT_SWORD_FORK, R.GT_SWORD): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_SWORD_ACCESS, disabled_case=True)
    ),
    (R.GT_SWORD_FORK, R.GT_ARIAS_SWORD_SWITCH): lambda rules, state: (
        rules.has(state, I.SWORD) or rules.has(state, I.BOW, I.BELL)
    ),
    (R.GT_UPPER_PATH, R.GT_UPPER_PATH_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_UPPER_PATH_ACCESS, disabled_case=False)
    ),
    (R.GT_UPPER_PATH, R.GT_BOTTOM): lambda *_: True,
    (R.GT_UPPER_PATH_CONNECTION, R.GT_UPPER_PATH): lambda rules, state: (
        rules.switches(state, I.SWITCH_GT_UPPER_PATH_ACCESS, disabled_case=True)
    ),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.MECH_START, R.GT_LADDER_SWITCH): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.MECH_START, R.MECH_BK): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_SHORTCUT, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_START, R.MECH_WATCHER): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_CANNON, disabled_case=rules.can(state, Logic.CRYSTAL))
        and rules.white_doors(state, I.DOOR_WHITE_MECH_2ND, disabled_case=True)
    ),
    (R.MECH_START, R.MECH_LINUS): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_MECH_LINUS, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_START, R.MECH_LOWER_VOID): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_VOID, disabled_case=True)
    ),
    (R.MECH_START, R.MECH_SACRIFICE): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.MECH_START, R.GT_BOSS): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.MECH_LINUS, R.MECH_START): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_MECH_LINUS, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_LINUS, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_LINUS, disabled_case=True)
    ),
    (R.MECH_SWORD_CONNECTION, R.MECH_BOOTS_CONNECTION): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_BOOTS, disabled_case=True)
        and (
            rules.switches(state, I.CRYSTAL_MECH_LOWER, disabled_case=rules.can(state, Logic.CRYSTAL))
            and (rules.has_any(state, I.CLAW, I.CLOAK) or rules.has(state, I.KYULI, I.ICARUS))
        )
    ),
    (R.MECH_SWORD_CONNECTION, R.GT_UPPER_PATH_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.MECH_SWORD_CONNECTION, R.MECH_LOWER_ARIAS): lambda rules, state: rules.has(state, I.ARIAS),
    (R.MECH_SWORD_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_UPPER_GT, disabled_case=False)
    ),
    (R.MECH_SWORD_CONNECTION, R.MECH_LINUS): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_LINUS, disabled_case=False)
    ),
    (R.MECH_SWORD_CONNECTION, R.GT_UPPER_ARIAS): lambda rules, state: (
        rules.has(state, I.ARIAS) or rules.switches(state, I.SWITCH_GT_UPPER_ARIAS, disabled_case=False)
    ),
    (R.MECH_BOOTS_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_VOID, disabled_case=True)
    ),
    (R.MECH_BOOTS_CONNECTION, R.MECH_SWORD_CONNECTION): lambda *_: True,
    (R.MECH_BOOTS_CONNECTION, R.MECH_BOOTS_LOWER): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_BOOTS, disabled_case=rules.has_any(state, I.EYE_RED, I.STAR))
    ),
    (R.MECH_BOOTS_LOWER, R.MECH_BOOTS_UPPER): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_BOOTS_LOWER, disabled_case=True) or rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.GT_UPPER_PATH_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_UPPER_GT, disabled_case=True)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_BOOTS_CONNECTION): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_VOID, disabled_case=True)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_SNAKE): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_SNAKE_1, disabled_case=True)
    ),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_SWORD_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_UPPER_GT, disabled_case=True)
    ),
    (R.MECH_SNAKE, R.MECH_BOTTOM_CAMPFIRE): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_SNAKE_1, disabled_case=False)
    ),
    (R.MECH_SNAKE, R.GT_VOID): lambda rules, state: rules.switches(state, I.SWITCH_MECH_SNAKE_2, disabled_case=True),
    (R.MECH_LOWER_VOID, R.MECH_START): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_VOID, disabled_case=True)
    ),
    (R.MECH_LOWER_VOID, R.MECH_UPPER_VOID): lambda rules, state: rules.has(state, I.VOID),
    (R.MECH_LOWER_VOID, R.HOTP_MECH_VOID_CONNECTION): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.MECH_WATCHER, R.MECH_START): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_CANNON, disabled_case=False)
        and rules.white_doors(state, I.DOOR_WHITE_MECH_2ND, disabled_case=True)
    ),
    (R.MECH_WATCHER, R.MECH_ROOTS): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.switches(state, I.SWITCH_MECH_WATCHER, disabled_case=True)
    ),
    (R.MECH_ROOTS, R.MECH_WATCHER): lambda *_: True,
    (R.MECH_ROOTS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.has(state, I.CLAW, I.BLOCK, I.BELL),
    (R.MECH_ROOTS, R.MECH_BK): lambda *_: True,
    (R.MECH_ROOTS, R.MECH_MUSIC): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_MUSIC, disabled_case=True)
    ),
    (R.MECH_BK, R.MECH_START): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_MECH_SHORTCUT, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_BK, R.MECH_AFTER_BK): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_MECH_BK, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_BK, R.MECH_ROOTS): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_MECH_CAMPFIRE, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_AFTER_BK, R.MECH_CHAINS): lambda rules, state: (
        rules.has(state, I.CLAW)
        or rules.white_doors(state, I.DOOR_WHITE_MECH_BK, disabled_case=True)
        or rules.switches(state, I.SWITCH_MECH_CHAINS, disabled_case=False)
    ),
    (R.MECH_AFTER_BK, R.MECH_BK): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_MECH_BK, disabled_case=(rules.hard and rules.has(state, I.KYULI_RAY)))
    ),
    (R.MECH_AFTER_BK, R.HOTP_EPIMETHEUS): lambda rules, state: rules.has(state, I.CLAW),
    (R.MECH_CHAINS, R.MECH_ARIAS_EYEBALL): lambda rules, state: rules.has(state, I.ARIAS),
    (R.MECH_CHAINS, R.MECH_SPLIT_PATH): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_SPLIT_PATH, disabled_case=True)
    ),
    (R.MECH_CHAINS, R.MECH_BOSS_SWITCHES): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_BOSS_1, disabled_case=False)
    ),
    (R.MECH_CHAINS, R.MECH_BOSS_CONNECTION): lambda rules, state: (
        rules.has(state, I.CLAW)
        or rules.switches(
            state,
            I.CRYSTAL_MECH_TO_BOSS_3,
            disabled_case=(rules.hard and (rules.can(state, Logic.BIG_MAGIC) or rules.has(state, I.KYULI_RAY))),
        )
    ),
    (R.MECH_CHAINS, R.MECH_AFTER_BK): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.switches(state, I.SWITCH_MECH_CHAINS, disabled_case=True)
    ),
    (R.MECH_ARIAS_EYEBALL, R.MECH_ZEEK_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_ARIAS, disabled_case=True) or rules.has(state, I.STAR, I.BELL)
    ),
    (R.MECH_ARIAS_EYEBALL, R.MECH_CHAINS): lambda rules, state: (
        rules.has(state, I.ARIAS, I.BELL)
        and rules.has_any(state, I.ALGUS, I.BRAM_WHIPLASH)
        and (rules.switches(state, I.SWITCH_MECH_ARIAS, disabled_case=False) or rules.has(state, I.STAR))
    ),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ARIAS_EYEBALL): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_ARIAS, disabled_case=False) or rules.has(state, I.STAR)
    ),
    (R.MECH_ZEEK_CONNECTION, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.MECH_ZEEK_CONNECTION, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ROOTS): lambda *_: True,
    (R.MECH_ZEEK_CONNECTION, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.MECH_ZEEK_CONNECTION, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.MECH_ZEEK_CONNECTION, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.MECH_ZEEK_CONNECTION, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ZEEK): lambda rules, state: (
        rules.red_doors(state, I.DOOR_RED_ZEEK, disabled_case=rules.reachable(state, L.MECH_RED_KEY))
    ),
    (R.MECH_ZEEK_CONNECTION, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.MECH_ZEEK_CONNECTION, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.MECH_SPLIT_PATH, R.MECH_RIGHT): lambda *_: True,  # until skulls are included
    (R.MECH_SPLIT_PATH, R.MECH_CHAINS): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_SPLIT_PATH, disabled_case=False)
    ),
    (R.MECH_RIGHT, R.MECH_OLD_MAN): lambda rules, state: rules.can(state, Logic.CRYSTAL),
    (R.MECH_RIGHT, R.MECH_SPLIT_PATH): lambda rules, state: rules.has(state, I.STAR),
    (R.MECH_RIGHT, R.MECH_POTS): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_POTS, disabled_case=True)
        and (
            rules.white_doors(state, I.DOOR_WHITE_MECH_ARENA, disabled_case=True)
            or rules.switches(state, I.SWITCH_MECH_EYEBALL, disabled_case=False)
        )
    ),
    (R.MECH_RIGHT, R.MECH_UPPER_VOID): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_UPPER_VOID, disabled_case=False)
        or (rules.has(state, I.CLAW) and rules.switches(state, I.SWITCH_MECH_UPPER_VOID_DROP, disabled_case=True))
    ),
    (R.MECH_UPPER_VOID, R.MECH_RIGHT): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_UPPER_VOID, disabled_case=True)
    ),
    (R.MECH_UPPER_VOID, R.MECH_LOWER_VOID): lambda rules, state: rules.has(state, I.VOID),
    (R.MECH_POTS, R.MECH_RIGHT): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_POTS, disabled_case=False)
        and (
            rules.white_doors(state, I.DOOR_WHITE_MECH_ARENA, disabled_case=True)
            or rules.switches(state, I.SWITCH_MECH_EYEBALL, disabled_case=True)
        )
    ),
    (R.MECH_POTS, R.MECH_TOP): lambda rules, state: rules.switches(state, I.SWITCH_MECH_POTS, disabled_case=False),
    (R.MECH_TOP, R.MECH_POTS): lambda rules, state: rules.switches(state, I.SWITCH_MECH_POTS, disabled_case=False),
    (R.MECH_TOP, R.MECH_TP_CONNECTION): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.white_doors(state, I.DOOR_WHITE_MECH_TOP, disabled_case=True)
    ),
    (R.MECH_TOP, R.CD_START): lambda rules, state: (
        rules.has(state, I.CYCLOPS, I.EYE_BLUE) and rules.blue_doors(state, I.DOOR_BLUE_MECH_CD, disabled_case=True)
    ),
    (R.MECH_TP_CONNECTION, R.HOTP_FALL_BOTTOM): lambda rules, state: rules.has(state, I.CLAW),
    (R.MECH_TP_CONNECTION, R.MECH_TOP): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.white_doors(state, I.DOOR_WHITE_MECH_TOP, disabled_case=True)
    ),
    (R.MECH_TP_CONNECTION, R.MECH_CHARACTER_SWAPS): lambda rules, state: (
        rules.has(state, I.ARIAS) or rules.switches(state, I.SWITCH_MECH_ARIAS_CYCLOPS, disabled_case=False)
    ),
    (R.MECH_CHARACTER_SWAPS, R.MECH_CLOAK_CONNECTION): lambda rules, state: (
        rules.switches(
            state,
            I.CRYSTAL_MECH_TRIPLE_1,
            I.CRYSTAL_MECH_TRIPLE_2,
            I.CRYSTAL_MECH_TRIPLE_3,
            disabled_case=rules.can(state, Logic.CRYSTAL),
        )
        and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.MECH_CHARACTER_SWAPS, R.MECH_TP_CONNECTION): lambda rules, state: (
        rules.has(state, I.ARIAS) or rules.switches(state, I.SWITCH_MECH_ARIAS_CYCLOPS, disabled_case=True)
    ),
    (R.MECH_CLOAK_CONNECTION, R.MECH_BOSS_SWITCHES): lambda *_: True,
    (R.MECH_CLOAK_CONNECTION, R.MECH_CHARACTER_SWAPS): lambda rules, state: (
        rules.switches(
            state,
            I.CRYSTAL_MECH_TRIPLE_1,
            I.CRYSTAL_MECH_TRIPLE_2,
            I.CRYSTAL_MECH_TRIPLE_3,
            disabled_case=False,
        )
    ),
    (R.MECH_CLOAK_CONNECTION, R.MECH_CLOAK): lambda rules, state: (
        rules.has(state, I.EYE_BLUE)
        and rules.switches(state, I.CRYSTAL_MECH_CLOAK, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_BOSS_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_BOSS_1, I.SWITCH_MECH_TO_BOSS_2, disabled_case=True)
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_CLOAK_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_BLOCK_STAIRS, disabled_case=False)
        or rules.switches(state, I.CRYSTAL_MECH_SLIMES, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_CHAINS): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_TO_BOSS_1, disabled_case=True)
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_BOSS): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_BOSS_2, disabled_case=True)
        or (rules.has(state, I.BLOCK, I.BELL) and (rules.has(state, I.KYULI) or rules.can(state, Logic.ARIAS_JUMP)))
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_BRAM_TUNNEL): lambda rules, state: (
        rules.switches(state, I.SWITCH_MECH_BOSS_1, disabled_case=True) and rules.has(state, I.STAR)
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_CHAINS): lambda *_: True,
    (R.MECH_BRAM_TUNNEL, R.MECH_BOSS_CONNECTION): lambda rules, state: rules.has(state, I.STAR),
    (R.MECH_BRAM_TUNNEL, R.HOTP_START_BOTTOM): lambda rules, state: rules.has(state, I.STAR),
    (R.MECH_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.MECH_BOSS, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.MECH_BOSS, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.MECH_BOSS, R.MECH_BOSS_CONNECTION): lambda *_: True,
    (R.MECH_BOSS, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.MECH_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.MECH_BOSS, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.MECH_BOSS, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.MECH_BOSS, R.HOTP_START): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.MECH_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.MECH_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.HOTP_START, R.MECH_BOSS): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.HOTP_START, R.HOTP_START_BOTTOM): lambda rules, state: (
        rules.has(state, I.STAR)
        or (rules.white_doors(state, I.DOOR_WHITE_HOTP_START, disabled_case=True) and rules.has(state, I.EYE_BLUE))
    ),
    (R.HOTP_START, R.HOTP_START_MID): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_1ST_ROOM, disabled_case=True)
    ),
    (R.HOTP_START_MID, R.HOTP_START_LEFT): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_LEFT_3, disabled_case=True)
        or (
            rules.has(state, I.STAR)
            and rules.switches(state, I.SWITCH_HOTP_LEFT_1, I.SWITCH_HOTP_LEFT_2, disabled_case=True)
        )
    ),
    (R.HOTP_START_MID, R.HOTP_START_BOTTOM): lambda rules, state: (
        rules.has(state, I.STAR) and rules.switches(state, I.SWITCH_HOTP_GHOSTS, disabled_case=True)
    ),
    (R.HOTP_START_MID, R.HOTP_LOWER_VOID): lambda rules, state: rules.has_any(state, I.ALGUS, I.BRAM_WHIPLASH),
    (R.HOTP_START_MID, R.HOTP_START): lambda *_: True,
    (R.HOTP_LOWER_VOID, R.HOTP_START_MID): lambda *_: True,
    (R.HOTP_LOWER_VOID, R.HOTP_UPPER_VOID): lambda rules, state: rules.has(state, I.VOID, I.CLAW),
    (R.HOTP_START_LEFT, R.HOTP_ELEVATOR): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_LEFT_BACKTRACK, disabled_case=False)
    ),
    (R.HOTP_START_LEFT, R.HOTP_START_MID): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_LEFT_3, disabled_case=False)
        or (
            rules.has(state, I.STAR)
            and rules.switches(state, I.SWITCH_HOTP_LEFT_1, I.SWITCH_HOTP_LEFT_2, disabled_case=True)
        )
    ),
    (R.HOTP_START_BOTTOM, R.MECH_BRAM_TUNNEL): lambda rules, state: rules.has(state, I.STAR),
    (R.HOTP_START_BOTTOM, R.HOTP_START): lambda rules, state: (
        rules.has(state, I.STAR)
        or (rules.white_doors(state, I.DOOR_WHITE_HOTP_START, disabled_case=True) and rules.has(state, I.EYE_BLUE))
    ),
    (R.HOTP_START_BOTTOM, R.HOTP_LOWER): lambda rules, state: (
        rules.switches(
            state, I.SWITCH_HOTP_BELOW_START, disabled_case=rules.reachable(state, L.HOTP_SWITCH_BELOW_START)
        )
    ),
    (R.HOTP_LOWER, R.HOTP_START_BOTTOM): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_BELOW_START, disabled_case=False)
    ),
    (R.HOTP_LOWER, R.HOTP_EPIMETHEUS): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_HOTP_STATUE, disabled_case=True)
    ),
    (R.HOTP_LOWER, R.HOTP_TP_TUTORIAL): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_HOTP_LOWER, disabled_case=rules.can(state, Logic.CRYSTAL))
        or rules.switches(state, I.SWITCH_HOTP_LOWER_SHORTCUT, disabled_case=False)
    ),
    (R.HOTP_LOWER, R.HOTP_MECH_VOID_CONNECTION): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_HOTP_BOTTOM, disabled_case=(rules.hard and rules.has(state, I.KYULI_RAY)))
    ),
    (R.HOTP_EPIMETHEUS, R.MECH_AFTER_BK): lambda rules, state: rules.has(state, I.CLAW),
    (R.HOTP_EPIMETHEUS, R.HOTP_LOWER): lambda *_: True,
    (R.HOTP_MECH_VOID_CONNECTION, R.HOTP_AMULET_CONNECTION): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_HOTP_ROCK_ACCESS, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.HOTP_MECH_VOID_CONNECTION, R.MECH_LOWER_VOID): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.HOTP_MECH_VOID_CONNECTION, R.HOTP_LOWER): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_HOTP_BOTTOM, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.HOTP_AMULET_CONNECTION, R.HOTP_AMULET): lambda rules, state: rules.has(state, I.CLAW, I.EYE_RED, I.EYE_BLUE),
    (R.HOTP_AMULET_CONNECTION, R.GT_BUTT): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_ROCK, disabled_case=True)
    ),
    (R.HOTP_AMULET_CONNECTION, R.HOTP_MECH_VOID_CONNECTION): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_HOTP_ROCK_ACCESS, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.HOTP_TP_TUTORIAL, R.HOTP_BELL_CAMPFIRE): lambda *_: True,  # until skulls are included
    (R.HOTP_TP_TUTORIAL, R.HOTP_LOWER): lambda *_: True,
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_LOWER_ARIAS): lambda rules, state: (
        rules.has(state, I.ARIAS) and (rules.has(state, I.BELL) or rules.can(state, Logic.ARIAS_JUMP))
    ),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_RED_KEY): lambda rules, state: rules.has(state, I.EYE_GREEN, I.CLOAK),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_CATH_CONNECTION): lambda rules, state: rules.has(state, I.EYE_GREEN),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_TP_TUTORIAL): lambda *_: False,  # until skulls are included
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_BELL): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_BELL_ACCESS, disabled_case=True)
        and (
            rules.switches(state, I.CRYSTAL_HOTP_BELL_ACCESS, disabled_case=rules.can(state, Logic.CRYSTAL))
            or (rules.has(state, I.BELL, I.BLOCK) and (rules.has(state, I.KYULI) or rules.can(state, Logic.ARIAS_JUMP)))
            or (rules.hard and rules.has(state, I.CLAW))
        )
    ),
    (R.HOTP_CATH_CONNECTION, R.HOTP_BELL): lambda *_: True,
    (R.HOTP_CATH_CONNECTION, R.CATH_START): lambda rules, state: (
        rules.has(state, I.VOID, I.CLAW)
        and rules.red_doors(state, I.DOOR_RED_CATH, disabled_case=rules.reachable(state, L.HOTP_RED_KEY))
    ),
    (R.HOTP_LOWER_ARIAS, R.HOTP_BELL_CAMPFIRE): lambda rules, state: rules.has(state, I.ARIAS),
    (R.HOTP_LOWER_ARIAS, R.HOTP_EYEBALL): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_TELEPORTS, disabled_case=True)
        or (rules.has(state, I.BLOCK, I.BELL) and (rules.has(state, I.KYULI) or rules.can(state, Logic.ARIAS_JUMP)))
    ),
    (R.HOTP_EYEBALL, R.HOTP_ELEVATOR): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_EYEBALL_SHORTCUT, I.SWITCH_HOTP_WORM_PILLAR, disabled_case=False)
        or rules.switches(state, I.SWITCH_HOTP_GHOST_BLOOD, disabled_case=True)
    ),
    (R.HOTP_EYEBALL, R.HOTP_LOWER_ARIAS): lambda *_: True,
    (R.HOTP_ELEVATOR, R.HOTP_OLD_MAN): lambda rules, state: (
        rules.has(state, I.CLOAK) and rules.switches(state, I.FACE_HOTP_OLD_MAN, disabled_case=rules.has(state, I.BOW))
    ),
    (R.HOTP_ELEVATOR, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.HOTP_ELEVATOR, R.HOTP_TOP_LEFT): lambda rules, state: rules.has(state, I.CLAW),
    (R.HOTP_ELEVATOR, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.HOTP_ELEVATOR, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.HOTP_ELEVATOR, R.HOTP_START_LEFT): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_LEFT_BACKTRACK, disabled_case=True)
    ),
    (R.HOTP_ELEVATOR, R.HOTP_EYEBALL): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_EYEBALL_SHORTCUT, I.SWITCH_HOTP_WORM_PILLAR, disabled_case=True)
        or rules.switches(state, I.SWITCH_HOTP_GHOST_BLOOD, disabled_case=False)
    ),
    (R.HOTP_ELEVATOR, R.HOTP_CLAW_LEFT): lambda rules, state: (
        (rules.switches(state, I.SWITCH_HOTP_TO_CLAW_2, disabled_case=True) and rules.can(state, Logic.EXTRA_HEIGHT))
        or (rules.has(state, I.BELL) and (rules.has(state, I.CLAW, I.CLOAK) or rules.has(state, I.KYULI, I.BLOCK)))
    ),
    (R.HOTP_ELEVATOR, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.HOTP_ELEVATOR, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.HOTP_ELEVATOR, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.HOTP_ELEVATOR, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.HOTP_ELEVATOR, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.HOTP_ELEVATOR, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.HOTP_CLAW_LEFT, R.HOTP_ELEVATOR): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.HOTP_CLAW_LEFT, R.HOTP_TOP_LEFT): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_HOTP_CLAW, disabled_case=True)
    ),
    (R.HOTP_CLAW_LEFT, R.HOTP_CLAW): lambda rules, state: rules.has(state, I.STAR),
    (R.HOTP_TOP_LEFT, R.HOTP_ELEVATOR): lambda *_: True,
    (R.HOTP_TOP_LEFT, R.HOTP_CLAW_CAMPFIRE): lambda *_: True,  # until enemy arenas are included
    (R.HOTP_TOP_LEFT, R.HOTP_CLAW_LEFT): lambda *_: True,
    (R.HOTP_TOP_LEFT, R.HOTP_ABOVE_OLD_MAN): lambda rules, state: (
        rules.has(state, I.EYE_GREEN)
        and (
            rules.switches(state, I.SWITCH_HOTP_TO_ABOVE_OLD_MAN, disabled_case=True)
            or (rules.has(state, I.BLOCK, I.BELL) and rules.can(state, Logic.ARIAS_JUMP))
        )
    ),
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_TOP_LEFT): lambda *_: True,
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_CLAW): lambda rules, state: (
        rules.switches(state, I.SWITCH_HOTP_CLAW_ACCESS, disabled_case=True)
        and (rules.has(state, I.KYULI) or rules.can(state, Logic.BLOCK_IN_WALL))
    ),
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_HEART): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_HOTP_AFTER_CLAW, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.HOTP_CLAW, R.HOTP_CLAW_CAMPFIRE): lambda rules, state: (
        rules.has(state, I.CLAW) and rules.switches(state, I.SWITCH_HOTP_CLAW_ACCESS, disabled_case=False)
    ),
    (R.HOTP_CLAW, R.HOTP_CLAW_LEFT): lambda rules, state: rules.has(state, I.STAR),
    (R.HOTP_HEART, R.HOTP_CLAW_CAMPFIRE): lambda rules, state: (
        rules.switches(
            state,
            I.CRYSTAL_HOTP_AFTER_CLAW,
            disabled_case=(
                rules.hard
                and (rules.has(state, I.CLOAK) or rules.has(state, I.ALGUS, I.ICARUS) or rules.has(state, I.KYULI_RAY))
            ),
        )
    ),
    (R.HOTP_HEART, R.HOTP_UPPER_ARIAS): lambda rules, state: rules.has(state, I.ARIAS),
    (R.HOTP_HEART, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: (
        rules.has(state, I.CLAW)
        and (
            rules.has(state, I.ICARUS)
            or rules.has(state, I.BLOCK, I.BELL)
            or rules.switches(state, I.CRYSTAL_HOTP_HEART, disabled_case=False)
        )
    ),
    (R.HOTP_UPPER_ARIAS, R.HOTP_HEART): lambda *_: True,
    (R.HOTP_UPPER_ARIAS, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: rules.has(state, I.CLAW),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_MAIDEN): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_HOTP_MAIDEN, disabled_case=True)
        and (rules.has(state, I.SWORD) or rules.has(state, I.KYULI, I.BLOCK, I.BELL))
    ),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_HEART): lambda *_: True,
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_TP_PUZZLE): lambda rules, state: rules.has(state, I.EYE_GREEN),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_BOSS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_HOTP_BOSS, disabled_case=True)
    ),
    (R.HOTP_TP_PUZZLE, R.HOTP_TP_FALL_TOP): lambda rules, state: (
        rules.has(state, I.STAR) or rules.switches(state, I.SWITCH_HOTP_TP_PUZZLE, disabled_case=True)
    ),
    (R.HOTP_TP_FALL_TOP, R.HOTP_FALL_BOTTOM): lambda rules, state: rules.has(state, I.CLOAK),
    (R.HOTP_TP_FALL_TOP, R.HOTP_TP_PUZZLE): lambda rules, state: (
        rules.has(state, I.STAR) or rules.switches(state, I.SWITCH_HOTP_TP_PUZZLE, disabled_case=False)
    ),
    (R.HOTP_TP_FALL_TOP, R.HOTP_GAUNTLET_CONNECTION): lambda rules, state: rules.has(state, I.CLAW),
    (R.HOTP_TP_FALL_TOP, R.HOTP_BOSS_CAMPFIRE): lambda rules, state: (
        rules.has(state, I.KYULI) or (rules.has(state, I.BLOCK) and rules.can(state, Logic.COMBO_HEIGHT))
    ),
    (R.HOTP_GAUNTLET_CONNECTION, R.HOTP_GAUNTLET): lambda rules, state: rules.has(state, I.CLAW, I.BANISH, I.BELL),
    (R.HOTP_FALL_BOTTOM, R.HOTP_TP_FALL_TOP): lambda rules, state: rules.has(state, I.CLAW),
    (R.HOTP_FALL_BOTTOM, R.MECH_TP_CONNECTION): lambda *_: True,
    (R.HOTP_FALL_BOTTOM, R.HOTP_UPPER_VOID): lambda rules, state: rules.has(state, I.EYE_GREEN),
    (R.HOTP_UPPER_VOID, R.HOTP_FALL_BOTTOM): lambda rules, state: rules.has(state, I.EYE_GREEN),
    (R.HOTP_UPPER_VOID, R.HOTP_TP_FALL_TOP): lambda *_: True,
    (R.HOTP_UPPER_VOID, R.HOTP_LOWER_VOID): lambda rules, state: rules.has(state, I.VOID),
    (R.HOTP_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.HOTP_BOSS, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.HOTP_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.HOTP_BOSS, R.HOTP_BOSS_CAMPFIRE): lambda *_: True,
    (R.HOTP_BOSS, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.HOTP_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.HOTP_BOSS, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.HOTP_BOSS, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.HOTP_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.HOTP_BOSS, R.ROA_START): lambda *_: True,
    (R.HOTP_BOSS, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.ROA_START, R.HOTP_BOSS): lambda *_: True,
    (R.ROA_START, R.ROA_WORMS): lambda rules, state: (
        rules.switches(
            state,
            I.CRYSTAL_ROA_1ST_ROOM,
            # this should be more complicated
            disabled_case=(rules.has(state, I.BELL) and rules.can(state, Logic.CRYSTAL)),
        )
    ),
    (R.ROA_WORMS, R.ROA_HEARTS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_WORMS, disabled_case=True)
        and (rules.switches(state, I.SWITCH_ROA_AFTER_WORMS, disabled_case=True) or rules.has(state, I.STAR))
    ),
    (R.ROA_WORMS, R.ROA_START): lambda rules, state: rules.can(state, Logic.CRYSTAL),
    (R.ROA_WORMS, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: rules.has(state, I.CLAW),
    (R.ROA_HEARTS, R.ROA_BOTTOM_ASCEND): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_1ST_SHORTCUT, disabled_case=False)
    ),
    (R.ROA_HEARTS, R.ROA_SPIKE_CLIMB): lambda *_: True,  # until enemy arenas are included
    (R.ROA_HEARTS, R.ROA_WORMS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_WORMS, disabled_case=True)
        and (
            rules.switches(state, I.SWITCH_ROA_AFTER_WORMS, disabled_case=False)
            or (rules.has(state, I.STAR, I.BELL) and rules.can(state, Logic.EXTRA_HEIGHT))
        )
    ),
    (R.ROA_SPIKE_CLIMB, R.ROA_HEARTS): lambda *_: False,  # until enemy arenas are included
    (R.ROA_SPIKE_CLIMB, R.ROA_BOTTOM_ASCEND): lambda rules, state: rules.has(state, I.CLAW),
    (R.ROA_BOTTOM_ASCEND, R.ROA_HEARTS): lambda *_: True,
    (R.ROA_BOTTOM_ASCEND, R.ROA_SPIKE_CLIMB): lambda *_: True,
    (R.ROA_BOTTOM_ASCEND, R.ROA_TOP_ASCENT): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_ASCEND, disabled_case=True)
    ),
    (R.ROA_BOTTOM_ASCEND, R.ROA_TRIPLE_REAPER): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_ASCEND, disabled_case=True) or (rules.has(state, I.KYULI, I.BLOCK, I.BELL))
    ),
    (R.ROA_TRIPLE_REAPER, R.ROA_BOTTOM_ASCEND): lambda *_: True,
    (R.ROA_TRIPLE_REAPER, R.ROA_ARENA): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_ROA_3_REAPERS, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.ROA_ARENA, R.ROA_FLAMES_CONNECTION): lambda rules, state: rules.has(state, I.CLAW),
    (R.ROA_ARENA, R.ROA_TRIPLE_REAPER): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_ROA_3_REAPERS, disabled_case=False)
    ),
    (R.ROA_ARENA, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: rules.has(state, I.KYULI),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_ARIAS_BABY_GORGON): lambda rules, state: (
        rules.has(state, I.ARIAS)
        and rules.switches(state, I.CRYSTAL_ROA_BABY_GORGON, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_WORMS): lambda *_: True,
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_FLAMES_CONNECTION): lambda rules, state: rules.has(state, I.STAR, I.BELL),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_LOWER_VOID): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_LOWER_VOID, disabled_case=False)
    ),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_ARENA): lambda *_: False,  # until arenas are included
    (R.ROA_LOWER_VOID, R.ROA_UPPER_VOID): lambda rules, state: rules.has(state, I.VOID),
    (R.ROA_LOWER_VOID, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_LOWER_VOID, disabled_case=True)
    ),
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_FLAMES_CONNECTION): lambda *_: True,  # until arenas are included
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_FLAMES): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_BABY_GORGON, disabled_case=False)
        and rules.has(state, I.BLOCK, I.KYULI, I.BELL)
    ),
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: (
        rules.has(state, I.STAR)
        or (rules.has(state, I.ARIAS) and rules.switches(state, I.CRYSTAL_ROA_BABY_GORGON, disabled_case=False))
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_WORM_CLIMB): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_ROA_FLAMES, disabled_case=True) and rules.has(state, I.CLAW)
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_LEFT_ASCENT): lambda rules, state: (
        rules.switches(
            state,
            I.CRYSTAL_ROA_LEFT_ASCEND,
            disabled_case=(rules.can(state, Logic.CRYSTAL) and rules.has(state, I.BELL)),
        )
        and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_ARIAS_BABY_GORGON): lambda *_: True,
    (R.ROA_FLAMES_CONNECTION, R.ROA_ARENA): lambda *_: True,
    (R.ROA_FLAMES_CONNECTION, R.ROA_FLAMES): lambda rules, state: (
        rules.has(state, I.GAUNTLET, I.BELL) and rules.can(state, Logic.EXTRA_HEIGHT)
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_LOWER_VOID_CONNECTION): lambda rules, state: rules.has(state, I.STAR),
    (R.ROA_FLAMES, R.ROA_ARIAS_BABY_GORGON): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_BABY_GORGON, disabled_case=True)
    ),
    (R.ROA_WORM_CLIMB, R.ROA_FLAMES_CONNECTION): lambda *_: True,
    (R.ROA_WORM_CLIMB, R.ROA_RIGHT_BRANCH): lambda rules, state: rules.has(state, I.CLAW),
    (R.ROA_RIGHT_BRANCH, R.ROA_WORM_CLIMB): lambda *_: True,
    (R.ROA_RIGHT_BRANCH, R.ROA_MIDDLE): lambda rules, state: rules.has(state, I.STAR),
    (R.ROA_LEFT_ASCENT, R.ROA_FLAMES_CONNECTION): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_ROA_LEFT_ASCEND, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.ROA_LEFT_ASCENT, R.ROA_TOP_ASCENT): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_ASCEND_SHORTCUT, disabled_case=False)
    ),
    (R.ROA_TOP_ASCENT, R.ROA_TRIPLE_SWITCH): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_TOP_ASCENT, R.ROA_LEFT_ASCENT): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_ASCEND_SHORTCUT, disabled_case=False)
    ),
    (R.ROA_TRIPLE_SWITCH, R.ROA_MIDDLE): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_TRIPLE_1, I.SWITCH_ROA_TRIPLE_3, disabled_case=False)
        and rules.has(state, I.CLAW, I.BELL)
    ),
    (R.ROA_TRIPLE_SWITCH, R.ROA_TOP_ASCENT): lambda rules, state: (
        rules.switches(
            state,
            I.SWITCH_ROA_TRIPLE_1,
            I.CRYSTAL_ROA_TRIPLE_2,
            I.SWITCH_ROA_TRIPLE_3,
            disabled_case=rules.can(state, Logic.CRYSTAL),
        )
    ),
    (R.ROA_MIDDLE, R.ROA_LEFT_SWITCH): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_MIDDLE, R.ROA_RIGHT_BRANCH): lambda rules, state: rules.has(state, I.STAR),
    (R.ROA_MIDDLE, R.ROA_RIGHT_SWITCH_1): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.switches(state, I.SWITCH_ROA_RIGHT_PATH, disabled_case=False)
    ),
    (R.ROA_MIDDLE, R.ROA_MIDDLE_LADDER): lambda rules, state: (
        # this could allow more
        rules.reachable(state, L.ROA_CRYSTAL_LADDER_L) and rules.reachable(state, L.ROA_CRYSTAL_LADDER_R)
    ),
    (R.ROA_MIDDLE, R.ROA_TRIPLE_SWITCH): lambda *_: True,
    (R.ROA_MIDDLE, R.ROA_LEFT_BABY_GORGON): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_RIGHT_SWITCH_1, R.ROA_RIGHT_SWITCH_2): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_MIDDLE_LADDER, R.ROA_MIDDLE): lambda *_: True,
    (R.ROA_MIDDLE_LADDER, R.ROA_UPPER_VOID): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_SHAFT_L, I.SWITCH_ROA_SHAFT_R, disabled_case=True)
    ),
    (R.ROA_UPPER_VOID, R.ROA_MIDDLE_LADDER): lambda *_: True,
    (R.ROA_UPPER_VOID, R.ROA_LOWER_VOID): lambda rules, state: rules.has(state, I.VOID),
    (R.ROA_UPPER_VOID, R.ROA_SP_CONNECTION): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_ROA_SHAFT, I.SWITCH_ROA_SHAFT_DOWNWARDS, disabled_case=False)
    ),
    (R.ROA_UPPER_VOID, R.ROA_SPIKE_BALLS): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_ROA_SPIKE_BALLS, disabled_case=rules.can(state, Logic.CRYSTAL))
    ),
    (R.ROA_SPIKE_BALLS, R.ROA_SPIKE_SPINNERS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_BALLS, disabled_case=True)
    ),
    (R.ROA_SPIKE_BALLS, R.ROA_UPPER_VOID): lambda *_: True,
    (R.ROA_SPIKE_SPINNERS, R.ROA_SPIDERS_1): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_SPINNERS, disabled_case=True)
    ),
    (R.ROA_SPIKE_SPINNERS, R.ROA_SPIKE_BALLS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_BALLS, disabled_case=True)
    ),
    (R.ROA_SPIDERS_1, R.ROA_RED_KEY): lambda rules, state: (
        rules.switches(state, I.FACE_ROA_SPIDERS, disabled_case=rules.has(state, I.BOW))
    ),
    (R.ROA_SPIDERS_1, R.ROA_SPIDERS_2): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.ROA_SPIDERS_1, R.ROA_SPIKE_SPINNERS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_ROA_SPINNERS, disabled_case=True)
    ),
    (R.ROA_SPIDERS_2, R.ROA_SPIDERS_1): lambda *_: True,
    (R.ROA_SPIDERS_2, R.ROA_BLOOD_POT_HALLWAY): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_SPIDERS, disabled_case=True)
    ),
    (R.ROA_BLOOD_POT_HALLWAY, R.ROA_SP_CONNECTION): lambda *_: True,  # until arenas are included
    (R.ROA_BLOOD_POT_HALLWAY, R.ROA_SPIDERS_2): lambda *_: True,
    (R.ROA_SP_CONNECTION, R.ROA_BLOOD_POT_HALLWAY): lambda *_: True,
    (R.ROA_SP_CONNECTION, R.SP_START): lambda rules, state: (
        rules.red_doors(state, I.DOOR_RED_SP, disabled_case=rules.reachable(state, L.ROA_RED_KEY))
    ),
    (R.ROA_SP_CONNECTION, R.ROA_ELEVATOR): lambda rules, state: (
        # can probably make it without claw
        rules.has(state, I.CLAW) and rules.switches(state, I.SWITCH_ROA_DARK_ROOM, disabled_case=True)
    ),
    (R.ROA_SP_CONNECTION, R.ROA_UPPER_VOID): lambda *_: True,
    (R.ROA_ELEVATOR, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.ROA_ELEVATOR, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.ROA_ELEVATOR, R.ROA_SP_CONNECTION): lambda *_: True,
    (R.ROA_ELEVATOR, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.ROA_ELEVATOR, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.ROA_ELEVATOR, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.ROA_ELEVATOR, R.ROA_ICARUS): lambda rules, state: rules.switches(state, I.SWITCH_ROA_ICARUS, disabled_case=True),
    (R.ROA_ELEVATOR, R.ROA_DARK_CONNECTION): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.switches(state, I.SWITCH_ROA_ELEVATOR, disabled_case=True)
    ),
    (R.ROA_ELEVATOR, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.ROA_ELEVATOR, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.ROA_ELEVATOR, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.ROA_ELEVATOR, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.ROA_DARK_CONNECTION, R.ROA_ELEVATOR): lambda *_: True,
    (R.ROA_DARK_CONNECTION, R.ROA_CENTAUR): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_BLOOD_POT, disabled_case=False)
    ),
    (R.ROA_DARK_CONNECTION, R.DARK_START): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.DARK_START, R.DARK_END): lambda rules, state: (
        rules.has(state, I.CLAW) and rules.switches(state, I.SWITCH_DARKNESS, disabled_case=True)
    ),
    (R.DARK_END, R.ROA_CENTAUR): lambda rules, state: rules.has(state, I.CLAW),
    (R.ROA_CENTAUR, R.ROA_DARK_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_BLOOD_POT, disabled_case=True)
        or rules.blue_doors(state, I.DOOR_BLUE_ROA_BLOOD, disabled_case=True)
    ),
    (R.ROA_CENTAUR, R.ROA_BOSS_CONNECTION): lambda rules, state: (
        rules.switches(
            state,
            I.CRYSTAL_ROA_CENTAUR,
            disabled_case=(
                rules.has(state, I.BELL, I.ARIAS) and (rules.can(state, Logic.CRYSTAL) or rules.has(state, I.STAR))
            ),
        )
    ),
    (R.ROA_BOSS_CONNECTION, R.ROA_BOSS): lambda rules, state: (
        rules.switches(state, I.CRYSTAL_ROA_CENTAUR, disabled_case=False)
        or (rules.has(state, I.BELL, I.STAR, I.ARIAS) and rules.can(state, Logic.EXTRA_HEIGHT))
    ),
    (R.ROA_BOSS_CONNECTION, R.ROA_CENTAUR): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_BOSS_ACCESS, disabled_case=False)
    ),
    (R.ROA_BOSS, R.ROA_APEX_CONNECTION): lambda rules, state: rules.has(state, I.EYE_GREEN),
    (R.ROA_BOSS, R.ROA_BOSS_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_BOSS_ACCESS, disabled_case=False)
    ),
    (R.ROA_APEX_CONNECTION, R.ROA_BOSS): lambda rules, state: rules.has(state, I.EYE_GREEN),
    (R.ROA_APEX_CONNECTION, R.APEX): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_APEX_ACCESS, disabled_case=True)
    ),
    (R.APEX, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.APEX, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.APEX, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.APEX, R.FINAL_BOSS): lambda rules, state: rules.has(state, I.EYE_RED, I.EYE_BLUE, I.EYE_GREEN, I.BELL),
    (R.APEX, R.ROA_APEX_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_ROA_APEX_ACCESS, disabled_case=False)
    ),
    (R.APEX, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.APEX, R.APEX_HEART): lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    (R.APEX, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.APEX, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.APEX, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.APEX, R.APEX_CENTAUR): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_APEX, disabled_case=True) and rules.has(state, I.STAR, I.ADORNED_KEY)
    ),
    (R.APEX, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.APEX, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.CAVES_START, R.CAVES_EPIMETHEUS): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_CAVES, disabled_case=True)
    ),
    (R.CAVES_START, R.GT_BOTTOM): lambda *_: True,
    (R.CAVES_EPIMETHEUS, R.CAVES_UPPER): lambda rules, state: (
        rules.has(state, I.CLAW) or rules.can(state, Logic.BLOCK_IN_WALL) or rules.can(state, Logic.COMBO_HEIGHT)
    ),
    (R.CAVES_EPIMETHEUS, R.CAVES_START): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_CAVES, disabled_case=True)
    ),
    (R.CAVES_UPPER, R.CAVES_EPIMETHEUS): lambda *_: True,
    (R.CAVES_UPPER, R.CAVES_ARENA): lambda rules, state: rules.has_any(state, I.SWORD, I.ALGUS_METEOR, I.KYULI_RAY),
    (R.CAVES_UPPER, R.CAVES_LOWER): lambda rules, state: (
        rules.switches(state, I.SWITCH_CAVES_SKELETONS, disabled_case=True)
    ),
    (R.CAVES_LOWER, R.CAVES_UPPER): lambda rules, state: (
        rules.switches(state, I.SWITCH_CAVES_SKELETONS, disabled_case=False)
    ),
    (R.CAVES_LOWER, R.CAVES_ITEM_CHAIN): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.CAVES_LOWER, R.CATA_START): lambda rules, state: (
        rules.switches(state, I.SWITCH_CAVES_CATA_1, I.SWITCH_CAVES_CATA_2, I.SWITCH_CAVES_CATA_3, disabled_case=True)
    ),
    (R.CATA_START, R.CATA_CLIMBABLE_ROOT): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_1ST_ROOM, disabled_case=True)
    ),
    (R.CATA_START, R.CAVES_LOWER): lambda rules, state: (
        rules.switches(state, I.SWITCH_CAVES_CATA_1, I.SWITCH_CAVES_CATA_2, I.SWITCH_CAVES_CATA_3, disabled_case=False)
    ),
    (R.CATA_CLIMBABLE_ROOT, R.CATA_TOP): lambda rules, state: (
        rules.has(state, I.EYE_RED) and rules.white_doors(state, I.DOOR_WHITE_CATA_TOP, disabled_case=True)
    ),
    (R.CATA_TOP, R.CATA_CLIMBABLE_ROOT): lambda rules, state: (
        rules.has(state, I.EYE_RED) and rules.white_doors(state, I.DOOR_WHITE_CATA_TOP, disabled_case=True)
    ),
    (R.CATA_TOP, R.CATA_ELEVATOR): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_ELEVATOR, disabled_case=True)
    ),
    (R.CATA_TOP, R.CATA_BOW_CAMPFIRE): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_TOP, disabled_case=True)
    ),
    (R.CATA_ELEVATOR, R.CATA_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_2),
    (R.CATA_ELEVATOR, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.CATA_ELEVATOR, R.TR_START): lambda rules, state: rules.elevator(state, I.ELEVATOR_TR),
    (R.CATA_ELEVATOR, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.CATA_ELEVATOR, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.CATA_ELEVATOR, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.CATA_ELEVATOR, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.CATA_ELEVATOR, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.CATA_ELEVATOR, R.CATA_TOP): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_ELEVATOR, disabled_case=False)
    ),
    (R.CATA_ELEVATOR, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.CATA_BOW_CAMPFIRE, R.CATA_TOP): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_TOP, disabled_case=False)
    ),
    (R.CATA_BOW_CAMPFIRE, R.CATA_BOW_CONNECTION): lambda rules, state: (
        rules.has(state, I.KYULI) and rules.blue_doors(state, I.DOOR_BLUE_CATA_SAVE, disabled_case=True)
    ),
    (R.CATA_BOW_CAMPFIRE, R.CATA_EYEBALL_BONES): lambda rules, state: (
        rules.switches(state, I.FACE_CATA_AFTER_BOW, disabled_case=rules.has(state, I.BOW))
    ),
    (R.CATA_BOW_CONNECTION, R.CATA_BOW): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_CATA_BOW, disabled_case=True)
    ),
    (R.CATA_BOW_CONNECTION, R.CATA_BOW_CAMPFIRE): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_CATA_SAVE, disabled_case=True)
    ),
    (R.CATA_BOW_CONNECTION, R.CATA_VERTICAL_SHORTCUT): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_VERTICAL_SHORTCUT, disabled_case=False)
    ),
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_BLUE_EYE_DOOR): lambda *_: True,
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_FLAMES_FORK): lambda *_: True,
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_BOW_CONNECTION): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_VERTICAL_SHORTCUT, disabled_case=True)
    ),
    (R.CATA_EYEBALL_BONES, R.CATA_SNAKE_MUSHROOMS): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.CATA_EYEBALL_BONES, R.CATA_BOW_CAMPFIRE): lambda *_: True,
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_DEV_ROOM_CONNECTION): lambda rules, state: rules.has(state, I.CLAW, I.BELL, I.ZEEK),
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_EYEBALL_BONES): lambda rules, state: rules.has(state, I.EYE_RED),
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_DOUBLE_SWITCH): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_CLAW_2, disabled_case=True)
        and (rules.has(state, I.CLAW) or rules.has(state, I.KYULI, I.ZEEK, I.BELL))
    ),
    (R.CATA_DEV_ROOM_CONNECTION, R.CATA_DEV_ROOM): lambda rules, state: (
        rules.red_doors(state, I.DOOR_RED_DEV_ROOM, disabled_case=rules.reachable(state, L.TR_RED_KEY))
    ),
    (R.CATA_DOUBLE_SWITCH, R.CATA_SNAKE_MUSHROOMS): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_CLAW_2, disabled_case=False)
    ),
    (R.CATA_DOUBLE_SWITCH, R.CATA_ROOTS_CAMPFIRE): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_WATER_1, I.SWITCH_CATA_WATER_2, disabled_case=True)
    ),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_BLUE_EYE_DOOR): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_POISON_ROOTS): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_CATA_ROOTS, disabled_case=True) and rules.has(state, I.KYULI)
    ),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_DOUBLE_SWITCH): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_WATER_1, I.SWITCH_CATA_WATER_2, disabled_case=False)
    ),
    (R.CATA_BLUE_EYE_DOOR, R.CATA_ROOTS_CAMPFIRE): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.CATA_BLUE_EYE_DOOR, R.CATA_FLAMES_FORK): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_CATA_BLUE, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_VERTICAL_SHORTCUT): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_SHORTCUT_ACCESS, I.SWITCH_CATA_AFTER_BLUE_DOOR, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_BLUE_EYE_DOOR): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_CATA_BLUE, disabled_case=True)
        or rules.switches(state, I.SWITCH_CATA_SHORTCUT_ACCESS, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_FLAMES): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_FLAMES_2, disabled_case=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_CENTAUR): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_LADDER_BLOCKS, disabled_case=True)
    ),
    (R.CATA_CENTAUR, R.CATA_4_FACES): lambda rules, state: rules.has(state, I.CLAW),
    (R.CATA_CENTAUR, R.CATA_FLAMES_FORK): lambda rules, state: (
        rules.switches(state, I.SWITCH_CATA_LADDER_BLOCKS, disabled_case=False)
    ),
    (R.CATA_CENTAUR, R.CATA_BOSS): lambda rules, state: (
        rules.switches(state, I.FACE_CATA_CAMPFIRE, disabled_case=False)
    ),
    (R.CATA_4_FACES, R.CATA_CENTAUR): lambda *_: True,
    (R.CATA_4_FACES, R.CATA_DOUBLE_DOOR): lambda rules, state: (
        rules.switches(state, I.FACE_CATA_X4, disabled_case=rules.has(state, I.BOW))
    ),
    (R.CATA_DOUBLE_DOOR, R.CATA_4_FACES): lambda rules, state: (
        rules.switches(state, I.FACE_CATA_X4, disabled_case=False)
    ),
    (R.CATA_DOUBLE_DOOR, R.CATA_VOID_R): lambda rules, state: (
        rules.has(state, I.BANISH, I.BELL)
        and rules.switches(state, I.FACE_CATA_DOUBLE_DOOR, disabled_case=rules.has(state, I.BOW))
    ),
    (R.CATA_VOID_R, R.CATA_DOUBLE_DOOR): lambda *_: False,  # until arenas are included
    (R.CATA_VOID_R, R.CATA_VOID_L): lambda rules, state: rules.has(state, I.VOID),
    (R.CATA_VOID_L, R.CATA_VOID_R): lambda rules, state: rules.has(state, I.VOID),
    (R.CATA_VOID_L, R.CATA_BOSS): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_CATA_PRISON, disabled_case=True) and rules.has(state, I.KYULI)
    ),
    (R.CATA_BOSS, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.CATA_BOSS, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.CATA_BOSS, R.CATA_CENTAUR): lambda rules, state: (
        rules.switches(state, I.FACE_CATA_CAMPFIRE, disabled_case=rules.has(state, I.BOW))
    ),
    (R.CATA_BOSS, R.CATA_VOID_L): lambda rules, state: (
        rules.white_doors(state, I.DOOR_WHITE_CATA_PRISON, disabled_case=True)
    ),
    (R.CATA_BOSS, R.TR_START): lambda rules, state: (
        rules.elevator(state, I.ELEVATOR_TR) or rules.switches(state, I.SWITCH_TR_ELEVATOR, disabled_case=True)
    ),
    (R.CATA_BOSS, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.CATA_BOSS, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.CATA_BOSS, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.CATA_BOSS, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.CATA_BOSS, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.CATA_BOSS, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.TR_START, R.CATA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_CATA_1),
    (R.TR_START, R.CATA_BOSS): lambda rules, state: (
        rules.elevator(state, I.ELEVATOR_CATA_2)
        or (rules.switches(state, I.SWITCH_TR_ELEVATOR, disabled_case=False) and rules.can(state, Logic.EXTRA_HEIGHT))
    ),
    (R.TR_START, R.HOTP_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_HOTP),
    (R.TR_START, R.HOTP_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_1),
    (R.TR_START, R.ROA_ELEVATOR): lambda rules, state: rules.elevator(state, I.ELEVATOR_ROA_2),
    (R.TR_START, R.TR_LEFT): lambda rules, state: (
        rules.blue_doors(state, I.DOOR_BLUE_TR, disabled_case=True)
        and rules.red_doors(state, I.DOOR_RED_TR, disabled_case=rules.reachable(state, L.TR_RED_KEY))
    ),
    (R.TR_START, R.APEX): lambda rules, state: rules.elevator(state, I.ELEVATOR_APEX),
    (R.TR_START, R.GT_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_GT_2),
    (R.TR_START, R.MECH_ZEEK_CONNECTION): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_1),
    (R.TR_START, R.MECH_BOSS): lambda rules, state: rules.elevator(state, I.ELEVATOR_MECH_2),
    (R.TR_START, R.TR_BRAM): lambda rules, state: rules.has(state, I.EYE_BLUE),
    (R.TR_LEFT, R.TR_TOP_RIGHT): lambda rules, state: False,
    (R.TR_LEFT, R.TR_BOTTOM_LEFT): lambda rules, state: False,
    (R.TR_BOTTOM_LEFT, R.TR_BOTTOM): lambda rules, state: False,
    (R.TR_TOP_RIGHT, R.TR_GOLD): lambda rules, state: False,
    (R.TR_TOP_RIGHT, R.TR_MIDDLE_RIGHT): lambda rules, state: False,
    (R.TR_MIDDLE_RIGHT, R.TD_DARK_ARIAS): lambda rules, state: False,
    (R.TR_MIDDLE_RIGHT, R.TR_BOTTOM): lambda rules, state: False,
    (R.TR_BOTTOM, R.TR_BOTTOM_LEFT): lambda rules, state: False,
    (R.CD_START, R.CD_2): lambda rules, state: False,
    (R.CD_START, R.CD_BOSS): lambda rules, state: False,
    (R.CD_2, R.CD_3): lambda rules, state: False,
    (R.CD_3, R.CD_MIDDLE): lambda rules, state: False,
    (R.CD_MIDDLE, R.CD_KYULI_ROUTE): lambda rules, state: False,
    (R.CD_MIDDLE, R.CD_ARIAS_ROUTE): lambda rules, state: False,
    (R.CD_KYULI_ROUTE, R.CD_CAMPFIRE_3): lambda rules, state: False,
    (R.CD_CAMPFIRE_3, R.CD_ARENA): lambda rules, state: False,
    (R.CD_ARENA, R.CD_STEPS): lambda rules, state: False,
    (R.CD_STEPS, R.CD_TOP): lambda rules, state: False,
    (R.CATH_START, R.CATH_START_LEFT): lambda rules, state: False,
    (R.CATH_START, R.CATH_START_RIGHT): lambda rules, state: False,
    (R.CATH_START_RIGHT, R.CATH_START_TOP_LEFT): lambda rules, state: False,
    (R.CATH_START_TOP_LEFT, R.CATH_START_LEFT): lambda rules, state: False,
    (R.CATH_START_LEFT, R.CATH_TP): lambda rules, state: False,
    (R.CATH_TP, R.CATH_LEFT_SHAFT): lambda rules, state: False,
    (R.CATH_LEFT_SHAFT, R.CATH_SHAFT_ACCESS): lambda rules, state: False,
    (R.CATH_LEFT_SHAFT, R.CATH_UNDER_CAMPFIRE): lambda rules, state: False,
    (R.CATH_UNDER_CAMPFIRE, R.CATH_CAMPFIRE_1): lambda rules, state: False,
    (R.CATH_CAMPFIRE_1, R.CATH_SHAFT_ACCESS): lambda rules, state: False,
    (R.CATH_SHAFT_ACCESS, R.CATH_ORB_ROOM): lambda rules, state: False,
    (R.CATH_ORB_ROOM, R.CATH_GOLD_BLOCK): lambda rules, state: False,
    (R.CATH_ORB_ROOM, R.CATH_RIGHT_SHAFT_CONNECTION): lambda rules, state: False,
    (R.CATH_RIGHT_SHAFT_CONNECTION, R.CATH_RIGHT_SHAFT): lambda rules, state: False,
    (R.CATH_RIGHT_SHAFT, R.CATH_TOP): lambda rules, state: False,
    (R.CATH_TOP, R.CATH_UPPER_SPIKE_PIT): lambda rules, state: False,
    (R.CATH_TOP, R.CATH_CAMPFIRE_2): lambda rules, state: False,
    (R.SP_START, R.SP_STAR_END): lambda rules, state: False,
    (R.SP_START, R.SP_CAMPFIRE_1): lambda rules, state: False,
    (R.SP_CAMPFIRE_1, R.SP_HEARTS): lambda rules, state: False,
    (R.SP_HEARTS, R.SP_ORBS): lambda rules, state: False,
    (R.SP_HEARTS, R.SP_FROG): lambda rules, state: False,
    (R.SP_HEARTS, R.SP_PAINTING): lambda rules, state: False,
    (R.SP_PAINTING, R.SP_SHAFT): lambda rules, state: False,
    (R.SP_SHAFT, R.SP_STAR): lambda rules, state: False,
    (R.SP_STAR, R.SP_STAR_CONNECTION): lambda rules, state: False,
    (R.SP_STAR_CONNECTION, R.SP_STAR_END): lambda rules, state: False,
    (R.SP_FROG, R.SP_CAMPFIRE_2): lambda rules, state: False,
}

ITEM_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.GT_ANCIENTS_RING: lambda rules, state: rules.has(state, I.EYE_RED),
    L.GT_BANISH: lambda rules, state: (
        rules.region(R.GT_BOTTOM).can_reach(state)
        and rules.region(R.GT_ASCENDANT_KEY).can_reach(state)
        and rules.region(R.GT_BUTT).can_reach(state)
    ),
    L.TR_ADORNED_KEY: lambda rules, state: False,
    L.CATH_BLOCK: lambda rules, state: False,
}

ATTACK_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.MECH_ATTACK_VOLANTIS: lambda rules, state: rules.has(state, I.CLAW),
    L.MECH_ATTACK_STAR: lambda rules, state: rules.has(state, I.STAR),
    L.ROA_ATTACK: lambda rules, state: rules.has(state, I.STAR),
    L.CAVES_ATTACK_RED: lambda rules, state: rules.has(state, I.EYE_RED),
    L.CAVES_ATTACK_BLUE: lambda rules, state: rules.has(state, I.EYE_RED, I.EYE_BLUE),
    L.CAVES_ATTACK_GREEN: lambda rules, state: (
        rules.has(state, I.EYE_RED, I.EYE_BLUE) and rules.has_any(state, I.EYE_GREEN, I.STAR)
    ),
    L.CD_ATTACK: lambda rules, state: False,
}

HEALTH_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.GT_HP_1_RING: lambda rules, state: (
        rules.has(state, I.STAR) or rules.blue_doors(state, I.DOOR_BLUE_GT_RING, disabled_case=True)
    ),
    L.GT_HP_5_KEY: lambda rules, state: rules.has(state, I.CLAW),
    L.MECH_HP_1_SWITCH: lambda rules, state: False,
    L.MECH_HP_3_CLAW: lambda rules, state: rules.has(state, I.CLAW),
    L.HOTP_HP_2_GAUNTLET: lambda rules, state: rules.has(state, I.CLAW, I.ZEEK, I.BELL),
    # double check
    L.HOTP_HP_5_OLD_MAN: lambda rules, state: (
        rules.has(state, I.CLAW) and (rules.has(state, I.BELL, I.BANISH) or rules.has(state, I.CHALICE))
    ),
    L.HOTP_HP_5_START: lambda rules, state: (
        rules.has(state, I.CLAW) and rules.blue_doors(state, I.DOOR_BLUE_HOTP_START, disabled_case=True)
    ),
    # TODO
    L.ROA_HP_2_RIGHT: lambda rules, state: (
        rules.has_any(state, I.GAUNTLET, I.CHALICE)
        and (rules.has(state, I.STAR) or rules.blue_doors(state, I.DOOR_BLUE_ROA_FLAMES))
    ),
    L.ROA_HP_5_SOLARIA: lambda rules, state: rules.has(state, I.KYULI),
    L.APEX_HP_1_CHALICE: lambda rules, state: rules.blue_doors(state, I.DOOR_BLUE_APEX, disabled_case=True),
    L.CAVES_HP_1_START: lambda rules, state: rules.has_any(state, I.BOW, I.CHALICE),
    L.CAVES_HP_1_CYCLOPS: lambda rules, state: rules.has_any(state, I.SWORD, I.ALGUS_METEOR, I.KYULI_RAY),
    # TODO
    L.CATA_HP_1_ABOVE_POISON: lambda rules, state: rules.has(state, I.BELL) or rules.has(state, I.ICARUS, I.CLAW),
    # TODO
    L.CATA_HP_2_GEMINI_BOTTOM: lambda rules, state: rules.has(state, I.CLAW),
    # TODO
    L.CATA_HP_2_GEMINI_TOP: lambda rules, state: rules.has(state, I.CLAW),
    L.CATA_HP_2_ABOVE_GEMINI: lambda rules, state: (
        (rules.has(state, I.CLAW) or rules.has(state, I.BLOCK, I.BELL))
        and (rules.has(state, I.GAUNTLET, I.BELL) or rules.has(state, I.CHALICE))
    ),
    L.CAVES_HP_5_CHAIN: lambda rules, state: rules.has(state, I.EYE_RED, I.EYE_BLUE, I.STAR, I.CLAW, I.BELL),
    L.CD_HP_1: lambda rules, state: False,
    # might need cloak or icarus?
    L.CATH_HP_1_TOP_LEFT: lambda *_: True,
    # might need cloak or icarus?
    L.CATH_HP_1_TOP_RIGHT: lambda *_: True,
    L.CATH_HP_2_CLAW: lambda rules, state: rules.has(state, I.CLAW),
    # double check
    L.CATH_HP_5_BELL: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
}

WHITE_KEY_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.MECH_WHITE_KEY_LINUS: lambda rules, state: False,
    # specifically kyuli?
    L.MECH_WHITE_KEY_TOP: lambda rules, state: False,
    L.ROA_WHITE_KEY_SAVE: lambda rules, state: False,
    L.ROA_WHITE_KEY_REAPERS: lambda rules, state: False,
}

BLUE_KEY_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.GT_BLUE_KEY_WALL: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.MECH_BLUE_KEY_SNAKE: lambda rules, state: False,
    L.MECH_BLUE_KEY_ARIAS: lambda rules, state: False,
    L.MECH_BLUE_KEY_BLOCKS: lambda rules, state: False,
    L.MECH_BLUE_KEY_SAVE: lambda rules, state: False,
    # double check
    L.MECH_BLUE_KEY_POT: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.HOTP_BLUE_KEY_STATUE: lambda rules, state: rules.has(state, I.CLAW),
    L.HOTP_BLUE_KEY_AMULET: lambda rules, state: False,
    L.HOTP_BLUE_KEY_LADDER: lambda rules, state: rules.can(state, Logic.EXTRA_HEIGHT),
    L.HOTP_BLUE_KEY_MAZE: lambda rules, state: False,
    L.ROA_BLUE_KEY_FACE: lambda rules, state: rules.has(state, I.BOW),
    # double check
    L.ROA_BLUE_KEY_FLAMES: lambda rules, state: rules.has_any(state, I.GAUNTLET, I.BLOCK),
    L.ROA_BLUE_KEY_BABY: lambda rules, state: False,
    L.ROA_BLUE_KEY_TOP: lambda rules, state: False,
    L.SP_BLUE_KEY_ARIAS: lambda rules, state: rules.has(state, I.ARIAS),
}

RED_KEY_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.GT_RED_KEY: lambda rules, state: rules.has(state, I.ZEEK, I.KYULI),
    L.ROA_RED_KEY: lambda rules, state: rules.has(state, I.CLOAK, I.CLAW, I.BELL),
    L.TR_RED_KEY: lambda rules, state: rules.has(state, I.CLAW),
}

SHOP_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
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

SWITCH_RULES: Dict[L, Callable[["AstalonRules", CollectionState], bool]] = {
    L.GT_SWITCH_2ND_ROOM: lambda rules, state: rules.white_doors(state, I.DOOR_WHITE_GT_START, disabled_case=True),
    L.GT_SWITCH_1ST_CYCLOPS: lambda rules, state: False,
    L.GT_SWITCH_SPIKE_TUNNEL: lambda rules, state: False,
    L.GT_SWITCH_BUTT_ACCESS: lambda rules, state: False,
    L.GT_SWITCH_GH: lambda rules, state: False,
    L.GT_SWITCH_ROTA: lambda rules, state: False,
    L.GT_SWITCH_UPPER_PATH_BLOCKS: lambda rules, state: False,
    L.GT_SWITCH_UPPER_PATH_ACCESS: lambda rules, state: False,
    L.GT_SWITCH_CROSSES: lambda rules, state: False,
    L.GT_SWITCH_GH_SHORTCUT: lambda rules, state: False,
    L.GT_SWITCH_ARIAS_PATH: lambda rules, state: False,
    L.GT_SWITCH_SWORD_ACCESS: lambda rules, state: False,
    L.GT_SWITCH_SWORD_BACKTRACK: lambda rules, state: False,
    L.GT_SWITCH_SWORD: lambda rules, state: False,
    L.GT_SWITCH_UPPER_ARIAS: lambda rules, state: False,
    L.GT_CRYSTAL_OLD_MAN_1: lambda rules, state: False,
    L.GT_CRYSTAL_OLD_MAN_2: lambda rules, state: False,
    L.GT_CRYSTAL_LADDER: lambda rules, state: False,
    L.MECH_SWITCH_WATCHER: lambda rules, state: False,
    L.MECH_SWITCH_CHAINS: lambda rules, state: False,
    L.MECH_SWITCH_BOSS_ACCESS_1: lambda rules, state: False,
    L.MECH_SWITCH_BOSS_ACCESS_2: lambda rules, state: False,
    L.MECH_SWITCH_SPLIT_PATH: lambda rules, state: False,
    L.MECH_SWITCH_SNAKE_1: lambda rules, state: False,
    L.MECH_SWITCH_BOOTS_ACCESS: lambda rules, state: False,
    L.MECH_SWITCH_UPPER_GT_ACCESS: lambda rules, state: False,
    L.MECH_SWITCH_UPPER_VOID_DROP: lambda rules, state: False,
    L.MECH_SWITCH_UPPER_VOID: lambda rules, state: False,
    L.MECH_SWITCH_LINUS: lambda rules, state: False,
    L.MECH_SWITCH_TO_BOSS_2: lambda rules, state: False,
    L.MECH_SWITCH_POTS: lambda rules, state: False,
    L.MECH_SWITCH_MAZE_BACKDOOR: lambda rules, state: False,
    L.MECH_SWITCH_TO_BOSS_1: lambda rules, state: False,
    L.MECH_SWITCH_BLOCK_STAIRS: lambda rules, state: False,
    L.MECH_SWITCH_ARIAS_CYCLOPS: lambda rules, state: False,
    L.MECH_SWITCH_BOOTS_LOWER: lambda rules, state: False,
    L.MECH_SWITCH_CHAINS_GAP: lambda rules, state: False,
    L.MECH_SWITCH_LOWER_KEY: lambda rules, state: False,
    L.MECH_SWITCH_ARIAS: lambda rules, state: False,
    L.MECH_SWITCH_SNAKE_2: lambda rules, state: False,
    L.MECH_SWITCH_KEY_BLOCKS: lambda rules, state: False,
    L.MECH_SWITCH_CANNON: lambda rules, state: False,
    L.MECH_SWITCH_EYEBALL: lambda rules, state: False,
    L.MECH_SWITCH_INVISIBLE: lambda rules, state: False,
    L.MECH_CRYSTAL_CANNON: lambda rules, state: False,
    L.MECH_CRYSTAL_LINUS: lambda rules, state: False,
    L.MECH_CRYSTAL_LOWER: lambda rules, state: False,
    L.MECH_CRYSTAL_TO_BOSS_3: lambda rules, state: False,
    L.MECH_CRYSTAL_TRIPLE_1: lambda rules, state: False,
    L.MECH_CRYSTAL_TRIPLE_2: lambda rules, state: False,
    L.MECH_CRYSTAL_TRIPLE_3: lambda rules, state: False,
    L.MECH_CRYSTAL_TOP: lambda rules, state: False,
    L.MECH_CRYSTAL_CLOAK: lambda rules, state: False,
    L.MECH_CRYSTAL_SLIMES: lambda rules, state: False,
    L.MECH_CRYSTAL_TO_CD: lambda rules, state: False,
    L.MECH_CRYSTAL_CAMPFIRE: lambda rules, state: False,
    L.MECH_CRYSTAL_1ST_ROOM: lambda rules, state: False,
    L.MECH_CRYSTAL_OLD_MAN: lambda rules, state: False,
    L.MECH_CRYSTAL_TOP_CHAINS: lambda rules, state: False,
    L.MECH_CRYSTAL_BK: lambda rules, state: False,
    L.MECH_FACE_ABOVE_VOLANTIS: lambda rules, state: False,
    L.HOTP_SWITCH_ROCK: lambda rules, state: False,
    L.HOTP_SWITCH_BELOW_START: lambda rules, state: False,
    L.HOTP_SWITCH_LEFT_2: lambda rules, state: False,
    L.HOTP_SWITCH_LEFT_1: lambda rules, state: False,
    L.HOTP_SWITCH_LOWER_SHORTCUT: lambda rules, state: False,
    L.HOTP_SWITCH_BELL: lambda rules, state: False,
    L.HOTP_SWITCH_GHOST_BLOOD: lambda rules, state: False,
    L.HOTP_SWITCH_TELEPORTS: lambda rules, state: False,
    L.HOTP_SWITCH_WORM_PILLAR: lambda rules, state: False,
    L.HOTP_SWITCH_TO_CLAW_1: lambda rules, state: False,
    L.HOTP_SWITCH_TO_CLAW_2: lambda rules, state: False,
    L.HOTP_SWITCH_CLAW_ACCESS: lambda rules, state: False,
    L.HOTP_SWITCH_GHOSTS: lambda rules, state: False,
    L.HOTP_SWITCH_LEFT_3: lambda rules, state: False,
    L.HOTP_SWITCH_ABOVE_OLD_MAN: lambda rules, state: False,
    L.HOTP_SWITCH_TO_ABOVE_OLD_MAN: lambda rules, state: False,
    L.HOTP_SWITCH_TP_PUZZLE: lambda rules, state: False,
    L.HOTP_SWITCH_EYEBALL_SHORTCUT: lambda rules, state: False,
    L.HOTP_SWITCH_BELL_ACCESS: lambda rules, state: False,
    L.HOTP_SWITCH_1ST_ROOM: lambda rules, state: False,
    L.HOTP_SWITCH_LEFT_BACKTRACK: lambda rules, state: False,
    L.HOTP_CRYSTAL_ROCK_ACCESS: lambda rules, state: False,
    L.HOTP_CRYSTAL_BOTTOM: lambda rules, state: False,
    L.HOTP_CRYSTAL_LOWER: lambda rules, state: False,
    L.HOTP_CRYSTAL_AFTER_CLAW: lambda rules, state: False,
    L.HOTP_CRYSTAL_MAIDEN_1: lambda rules, state: False,
    L.HOTP_CRYSTAL_MAIDEN_2: lambda rules, state: False,
    L.HOTP_CRYSTAL_BELL_ACCESS: lambda rules, state: False,
    L.HOTP_CRYSTAL_HEART: lambda rules, state: False,
    L.HOTP_CRYSTAL_BELOW_PUZZLE: lambda rules, state: False,
    L.HOTP_FACE_OLD_MAN: lambda rules, state: False,
    L.ROA_SWITCH_ASCEND: lambda rules, state: False,
    L.ROA_SWITCH_AFTER_WORMS: lambda rules, state: False,
    L.ROA_SWITCH_RIGHT_PATH: lambda rules, state: False,
    L.ROA_SWITCH_APEX_ACCESS: lambda rules, state: False,
    L.ROA_SWITCH_ICARUS: lambda rules, state: False,
    L.ROA_SWITCH_SHAFT_L: lambda rules, state: False,
    L.ROA_SWITCH_SHAFT_R: lambda rules, state: False,
    L.ROA_SWITCH_ELEVATOR: lambda rules, state: False,
    L.ROA_SWITCH_SHAFT_DOWNWARDS: lambda rules, state: False,
    L.ROA_SWITCH_SPIDERS: lambda rules, state: False,
    L.ROA_FACE_SPIDERS: lambda rules, state: False,
    L.ROA_SWITCH_DARK_ROOM: lambda rules, state: False,
    L.ROA_SWITCH_ASCEND_SHORTCUT: lambda rules, state: False,
    L.ROA_SWITCH_1ST_SHORTCUT: lambda rules, state: False,
    L.ROA_SWITCH_SPIKE_CLIMB: lambda rules, state: False,
    L.ROA_SWITCH_ABOVE_CENTAUR: lambda rules, state: False,
    L.ROA_SWITCH_BLOOD_POT: lambda rules, state: False,
    L.ROA_SWITCH_WORMS: lambda rules, state: False,
    L.ROA_SWITCH_TRIPLE_1: lambda rules, state: False,
    L.ROA_SWITCH_TRIPLE_3: lambda rules, state: False,
    L.ROA_SWITCH_BABY_GORGON: lambda rules, state: False,
    L.ROA_SWITCH_BOSS_ACCESS: lambda rules, state: False,
    L.ROA_SWITCH_BLOOD_POT_L: lambda rules, state: False,
    L.ROA_SWITCH_BLOOD_POT_R: lambda rules, state: False,
    L.ROA_SWITCH_LOWER_VOID: lambda rules, state: False,
    L.ROA_CRYSTAL_1ST_ROOM: lambda rules, state: False,
    L.ROA_CRYSTAL_BABY_GORGON: lambda rules, state: False,
    L.ROA_CRYSTAL_LADDER_R: lambda rules, state: False,
    L.ROA_CRYSTAL_LADDER_L: lambda rules, state: False,
    L.ROA_CRYSTAL_CENTAUR: lambda rules, state: False,
    L.ROA_CRYSTAL_SPIKE_BALLS: lambda rules, state: False,
    L.ROA_CRYSTAL_LEFT_ASCEND: lambda rules, state: False,
    L.ROA_CRYSTAL_SHAFT: lambda rules, state: False,
    L.ROA_CRYSTAL_BRANCH_R: lambda rules, state: False,
    L.ROA_CRYSTAL_BRANCH_L: lambda rules, state: False,
    L.ROA_CRYSTAL_3_REAPERS: lambda rules, state: False,
    L.ROA_CRYSTAL_TRIPLE_2: lambda rules, state: False,
    L.ROA_FACE_BLUE_KEY: lambda rules, state: False,
    L.DARK_SWITCH: lambda rules, state: False,
    L.APEX_SWITCH: lambda rules, state: False,
    L.CAVES_SWITCH_SKELETONS: lambda rules, state: False,
    L.CAVES_SWITCH_CATA_ACCESS_1: lambda rules, state: False,
    L.CAVES_SWITCH_CATA_ACCESS_2: lambda rules, state: False,
    L.CAVES_SWITCH_CATA_ACCESS_3: lambda rules, state: False,
    L.CAVES_FACE_1ST_ROOM: lambda rules, state: False,
    L.CATA_SWITCH_ELEVATOR: lambda rules, state: False,
    L.CATA_SWITCH_SHORTCUT: lambda rules, state: False,
    L.CATA_SWITCH_TOP: lambda rules, state: False,
    L.CATA_SWITCH_CLAW_1: lambda rules, state: False,
    L.CATA_SWITCH_CLAW_2: lambda rules, state: False,
    L.CATA_SWITCH_WATER_1: lambda rules, state: False,
    L.CATA_SWITCH_WATER_2: lambda rules, state: False,
    L.CATA_SWITCH_DEV_ROOM: lambda rules, state: False,
    L.CATA_SWITCH_AFTER_BLUE_DOOR: lambda rules, state: False,
    L.CATA_SWITCH_SHORTCUT_ACCESS: lambda rules, state: False,
    L.CATA_SWITCH_LADDER_BLOCKS: lambda rules, state: False,
    L.CATA_SWITCH_MID_SHORTCUT: lambda rules, state: False,
    L.CATA_SWITCH_1ST_ROOM: lambda rules, state: False,
    L.CATA_SWITCH_FLAMES_2: lambda rules, state: False,
    L.CATA_SWITCH_FLAMES_1: lambda rules, state: False,
    L.CATA_CRYSTAL_POISON_ROOTS: lambda rules, state: False,
    L.CATA_FACE_AFTER_BOW: lambda rules, state: False,
    L.CATA_FACE_BOW: lambda rules, state: False,
    L.CATA_FACE_X4: lambda rules, state: False,
    L.CATA_FACE_CAMPFIRE: lambda rules, state: False,
    L.CATA_FACE_DOUBLE_DOOR: lambda rules, state: False,
    L.CATA_FACE_BOTTOM: lambda rules, state: False,
    L.TR_SWITCH_ADORNED_L: lambda rules, state: False,
    L.TR_SWITCH_ADORNED_M: lambda rules, state: False,
    L.TR_SWITCH_ADORNED_R: lambda rules, state: False,
    L.TR_SWITCH_ELEVATOR: lambda rules, state: False,
    L.TR_SWITCH_BOTTOM: lambda rules, state: False,
    L.TR_CRYSTAL_GOLD: lambda rules, state: False,
    L.TR_CRYSTAL_DARK_ARIAS: lambda rules, state: False,
    L.CD_SWITCH_1: lambda rules, state: False,
    L.CD_SWITCH_2: lambda rules, state: False,
    L.CD_SWITCH_3: lambda rules, state: False,
    L.CD_SWITCH_CAMPFIRE: lambda rules, state: False,
    L.CD_SWITCH_TOP: lambda rules, state: False,
    L.CD_CRYSTAL_BACKTRACK: lambda rules, state: False,
    L.CD_CRYSTAL_START: lambda rules, state: False,
    L.CD_CRYSTAL_CAMPFIRE: lambda rules, state: False,
    L.CD_CRYSTAL_STEPS: lambda rules, state: False,
    L.CATH_SWITCH_BOTTOM: lambda rules, state: False,
    L.CATH_SWITCH_BESIDE_SHAFT: lambda rules, state: False,
    L.CATH_SWITCH_TOP_CAMPFIRE: lambda rules, state: False,
    L.CATH_CRYSTAL_1ST_ROOM: lambda rules, state: False,
    L.CATH_CRYSTAL_SHAFT: lambda rules, state: False,
    L.CATH_CRYSTAL_SPIKE_PIT: lambda rules, state: False,
    L.CATH_CRYSTAL_TOP_L: lambda rules, state: False,
    L.CATH_CRYSTAL_TOP_R: lambda rules, state: False,
    L.CATH_CRYSTAL_SHAFT_ACCESS: lambda rules, state: False,
    L.CATH_CRYSTAL_ORBS: lambda rules, state: False,
    L.CATH_FACE_LEFT: lambda rules, state: False,
    L.CATH_FACE_RIGHT: lambda rules, state: False,
    L.SP_SWITCH_DOUBLE_DOORS: lambda rules, state: False,
    L.SP_SWITCH_BUBBLES: lambda rules, state: False,
    L.SP_SWITCH_AFTER_STAR: lambda rules, state: False,
    L.SP_CRYSTAL_BLOCKS: lambda rules, state: False,
    L.SP_CRYSTAL_STAR: lambda rules, state: False,
}


class AstalonRules:
    world: "AstalonWorld"
    player: int
    options: AstalonOptions

    def __init__(self, world: "AstalonWorld"):
        self.world = world
        self.player = world.player
        self.options = world.options

    def region(self, name: R):
        return self.world.multiworld.get_region(name.value, self.player)

    def entrance(self, from_: R, to_: R):
        return self.world.multiworld.get_entrance(f"{from_.value} -> {to_.value}", self.player)

    def location(self, name: L):
        return self.world.multiworld.get_location(name.value, self.player)

    def can_get_zeek(self, state: CollectionState) -> bool:
        return self.region(R.MECH_ZEEK).can_reach(state) and self.region(R.CD_BOSS).can_reach(state)

    def can_get_bram(self, state: CollectionState) -> bool:
        return self.region(R.TR_BRAM).can_reach(state)

    def _has(self, state: CollectionState, item: I, count: int = 1) -> bool:
        if item in CHARACTERS:
            if self.options.randomize_characters == RandomizeCharacters.option_vanilla:
                if item in {I.ALGUS, I.ARIAS, I.KYULI}:
                    return True
                elif item == I.ZEEK:
                    return self.can_get_zeek(state)
                elif item == I.BRAM:
                    return self.can_get_bram(state)
            else:
                return state.has(item.value, self.player)

        if item == I.CLOAK and not self._has(state, I.ALGUS):
            return False
        if item in {I.SWORD, I.BOOTS} and not self._has(state, I.ARIAS):
            return False
        if item in {I.CLAW, I.BOW} and not self._has(state, I.KYULI):
            return False
        if item == I.BLOCK and not self._has(state, I.ZEEK):
            return False
        if item == I.STAR and not self._has(state, I.BRAM):
            return False
        if item == I.BANISH and not self.has_any(state, I.ALGUS, I.ZEEK):
            return False
        if item == I.GAUNTLET and not self.has_any(state, I.ARIAS, I.BRAM):
            return False

        if item == I.CYCLOPS:
            # not yet randomized
            return self.region(R.MECH_ZEEK).can_reach(state)

        if item in {I.ALGUS_ARCANIST, I.ALGUS_METEOR, I.ALGUS_SHOCK} and not self._has(state, I.ALGUS):
            return False
        if item in {I.ARIAS_GORGONSLAYER, I.ARIAS_LAST_STAND, I.ARIAS_LIONHEART} and not self._has(state, I.ARIAS):
            return False
        if item in {I.KYULI_ASSASSIN, I.KYULI_BULLSEYE, I.KYULI_RAY} and not self._has(state, I.KYULI):
            return False
        if item in {I.ZEEK_JUNKYARD, I.ZEEK_ORBS, I.ZEEK_LOOT} and not self._has(state, I.ZEEK):
            return False
        if item in {I.BRAM_AXE, I.BRAM_HUNTER, I.BRAM_WHIPLASH} and not self._has(state, I.BRAM):
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

    def white_doors(
        self,
        state: CollectionState,
        *doors: WhiteDoors,
        disabled_case: Union[bool, Callable[["AstalonRules", CollectionState], bool]],
    ) -> bool:
        return self._togglable(state, self.options.randomize_white_keys, disabled_case, *doors)

    def blue_doors(
        self,
        state: CollectionState,
        *doors: BlueDoors,
        disabled_case: Union[bool, Callable[["AstalonRules", CollectionState], bool]],
    ) -> bool:
        return self._togglable(state, self.options.randomize_blue_keys, disabled_case, *doors)

    def red_doors(
        self,
        state: CollectionState,
        *doors: RedDoors,
        disabled_case: Union[bool, Callable[["AstalonRules", CollectionState], bool]],
    ) -> bool:
        return self._togglable(state, self.options.randomize_switches, disabled_case, *doors)

    def switches(
        self,
        state: CollectionState,
        *switches: Switches,
        disabled_case: Union[bool, Callable[["AstalonRules", CollectionState], bool]],
    ) -> bool:
        return self._togglable(state, self.options.randomize_switches, disabled_case, *switches)

    def _togglable(
        self,
        state: CollectionState,
        option: bool,
        disabled_case: Union[bool, Callable[["AstalonRules", CollectionState], bool]],
        *items: I,
    ) -> bool:
        if not option:
            if isinstance(disabled_case, bool):
                return disabled_case
            return disabled_case(self, state)
        for item in items:
            if not self._has(state, item):
                return False
        return True

    def elevator(self, state: CollectionState, destination: Elevators) -> bool:
        if not self._has(state, I.ASCENDANT_KEY):
            return False
        if self.options.free_apex_elevator and destination == I.ELEVATOR_APEX:
            return True
        return self.options.randomize_elevator and self._has(state, destination)

    def cheap_shop(self, state: CollectionState) -> bool:
        # TODO
        return self.region(R.GT_LEFT).can_reach(state)

    def moderate_shop(self, state: CollectionState) -> bool:
        # TODO
        return self.region(R.MECH_START).can_reach(state)

    def expensive_shop(self, state: CollectionState) -> bool:
        # TODO
        return self.region(R.ROA_START).can_reach(state)

    def can(self, state: CollectionState, logic: L, gold_block=False) -> bool:
        if logic == Logic.ARIAS_JUMP:
            return self.hard and self._has(state, I.ARIAS)
        if logic == Logic.EXTRA_HEIGHT:
            return (
                self._has(state, I.KYULI)
                or self._has(state, I.BLOCK)
                or (gold_block and self._has(state, I.ZEEK))
                or self.can(state, Logic.ARIAS_JUMP)
            )
        if logic == Logic.COMBO_HEIGHT:
            return self.hard and self.can(state, Logic.ARIAS_JUMP) and self._has(state, I.BELL, I.BLOCK)
        if logic == Logic.BLOCK_IN_WALL:
            return self.hard and (self._has(state, I.BLOCK) or (gold_block and self._has(state, I.ZEEK)))
        if logic == Logic.CRYSTAL:
            if self._has(state, I.ALGUS) or self._has(state, I.ZEEK, I.BANISH):
                return True
            if self.hard:
                return self._has(state, I.KYULI_RAY) or self._has(state, I.BRAM_WHIPLASH)
        if logic == Logic.BIG_MAGIC:
            return self.hard and self._has(state, I.BANISH, I.ALGUS_ARCANIST)
        return False

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

    @property
    def easy(self):
        return self.options.difficulty >= Difficulty.option_easy

    @property
    def hard(self):
        return self.options.difficulty >= Difficulty.option_hard

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
