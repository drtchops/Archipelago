from rule_builder.options import OptionFilter
from rule_builder.rules import Filtered, Rule, True_

from ..bases import AstalonWorldBase
from ..items import (
    BlueDoor,
    Character,
    Crystal,
    Elevator,
    Events,
    Eye,
    Face,
    KeyItem,
    RedDoor,
    ShopUpgrade,
    Switch,
    WhiteDoor,
)
from ..locations import LocationName as L
from ..options import (
    ApexElevator,
    Difficulty,
    RandomizeBlueKeys,
    RandomizeCharacters,
    RandomizeRedKeys,
    RandomizeSwitches,
    RandomizeWhiteKeys,
)
from ..regions import RegionName as R
from .custom_rules import (
    CanReachEntrance,
    CanReachRegion,
    HardLogic,
    Has,
    HasAll,
    HasBlue,
    HasElevator,
    HasGoal,
    HasRed,
    HasSwitch,
    HasWhite,
)

easy = [OptionFilter(Difficulty, Difficulty.option_easy)]
characters_off = [OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla)]
characters_on = [OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla, operator="gt")]
white_off = [OptionFilter(RandomizeWhiteKeys, RandomizeWhiteKeys.option_false)]
blue_off = [OptionFilter(RandomizeBlueKeys, RandomizeBlueKeys.option_false)]
red_off = [OptionFilter(RandomizeRedKeys, RandomizeRedKeys.option_false)]
switch_off = [OptionFilter(RandomizeSwitches, RandomizeSwitches.option_false)]

has_algus = True_(options=characters_off) | Has(Character.ALGUS, options=characters_on)
has_arias = True_(options=characters_off) | Has(Character.ARIAS, options=characters_on)
has_kyuli = True_(options=characters_off) | Has(Character.KYULI, options=characters_on)
has_bram = Has(Character.BRAM)
has_zeek = Has(Character.ZEEK)

has_cloak = has_algus & Has(KeyItem.CLOAK)
has_sword = has_arias & Has(KeyItem.SWORD)
has_boots = has_arias & Has(KeyItem.BOOTS)
has_claw = has_kyuli & Has(KeyItem.CLAW)
has_bow = has_kyuli & Has(KeyItem.BOW)
has_block = has_zeek & Has(KeyItem.BLOCK)
has_star = has_bram & Has(KeyItem.STAR)
has_banish = (has_algus | has_zeek) & Has(KeyItem.BANISH)
has_gauntlet = (has_arias | has_bram) & Has(KeyItem.GAUNTLET)

has_algus_arcanist = has_algus & Has(ShopUpgrade.ALGUS_ARCANIST)
has_algus_meteor = has_algus & Has(ShopUpgrade.ALGUS_METEOR)
has_algus_shock = has_algus & Has(ShopUpgrade.ALGUS_SHOCK)
has_arias_gorgonslayer = has_arias & Has(ShopUpgrade.ARIAS_GORGONSLAYER)
has_arias_last_stand = has_arias & Has(ShopUpgrade.ARIAS_LAST_STAND)
has_arias_lionheart = has_arias & Has(ShopUpgrade.ARIAS_LIONHEART)
has_kyuli_assassin = has_kyuli & Has(ShopUpgrade.KYULI_ASSASSIN)
has_kyuli_bullseye = has_kyuli & Has(ShopUpgrade.KYULI_BULLSEYE)
has_kyuli_ray = has_kyuli & Has(ShopUpgrade.KYULI_RAY)
has_zeek_junkyard = has_zeek & Has(ShopUpgrade.ZEEK_JUNKYARD)
has_zeek_orbs = has_zeek & Has(ShopUpgrade.ZEEK_ORBS)
has_zeek_loot = has_zeek & Has(ShopUpgrade.ZEEK_LOOT)
has_bram_axe = has_bram & Has(ShopUpgrade.BRAM_AXE)
has_bram_hunter = has_bram & Has(ShopUpgrade.BRAM_HUNTER)
has_bram_whiplash = has_bram & Has(ShopUpgrade.BRAM_WHIPLASH)
chalice_on_easy = HardLogic(True_()) | Has(KeyItem.CHALICE, options=easy)

# can_uppies = Macro(
#     HardLogic(has_arias | has_bram),
#     "Can do uppies",
#     "Perform a higher jump by jumping while attacking with Arias or Bram",
# )
can_uppies = HardLogic(has_arias | has_bram)
can_extra_height = has_kyuli | has_block | can_uppies
can_extra_height_gold_block = has_kyuli | has_zeek | can_uppies
can_combo_height = can_uppies & has_block & Has(KeyItem.BELL)
can_block_in_wall = HardLogic(has_block)
can_crystal_limited = has_algus | HardLogic(has_kyuli_ray)
can_crystal_no_whiplash = can_crystal_limited | has_block | (has_zeek & has_banish)
can_crystal_no_block = can_crystal_limited | has_bram_whiplash
can_crystal = can_crystal_no_whiplash | has_bram_whiplash
can_big_magic = HardLogic(has_algus_arcanist & has_banish)
can_kill_ghosts = has_banish | has_block | (has_algus_meteor & chalice_on_easy)

otherwise_crystal = can_crystal << switch_off
otherwise_bow = has_bow << switch_off

elevator_apex = HasElevator(
    Elevator.APEX,
    options=[OptionFilter(ApexElevator, ApexElevator.option_included)],
) | Has(
    KeyItem.ASCENDANT_KEY,
    options=[OptionFilter(ApexElevator, ApexElevator.option_vanilla)],
)

# TODO: better implementations
shop_cheap = CanReachRegion(R.GT_LEFT)
shop_moderate = CanReachRegion(R.MECH_START)
shop_expensive = CanReachRegion(R.ROA_START)

