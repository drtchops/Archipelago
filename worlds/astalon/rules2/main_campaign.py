from typing import Dict, Tuple

from ..items import BlueDoor, Character, Crystal, Elevator, Eye, KeyItem, ShopUpgrade, Switch, WhiteDoor
from ..regions import RegionName as R
from .base import (
    And,
    CanReach,
    False_,
    Has,
    HasAll,
    HasAny,
    HasBlue,
    HasElevator,
    HasSwitch,
    HasWhite,
    Or,
    Rule,
    True_,
)

easy = (("difficulty", 0),)
hard = (("difficulty", 1),)
characters_off = (("randomize_characters", 0),)
characters_on = (("randomize_characters__gt", 0),)
white_off = (("randomize_white_keys", 0),)
white_on = (("randomize_white_keys", 1),)
blue_off = (("randomize_blue_keys", 0),)
blue_on = (("randomize_blue_keys", 1),)
red_off = (("randomize_red_keys", 0),)
red_on = (("randomize_red_keys", 1),)
switch_off = (("randomize_switches", 0),)
switch_on = (("randomize_switches", 1),)

true = True_()
false = False_()

can_uppies = Or(True_(opts=characters_off), HasAny(Character.ARIAS, Character.BRAM, opts=characters_on), opts=hard)
can_extra_height = Or(HasAny(Character.KYULI, KeyItem.BLOCK), can_uppies)
can_extra_height_gold_block = Or(HasAny(Character.KYULI, Character.ZEEK), can_uppies)
can_combo_height = And(can_uppies, HasAll(KeyItem.BELL, KeyItem.BLOCK))
can_block_in_wall = HasAll(Character.ZEEK, KeyItem.BLOCK, opts=hard)
can_crystal = Or(
    HasAny(Character.ALGUS, KeyItem.BLOCK),
    HasAll(Character.ZEEK, KeyItem.BANISH),
    Has(ShopUpgrade.KYULI_RAY, opts=hard),
)
can_crystal_whiplash = Or(can_crystal, Has(ShopUpgrade.BRAM_WHIPLASH))
can_big_magic = HasAll(Character.ALGUS, KeyItem.BANISH, ShopUpgrade.ALGUS_ARCANIST, opts=hard)
can_kill_ghosts = Or(
    HasAny(KeyItem.BANISH, KeyItem.BLOCK),
    HasAll(ShopUpgrade.ALGUS_METEOR, KeyItem.CHALICE, opts=easy),
    Has(ShopUpgrade.ALGUS_METEOR, opts=hard),
)

elevator_apex = Or(
    HasElevator(Elevator.APEX, opts=(("apex_elevator", 1),)),
    Has(KeyItem.ASCENDANT_KEY, opts=(("apex_elevator", 0),)),
)

