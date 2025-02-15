from typing import Dict, Tuple

from .items import BlueDoor, Character, Elevator, Eye, KeyItem, ShopUpgrade, Switch, WhiteDoor
from .logic import And, False_, Has, HasAll, HasAny, HasBlueDoor, HasElevator, HasSwitch, HasWhiteDoor, Or, Rule, True_
from .regions import RegionName as R

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
elevator_off = (("randomize_elevator", 0),)
elevator_on = (("randomize_elevator", 1),)
free_apex_on = (("apex_elevator", 0),)
free_apex_off = (("apex_elevator", 1),)

true = True_()
false = False_()

has_algus = Or(Has(Character.ALGUS, opts=characters_on), True_(opts=characters_off))
has_arias = Or(Has(Character.ARIAS, opts=characters_on), True_(opts=characters_off))
has_kyuli = Or(Has(Character.KYULI, opts=characters_on), True_(opts=characters_off))

has_cloak = And(has_algus, Has(KeyItem.CLOAK))
has_sword = And(has_arias, Has(KeyItem.SWORD))
has_boots = And(has_arias, Has(KeyItem.BOOTS))
has_claw = And(has_kyuli, Has(KeyItem.CLAW))
has_bow = And(has_kyuli, Has(KeyItem.BOW))
has_block = HasAll(Character.ZEEK, KeyItem.BLOCK)
has_star = HasAll(Character.BRAM, KeyItem.STAR)
has_banish = And(Or(has_algus, Has(Character.ZEEK)), Has(KeyItem.BANISH))
has_gauntlet = And(Or(has_arias, Has(Character.BRAM)), Has(KeyItem.GAUNTLET))

has_algus_arcanist = And(has_algus, Has(ShopUpgrade.ALGUS_ARCANIST))
has_algus_meteor = And(has_algus, Has(ShopUpgrade.ALGUS_METEOR))
has_algus_shock = And(has_algus, Has(ShopUpgrade.ALGUS_SHOCK))
has_arias_gorgonslayer = And(has_arias, Has(ShopUpgrade.ARIAS_GORGONSLAYER))
has_arias_last_stand = And(has_arias, Has(ShopUpgrade.ARIAS_LAST_STAND))
has_arias_lionheart = And(has_arias, Has(ShopUpgrade.ARIAS_LIONHEART))
has_kyuli_assassin = And(has_kyuli, Has(ShopUpgrade.KYULI_ASSASSIN))
has_kyuli_bullseye = And(has_kyuli, Has(ShopUpgrade.KYULI_BULLSEYE))
has_kyuli_ray = And(has_kyuli, Has(ShopUpgrade.KYULI_RAY))
has_zeek_junkyard = HasAll(Character.ZEEK, ShopUpgrade.ZEEK_JUNKYARD)
has_zeek_orbs = HasAll(Character.ZEEK, ShopUpgrade.ZEEK_ORBS)
has_zeek_loot = HasAll(Character.ZEEK, ShopUpgrade.ZEEK_LOOT)
has_bram_axe = HasAll(Character.BRAM, ShopUpgrade.BRAM_AXE)
has_bram_hunter = HasAll(Character.BRAM, ShopUpgrade.BRAM_HUNTER)
has_bram_whiplash = HasAll(Character.BRAM, ShopUpgrade.BRAM_WHIPLASH)

can_uppies = Or(True_(opts=characters_off), HasAny(Character.ARIAS, Character.BRAM, opts=characters_on), opts=hard)
can_extra_height = Or(has_kyuli, has_block, can_uppies)
can_extra_height_gold_block = Or(has_kyuli, Has(Character.ZEEK), can_uppies)
can_combo_height = And(can_uppies, HasAll(KeyItem.BELL), has_block)
can_magic_block_in_wall = HasAll(Character.ZEEK, KeyItem.BLOCK, opts=hard)
can_gold_block_in_wall = Has(Character.ZEEK, opts=hard)
can_crystal = Or(has_algus, has_block, has_banish, And(has_kyuli_ray, opts=hard))
can_crystal_whiplash = Or(can_crystal, has_bram_whiplash)
can_big_magic = And(has_banish, has_algus_arcanist, opts=hard)
can_kill_ghosts = Or(
    has_banish,
    has_block,
    And(has_algus_meteor, Has(KeyItem.CHALICE), opts=easy),
    And(has_algus_meteor, opts=hard),
)

elevator_apex = Or(
    HasAll(KeyItem.ASCENDANT_KEY, Elevator.APEX, opts=elevator_on + free_apex_off),
    Has(KeyItem.ASCENDANT_KEY, opts=free_apex_on),
)

ENTRANCE_RULES2: Dict[Tuple[R, R], Rule] = {
    (R.SHOP, R.SHOP_ALGUS): has_algus,
    (R.SHOP, R.SHOP_ARIAS): has_arias,
    (R.SHOP, R.SHOP_KYULI): has_kyuli,
    (R.SHOP, R.SHOP_ZEEK): Has(Character.ZEEK),
    (R.SHOP, R.SHOP_BRAM): Has(Character.BRAM),
    (R.GT_ENTRANCE, R.GT_BESTIARY): Or(HasBlueDoor(BlueDoor.GT_HUNTER), True_(opts=blue_off)),
    (R.GT_ENTRANCE, R.GT_BABY_GORGON): And(
        Has(Eye.GREEN),
        Or(
            Has(KeyItem.CLAW),
            And(
                Has(Character.ZEEK),
                Or(And(has_kyuli, Has(KeyItem.BELL)), Has(KeyItem.BLOCK)),
                opts=hard,
            ),
        ),
    ),
    (R.GT_ENTRANCE, R.GT_BOTTOM): Or(HasWhiteDoor(WhiteDoor.GT_START), True_(opts=white_off)),
    (R.GT_ENTRANCE, R.GT_VOID): Has(KeyItem.VOID),
    (R.GT_ENTRANCE, R.GT_GORGONHEART): Or(HasSwitch(Switch.GT_GH_SHORTCUT), Has(KeyItem.ICARUS), has_boots),
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
    (R.GT_BOTTOM, R.GT_GORGONHEART): Or(HasWhiteDoor(WhiteDoor.GT_MAP), True_(opts=white_off)),
}