MAIN_ENTRANCE_RULES: dict[tuple[R, R], Rule[AstalonWorldBase]] = {
    (R.SHOP, R.SHOP_ALGUS): has_algus,
    (R.SHOP, R.SHOP_ARIAS): has_arias,
    (R.SHOP, R.SHOP_KYULI): has_kyuli,
    (R.SHOP, R.SHOP_ZEEK): has_zeek,
    (R.SHOP, R.SHOP_BRAM): has_bram,
    (R.GT_ENTRANCE, R.GT_BESTIARY): HasBlue(BlueDoor.GT_HUNTER, otherwise=True),
    (R.GT_ENTRANCE, R.GT_BABY_GORGON): (
        Has(Eye.GREEN) & (has_claw | HardLogic(has_zeek & ((has_kyuli & Has(KeyItem.BELL)) | has_block)))
    ),
    (R.GT_ENTRANCE, R.GT_BOTTOM): (
        HasSwitch(Switch.GT_2ND_ROOM) | HasWhite(WhiteDoor.GT_START, otherwise=True, options=switch_off)
    ),
    (R.GT_ENTRANCE, R.GT_VOID): Has(KeyItem.VOID),
    (R.GT_ENTRANCE, R.GT_GORGONHEART): HasSwitch(Switch.GT_GH_SHORTCUT) | has_boots | HardLogic(Has(KeyItem.ICARUS)),
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
    (R.GT_BOTTOM, R.GT_UPPER_PATH): (
        HasSwitch(Crystal.GT_ROTA) | can_uppies | (has_star & HasBlue(BlueDoor.GT_RING, otherwise=True)) | has_block
    ),
    (R.GT_BOTTOM, R.CAVES_START): has_kyuli | HardLogic(has_zeek | has_boots),
    (R.GT_VOID, R.GT_BOTTOM): Has(Eye.RED),
    (R.GT_VOID, R.MECH_SNAKE): HasSwitch(Switch.MECH_SNAKE_2),
    (R.GT_GORGONHEART, R.GT_ORBS_DOOR): HasBlue(BlueDoor.GT_ORBS, otherwise=True),
    (R.GT_GORGONHEART, R.GT_LEFT): HasSwitch(Switch.GT_CROSSES) | HasSwitch(Switch.GT_1ST_CYCLOPS, otherwise=True),
    (R.GT_LEFT, R.GT_GORGONHEART): HasSwitch(Switch.GT_CROSSES, otherwise=True) | HasSwitch(Switch.GT_1ST_CYCLOPS),
    (R.GT_LEFT, R.GT_ORBS_HEIGHT): can_extra_height,
    (R.GT_LEFT, R.GT_ASCENDANT_KEY): HasBlue(BlueDoor.GT_ASCENDANT, otherwise=True),
    (R.GT_LEFT, R.GT_TOP_LEFT): (
        HasSwitch(Switch.GT_ARIAS) | has_arias | has_claw | (has_block & has_kyuli & Has(KeyItem.BELL))
    ),
    (R.GT_LEFT, R.GT_TOP_RIGHT): can_extra_height,
    (R.GT_TOP_LEFT, R.GT_BUTT): (
        HasSwitch(Switch.GT_BUTT_ACCESS) | CanReachRegion(R.GT_SPIKE_TUNNEL_SWITCH, options=switch_off)
    ),
    (R.GT_TOP_RIGHT, R.GT_SPIKE_TUNNEL): (
        HasSwitch(Switch.GT_SPIKE_TUNNEL) | CanReachRegion(R.GT_TOP_LEFT, options=switch_off)
    ),
    (R.GT_SPIKE_TUNNEL, R.GT_TOP_RIGHT): HasSwitch(Switch.GT_SPIKE_TUNNEL),
    (R.GT_SPIKE_TUNNEL, R.GT_SPIKE_TUNNEL_SWITCH): can_extra_height,
    (R.GT_SPIKE_TUNNEL_SWITCH, R.GT_BUTT): HardLogic(has_star) | Filtered(has_star & Has(KeyItem.BELL), options=easy),
    (R.GT_BUTT, R.GT_TOP_LEFT): HasSwitch(Switch.GT_BUTT_ACCESS),
    (R.GT_BUTT, R.GT_SPIKE_TUNNEL_SWITCH): has_star,
    (R.GT_BUTT, R.GT_BOSS): HasWhite(WhiteDoor.GT_TAUROS) | CanReachRegion(R.GT_TOP_RIGHT, options=white_off),
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
    (R.GT_UPPER_ARIAS, R.GT_OLD_MAN_FORK): (
        HasSwitch(Crystal.GT_LADDER) | CanReachRegion(R.GT_LADDER_SWITCH, options=switch_off)
    ),
    (R.GT_UPPER_ARIAS, R.MECH_SWORD_CONNECTION): (
        has_arias | HasSwitch(Switch.GT_UPPER_ARIAS) | CanReachRegion(R.GT_ARIAS_SWORD_SWITCH, options=switch_off)
    ),
    (R.GT_OLD_MAN_FORK, R.GT_UPPER_ARIAS): (
        HasSwitch(Crystal.GT_LADDER) | CanReachRegion(R.GT_LADDER_SWITCH, options=switch_off)
    ),
    (R.GT_OLD_MAN_FORK, R.GT_SWORD_FORK): HasBlue(BlueDoor.GT_SWORD, otherwise=True),
    (R.GT_OLD_MAN_FORK, R.GT_OLD_MAN): (
        # TODO: you don't need both switches, revisit when adding old man
        has_claw | HasSwitch(Crystal.GT_OLD_MAN_1, Crystal.GT_OLD_MAN_2) | otherwise_crystal
    ),
    (R.GT_SWORD_FORK, R.GT_SWORD): HasSwitch(Switch.GT_SWORD_ACCESS, otherwise=True),
    (R.GT_SWORD_FORK, R.GT_ARIAS_SWORD_SWITCH): has_sword | (has_bow & Has(KeyItem.BELL)),
    (R.GT_UPPER_PATH, R.GT_UPPER_PATH_CONNECTION): HasSwitch(Switch.GT_UPPER_PATH_ACCESS),
    (R.GT_UPPER_PATH_CONNECTION, R.GT_UPPER_PATH): HasSwitch(Switch.GT_UPPER_PATH_ACCESS, otherwise=True),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_SWORD_CONNECTION): HasSwitch(Switch.MECH_TO_UPPER_GT),
    (R.GT_UPPER_PATH_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): HasSwitch(Switch.MECH_TO_UPPER_GT),
    (R.MECH_START, R.GT_LADDER_SWITCH): Has(Eye.RED) & can_crystal,
    (R.MECH_START, R.MECH_BK): HasBlue(BlueDoor.MECH_SHORTCUT, otherwise=True) & can_extra_height,
    (R.MECH_START, R.MECH_WATCHER): (
        (HasSwitch(Switch.MECH_CANNON) | otherwise_crystal)
        & (
            HasWhite(WhiteDoor.MECH_2ND)
            | Filtered(
                CanReachRegion(R.MECH_SWORD_CONNECTION) & HasSwitch(Switch.MECH_LOWER_KEY, otherwise=True),
                options=white_off,
            )
        )
    ),
    (R.MECH_START, R.MECH_LINUS): HasSwitch(Crystal.MECH_LINUS) | otherwise_crystal,
    (R.MECH_START, R.MECH_LOWER_VOID): HasBlue(BlueDoor.MECH_RED, otherwise=True),
    (R.MECH_START, R.MECH_SACRIFICE): can_extra_height,
    (R.MECH_START, R.GT_BOSS): Has(Eye.RED),
    (R.MECH_LINUS, R.MECH_START): HasSwitch(Crystal.MECH_LINUS) | otherwise_crystal,
    (R.MECH_LINUS, R.MECH_SWORD_CONNECTION): HasSwitch(Switch.MECH_LINUS, otherwise=True),
    (R.MECH_SWORD_CONNECTION, R.MECH_BOOTS_CONNECTION): (
        HasBlue(BlueDoor.MECH_BOOTS, otherwise=True)
        & (
            HasSwitch(Crystal.MECH_LOWER)
            | otherwise_crystal
            | has_claw
            | has_cloak
            | (has_kyuli & Has(KeyItem.ICARUS))
            | HardLogic(has_boots)
        )
    ),
    (R.MECH_SWORD_CONNECTION, R.GT_UPPER_PATH_CONNECTION): HasSwitch(Switch.MECH_TO_UPPER_GT),
    (R.MECH_SWORD_CONNECTION, R.MECH_LOWER_ARIAS): has_arias,
    (R.MECH_SWORD_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): HasSwitch(Switch.MECH_TO_UPPER_GT),
    (R.MECH_SWORD_CONNECTION, R.MECH_LINUS): HasSwitch(Switch.MECH_LINUS),
    (R.MECH_SWORD_CONNECTION, R.GT_UPPER_ARIAS): has_arias | HasSwitch(Switch.GT_UPPER_ARIAS),
    (R.MECH_BOOTS_CONNECTION, R.MECH_BOTTOM_CAMPFIRE): HasBlue(BlueDoor.MECH_VOID, otherwise=True),
    (R.MECH_BOOTS_CONNECTION, R.MECH_BOOTS_LOWER): (
        HasSwitch(Switch.MECH_BOOTS) | Filtered(Has(Eye.RED) | has_star, options=switch_off)
    ),
    (R.MECH_BOOTS_LOWER, R.MECH_BOOTS_UPPER): HasSwitch(Switch.MECH_BOOTS_LOWER, otherwise=True) | can_extra_height,
    (R.MECH_BOTTOM_CAMPFIRE, R.GT_UPPER_PATH_CONNECTION): HasSwitch(Switch.MECH_TO_UPPER_GT, otherwise=True),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_BOOTS_CONNECTION): HasBlue(BlueDoor.MECH_VOID, otherwise=True),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_SNAKE): HasSwitch(Switch.MECH_SNAKE_1, otherwise=True),
    (R.MECH_BOTTOM_CAMPFIRE, R.MECH_SWORD_CONNECTION): HasSwitch(Switch.MECH_TO_UPPER_GT, otherwise=True),
    (R.MECH_SNAKE, R.MECH_BOTTOM_CAMPFIRE): HasSwitch(Switch.MECH_SNAKE_1),
    (R.MECH_SNAKE, R.GT_VOID): HasSwitch(Switch.MECH_SNAKE_2, otherwise=True),
    (R.MECH_LOWER_VOID, R.MECH_START): HasBlue(BlueDoor.MECH_RED, otherwise=True),
    (R.MECH_LOWER_VOID, R.MECH_UPPER_VOID): Has(KeyItem.VOID),
    (R.MECH_LOWER_VOID, R.HOTP_MECH_VOID_CONNECTION): Has(Eye.BLUE),
    (R.MECH_WATCHER, R.MECH_START): HasSwitch(Switch.MECH_CANNON) & HasWhite(WhiteDoor.MECH_2ND),
    (R.MECH_WATCHER, R.MECH_ROOTS): has_claw | HasSwitch(Switch.MECH_WATCHER, otherwise=True),
    (R.MECH_ROOTS, R.MECH_ZEEK_CONNECTION): has_claw & has_block & Has(KeyItem.BELL),
    (R.MECH_ROOTS, R.MECH_MUSIC): HasBlue(BlueDoor.MECH_MUSIC, otherwise=True),
    (R.MECH_BK, R.MECH_START): HasBlue(BlueDoor.MECH_SHORTCUT, otherwise=True) & (has_kyuli | can_combo_height),
    (R.MECH_BK, R.MECH_AFTER_BK): HasSwitch(Crystal.MECH_BK) | otherwise_crystal,
    (R.MECH_BK, R.MECH_ROOTS): HasSwitch(Crystal.MECH_CAMPFIRE) | otherwise_crystal,
    (R.MECH_BK, R.MECH_TRIPLE_SWITCHES): (
        can_crystal
        & HasSwitch(
            Crystal.MECH_BK,
            Switch.MECH_TO_BOSS_1,
            Crystal.MECH_TRIPLE_1,
            Crystal.MECH_TRIPLE_2,
            Crystal.MECH_TRIPLE_3,
        )
        & (HasWhite(WhiteDoor.MECH_BK) | HasSwitch(Switch.MECH_CHAINS))
    ),
    (R.MECH_AFTER_BK, R.MECH_CHAINS_CANDLE): has_claw | HasWhite(WhiteDoor.MECH_BK, otherwise=True),
    (R.MECH_AFTER_BK, R.MECH_CHAINS): HasSwitch(Switch.MECH_CHAINS),
    (R.MECH_AFTER_BK, R.MECH_BK): HasSwitch(Crystal.MECH_BK) | HardLogic(has_kyuli_ray, options=switch_off),
    (R.MECH_AFTER_BK, R.HOTP_EPIMETHEUS): has_claw,
    (R.MECH_CHAINS, R.MECH_CHAINS_CANDLE): has_claw,
    (R.MECH_CHAINS, R.MECH_ARIAS_EYEBALL): has_arias,
    (R.MECH_CHAINS, R.MECH_SPLIT_PATH): HasSwitch(Switch.MECH_SPLIT_PATH, otherwise=True),
    (R.MECH_CHAINS, R.MECH_BOSS_SWITCHES): HasSwitch(Switch.MECH_TO_BOSS_1),
    (R.MECH_CHAINS, R.MECH_BOSS_CONNECTION): (
        has_claw
        | HasSwitch(Switch.MECH_TO_BOSS_2)
        | HasSwitch(Crystal.MECH_TO_BOSS_3)
        | HardLogic(can_big_magic | has_kyuli_ray, options=switch_off)
    ),
    (R.MECH_CHAINS, R.MECH_AFTER_BK): HasSwitch(Switch.MECH_CHAINS, otherwise=True),
    (R.MECH_ARIAS_EYEBALL, R.MECH_ZEEK_CONNECTION): (
        HasSwitch(Switch.MECH_ARIAS, otherwise=True) | (has_star & Has(KeyItem.BELL))
    ),
    (R.MECH_ARIAS_EYEBALL, R.MECH_CHAINS): (
        has_arias & Has(KeyItem.BELL) & (has_algus | has_bram_whiplash) & (HasSwitch(Switch.MECH_ARIAS) | has_star)
    ),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ARIAS_EYEBALL): HasSwitch(Switch.MECH_ARIAS) | (has_star & has_arias),
    (R.MECH_ZEEK_CONNECTION, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.MECH_ZEEK_CONNECTION, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.MECH_ZEEK_CONNECTION, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.MECH_ZEEK_CONNECTION, R.TR_START): HasElevator(Elevator.TR),
    (R.MECH_ZEEK_CONNECTION, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.MECH_ZEEK_CONNECTION, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_ZEEK): HasRed(RedDoor.ZEEK) | CanReachRegion(R.MECH_LOWER_VOID, options=red_off),
    (R.MECH_ZEEK_CONNECTION, R.APEX): elevator_apex,
    (R.MECH_ZEEK_CONNECTION, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.MECH_ZEEK_CONNECTION, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.MECH_SPLIT_PATH, R.MECH_CHAINS): HasSwitch(Switch.MECH_SPLIT_PATH),
    (R.MECH_RIGHT, R.MECH_TRIPLE_SWITCHES): HardLogic(
        HasSwitch(
            Switch.MECH_SPLIT_PATH,
            Switch.MECH_TO_BOSS_1,
            Crystal.MECH_TRIPLE_1,
            Crystal.MECH_TRIPLE_2,
            Crystal.MECH_TRIPLE_3,
        )
        & has_star
        & has_bram_whiplash
    ),
    (R.MECH_RIGHT, R.MECH_OLD_MAN): (
        HasSwitch(Crystal.MECH_OLD_MAN) | otherwise_crystal | (has_kyuli & has_block & Has(KeyItem.BELL))
    ),
    (R.MECH_RIGHT, R.MECH_SPLIT_PATH): has_star,
    (R.MECH_RIGHT, R.MECH_BELOW_POTS): (
        HasWhite(WhiteDoor.MECH_ARENA, otherwise=True) | HasSwitch(Switch.MECH_EYEBALL)
    ),
    (R.MECH_RIGHT, R.MECH_UPPER_VOID): (
        HasSwitch(Switch.MECH_UPPER_VOID) | (has_claw & HasSwitch(Switch.MECH_UPPER_VOID_DROP, otherwise=True))
    ),
    (R.MECH_UPPER_VOID, R.MECH_RIGHT): HasSwitch(Switch.MECH_UPPER_VOID, otherwise=True),
    (R.MECH_UPPER_VOID, R.MECH_LOWER_VOID): Has(KeyItem.VOID),
    (R.MECH_BELOW_POTS, R.MECH_RIGHT): (
        HasWhite(WhiteDoor.MECH_ARENA) | HasSwitch(Switch.MECH_EYEBALL, otherwise=True)
    ),
    (R.MECH_BELOW_POTS, R.MECH_POTS): HasSwitch(Switch.MECH_POTS, otherwise=True),
    (R.MECH_POTS, R.MECH_BELOW_POTS): HasSwitch(Switch.MECH_POTS),
    (R.MECH_POTS, R.MECH_TOP): HasSwitch(Switch.MECH_POTS, otherwise=True),
    (R.MECH_TOP, R.MECH_POTS): HasSwitch(Switch.MECH_POTS),
    (R.MECH_TOP, R.MECH_TP_CONNECTION): (
        has_claw
        | HasWhite(WhiteDoor.MECH_TOP)
        | Filtered(can_extra_height & (HasSwitch(Crystal.MECH_TOP) | otherwise_crystal), options=white_off)
    ),
    (R.MECH_TOP, R.MECH_CD_ACCESS): (
        Has(Eye.BLUE)
        & HasBlue(BlueDoor.MECH_CD, otherwise=True)
        & (HasSwitch(Crystal.MECH_TO_CD) | otherwise_crystal | (has_kyuli & has_block & Has(KeyItem.BELL)))
    ),
    (R.MECH_CD_ACCESS, R.CD_START): Has(KeyItem.CYCLOPS),
    (R.MECH_TOP, R.MECH_TRIPLE_SWITCHES): (
        can_crystal
        & (HasSwitch(Switch.MECH_ARIAS_CYCLOPS) | (has_arias << switch_off))
        & (
            HasWhite(WhiteDoor.MECH_TOP)
            | Filtered(can_extra_height & (HasSwitch(Crystal.MECH_TOP) | otherwise_crystal), options=white_off)
            | (has_claw & Has(KeyItem.BELL))
        )
    ),
    (R.MECH_TP_CONNECTION, R.HOTP_FALL_BOTTOM): has_claw | HasSwitch(Switch.MECH_MAZE_BACKDOOR),
    (R.MECH_TP_CONNECTION, R.MECH_TOP): has_claw | HasWhite(WhiteDoor.MECH_TOP),
    (R.MECH_TP_CONNECTION, R.MECH_CHARACTER_SWAPS): (
        (has_arias & (HasWhite(WhiteDoor.MECH_TOP, otherwise=True) | Has(KeyItem.BELL)))
        | HasSwitch(Switch.MECH_ARIAS_CYCLOPS)
    ),
    (R.MECH_CHARACTER_SWAPS, R.MECH_CLOAK_CONNECTION): (
        (HasSwitch(Crystal.MECH_TRIPLE_1, Crystal.MECH_TRIPLE_2, Crystal.MECH_TRIPLE_3) | otherwise_crystal)
        & can_extra_height
    ),
    (R.MECH_CHARACTER_SWAPS, R.MECH_TP_CONNECTION): has_arias | HasSwitch(Switch.MECH_ARIAS_CYCLOPS, otherwise=True),
    (R.MECH_CLOAK_CONNECTION, R.MECH_CHARACTER_SWAPS): HasSwitch(
        Crystal.MECH_TRIPLE_1,
        Crystal.MECH_TRIPLE_2,
        Crystal.MECH_TRIPLE_3,
    ),
    (R.MECH_CLOAK_CONNECTION, R.MECH_CLOAK): Has(Eye.BLUE) & (HasSwitch(Crystal.MECH_CLOAK) | otherwise_crystal),
    (R.MECH_BOSS_SWITCHES, R.MECH_CLOAK_CONNECTION): (
        HasSwitch(Switch.MECH_BLOCK_STAIRS) | HasSwitch(Crystal.MECH_SLIMES) | otherwise_crystal
    ),
    (R.MECH_BOSS_SWITCHES, R.MECH_CHAINS): HasSwitch(Switch.MECH_TO_BOSS_1, otherwise=True),
    (R.MECH_BOSS_SWITCHES, R.MECH_BOSS_CONNECTION): HasSwitch(
        Switch.MECH_TO_BOSS_1,
        Switch.MECH_TO_BOSS_2,
        otherwise=True,
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_BOSS): (
        HasSwitch(Switch.MECH_BOSS_2, otherwise=True) | (has_block & Has(KeyItem.BELL) & (has_kyuli | can_uppies))
    ),
    (R.MECH_BOSS_CONNECTION, R.MECH_BRAM_TUNNEL_CONNECTION): HasSwitch(Switch.MECH_BOSS_1, otherwise=True),
    (R.MECH_BRAM_TUNNEL_CONNECTION, R.MECH_BOSS_CONNECTION): HasSwitch(Switch.MECH_BOSS_1),
    (R.MECH_BRAM_TUNNEL_CONNECTION, R.MECH_BRAM_TUNNEL): has_star,
    (R.MECH_BRAM_TUNNEL, R.MECH_BRAM_TUNNEL_CONNECTION): has_star,
    (R.MECH_BRAM_TUNNEL, R.HOTP_START_BOTTOM): has_star,
    (R.MECH_BOSS, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.MECH_BOSS, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.MECH_BOSS, R.TR_START): HasElevator(Elevator.TR),
    (R.MECH_BOSS, R.MECH_TRIPLE_SWITCHES): (
        can_crystal
        & HasSwitch(Switch.MECH_TO_BOSS_1, Crystal.MECH_TRIPLE_1, Crystal.MECH_TRIPLE_2, Crystal.MECH_TRIPLE_3)
    ),
    (R.MECH_BOSS, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.MECH_BOSS, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.MECH_BOSS, R.APEX): elevator_apex,
    (R.MECH_BOSS, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.MECH_BOSS, R.HOTP_START): Has(Eye.BLUE),
    (R.MECH_BOSS, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.MECH_BOSS, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.HOTP_START, R.MECH_BOSS): Has(Eye.BLUE),
    (R.HOTP_START, R.HOTP_START_BOTTOM): (
        has_star
        | (Has(Eye.BLUE) & (HasWhite(WhiteDoor.HOTP_START) | CanReachRegion(R.HOTP_START_LEFT, options=white_off)))
    ),
    (R.HOTP_START, R.HOTP_START_MID): HasSwitch(Switch.HOTP_1ST_ROOM, otherwise=True),
    (R.HOTP_START_MID, R.HOTP_START_LEFT): (
        HasSwitch(Switch.HOTP_LEFT_3, otherwise=True)
        | (has_star & HasSwitch(Switch.HOTP_LEFT_1, Switch.HOTP_LEFT_2, otherwise=True))
    ),
    (R.HOTP_START_MID, R.HOTP_START_BOTTOM_MID): HasSwitch(Switch.HOTP_GHOSTS, otherwise=True),
    (R.HOTP_START_MID, R.HOTP_LOWER_VOID): HardLogic(has_algus | has_bram_whiplash),
    (R.HOTP_LOWER_VOID, R.HOTP_UPPER_VOID): Has(KeyItem.VOID) & has_claw,
    (R.HOTP_START_LEFT, R.HOTP_ELEVATOR): HasSwitch(Switch.HOTP_LEFT_BACKTRACK),
    (R.HOTP_START_LEFT, R.HOTP_START_MID): (
        HasSwitch(Switch.HOTP_LEFT_3) | (has_star & HasSwitch(Switch.HOTP_LEFT_1, Switch.HOTP_LEFT_2, otherwise=True))
    ),
    (R.HOTP_START_BOTTOM, R.MECH_BRAM_TUNNEL): has_star,
    (R.HOTP_START_BOTTOM, R.HOTP_START): has_star | (HasWhite(WhiteDoor.HOTP_START) & Has(Eye.BLUE)),
    (R.HOTP_START_BOTTOM, R.HOTP_START_BOTTOM_MID): has_block & has_star & Has(KeyItem.BELL),
    (R.HOTP_START_BOTTOM, R.HOTP_LOWER): (
        HasSwitch(Switch.HOTP_BELOW_START) | CanReachRegion(R.HOTP_START_BOTTOM_MID, options=switch_off)
    ),
    (R.HOTP_START_BOTTOM_MID, R.HOTP_START_MID): HasSwitch(Switch.HOTP_GHOSTS),
    (R.HOTP_START_BOTTOM_MID, R.HOTP_START_BOTTOM): has_star,
    (R.HOTP_LOWER, R.HOTP_START_BOTTOM): HasSwitch(Switch.HOTP_BELOW_START),
    (R.HOTP_LOWER, R.HOTP_EPIMETHEUS): HasBlue(BlueDoor.HOTP_STATUE, otherwise=True),
    (R.HOTP_LOWER, R.HOTP_TP_TUTORIAL): (
        HasSwitch(Crystal.HOTP_LOWER) | HasSwitch(Switch.HOTP_LOWER_SHORTCUT) | otherwise_crystal
    ),
    (R.HOTP_LOWER, R.HOTP_MECH_VOID_CONNECTION): (
        HasSwitch(Crystal.HOTP_BOTTOM) | HardLogic(has_kyuli_ray, options=switch_off)
    ),
    (R.HOTP_EPIMETHEUS, R.MECH_AFTER_BK): has_claw,
    (R.HOTP_MECH_VOID_CONNECTION, R.HOTP_AMULET_CONNECTION): HasSwitch(Crystal.HOTP_ROCK_ACCESS) | otherwise_crystal,
    (R.HOTP_MECH_VOID_CONNECTION, R.MECH_LOWER_VOID): Has(Eye.BLUE),
    (R.HOTP_MECH_VOID_CONNECTION, R.HOTP_LOWER): HasSwitch(Crystal.HOTP_BOTTOM) | otherwise_crystal,
    (R.HOTP_AMULET_CONNECTION, R.HOTP_AMULET): has_claw & HasAll(Eye.RED, Eye.BLUE),
    (R.HOTP_AMULET_CONNECTION, R.GT_BUTT): HasSwitch(Switch.HOTP_ROCK, otherwise=True),
    (R.HOTP_AMULET_CONNECTION, R.HOTP_MECH_VOID_CONNECTION): HasSwitch(Crystal.HOTP_ROCK_ACCESS) | otherwise_crystal,
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_LOWER_ARIAS): has_arias & (Has(KeyItem.BELL) | can_uppies),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_RED_KEY): Has(Eye.GREEN) & has_cloak,
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_CATH_CONNECTION): Has(Eye.GREEN),
    (R.HOTP_BELL_CAMPFIRE, R.HOTP_BELL): (
        HasSwitch(Switch.HOTP_BELL_ACCESS, otherwise=True)
        & (
            HasSwitch(Crystal.HOTP_BELL_ACCESS)
            | otherwise_crystal
            | (has_block & Has(KeyItem.BELL) & (has_kyuli | can_uppies))
            | HardLogic(has_claw)
        )
    ),
    (R.HOTP_CATH_CONNECTION, R.CATH_START): (
        Has(KeyItem.VOID) & has_claw & (HasRed(RedDoor.CATH) | CanReachRegion(R.HOTP_RED_KEY, options=red_off))
    ),
    (R.HOTP_LOWER_ARIAS, R.HOTP_BELL_CAMPFIRE): has_arias,
    (R.HOTP_LOWER_ARIAS, R.HOTP_GHOST_BLOOD): (
        HasSwitch(Switch.HOTP_TELEPORTS, otherwise=True) | (has_block & Has(KeyItem.BELL) & (has_kyuli | can_uppies))
    ),
    (R.HOTP_GHOST_BLOOD, R.HOTP_EYEBALL): HasSwitch(Switch.HOTP_GHOST_BLOOD, otherwise=True),
    (R.HOTP_GHOST_BLOOD, R.HOTP_WORM_SHORTCUT): HasSwitch(Switch.HOTP_EYEBALL_SHORTCUT),
    (R.HOTP_WORM_SHORTCUT, R.HOTP_GHOST_BLOOD): HasSwitch(Switch.HOTP_EYEBALL_SHORTCUT, otherwise=True),
    (R.HOTP_WORM_SHORTCUT, R.HOTP_ELEVATOR): HasSwitch(Switch.HOTP_WORM_PILLAR),
    (R.HOTP_ELEVATOR, R.HOTP_OLD_MAN): has_cloak & (HasSwitch(Face.HOTP_OLD_MAN) | otherwise_bow),
    (R.HOTP_ELEVATOR, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.HOTP_ELEVATOR, R.HOTP_TOP_LEFT): has_claw,
    (R.HOTP_ELEVATOR, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.HOTP_ELEVATOR, R.TR_START): HasElevator(Elevator.TR),
    (R.HOTP_ELEVATOR, R.HOTP_START_LEFT): HasSwitch(Switch.HOTP_LEFT_BACKTRACK, otherwise=True),
    (R.HOTP_ELEVATOR, R.HOTP_WORM_SHORTCUT): HasSwitch(Switch.HOTP_WORM_PILLAR, otherwise=True),
    (R.HOTP_ELEVATOR, R.HOTP_SPIKE_TP_SECRET): Has(KeyItem.CHALICE),
    (R.HOTP_ELEVATOR, R.HOTP_CLAW_LEFT): (
        (HasSwitch(Switch.HOTP_TO_CLAW_2, otherwise=True) & can_extra_height)
        | (Has(KeyItem.BELL) & ((has_claw & has_cloak) | (has_kyuli & has_block)))
    ),
    (R.HOTP_ELEVATOR, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.HOTP_ELEVATOR, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.HOTP_ELEVATOR, R.APEX): elevator_apex,
    (R.HOTP_ELEVATOR, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.HOTP_ELEVATOR, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.HOTP_ELEVATOR, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.HOTP_CLAW_LEFT, R.HOTP_ELEVATOR): can_extra_height,
    (R.HOTP_CLAW_LEFT, R.HOTP_TOP_LEFT): HasWhite(WhiteDoor.HOTP_CLAW, otherwise=True),
    (R.HOTP_CLAW_LEFT, R.HOTP_CLAW): has_star,
    (R.HOTP_TOP_LEFT, R.HOTP_ABOVE_OLD_MAN): (
        Has(Eye.GREEN)
        & (HasSwitch(Switch.HOTP_TO_ABOVE_OLD_MAN, otherwise=True) | (has_block & Has(KeyItem.BELL) & can_uppies))
    ),
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_CLAW): (
        HasSwitch(Switch.HOTP_CLAW_ACCESS, otherwise=True) & (has_kyuli | can_block_in_wall)
    ),
    (R.HOTP_CLAW_CAMPFIRE, R.HOTP_HEART): HasSwitch(Crystal.HOTP_AFTER_CLAW) | otherwise_crystal,
    (R.HOTP_CLAW, R.HOTP_CLAW_CAMPFIRE): has_claw & HasSwitch(Switch.HOTP_CLAW_ACCESS),
    (R.HOTP_CLAW, R.HOTP_CLAW_LEFT): has_star,
    (R.HOTP_HEART, R.HOTP_CLAW_CAMPFIRE): (
        HasSwitch(Crystal.HOTP_AFTER_CLAW)
        | HardLogic(
            ((has_cloak & has_banish & has_algus_arcanist) | (has_algus & Has(KeyItem.ICARUS)) | has_kyuli_ray),
            options=switch_off,
        )
    ),
    (R.HOTP_HEART, R.HOTP_UPPER_ARIAS): has_arias,
    (R.HOTP_HEART, R.HOTP_BOSS_CAMPFIRE): (
        has_claw & (Has(KeyItem.ICARUS) | (has_block & Has(KeyItem.BELL)) | HasSwitch(Crystal.HOTP_HEART))
    ),
    (R.HOTP_UPPER_ARIAS, R.HOTP_BOSS_CAMPFIRE): has_claw,
    (R.HOTP_BOSS_CAMPFIRE, R.MECH_TRIPLE_SWITCHES): (
        Has(Eye.GREEN) & has_cloak & HasSwitch(Switch.HOTP_TP_PUZZLE, Switch.MECH_ARIAS_CYCLOPS)
    ),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_MAIDEN): (
        HasBlue(BlueDoor.HOTP_MAIDEN, otherwise=True) & (has_sword | (has_kyuli & has_block & Has(KeyItem.BELL)))
    ),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_TP_PUZZLE): Has(Eye.GREEN),
    (R.HOTP_BOSS_CAMPFIRE, R.HOTP_BOSS): HasWhite(WhiteDoor.HOTP_BOSS) | (has_arias << white_off),
    (R.HOTP_TP_PUZZLE, R.HOTP_TP_FALL_TOP): has_star | HasSwitch(Switch.HOTP_TP_PUZZLE, otherwise=True),
    (R.HOTP_TP_FALL_TOP, R.HOTP_FALL_BOTTOM): has_cloak,
    (R.HOTP_TP_FALL_TOP, R.HOTP_TP_PUZZLE): has_star | HasSwitch(Switch.HOTP_TP_PUZZLE),
    (R.HOTP_TP_FALL_TOP, R.HOTP_GAUNTLET_CONNECTION): has_claw,
    (R.HOTP_TP_FALL_TOP, R.HOTP_BOSS_CAMPFIRE): has_kyuli | (has_block & can_combo_height),
    (R.HOTP_GAUNTLET_CONNECTION, R.HOTP_GAUNTLET): has_claw & Has(KeyItem.BELL) & can_kill_ghosts,
    (R.HOTP_FALL_BOTTOM, R.HOTP_TP_FALL_TOP): has_claw,
    (R.HOTP_FALL_BOTTOM, R.HOTP_UPPER_VOID): Has(Eye.GREEN),
    (R.HOTP_UPPER_VOID, R.HOTP_FALL_BOTTOM): Has(Eye.GREEN),
    (R.HOTP_UPPER_VOID, R.HOTP_LOWER_VOID): Has(KeyItem.VOID),
    (R.HOTP_BOSS, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.HOTP_BOSS, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.HOTP_BOSS, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.HOTP_BOSS, R.TR_START): HasElevator(Elevator.TR),
    (R.HOTP_BOSS, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.HOTP_BOSS, R.APEX): elevator_apex,
    (R.HOTP_BOSS, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.HOTP_BOSS, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.HOTP_BOSS, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.ROA_START, R.ROA_WORMS): (
        # this should be more complicated
        HasSwitch(Crystal.ROA_1ST_ROOM) | Filtered(Has(KeyItem.BELL) & can_crystal, options=switch_off)
    ),
    (R.ROA_WORMS, R.ROA_START): (
        HasSwitch(Switch.ROA_WORMS, otherwise=True) | HasSwitch(Crystal.ROA_1ST_ROOM) | otherwise_crystal
    ),
    (R.ROA_WORMS, R.ROA_WORMS_CONNECTION): (
        HasWhite(WhiteDoor.ROA_WORMS) | HasSwitch(Switch.ROA_WORMS, otherwise=True, options=white_off)
    ),
    (R.ROA_WORMS, R.ROA_LOWER_VOID_CONNECTION): has_claw,
    (R.ROA_HEARTS, R.ROA_BOTTOM_ASCEND): HasSwitch(Switch.ROA_1ST_SHORTCUT),
    (R.ROA_WORMS_CONNECTION, R.ROA_WORMS): HasWhite(WhiteDoor.ROA_WORMS),
    (R.ROA_WORMS_CONNECTION, R.ROA_HEARTS): HasSwitch(Switch.ROA_AFTER_WORMS, otherwise=True) | has_star,
    (R.ROA_HEARTS, R.ROA_WORMS_CONNECTION): (
        HasSwitch(Switch.ROA_AFTER_WORMS) | (has_star & Has(KeyItem.BELL) & can_extra_height)
    ),
    (R.ROA_SPIKE_CLIMB, R.ROA_BOTTOM_ASCEND): has_claw,
    (R.ROA_BOTTOM_ASCEND, R.ROA_TOP_ASCENT): HasWhite(WhiteDoor.ROA_ASCEND, otherwise=True),
    (R.ROA_BOTTOM_ASCEND, R.ROA_TRIPLE_REAPER): (
        HasSwitch(Switch.ROA_ASCEND, otherwise=True) | (has_kyuli & has_block & Has(KeyItem.BELL))
    ),
    (R.ROA_TRIPLE_REAPER, R.ROA_ARENA): HasSwitch(Crystal.ROA_3_REAPERS) | otherwise_crystal,
    (R.ROA_ARENA, R.ROA_FLAMES_CONNECTION): has_claw,
    (R.ROA_ARENA, R.ROA_TRIPLE_REAPER): HasSwitch(Crystal.ROA_3_REAPERS),
    (R.ROA_ARENA, R.ROA_LOWER_VOID_CONNECTION): has_kyuli,
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_LOWER_VOID): HasSwitch(Switch.ROA_LOWER_VOID),
    (R.ROA_LOWER_VOID_CONNECTION, R.ROA_ARIAS_BABY_GORGON_CONNECTION): has_kyuli | can_uppies | can_block_in_wall,
    (R.ROA_LOWER_VOID, R.ROA_UPPER_VOID): Has(KeyItem.VOID),
    (R.ROA_LOWER_VOID, R.ROA_LOWER_VOID_CONNECTION): HasSwitch(Switch.ROA_LOWER_VOID, otherwise=True),
    (R.ROA_ARIAS_BABY_GORGON_CONNECTION, R.ROA_ARIAS_BABY_GORGON): (
        has_arias
        & (HardLogic(True_()) | Has(KeyItem.BELL, options=easy))
        & (HasSwitch(Crystal.ROA_BABY_GORGON) | otherwise_crystal)
    ),
    (R.ROA_ARIAS_BABY_GORGON_CONNECTION, R.ROA_FLAMES_CONNECTION): has_star & Has(KeyItem.BELL),
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_FLAMES): (
        HasSwitch(Switch.ROA_BABY_GORGON) & has_block & has_kyuli & Has(KeyItem.BELL)
    ),
    (R.ROA_ARIAS_BABY_GORGON, R.ROA_ARIAS_BABY_GORGON_CONNECTION): has_arias & HasSwitch(Crystal.ROA_BABY_GORGON),
    (R.ROA_FLAMES_CONNECTION, R.ROA_WORM_CLIMB): HasBlue(BlueDoor.ROA_FLAMES, otherwise=True) & has_claw,
    (R.ROA_FLAMES_CONNECTION, R.ROA_LEFT_ASCENT): (
        (HasSwitch(Crystal.ROA_LEFT_ASCEND) | Filtered(can_crystal & Has(KeyItem.BELL), options=switch_off))
        & can_extra_height
    ),
    (R.ROA_FLAMES_CONNECTION, R.ROA_ARIAS_BABY_GORGON_CONNECTION): has_star,
    (R.ROA_FLAMES_CONNECTION, R.ROA_ARIAS_BABY_GORGON): HardLogic(has_bram_axe | has_kyuli_ray),
    (R.ROA_FLAMES_CONNECTION, R.ROA_FLAMES): has_gauntlet & Has(KeyItem.BELL) & can_extra_height,
    (R.ROA_FLAMES_CONNECTION, R.ROA_LEFT_ASCENT_CRYSTAL): Has(KeyItem.BELL) & has_kyuli & can_crystal,
    (R.ROA_FLAMES, R.ROA_ARIAS_BABY_GORGON): HasSwitch(Switch.ROA_BABY_GORGON, otherwise=True),
    (R.ROA_WORM_CLIMB, R.ROA_RIGHT_BRANCH): has_claw,
    (R.ROA_RIGHT_BRANCH, R.ROA_MIDDLE): has_star,
    (R.ROA_LEFT_ASCENT, R.ROA_FLAMES_CONNECTION): (
        # this is overly restrictive, but whatever
        (HasSwitch(Crystal.ROA_LEFT_ASCEND) | otherwise_crystal) & (has_kyuli & Has(KeyItem.BELL))
    ),
    (R.ROA_LEFT_ASCENT, R.ROA_TOP_ASCENT): HasSwitch(Switch.ROA_ASCEND_SHORTCUT),
    (R.ROA_LEFT_ASCENT, R.ROA_LEFT_ASCENT_CRYSTAL): has_algus,
    (R.ROA_TOP_ASCENT, R.ROA_TRIPLE_SWITCH): can_extra_height,
    (R.ROA_TOP_ASCENT, R.ROA_LEFT_ASCENT): HasSwitch(Switch.ROA_ASCEND_SHORTCUT),
    (R.ROA_TOP_ASCENT, R.ROA_MIDDLE): can_extra_height & HasSwitch(Switch.ROA_ASCEND_SHORTCUT),
    (R.ROA_TRIPLE_SWITCH, R.ROA_MIDDLE): (
        (HasSwitch(Switch.ROA_TRIPLE_1, Switch.ROA_TRIPLE_3) | otherwise_crystal) & has_claw & Has(KeyItem.BELL)
    ),
    (R.ROA_MIDDLE, R.ROA_LEFT_SWITCH): can_extra_height,
    (R.ROA_MIDDLE, R.ROA_RIGHT_BRANCH): has_star,
    (R.ROA_MIDDLE, R.ROA_RIGHT_SWITCH_1): has_kyuli | HasSwitch(Switch.ROA_RIGHT_PATH),
    (R.ROA_MIDDLE, R.ROA_MIDDLE_LADDER): (
        # this could allow more
        HasSwitch(Crystal.ROA_LADDER_L, Crystal.ROA_LADDER_R)
        | Filtered(
            can_crystal & CanReachRegion(R.ROA_LEFT_SWITCH) & CanReachRegion(R.ROA_RIGHT_SWITCH_2),
            options=switch_off,
        )
    ),
    (R.ROA_MIDDLE, R.ROA_TOP_ASCENT): HasSwitch(Switch.ROA_ASCEND_SHORTCUT, otherwise=True),
    (R.ROA_MIDDLE, R.ROA_TRIPLE_SWITCH): HasSwitch(Switch.ROA_TRIPLE_1, Switch.ROA_TRIPLE_3),
    (R.ROA_MIDDLE, R.ROA_LEFT_BABY_GORGON): can_extra_height,
    (R.ROA_RIGHT_SWITCH_1, R.ROA_RIGHT_SWITCH_2): can_extra_height,
    (R.ROA_MIDDLE_LADDER, R.ROA_UPPER_VOID): HasSwitch(
        Switch.ROA_SHAFT_L,
        Switch.ROA_SHAFT_R,
        otherwise=True,
    ),
    (R.ROA_MIDDLE_LADDER, R.ROA_RIGHT_SWITCH_CANDLE): has_algus | has_bram_axe | has_bram_whiplash,
    (R.ROA_UPPER_VOID, R.ROA_LOWER_VOID): Has(KeyItem.VOID),
    (R.ROA_UPPER_VOID, R.ROA_SP_CONNECTION): HasSwitch(Crystal.ROA_SHAFT, Switch.ROA_SHAFT_DOWNWARDS),
    (R.ROA_UPPER_VOID, R.ROA_SPIKE_BALLS): HasSwitch(Crystal.ROA_SPIKE_BALLS) | otherwise_crystal,
    (R.ROA_SPIKE_BALLS, R.ROA_SPIKE_SPINNERS): HasWhite(WhiteDoor.ROA_BALLS, otherwise=True),
    (R.ROA_SPIKE_SPINNERS, R.ROA_SPIDERS_1): HasWhite(WhiteDoor.ROA_SPINNERS, otherwise=True),
    (R.ROA_SPIKE_SPINNERS, R.ROA_SPIKE_BALLS): HasWhite(WhiteDoor.ROA_BALLS, otherwise=True),
    (R.ROA_SPIDERS_1, R.ROA_RED_KEY): HasSwitch(Face.ROA_SPIDERS) | otherwise_bow,
    (R.ROA_SPIDERS_1, R.ROA_SPIDERS_2): can_extra_height,
    (R.ROA_SPIDERS_2, R.ROA_BLOOD_POT_HALLWAY): HasSwitch(Switch.ROA_SPIDERS, otherwise=True),
    (R.ROA_SP_CONNECTION, R.SP_START): (
        HasRed(RedDoor.SP)
        | Filtered(has_cloak & has_claw & Has(KeyItem.BELL) & CanReachRegion(R.ROA_RED_KEY), options=red_off)
    ),
    # can probably make it without claw
    (R.ROA_SP_CONNECTION, R.ROA_ELEVATOR): has_claw & HasSwitch(Switch.ROA_DARK_ROOM, otherwise=True),
    (R.ROA_ELEVATOR, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.ROA_ELEVATOR, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.ROA_ELEVATOR, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.ROA_ELEVATOR, R.TR_START): HasElevator(Elevator.TR),
    (R.ROA_ELEVATOR, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.ROA_ELEVATOR, R.ROA_ICARUS): HasSwitch(Switch.ROA_ICARUS, otherwise=True),
    (R.ROA_ELEVATOR, R.ROA_DARK_CONNECTION): has_claw | HasSwitch(Switch.ROA_ELEVATOR, otherwise=True),
    (R.ROA_ELEVATOR, R.APEX): elevator_apex,
    (R.ROA_ELEVATOR, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.ROA_ELEVATOR, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.ROA_ELEVATOR, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.ROA_DARK_CONNECTION, R.ROA_TOP_CENTAUR): HasSwitch(Switch.ROA_BLOOD_POT),
    (R.ROA_DARK_CONNECTION, R.DARK_START): can_extra_height,
    (R.DARK_START, R.DARK_END): has_claw & HasSwitch(Switch.DARKNESS, otherwise=True),
    (R.DARK_END, R.ROA_DARK_EXIT): has_claw,
    (R.ROA_DARK_EXIT, R.ROA_ABOVE_CENTAUR_R): has_arias & Has(KeyItem.BELL) & (HardLogic(True_()) | has_kyuli),
    (R.ROA_DARK_EXIT, R.ROA_CRYSTAL_ABOVE_CENTAUR): HardLogic(has_kyuli_ray),
    (R.ROA_TOP_CENTAUR, R.ROA_DARK_CONNECTION): (
        HasSwitch(Switch.ROA_BLOOD_POT, otherwise=True) | HasBlue(BlueDoor.ROA_BLOOD, otherwise=True)
    ),
    (R.ROA_TOP_CENTAUR, R.ROA_DARK_EXIT): can_extra_height,
    (R.ROA_TOP_CENTAUR, R.ROA_BOSS_CONNECTION): (
        HasSwitch(Crystal.ROA_CENTAUR) | CanReachRegion(R.ROA_CRYSTAL_ABOVE_CENTAUR)
    ),
    (R.ROA_ABOVE_CENTAUR_R, R.ROA_DARK_EXIT): has_arias & Has(KeyItem.BELL),
    (R.ROA_ABOVE_CENTAUR_R, R.ROA_ABOVE_CENTAUR_L): has_star & Has(KeyItem.BELL),
    (R.ROA_ABOVE_CENTAUR_R, R.ROA_CRYSTAL_ABOVE_CENTAUR): can_crystal_no_whiplash,
    (R.ROA_ABOVE_CENTAUR_L, R.ROA_ABOVE_CENTAUR_R): has_star & Has(KeyItem.BELL),
    (R.ROA_ABOVE_CENTAUR_L, R.ROA_CRYSTAL_ABOVE_CENTAUR): can_crystal_no_block,
    (R.ROA_BOSS_CONNECTION, R.ROA_ABOVE_CENTAUR_L): can_extra_height,
    (R.ROA_BOSS_CONNECTION, R.ROA_TOP_CENTAUR): (
        HasSwitch(Crystal.ROA_CENTAUR) | CanReachRegion(R.ROA_CRYSTAL_ABOVE_CENTAUR)
    ),
    (R.ROA_BOSS_CONNECTION, R.ROA_BOSS): HasSwitch(Switch.ROA_BOSS_ACCESS, otherwise=True),
    (R.ROA_BOSS, R.ROA_APEX_CONNECTION): Has(Eye.GREEN),
    (R.ROA_BOSS, R.ROA_BOSS_CONNECTION): HasSwitch(Switch.ROA_BOSS_ACCESS),
    (R.ROA_APEX_CONNECTION, R.ROA_BOSS): Has(Eye.GREEN),
    (R.ROA_APEX_CONNECTION, R.APEX): HasSwitch(Switch.ROA_APEX_ACCESS, otherwise=True),
    (R.APEX, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.APEX, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.APEX, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.APEX, R.FINAL_BOSS): (
        HasAll(Eye.RED, Eye.BLUE, Eye.GREEN) & (HardLogic(True_()) | Has(KeyItem.BELL, options=easy)) & HasGoal()
    ),
    (R.APEX, R.ROA_APEX_CONNECTION): HasSwitch(Switch.ROA_APEX_ACCESS),
    (R.APEX, R.TR_START): HasElevator(Elevator.TR),
    (R.APEX, R.APEX_HEART): can_extra_height,
    (R.APEX, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.APEX, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.APEX, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.APEX, R.APEX_CENTAUR_ACCESS): HasBlue(BlueDoor.APEX, otherwise=True) & has_star,
    (R.APEX, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.APEX, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.APEX_CENTAUR_ACCESS, R.APEX_CENTAUR): Has(KeyItem.ADORNED_KEY),
    (R.CAVES_START, R.CAVES_EPIMETHEUS): HasBlue(BlueDoor.CAVES, otherwise=True),
    (R.CAVES_EPIMETHEUS, R.CAVES_UPPER): has_kyuli | can_block_in_wall | can_combo_height,
    (R.CAVES_EPIMETHEUS, R.CAVES_START): HasBlue(BlueDoor.CAVES, otherwise=True),
    (R.CAVES_UPPER, R.CAVES_ARENA): has_sword | has_kyuli_ray | (has_algus_meteor & chalice_on_easy),
    (R.CAVES_UPPER, R.CAVES_LOWER): HasSwitch(Switch.CAVES_SKELETONS, otherwise=True),
    (R.CAVES_LOWER, R.CAVES_UPPER): HasSwitch(Switch.CAVES_SKELETONS),
    (R.CAVES_LOWER, R.CAVES_ITEM_CHAIN): Has(Eye.RED),
    (R.CAVES_LOWER, R.CATA_START): HasSwitch(
        Switch.CAVES_CATA_1,
        Switch.CAVES_CATA_2,
        Switch.CAVES_CATA_3,
        otherwise=True,
    ),
    (R.CATA_START, R.CATA_CLIMBABLE_ROOT): HasSwitch(Switch.CATA_1ST_ROOM, otherwise=True),
    (R.CATA_START, R.CAVES_LOWER): HasSwitch(Switch.CAVES_CATA_1, Switch.CAVES_CATA_2, Switch.CAVES_CATA_3),
    (R.CATA_CLIMBABLE_ROOT, R.CATA_TOP): Has(Eye.RED) & HasWhite(WhiteDoor.CATA_TOP, otherwise=True),
    (R.CATA_TOP, R.CATA_CLIMBABLE_ROOT): Has(Eye.RED) & HasWhite(WhiteDoor.CATA_TOP, otherwise=True),
    (R.CATA_TOP, R.CATA_ELEVATOR): HasSwitch(Switch.CATA_ELEVATOR, otherwise=True),
    (R.CATA_TOP, R.CATA_BOW_CAMPFIRE): HasSwitch(Switch.CATA_TOP, otherwise=True),
    (R.CATA_ELEVATOR, R.CATA_BOSS): HasElevator(Elevator.CATA_2),
    (R.CATA_ELEVATOR, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.CATA_ELEVATOR, R.TR_START): HasElevator(Elevator.TR),
    (R.CATA_ELEVATOR, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.CATA_ELEVATOR, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.CATA_ELEVATOR, R.APEX): elevator_apex,
    (R.CATA_ELEVATOR, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.CATA_ELEVATOR, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.CATA_ELEVATOR, R.CATA_TOP): HasSwitch(Switch.CATA_ELEVATOR),
    (R.CATA_ELEVATOR, R.CATA_MULTI): HasBlue(BlueDoor.CATA_ORBS, otherwise=True),
    (R.CATA_ELEVATOR, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.CATA_BOW_CAMPFIRE, R.CATA_TOP): HasSwitch(Switch.CATA_TOP),
    (R.CATA_BOW_CAMPFIRE, R.CATA_BOW_CONNECTION): has_kyuli & HasBlue(BlueDoor.CATA_SAVE, otherwise=True),
    (R.CATA_BOW_CAMPFIRE, R.CATA_EYEBALL_BONES): HasSwitch(Face.CATA_AFTER_BOW) | otherwise_bow,
    (R.CATA_BOW_CONNECTION, R.CATA_BOW): HasBlue(BlueDoor.CATA_BOW, otherwise=True) & has_kyuli,
    (R.CATA_BOW_CONNECTION, R.CATA_BOW_CAMPFIRE): HasBlue(BlueDoor.CATA_SAVE, otherwise=True),
    (R.CATA_BOW_CONNECTION, R.CATA_VERTICAL_SHORTCUT): HasSwitch(Switch.CATA_VERTICAL_SHORTCUT),
    (R.CATA_VERTICAL_SHORTCUT, R.CATA_BOW_CONNECTION): (
        HasSwitch(Switch.CATA_VERTICAL_SHORTCUT, otherwise=True)
        & (HasSwitch(Switch.CATA_MID_SHORTCUT, otherwise=True) | (has_kyuli & Has(KeyItem.ICARUS)))
    ),
    (R.CATA_EYEBALL_BONES, R.CATA_SNAKE_MUSHROOMS): Has(Eye.RED),
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_DEV_ROOM_CONNECTION): has_claw & Has(KeyItem.BELL) & has_zeek,
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_EYEBALL_BONES): Has(Eye.RED),
    (R.CATA_SNAKE_MUSHROOMS, R.CATA_DOUBLE_SWITCH): (
        HasSwitch(Switch.CATA_CLAW_2, otherwise=True) & (has_claw | (has_kyuli & has_zeek & Has(KeyItem.BELL)))
    ),
    (R.CATA_DEV_ROOM_CONNECTION, R.CATA_DEV_ROOM): (
        HasRed(RedDoor.DEV_ROOM) | Filtered(has_zeek & has_kyuli & CanReachRegion(R.GT_BOSS), options=red_off)
    ),
    (R.CATA_DOUBLE_SWITCH, R.CATA_SNAKE_MUSHROOMS): HasSwitch(Switch.CATA_CLAW_2),
    (R.CATA_DOUBLE_SWITCH, R.CATA_ROOTS_CAMPFIRE): HasSwitch(
        Switch.CATA_WATER_1,
        Switch.CATA_WATER_2,
        otherwise=True,
    ),
    (R.CATA_ROOTS_CAMPFIRE, R.CATA_DOUBLE_SWITCH): HasSwitch(Switch.CATA_WATER_1, Switch.CATA_WATER_2),
    (R.CATA_BELOW_ROOTS_CAMPFIRE, R.CATA_ROOTS_CAMPFIRE): has_claw,
    (R.CATA_BELOW_ROOTS_CAMPFIRE, R.CATA_BLUE_EYE_DOOR): Has(Eye.BLUE),
    (R.CATA_BELOW_ROOTS_CAMPFIRE, R.CATA_ABOVE_ROOTS): has_claw,
    (R.CATA_BELOW_ROOTS_CAMPFIRE, R.CATA_POISON_ROOTS): HasBlue(BlueDoor.CATA_ROOTS, otherwise=True) & has_kyuli,
    (R.CATA_BLUE_EYE_DOOR, R.CATA_BELOW_ROOTS_CAMPFIRE): Has(Eye.BLUE),
    (R.CATA_BLUE_EYE_DOOR, R.CATA_FLAMES_FORK): HasWhite(WhiteDoor.CATA_BLUE, otherwise=True),
    (R.CATA_FLAMES_FORK, R.CATA_VERTICAL_SHORTCUT): (
        HasSwitch(Switch.CATA_SHORTCUT_ACCESS, Switch.CATA_AFTER_BLUE_DOOR, otherwise=True) | HardLogic(has_claw)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_BLUE_EYE_DOOR): (
        HasWhite(WhiteDoor.CATA_BLUE, otherwise=True) | HasSwitch(Switch.CATA_SHORTCUT_ACCESS, otherwise=True)
    ),
    (R.CATA_FLAMES_FORK, R.CATA_FLAMES): HasSwitch(Switch.CATA_FLAMES_2, otherwise=True),
    (R.CATA_FLAMES_FORK, R.CATA_CENTAUR): HasSwitch(Switch.CATA_LADDER_BLOCKS, otherwise=True),
    (R.CATA_CENTAUR, R.CATA_4_FACES): has_claw,
    (R.CATA_CENTAUR, R.CATA_FLAMES_FORK): HasSwitch(Switch.CATA_LADDER_BLOCKS),
    (R.CATA_CENTAUR, R.CATA_BOSS): HasSwitch(Face.CATA_CAMPFIRE),
    (R.CATA_4_FACES, R.CATA_DOUBLE_DOOR): HasSwitch(Face.CATA_X4) | otherwise_bow,
    (R.CATA_DOUBLE_DOOR, R.CATA_4_FACES): HasSwitch(Face.CATA_X4),
    (R.CATA_DOUBLE_DOOR, R.CATA_VOID_R): (
        Has(KeyItem.BELL) & can_kill_ghosts & (HasSwitch(Face.CATA_DOUBLE_DOOR) | otherwise_bow)
    ),
    (R.CATA_VOID_R, R.CATA_VOID_L): Has(KeyItem.VOID),
    (R.CATA_VOID_L, R.CATA_VOID_R): Has(KeyItem.VOID),
    (R.CATA_VOID_L, R.CATA_BOSS): HasWhite(WhiteDoor.CATA_PRISON, otherwise=True) & has_kyuli,
    (R.CATA_BOSS, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.CATA_BOSS, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.CATA_BOSS, R.CATA_CENTAUR): HasSwitch(Face.CATA_CAMPFIRE) | otherwise_bow,
    (R.CATA_BOSS, R.CATA_VOID_L): HasWhite(WhiteDoor.CATA_PRISON, otherwise=True),
    (R.CATA_BOSS, R.TR_START): HasElevator(Elevator.TR) | HasSwitch(Switch.TR_ELEVATOR, otherwise=True),
    (R.CATA_BOSS, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.CATA_BOSS, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.CATA_BOSS, R.APEX): elevator_apex,
    (R.CATA_BOSS, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.CATA_BOSS, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.CATA_BOSS, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.TR_START, R.CATA_ELEVATOR): HasElevator(Elevator.CATA_1),
    (R.TR_START, R.CATA_BOSS): HasElevator(Elevator.CATA_2) | (HasSwitch(Switch.TR_ELEVATOR) & can_extra_height),
    (R.TR_START, R.HOTP_ELEVATOR): HasElevator(Elevator.HOTP),
    (R.TR_START, R.HOTP_BOSS): HasElevator(Elevator.ROA_1),
    (R.TR_START, R.ROA_ELEVATOR): HasElevator(Elevator.ROA_2),
    (R.TR_START, R.TR_LEFT): (
        HasBlue(BlueDoor.TR, otherwise=True)
        & (HasRed(RedDoor.TR) | Filtered(has_claw & CanReachRegion(R.CATA_BOSS), options=red_off))
        & can_extra_height
    ),
    (R.TR_START, R.APEX): elevator_apex,
    (R.TR_START, R.GT_BOSS): HasElevator(Elevator.GT_2),
    (R.TR_START, R.MECH_ZEEK_CONNECTION): HasElevator(Elevator.MECH_1),
    (R.TR_START, R.MECH_BOSS): HasElevator(Elevator.MECH_2),
    (R.TR_START, R.TR_BRAM): Has(Eye.BLUE),
    (R.TR_LEFT, R.TR_TOP_RIGHT): has_star & Has(KeyItem.BELL),
    (R.TR_LEFT, R.TR_BOTTOM_LEFT): Has(KeyItem.BELL) & can_kill_ghosts,
    (R.TR_BOTTOM_LEFT, R.TR_BOTTOM): Has(Eye.BLUE),
    (R.TR_TOP_RIGHT, R.TR_GOLD): has_zeek & Has(KeyItem.BELL) & (has_kyuli | has_block | can_uppies),
    (R.TR_TOP_RIGHT, R.TR_MIDDLE_RIGHT): (
        HasSwitch(Crystal.TR_GOLD) | Filtered(Has(KeyItem.BELL) & has_claw & can_crystal, options=switch_off)
    ),
    (R.TR_MIDDLE_RIGHT, R.TR_DARK_ARIAS): Has(Eye.GREEN),
    (R.TR_MIDDLE_RIGHT, R.TR_BOTTOM): HasSwitch(Switch.TR_BOTTOM, otherwise=True),
    (R.TR_BOTTOM, R.TR_BOTTOM_LEFT): Has(Eye.BLUE),
    (R.CD_START, R.CD_2): HasSwitch(Switch.CD_1, otherwise=True) | HasSwitch(Crystal.CD_BACKTRACK),
    (R.CD_START, R.CD_BOSS): CanReachRegion(R.CD_ARIAS_ROUTE) & CanReachRegion(R.CD_TOP),
    (R.CD_3, R.CD_MIDDLE): HasSwitch(Switch.CD_3, otherwise=True),
    (R.CD_MIDDLE, R.CD_KYULI_ROUTE): HasSwitch(Switch.CD_CAMPFIRE, otherwise=True),
    (R.CD_MIDDLE, R.CD_ARIAS_ROUTE): has_arias,
    (R.CD_KYULI_ROUTE, R.CD_CAMPFIRE_3): has_kyuli,
    (R.CD_CAMPFIRE_3, R.CD_ARENA): HasSwitch(Crystal.CD_CAMPFIRE) | otherwise_crystal,
    (R.CD_STEPS, R.CD_TOP): HasSwitch(Crystal.CD_STEPS) | otherwise_crystal,
    (R.CATH_START, R.CATH_START_LEFT): (
        (
            HasSwitch(Crystal.CATH_1ST_ROOM)
            | Filtered(can_crystal & CanReachRegion(R.CATH_START_TOP_LEFT), options=switch_off)
        )
        & has_claw
    ),
    (R.CATH_START_RIGHT, R.CATH_START_TOP_LEFT): HasSwitch(Switch.CATH_BOTTOM, otherwise=True),
    (R.CATH_START_TOP_LEFT, R.CATH_START_LEFT): HasSwitch(Face.CATH_L),
    (R.CATH_START_LEFT, R.CATH_TP): HasSwitch(Face.CATH_R) | otherwise_bow,
    (R.CATH_LEFT_SHAFT, R.CATH_SHAFT_ACCESS): HasSwitch(Crystal.CATH_SHAFT_ACCESS) & has_claw,
    (R.CATH_LEFT_SHAFT, R.CATH_UNDER_CAMPFIRE): HasSwitch(Crystal.CATH_SHAFT) | otherwise_crystal,
    (R.CATH_UNDER_CAMPFIRE, R.CATH_CAMPFIRE_1): has_zeek & Has(KeyItem.BELL),
    (R.CATH_CAMPFIRE_1, R.CATH_SHAFT_ACCESS): has_kyuli,
    (R.CATH_SHAFT_ACCESS, R.CATH_ORB_ROOM): HasSwitch(Switch.CATH_BESIDE_SHAFT, otherwise=True),
    (R.CATH_ORB_ROOM, R.CATH_GOLD_BLOCK): (
        HasSwitch(Crystal.CATH_ORBS) | Filtered(can_crystal & Has(KeyItem.BELL), options=switch_off)
    ),
    (R.CATH_RIGHT_SHAFT_CONNECTION, R.CATH_RIGHT_SHAFT): Has(KeyItem.BELL) & has_zeek & has_bow,
    (R.CATH_RIGHT_SHAFT, R.CATH_TOP): has_claw,
    (R.CATH_TOP, R.CATH_UPPER_SPIKE_PIT): (
        HasSwitch(Crystal.CATH_SPIKE_PIT) | otherwise_crystal | HardLogic(has_cloak & has_block & Has(KeyItem.BELL))
    ),
    (R.CATH_TOP, R.CATH_CAMPFIRE_2): HasSwitch(Switch.CATH_TOP_CAMPFIRE, otherwise=True),
    (R.SP_START, R.SP_STAR_END): has_block & Has(KeyItem.BELL) & has_claw,
    (R.SP_START, R.SP_CAMPFIRE_1): HasSwitch(Crystal.SP_BLOCKS) | otherwise_crystal,
    (R.SP_CAMPFIRE_1, R.SP_HEARTS): HasSwitch(Switch.SP_BUBBLES, otherwise=True),
    (R.SP_HEARTS, R.SP_CAMPFIRE_1): HasSwitch(Switch.SP_BUBBLES),
    (R.SP_HEARTS, R.SP_ORBS): has_star & Has(KeyItem.BELL) & has_kyuli,
    (R.SP_HEARTS, R.SP_FROG): HasSwitch(Switch.SP_DOUBLE_DOORS, otherwise=True),
    (R.SP_PAINTING, R.SP_HEARTS): Has(KeyItem.BELL) & has_algus_meteor & chalice_on_easy,
    (R.SP_PAINTING, R.SP_SHAFT): has_claw & HasBlue(BlueDoor.SP, otherwise=True),
    (R.SP_SHAFT, R.SP_PAINTING): HasBlue(BlueDoor.SP, otherwise=True),
    (R.SP_SHAFT, R.SP_STAR): has_claw & Has(KeyItem.BELL) & (HasSwitch(Crystal.SP_STAR) | otherwise_crystal),
    (R.SP_STAR, R.SP_SHAFT): Has(KeyItem.BELL) & has_algus_meteor & chalice_on_easy & HasSwitch(Crystal.SP_STAR),
    (R.SP_STAR, R.SP_STAR_CONNECTION): has_star,
    (R.SP_STAR_CONNECTION, R.SP_STAR): has_star,
    (R.SP_STAR_CONNECTION, R.SP_STAR_END): has_star & (HasSwitch(Switch.SP_AFTER_STAR) | (has_arias << switch_off)),
    (R.SP_STAR_END, R.SP_STAR_CONNECTION): has_star & HasSwitch(Switch.SP_AFTER_STAR),
}