MAIN_ENTRANCE_RULES: Dict[Tuple[R, R], Rule] = {
    (R.SHOP, R.SHOP_ALGUS): Has(Character.ALGUS),
    (R.SHOP, R.SHOP_ARIAS): Has(Character.ARIAS),
    (R.SHOP, R.SHOP_KYULI): Has(Character.KYULI),
    (R.SHOP, R.SHOP_ZEEK): Has(Character.ZEEK),
    (R.SHOP, R.SHOP_BRAM): Has(Character.BRAM),
    (R.GT_ENTRANCE, R.GT_BESTIARY): HasBlue(BlueDoor.GT_HUNTER, otherwise=True),
    (R.GT_ENTRANCE, R.GT_BABY_GORGON): And(
        Has(Eye.GREEN),
        Or(
            Has(KeyItem.CLAW),
            And(
                Has(Character.ZEEK),
                Or(HasAll(Character.KYULI, KeyItem.BELL), Has(KeyItem.BLOCK)),
                opts=hard,
            ),
        ),
    ),
    (R.GT_ENTRANCE, R.GT_BOTTOM): Or(
        HasSwitch(Switch.GT_2ND_ROOM),
        HasWhite(WhiteDoor.GT_START, otherwise=True, opts=switch_off),
    ),
    (R.GT_ENTRANCE, R.GT_VOID): Has(KeyItem.VOID),
    (R.GT_ENTRANCE, R.GT_GORGONHEART): Or(HasSwitch(Switch.GT_GH_SHORTCUT), HasAny(KeyItem.ICARUS, KeyItem.BOOTS)),
    (R.GT_ENTRANCE, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.GT_ENTRANCE, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.GT_ENTRANCE, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.GT_ENTRANCE, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.GT_ENTRANCE, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.GT_ENTRANCE, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.GT_ENTRANCE, R.APEX): elevator_apex,
    (R.GT_ENTRANCE, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.GT_ENTRANCE, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.GT_ENTRANCE, R.TR_START): HasElevator(Elevator.TR),
    (R.GT_BOTTOM, R.GT_VOID): Has(Eye.RED),
    (R.GT_BOTTOM, R.GT_GORGONHEART): HasWhite(WhiteDoor.GT_MAP, otherwise=True),
    (R.GT_BOTTOM, R.GT_UPPER_PATH): Or(
        HasSwitch(Crystal.GT_ROTA),
        can_uppies,
        And(Has(KeyItem.STAR), HasBlue(BlueDoor.GT_RING, otherwise=True)),
        Has(KeyItem.BLOCK),
    ),
    (R.GT_BOTTOM, R.CAVES_START): Or(
        Has(Character.KYULI),
        HasAny(Character.ZEEK, KeyItem.BOOTS, opts=hard),
    ),
    (R.GT_VOID, R.GT_BOTTOM): Has(Eye.RED),
    (R.GT_VOID, R.MECH_SNAKE): HasSwitch(Switch.MECH_SNAKE_2),
    (R.GT_GORGONHEART, R.GT_ORBS_DOOR): HasBlue(BlueDoor.GT_ORBS, otherwise=True),
    (R.GT_GORGONHEART, R.GT_LEFT): Or(HasSwitch(Switch.GT_CROSSES), HasSwitch(Switch.GT_1ST_CYCLOPS, otherwise=True)),
    (R.GT_LEFT, R.GT_GORGONHEART): Or(HasSwitch(Switch.GT_CROSSES, otherwise=True), HasSwitch(Switch.GT_1ST_CYCLOPS)),
    (R.GT_LEFT, R.GT_ORBS_HEIGHT): can_extra_height,
    (R.GT_LEFT, R.GT_ASCENDANT_KEY): HasBlue(BlueDoor.GT_ASCENDANT, otherwise=True),
    (R.GT_LEFT, R.GT_TOP_LEFT): Or(
        HasSwitch(Switch.GT_ARIAS),
        HasAny(Character.ARIAS, KeyItem.CLAW),
        HasAll(KeyItem.BLOCK, Character.KYULI, KeyItem.BELL),
    ),
    (R.GT_LEFT, R.GT_TOP_RIGHT): can_extra_height,
    (R.GT_TOP_LEFT, R.GT_BUTT): Or(
        HasSwitch(Switch.GT_BUTT_ACCESS),
        CanReach(R.GT_SPIKE_TUNNEL_SWITCH, opts=switch_off),
    ),
    (R.GT_TOP_RIGHT, R.GT_SPIKE_TUNNEL): Or(
        HasSwitch(Switch.GT_SPIKE_TUNNEL),
        CanReach(R.GT_TOP_LEFT, opts=switch_off),
    ),
    (R.GT_SPIKE_TUNNEL, R.GT_TOP_RIGHT): HasSwitch(Switch.GT_SPIKE_TUNNEL),
    (R.GT_SPIKE_TUNNEL, R.GT_SPIKE_TUNNEL_SWITCH): can_extra_height,
    (R.GT_SPIKE_TUNNEL_SWITCH, R.GT_BUTT): Or(
        Has(KeyItem.STAR, opts=hard),
        HasAll(KeyItem.STAR, KeyItem.BELL, opts=easy),
    ),
    (R.GT_BUTT, R.GT_TOP_LEFT): HasSwitch(Switch.GT_BUTT_ACCESS),
    (R.GT_BUTT, R.GT_SPIKE_TUNNEL_SWITCH): Has(KeyItem.STAR),
    (R.GT_BUTT, R.GT_BOSS): HasWhite(WhiteDoor.GT_TAUROS, otherwise=True),
    (R.GT_BOSS, R.GT_BUTT): HasWhite(WhiteDoor.GT_TAUROS),
    (R.GT_BOSS, R.MECH_START): Has(Eye.RED),
    (R.GT_BOSS, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.GT_BOSS, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.GT_BOSS, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.GT_BOSS, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.GT_BOSS, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.GT_BOSS, R.APEX): elevator_apex,
    (R.GT_BOSS, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.GT_BOSS, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.GT_BOSS, R.TR_START): HasElevator(Elevator.TR),
    (R.GT_UPPER_ARIAS, R.GT_OLD_MAN_FORK): Or(
        HasSwitch(Crystal.GT_LADDER),
        CanReach(R.GT_LADDER_SWITCH, opts=switch_off),
    ),
    (R.GT_UPPER_ARIAS, R.MECH_SWORD_CONNECTION): Or(
        Has(Character.ARIAS),
        HasSwitch(Switch.GT_UPPER_ARIAS),
        CanReach(R.GT_ARIAS_SWORD_SWITCH, opts=switch_off),
    ),
    (R.GT_OLD_MAN_FORK, R.GT_UPPER_ARIAS): Or(
        HasSwitch(Crystal.GT_LADDER),
        CanReach(R.GT_LADDER_SWITCH, opts=switch_off),
    ),
    (R.GT_OLD_MAN_FORK, R.GT_SWORD_FORK): HasBlue(BlueDoor.GT_SWORD, otherwise=True),
    (R.GT_OLD_MAN_FORK, R.GT_OLD_MAN): Or(
        Has(KeyItem.CLAW),
        # TODO: you don't need both switches, revisit when adding old man
        And(HasSwitch(Crystal.GT_OLD_MAN_1), HasSwitch(Crystal.GT_OLD_MAN_2)),
        And(can_crystal, opts=switch_off),
    ),
    (R.GT_SWORD_FORK, R.GT_SWORD): HasSwitch(Switch.GT_SWORD_ACCESS, otherwise=True),
    (R.GT_SWORD_FORK, R.GT_ARIAS_SWORD_SWITCH): Or(Has(KeyItem.SWORD), HasAll(KeyItem.BOW, KeyItem.BELL)),
    (R.GT_UPPER_PATH, R.GT_UPPER_PATH_CONNECTION): HasSwitch(Switch.GT_UPPER_PATH_ACCESS),
    (R.GT_UPPER_PATH_CONNECTION, R.GT_UPPER_PATH): HasSwitch(Switch.GT_UPPER_PATH_ACCESS, otherwise=True),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_SWORD_CONNECTION): HasSwitch(Switch.MECH_TO_UPPER_GT),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): HasSwitch(Switch.MECH_TO_UPPER_GT),
    (R.MECH_START, R.GT_LADDER_SWITCH): And(Has(Eye.RED), can_crystal),
}
