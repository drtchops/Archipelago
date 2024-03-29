from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Dict, Tuple

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import BlueDoors, Items, RedDoors, WhiteDoors
from .Locations import Locations
from .Options import AstalonOptions
from .Regions import Regions

if TYPE_CHECKING:
    from . import AstalonWorld


@dataclass
class AstalonRules:
    world: "AstalonWorld"
    player: int
    options: AstalonOptions
    entrance_rules: Dict[Tuple[Regions, Regions], Callable[[CollectionState], bool]]
    item_rules: Dict[Locations, Callable[[CollectionState], bool]]
    familiar_rules: Dict[Locations, Callable[[CollectionState], bool]]
    attack_rules: Dict[Locations, Callable[[CollectionState], bool]]
    health_rules: Dict[Locations, Callable[[CollectionState], bool]]
    white_key_rules: Dict[Locations, Callable[[CollectionState], bool]]
    blue_key_rules: Dict[Locations, Callable[[CollectionState], bool]]
    red_key_rules: Dict[Locations, Callable[[CollectionState], bool]]

    def __init__(self, world: "AstalonWorld"):
        self.world = world
        self.player = world.player
        self.options = world.options

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
                self.has(state, Items.CLAW)
                and self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA, Items.DOOR_WHITE_MECH_TOP)
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
                self.has(state, Items.EYE_GREEN, Items.BOW, Items.BELL, Items.ZEEK, Items.CLAW)
                and self.red_doors(state, Items.DOOR_RED_CATH, else_case=self.has(state, Items.CLOAK))
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
                self.red_doors(state, Items.DOOR_RED_SP, else_case=self.has(state, Items.CLOAK, Items.BOW))
            ),
            (Regions.APEX, Regions.BOSS): lambda state: (
                # if difficulties are added, bell shouldn't be required on hard
                # TODO: minimum amount of hp/attack upgrades for logical completion?
                self.has(state, Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.BELL)
            ),
            (Regions.CATA_UPPER, Regions.CATA_MID): lambda state: (
                self.has(state, Items.EYE_RED) and self.white_doors(state, Items.DOOR_WHITE_CATA_TOP)
            ),
            (Regions.CATA_MID, Regions.CATA_LOWER): lambda state: (
                self.has(state, Items.BOW, Items.EYE_BLUE)
                and self.has(state, Items.DOOR_WHITE_CATA_BLUE)
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
                and self.white_doors(state, Items.DOOR_WHITE_MECH_ARENA, Items.DOOR_WHITE_MECH_TOP)
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
            Locations.TR_ADORNED_KEY: lambda state: self.has(state, Items.EYE_GREEN, Items.STAR, Items.ZEEK),
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
            Locations.GT_HP_1_RING: lambda state: self.blue_doors(state, Items.DOOR_BLUE_GT_RING),
            Locations.GT_HP_5_KEY: lambda state: (
                self.has(state, Items.CLAW) and self.blue_doors(state, Items.DOOR_BLUE_GT_ASCENDANT)
            ),
            Locations.MECH_HP_1_SWITCH: lambda _: True,
            Locations.MECH_HP_1_STAR: lambda state: self.has(state, Items.STAR),
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
            Locations.ROA_HP_2_RIGHT: lambda state: self.has_any(state, Items.GAUNTLET, Items.STAR, Items.CHALICE),
            Locations.ROA_HP_5_SOLARIA: lambda _: True,
            Locations.DARK_HP_4: lambda _: True,
            Locations.APEX_HP_1_CHALICE: lambda state: self.blue_doors(state, Items.DOOR_BLUE_APEX),
            Locations.APEX_HP_5_HEART: lambda _: True,
            Locations.CATA_HP_1_START: lambda state: self.has_any(state, Items.BOW, Items.CHALICE),
            Locations.CATA_HP_1_CYCLOPS: lambda state: self.has(state, Items.SWORD),
            Locations.CATA_HP_1_ABOVE_POISON: lambda state: (
                self.has(state, Items.BELL) or self.has(state, Items.ICARUS, Items.CLAW)
            ),
            Locations.CATA_HP_2_BEFOER_POISON: lambda _: True,
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

    def can_reach_zeek(self, state: CollectionState):
        if not self.region(Regions.MECH_UPPER).can_reach(state):
            return False
        if self.options.randomize_red_keys:
            return self.has(state, Items.DOOR_RED_ZEEK)
        # can reach one of the red keys
        return (
            self.blue_doors(state, Items.DOOR_BLUE_MECH_VOID)
            or (self.region(Regions.HOTP_BELL).can_reach(state) and self.has(state, Items.EYE_GREEN, Items.CLOAK))
            or (self.region(Regions.ROA_UPPER).can_reach(state) and self.has(state, Items.BOW, Items.CLOAK))
        )

    def has_zeek(self, state: CollectionState):
        if self.options.start_with_zeek:
            return True
        return self.can_reach_zeek(state) and self.region(Regions.CD).can_reach(state)

    def can_reach_bram(self, state: CollectionState):
        return self.region(Regions.TR).can_reach(state) and self.has(state, Items.EYE_BLUE)

    def has_bram(self, state: CollectionState):
        if self.options.start_with_bram:
            return True
        return self.can_reach_bram(state)

    def _has(self, state: CollectionState, item: Items, count: int = 1):
        if item in {Items.ALGUS, Items.ARIAS, Items.KYULI}:
            # not yet randomized
            return True
        elif item == Items.ZEEK:
            # not yet randomized, but optional
            return self.has_zeek(state)
        elif item == Items.BRAM:
            # not yet randomized, but optional
            return self.has_bram(state)

        elif item == Items.CLOAK and not self._has(state, Items.ALGUS):
            return False
        elif item in {Items.SWORD, Items.BOOTS} and not self._has(state, Items.ARIAS):
            return False
        elif item in {Items.CLAW, Items.BOW} and not self._has(state, Items.KYULI):
            return False
        elif item == Items.BLOCK and not self._has(state, Items.ZEEK):
            return False
        elif item == Items.STAR and not self._has(state, Items.BRAM):
            return False
        elif item == Items.BANISH and not self.has_any(state, Items.ALGUS, Items.ZEEK):
            return False
        elif item == Items.GAUNTLET and not self.has_any(state, Items.ARIAS, Items.BRAM):
            return False

        elif item == Items.CYCLOPS:
            # not yet randomized
            return self.can_reach_zeek(state)

        return state.has(item.value, self.player, count=count)

    def has(self, state: CollectionState, *items: Items, count: int = 1):
        # cover extra logic instead of calling state.has_all
        for item in items:
            if not self._has(state, item, count=count):
                return False
        return True

    def has_any(self, state: CollectionState, *items: Items):
        # cover extra logic instead of calling state.has_any
        for item in items:
            if self._has(state, item):
                return True
        return False

    def white_doors(self, state: CollectionState, *doors: WhiteDoors, else_case=True):
        if not self.options.randomize_white_keys:
            return else_case
        return self.has(state, *doors)

    def blue_doors(self, state: CollectionState, *doors: BlueDoors, else_case=True):
        if not self.options.randomize_blue_keys:
            return else_case
        return self.has(state, *doors)

    def red_doors(self, state: CollectionState, *doors: RedDoors, else_case=True):
        if not self.options.randomize_red_keys:
            return else_case
        return self.has(state, *doors)

    def set_region_rules(self):
        for (from_, to_), rule in self.entrance_rules.items():
            set_rule(self.entrance(from_, to_), rule)

    def set_location_rules(self):
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

        # if self.options.randomize_familiars:
        #     for location, rule in self.familiar_rules.items():
        #         set_rule(self.location(location), rule)