MAIN_LOCATION_RULES: dict[L, Rule[AstalonWorldBase]] = {
    L.GT_GORGONHEART: (
        HasSwitch(Switch.GT_GH, otherwise=True) | has_kyuli | has_boots | has_block | has_cloak | Has(KeyItem.ICARUS)
    ),
    L.GT_ANCIENTS_RING: Has(Eye.RED),
    L.GT_BANISH: (
        CanReachRegion(R.GT_BOTTOM)
        & CanReachRegion(R.GT_ASCENDANT_KEY)
        & CanReachRegion(R.GT_BUTT)
        & (has_algus | has_kyuli | has_bram | has_zeek | has_sword)
    ),
    L.HOTP_BELL: HasSwitch(Switch.HOTP_BELL, otherwise=True) | has_kyuli | can_combo_height,
    L.HOTP_CLAW: can_extra_height,
    L.HOTP_MAIDEN_RING: HasSwitch(Crystal.HOTP_MAIDEN_1, Crystal.HOTP_MAIDEN_2) | otherwise_crystal,
    L.TR_ADORNED_KEY: (
        HasSwitch(Switch.TR_ADORNED_L, Switch.TR_ADORNED_M, Switch.TR_ADORNED_R)
        | Filtered(
            has_claw
            & has_zeek
            & HasAll(Eye.RED, KeyItem.BELL)
            & CanReachRegion(R.TR_BOTTOM)
            & CanReachRegion(R.TR_LEFT)
            & CanReachRegion(R.TR_DARK_ARIAS),
            options=switch_off,
        )
    ),
    L.CATH_BLOCK: HasSwitch(Crystal.CATH_TOP_L, Crystal.CATH_TOP_R) | otherwise_crystal,
    L.MECH_ZEEK: Has(KeyItem.CROWN),
    L.MECH_ATTACK_VOLANTIS: has_claw,
    L.MECH_ATTACK_STAR: has_star,
    L.ROA_ATTACK: has_star & Has(KeyItem.BELL) & can_extra_height,
    L.CAVES_ATTACK_RED: Has(Eye.RED),
    L.CAVES_ATTACK_BLUE: HasAll(Eye.RED, Eye.BLUE),
    L.CAVES_ATTACK_GREEN: HasAll(Eye.RED, Eye.BLUE) & (Has(Eye.GREEN) | has_star),
    L.CD_ATTACK: HasSwitch(Switch.CD_TOP, otherwise=True) | (has_block & Has(KeyItem.BELL) & has_kyuli),
    L.GT_HP_1_RING: has_star | (CanReachRegion(R.GT_UPPER_PATH) & HasBlue(BlueDoor.GT_RING, otherwise=True)),
    L.GT_HP_5_KEY: has_claw,
    L.MECH_HP_1_SWITCH: HasSwitch(Switch.MECH_INVISIBLE, otherwise=True),
    L.MECH_HP_3_CLAW: has_claw,
    L.HOTP_HP_2_GAUNTLET: has_claw & has_zeek & Has(KeyItem.BELL),
    L.HOTP_HP_5_OLD_MAN: (
        has_claw
        & ((Has(KeyItem.BELL) & can_kill_ghosts) | Has(KeyItem.CHALICE))
        & HasSwitch(Switch.HOTP_ABOVE_OLD_MAN, otherwise=True)
    ),
    L.HOTP_HP_5_START: has_claw & HasBlue(BlueDoor.HOTP_START, otherwise=True),
    L.ROA_HP_2_RIGHT: (
        (has_gauntlet | Has(KeyItem.CHALICE) | has_star)
        & Has(KeyItem.BELL)
        & has_kyuli
        & (HasSwitch(Crystal.ROA_BRANCH_L, Crystal.ROA_BRANCH_R) | otherwise_crystal)
    ),
    L.ROA_HP_5_SOLARIA: has_kyuli,
    L.APEX_HP_1_CHALICE: HasBlue(BlueDoor.APEX, otherwise=True),
    L.APEX_HP_5_HEART: has_kyuli | has_block,
    L.CAVES_HP_1_START: Has(KeyItem.CHALICE) | HasSwitch(Face.CAVES_1ST_ROOM) | otherwise_bow,
    L.CATA_HP_1_ABOVE_POISON: (
        has_kyuli
        & (
            HasSwitch(Crystal.CATA_POISON_ROOTS)
            | Filtered(can_crystal & Has(KeyItem.BELL), options=switch_off)
            | HardLogic(Has(KeyItem.ICARUS) & has_claw)
        )
    ),
    L.CATA_HP_2_GEMINI_BOTTOM: has_kyuli & (HasSwitch(Face.CATA_BOTTOM) | otherwise_bow),
    L.CATA_HP_2_GEMINI_TOP: has_kyuli,
    L.CATA_HP_2_ABOVE_GEMINI: (
        (has_claw | (has_block & Has(KeyItem.BELL))) & ((has_gauntlet & Has(KeyItem.BELL)) | Has(KeyItem.CHALICE))
    ),
    L.CAVES_HP_5_CHAIN: HasAll(Eye.RED, Eye.BLUE, KeyItem.BELL) & has_star & has_claw,
    L.CD_HP_1: HasSwitch(Switch.CD_TOP, otherwise=True) | (has_block & Has(KeyItem.BELL) & has_kyuli),
    L.CATH_HP_1_TOP_LEFT: has_cloak | Has(KeyItem.ICARUS),
    L.CATH_HP_1_TOP_RIGHT: has_cloak | Has(KeyItem.ICARUS),
    L.CATH_HP_2_CLAW: has_claw,
    L.CATH_HP_5_BELL: has_kyuli | has_block | Has(KeyItem.ICARUS) | has_cloak,
    L.MECH_WHITE_KEY_LINUS: HasSwitch(Switch.MECH_LOWER_KEY, otherwise=True),
    L.MECH_WHITE_KEY_TOP: (HasSwitch(Crystal.MECH_TOP) | otherwise_crystal) & can_extra_height,
    L.ROA_WHITE_KEY_SAVE: HasSwitch(Switch.ROA_WORMS, otherwise=True),
    L.CATA_WHITE_KEY_PRISON: can_extra_height | has_cloak | Has(KeyItem.ICARUS),
    L.MECH_BLUE_KEY_BLOCKS: HasSwitch(Switch.MECH_KEY_BLOCKS, otherwise=True),
    L.MECH_BLUE_KEY_SAVE: has_claw,
    L.MECH_BLUE_KEY_POT: has_kyuli | can_combo_height,
    L.HOTP_BLUE_KEY_STATUE: has_claw,
    L.HOTP_BLUE_KEY_AMULET: has_kyuli | can_combo_height,
    L.HOTP_BLUE_KEY_LADDER: can_extra_height,
    L.HOTP_BLUE_KEY_MAZE: HasSwitch(Crystal.HOTP_BELOW_PUZZLE) | otherwise_crystal,
    L.ROA_BLUE_KEY_FACE: HasSwitch(Face.ROA_BLUE_KEY) | otherwise_bow,
    L.ROA_BLUE_KEY_FLAMES: (
        (has_block & has_kyuli & Has(KeyItem.BELL)) | CanReachEntrance(R.ROA_FLAMES, R.ROA_ARIAS_BABY_GORGON)
    ),
    L.ROA_BLUE_KEY_TOP: can_extra_height,
    L.SP_BLUE_KEY_ARIAS: has_arias,
    L.GT_RED_KEY: has_zeek & has_kyuli,
    L.ROA_RED_KEY: has_cloak & has_claw & Has(KeyItem.BELL),
    L.TR_RED_KEY: has_claw,
    L.SHOP_GIFT: shop_moderate,
    L.SHOP_KNOWLEDGE: shop_cheap,
    L.SHOP_MERCY: shop_expensive,
    L.SHOP_ORB_SEEKER: shop_cheap,
    L.SHOP_CARTOGRAPHER: shop_cheap,
    L.SHOP_DEATH_ORB: shop_moderate,
    L.SHOP_DEATH_POINT: shop_moderate,
    L.SHOP_TITANS_EGO: shop_moderate,
    L.SHOP_ALGUS_ARCANIST: shop_moderate,
    L.SHOP_ALGUS_SHOCK: shop_moderate,
    L.SHOP_ALGUS_METEOR: shop_expensive,
    L.SHOP_ARIAS_GORGONSLAYER: shop_moderate,
    L.SHOP_ARIAS_LAST_STAND: shop_expensive,
    L.SHOP_ARIAS_LIONHEART: shop_moderate,
    L.SHOP_KYULI_ASSASSIN: shop_cheap,
    L.SHOP_KYULI_BULLSEYE: shop_moderate,
    L.SHOP_KYULI_RAY: shop_expensive,
    L.SHOP_ZEEK_JUNKYARD: shop_moderate,
    L.SHOP_ZEEK_ORBS: shop_moderate,
    L.SHOP_ZEEK_LOOT: shop_cheap,
    L.SHOP_BRAM_AXE: shop_expensive,
    L.SHOP_BRAM_HUNTER: shop_moderate,
    L.SHOP_BRAM_WHIPLASH: shop_moderate,
    L.GT_SWITCH_2ND_ROOM: HasWhite(WhiteDoor.GT_START, otherwise=True),
    L.GT_SWITCH_BUTT_ACCESS: can_extra_height,
    L.GT_SWITCH_UPPER_PATH_ACCESS: (
        HasSwitch(Switch.GT_UPPER_PATH_BLOCKS, otherwise=True) | (has_kyuli & has_block & has_zeek & Has(KeyItem.BELL))
    ),
    L.GT_CRYSTAL_ROTA: (
        can_crystal
        & (
            Has(KeyItem.BELL)
            | (
                CanReachEntrance(R.MECH_BOTTOM_CAMPFIRE, R.GT_UPPER_PATH_CONNECTION)
                & CanReachEntrance(R.GT_UPPER_PATH_CONNECTION, R.GT_UPPER_PATH)
            )
        )
    ),
    L.GT_CRYSTAL_OLD_MAN_1: (
        can_crystal
        & (
            Has(KeyItem.BELL)
            | HasSwitch(Switch.GT_UPPER_ARIAS)
            | CanReachRegion(R.GT_ARIAS_SWORD_SWITCH, options=switch_off)
        )
    ),
    L.GT_CRYSTAL_OLD_MAN_2: (
        can_crystal
        & HasSwitch(Crystal.GT_OLD_MAN_1, otherwise=True)
        & (
            Has(KeyItem.BELL)
            | HasSwitch(Switch.GT_UPPER_ARIAS)
            | CanReachRegion(R.GT_ARIAS_SWORD_SWITCH, options=switch_off)
        )
    ),
    L.MECH_SWITCH_BOOTS_ACCESS: Has(Eye.RED) | has_star,
    L.MECH_SWITCH_UPPER_VOID_DROP: has_claw,
    L.MECH_SWITCH_CANNON: HasSwitch(Crystal.MECH_CANNON) | otherwise_crystal,
    L.MECH_SWITCH_ARIAS: has_arias,
    L.MECH_CRYSTAL_CANNON: can_crystal,
    L.MECH_CRYSTAL_LINUS: can_crystal,
    L.MECH_CRYSTAL_LOWER: can_crystal,
    L.MECH_CRYSTAL_TO_BOSS_3: can_crystal,
    L.MECH_CRYSTAL_TOP: can_crystal,
    L.MECH_CRYSTAL_CLOAK: can_crystal & Has(Eye.BLUE),
    L.MECH_CRYSTAL_SLIMES: can_crystal,
    L.MECH_CRYSTAL_TO_CD: can_crystal & Has(Eye.BLUE) & HasBlue(BlueDoor.MECH_CD, otherwise=True),
    L.MECH_CRYSTAL_CAMPFIRE: can_crystal,
    L.MECH_CRYSTAL_1ST_ROOM: can_crystal,
    L.MECH_CRYSTAL_OLD_MAN: can_crystal,
    L.MECH_CRYSTAL_TOP_CHAINS: can_crystal,
    L.MECH_CRYSTAL_BK: can_crystal,
    L.MECH_FACE_ABOVE_VOLANTIS: has_bow & has_claw,
    L.HOTP_SWITCH_LOWER_SHORTCUT: HasSwitch(Crystal.HOTP_LOWER) | otherwise_crystal,
    L.HOTP_SWITCH_TO_CLAW_2: (
        HasSwitch(Switch.HOTP_TO_CLAW_1, otherwise=True)
        | (HasSwitch(Switch.HOTP_TO_CLAW_2, otherwise=True) & can_extra_height)
        | has_claw
    ),
    L.HOTP_SWITCH_CLAW_ACCESS: has_kyuli | can_block_in_wall,
    L.HOTP_SWITCH_LEFT_3: (
        HasSwitch(Switch.HOTP_LEFT_1, Switch.HOTP_LEFT_2, otherwise=True)
        | (has_star & CanReachRegion(R.HOTP_START_LEFT))
    ),
    L.HOTP_CRYSTAL_ROCK_ACCESS: can_crystal,
    L.HOTP_CRYSTAL_BOTTOM: can_crystal,
    L.HOTP_CRYSTAL_LOWER: can_crystal,
    L.HOTP_CRYSTAL_AFTER_CLAW: can_crystal,
    L.HOTP_CRYSTAL_MAIDEN_1: can_crystal,
    L.HOTP_CRYSTAL_MAIDEN_2: can_crystal & (HasSwitch(Crystal.HOTP_MAIDEN_1, otherwise=True) | has_kyuli),
    L.HOTP_CRYSTAL_BELL_ACCESS: can_crystal,
    L.HOTP_CRYSTAL_HEART: can_crystal,
    L.HOTP_CRYSTAL_BELOW_PUZZLE: can_crystal,
    L.HOTP_FACE_OLD_MAN: has_bow,
    L.ROA_SWITCH_SPIKE_CLIMB: has_claw,
    L.ROA_SWITCH_TRIPLE_3: HasSwitch(Crystal.ROA_TRIPLE_2) | otherwise_crystal,
    L.ROA_CRYSTAL_1ST_ROOM: can_crystal & has_kyuli & Has(KeyItem.BELL),
    L.ROA_CRYSTAL_BABY_GORGON: can_crystal,
    L.ROA_CRYSTAL_LADDER_R: can_crystal_no_whiplash & (Has(KeyItem.BELL) | HardLogic(has_kyuli_ray)),
    L.ROA_CRYSTAL_LADDER_L: can_crystal_no_whiplash & (Has(KeyItem.BELL) | HardLogic(has_kyuli_ray)),
    L.ROA_CRYSTAL_CENTAUR: can_crystal & Has(KeyItem.BELL) & has_arias,
    L.ROA_CRYSTAL_SPIKE_BALLS: can_crystal,
    L.ROA_CRYSTAL_SHAFT: can_crystal,
    L.ROA_CRYSTAL_BRANCH_R: can_crystal & has_kyuli & Has(KeyItem.BELL),
    L.ROA_CRYSTAL_BRANCH_L: can_crystal & has_kyuli & Has(KeyItem.BELL),
    L.ROA_CRYSTAL_3_REAPERS: can_crystal,
    L.ROA_CRYSTAL_TRIPLE_2: can_crystal & HasSwitch(Switch.ROA_TRIPLE_1, otherwise=True),
    L.ROA_FACE_SPIDERS: has_bow,
    L.ROA_FACE_BLUE_KEY: has_bow,
    L.DARK_SWITCH: has_claw,
    L.CAVES_FACE_1ST_ROOM: has_bow,
    L.CATA_SWITCH_CLAW_2: HasSwitch(Switch.CATA_CLAW_1, otherwise=True),
    L.CATA_SWITCH_FLAMES_2: HasSwitch(Switch.CATA_FLAMES_1, otherwise=True),
    L.CATA_CRYSTAL_POISON_ROOTS: can_crystal,
    L.CATA_FACE_AFTER_BOW: has_bow,
    L.CATA_FACE_BOW: has_bow,
    L.CATA_FACE_X4: has_bow,
    L.CATA_FACE_CAMPFIRE: has_bow,
    L.CATA_FACE_DOUBLE_DOOR: has_bow,
    L.CATA_FACE_BOTTOM: has_bow,
    L.TR_SWITCH_ADORNED_L: has_claw,
    L.TR_SWITCH_ADORNED_M: Has(Eye.RED),
    L.TR_SWITCH_ADORNED_R: HasSwitch(Crystal.TR_DARK_ARIAS, otherwise=True) & has_zeek & Has(KeyItem.BELL) & has_claw,
    L.TR_CRYSTAL_GOLD: can_crystal & Has(KeyItem.BELL) & has_claw,
    L.TR_CRYSTAL_DARK_ARIAS: can_crystal & has_zeek & Has(KeyItem.BELL) & has_claw,
    L.CD_SWITCH_1: HasSwitch(Crystal.CD_START) | otherwise_crystal,
    L.CD_CRYSTAL_BACKTRACK: can_crystal,
    L.CD_CRYSTAL_START: can_crystal,
    L.CD_CRYSTAL_CAMPFIRE: can_crystal,
    L.CD_CRYSTAL_STEPS: can_crystal,
    L.CATH_CRYSTAL_1ST_ROOM: can_crystal,
    L.CATH_CRYSTAL_SHAFT: can_crystal,
    L.CATH_CRYSTAL_SPIKE_PIT: can_crystal,
    L.CATH_CRYSTAL_TOP_L: can_crystal,
    L.CATH_CRYSTAL_TOP_R: can_crystal,
    L.CATH_CRYSTAL_SHAFT_ACCESS: can_crystal,
    L.CATH_CRYSTAL_ORBS: can_crystal,
    L.CATH_FACE_LEFT: has_bow,
    L.CATH_FACE_RIGHT: has_bow,
    L.SP_SWITCH_AFTER_STAR: has_arias,
    L.SP_CRYSTAL_BLOCKS: can_crystal,
    L.SP_CRYSTAL_STAR: can_crystal,
    L.ROA_CANDLE_ARENA: can_extra_height | has_bram_axe | CanReachRegion(R.ROA_FLAMES_CONNECTION),
    L.ROA_CANDLE_HIDDEN_4: has_kyuli | has_bram_axe,
    L.ROA_CANDLE_HIDDEN_5: has_kyuli,
    L.CATA_CANDLE_DEV_ROOM: has_claw | HasSwitch(Switch.CATA_DEV_ROOM, otherwise=True),
    L.CATA_CANDLE_PRISON: HasBlue(BlueDoor.CATA_PRISON_RIGHT, otherwise=True),
}

COMPLETION_RULE: Rule[AstalonWorldBase] = Has(Events.VICTORY)
