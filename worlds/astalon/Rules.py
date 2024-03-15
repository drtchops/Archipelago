from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import Items
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
    entrance_rules: dict[tuple[Regions, Regions], Callable[[CollectionState], bool]]
    item_rules: dict[Locations, Callable[[CollectionState], bool]]
    familiar_rules: dict[Locations, Callable[[CollectionState], bool]]
    attack_rules: dict[Locations, Callable[[CollectionState], bool]]
    health_rules: dict[Locations, Callable[[CollectionState], bool]]
    white_key_rules: dict[Locations, Callable[[CollectionState], bool]]
    blue_key_rules: dict[Locations, Callable[[CollectionState], bool]]
    red_key_rules: dict[Locations, Callable[[CollectionState], bool]]

    def __init__(self, world: "AstalonWorld"):
        self.world = world
        self.player = world.player
        self.options = world.options

        self.entrance_rules = {
            (Regions.GT, Regions.MECH): lambda state: self.has(state, Items.EYE_RED),
            (Regions.GT, Regions.APEX): lambda state: (
                self.has(state, Items.ASCENDANT_KEY) if self.options.free_apex_elevator else False
            ),
            (Regions.GT, Regions.CATA): lambda _: True,
            (Regions.MECH, Regions.HOTP): lambda state: self.has_any(state, Items.EYE_BLUE, Items.STAR, Items.CLAW),
            (Regions.MECH, Regions.CD): lambda state: self.has_all(state, Items.CYCLOPS, Items.EYE_BLUE),
            (Regions.HOTP, Regions.ROA): lambda state: self.has_all(
                # bell not needed if kyuli has claw and beam, should redo logic once shop is in rando
                # algus can hit the switch if he has banish and bigger projectiles, though this doesn't seem to matter checks-wise yet
                state,
                Items.CLAW,
                Items.BELL,
            ),
            (Regions.HOTP, Regions.CATH): lambda state: (
                self.has_all(state, Items.EYE_GREEN, Items.BOW, Items.BELL, Items.ZEEK)
                and (self.has(state, Items.DOOR_RED_CATH) if self.options.randomize_red_keys else True)
            ),
            (Regions.ROA, Regions.APEX): lambda state: self.has(state, Items.EYE_GREEN),
            (Regions.ROA, Regions.SP): lambda state: (
                self.has(state, Items.DOOR_RED_SP)
                if self.options.randomize_red_keys
                else (self.has(state, Items.CLOAK) and self.has_any(state, Items.EYE_GREEN, Items.BOW))
            ),
            (Regions.APEX, Regions.BOSS): lambda state: (
                # if difficulties are added, bell shouldn't be required on hard
                # TODO: minimum amount of hp/attack upgrades for logical completion?
                self.has_all(state, Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.BELL)
            ),
            (Regions.CATA, Regions.TR): lambda state: (
                self.has_all(
                    state, Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.VOID, Items.CLAW, Items.BELL, Items.BANISH
                )
            ),
        }

        self.item_rules = {
            Locations.GT_GORGONHEART: lambda _: True,
            Locations.GT_ANCIENTS_RING: lambda state: self.has(state, Items.EYE_RED),
            Locations.GT_SWORD: lambda state: self.has(state, Items.EYE_RED),
            Locations.GT_MAP: lambda state: self.has(state, Items.EYE_RED),
            Locations.GT_ASCENDANT_KEY: lambda _: True,
            Locations.GT_BANISH: lambda _: True,
            Locations.GT_VOID: lambda state: self.has(state, Items.EYE_RED),
            Locations.GT_EYE_RED: lambda _: True,
            Locations.MECH_BOOTS: lambda _: True,
            Locations.MECH_CLOAK: lambda state: self.has(state, Items.EYE_BLUE),
            # Locations.MECH_CYCLOPS: lambda state: self.can_reach_zeek(state),
            Locations.MECH_EYE_BLUE: lambda _: True,
            Locations.HOTP_BELL: lambda state: (
                self.has_any(state, Items.EYE_BLUE, Items.STAR) or self.hotp_backdoor(state)
            ),
            Locations.HOTP_AMULET: lambda state: self.has_all(state, Items.CLAW, Items.EYE_BLUE),
            Locations.HOTP_CLAW: lambda state: self.central_hotp(state),
            Locations.HOTP_GAUNTLET: lambda state: self.has_all(state, Items.CLAW, Items.BELL, Items.BANISH),
            Locations.HOTP_MAIDEN_RING: lambda state: (
                self.has_all(state, Items.SWORD, Items.BANISH, Items.BELL, Items.CLAW)
            ),
            Locations.ROA_ICARUS: lambda _: True,
            Locations.ROA_EYE_GREEN: lambda _: True,
            Locations.APEX_CHALICE: lambda state: self.has_all(state, Items.ADORNED_KEY, Items.STAR),
            Locations.CATA_BOW: lambda state: self.has(state, Items.EYE_RED),
            Locations.TR_ADORNED_KEY: lambda state: (
                self.has_all(
                    state, Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.STAR, Items.ZEEK, Items.BANISH
                )
            ),
            # Locations.CD_CROWN: lambda _: True,
            Locations.CATH_BLOCK: lambda _: True,
            Locations.SP_STAR: lambda _: True,
        }

        self.attack_rules = {
            Locations.GT_ATTACK: lambda state: (
                self.has(state, Items.EYE_GREEN)
                and (self.has(state, Items.CLAW) or self.has_all(state, Items.ZEEK, Items.BELL))
            ),
            Locations.MECH_ATTACK_VOLANTIS: lambda state: (
                self.has(state, Items.CLAW)
                and (
                    self.has(state, Items.EYE_BLUE)
                    or self.has_all(state, Items.EYE_GREEN, Items.VOID)
                    or self.has_all(state, Items.STAR, Items.BELL)
                )
            ),
            Locations.MECH_ATTACK_STAR: lambda state: self.has(state, Items.STAR),
            Locations.ROA_ATTACK: lambda state: self.has(state, Items.STAR),
            Locations.CATA_ATTACK_RED: lambda state: self.has(state, Items.EYE_RED),
            Locations.CATA_ATTACK_BLUE: lambda state: self.has_all(state, Items.EYE_RED, Items.EYE_BLUE),
            Locations.CATA_ATTACK_GREEN: lambda state: (
                self.has_all(state, Items.EYE_RED, Items.EYE_BLUE) and self.has_any(state, Items.EYE_GREEN, Items.STAR)
            ),
            Locations.CATA_ATTACK_ROOT: lambda _: True,
            Locations.CATA_ATTACK_POISON: lambda state: self.has_all(state, Items.EYE_RED, Items.BOW),
            Locations.CD_ATTACK: lambda _: True,
            Locations.CATH_ATTACK: lambda _: True,
            Locations.SP_ATTACK: lambda _: True,
        }

        self.health_rules = {
            Locations.GT_HP_1_RING: lambda state: self.has_all(state, Items.EYE_RED, Items.SWORD),
            Locations.GT_HP_5_KEY: lambda state: self.has(state, Items.CLAW),
            Locations.MECH_HP_1_SWITCH: lambda _: True,
            Locations.MECH_HP_1_STAR: lambda state: self.has(state, Items.STAR),
            Locations.MECH_HP_3_CLAW: lambda state: self.has(state, Items.CLAW),
            Locations.HOTP_HP_1_CLAW: lambda state: self.central_hotp(state),
            Locations.HOTP_HP_2_LADDER: lambda state: self.central_hotp(state),
            Locations.HOTP_HP_2_GAUNTLET: lambda state: self.has_all(state, Items.CLAW, Items.ZEEK, Items.BELL),
            Locations.HOTP_HP_5_OLD_MAN: lambda state: (
                self.central_hotp(state)
                and self.has_all(state, Items.EYE_GREEN, Items.CLAW)
                and (self.has_all(state, Items.BELL, Items.BANISH) or self.has(state, Items.CHALICE))
            ),
            Locations.HOTP_HP_5_MAZE: lambda state: (
                self.has(state, Items.EYE_BLUE)
                or self.has_all(state, Items.EYE_GREEN, Items.CLAW, Items.VOID)
                or self.has_all(state, Items.STAR, Items.BELL)
                # bram with star and range/axe could make this without bell
            ),
            Locations.HOTP_HP_5_START: lambda state: (
                self.has(state, Items.CLAW) and self.has_any(state, Items.BELL, Items.EYE_BLUE)
            ),
            Locations.ROA_HP_1_LEFT: lambda _: True,
            Locations.ROA_HP_2_RIGHT: lambda state: self.has_any(state, Items.GAUNTLET, Items.STAR, Items.CHALICE),
            Locations.ROA_HP_5_SOLARIA: lambda state: self.has(state, Items.EYE_GREEN),
            Locations.DARK_HP_4: lambda _: True,
            Locations.APEX_HP_1_CHALICE: lambda _: True,
            Locations.APEX_HP_5_HEART: lambda _: True,
            Locations.CATA_HP_1_START: lambda state: self.has_any(state, Items.BOW, Items.CHALICE),
            Locations.CATA_HP_1_CYCLOPS: lambda state: self.has(state, Items.SWORD),
            Locations.CATA_HP_1_ABOVE_POISON: lambda state: (
                self.has_all(state, Items.EYE_RED, Items.BOW)
                and (self.has(state, Items.BELL) or self.has_all(state, Items.ICARUS, Items.CLAW))
            ),
            Locations.CATA_HP_2_BEFOER_POISON: lambda state: self.has_all(state, Items.EYE_RED, Items.BOW),
            Locations.CATA_HP_2_AFTER_POISON: lambda state: self.has_all(state, Items.EYE_RED, Items.BOW),
            Locations.CATA_HP_2_GEMINI_BOTTOM: lambda state: (
                self.has_all(state, Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.CLAW)
            ),
            Locations.CATA_HP_2_GEMINI_TOP: lambda state: (
                self.has_all(state, Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.CLAW)
            ),
            Locations.CATA_HP_2_ABOVE_GEMINI: lambda state: (
                self.has_all(state, Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.CLAW)
                and (self.has_all(state, Items.GAUNTLET, Items.BELL) or self.has(state, Items.CHALICE))
            ),
            Locations.CATA_HP_5_CHAIN: lambda state: (
                self.has_all(state, Items.EYE_RED, Items.EYE_BLUE, Items.STAR, Items.CLAW)
            ),
            Locations.TR_HP_1_BOTTOM: lambda state: (
                self.has(state, Items.DOOR_RED_TR) if self.options.randomize_red_keys else True
            ),
            Locations.TR_HP_2_TOP: lambda state: (
                self.has(state, Items.DOOR_RED_TR) if self.options.randomize_red_keys else True
            ),
            Locations.CD_HP_1: lambda _: True,
            Locations.CATH_HP_1_TOP_LEFT: lambda _: True,
            Locations.CATH_HP_1_TOP_RIGHT: lambda _: True,
            Locations.CATH_HP_2_CLAW: lambda state: self.has(state, Items.CLAW),
            Locations.CATH_HP_5_BELL: lambda _: True,
            Locations.SP_HP_1: lambda _: True,
        }

        self.white_key_rules = {}

        self.blue_key_rules = {}

        self.red_key_rules = {
            Locations.GT_RED_KEY: lambda state: self.has_all(state, Items.ZEEK),
            Locations.MECH_RED_KEY: lambda _: True,
            Locations.HOTP_RED_KEY: lambda state: (
                self.has_all(state, Items.EYE_GREEN, Items.CLOAK)
                and (self.has_any(state, Items.EYE_BLUE, Items.STAR) or self.hotp_backdoor(state))
            ),
            Locations.ROA_RED_KEY: lambda state: self.has_all(state, Items.CLOAK, Items.BOW),
            Locations.TR_RED_KEY: lambda _: True,
        }

        self.familiar_rules = {
            Locations.GT_OLD_MAN: lambda state: (
                self.has(state, Items.EYE_RED) and self.has_any(state, Items.BELL, Items.SWORD)
            ),
            Locations.MECH_OLD_MAN: lambda _: True,
            Locations.HOTP_OLD_MAN: lambda state: self.has_all(state, Items.CLOAK, Items.BOW, Items.BELL),
            Locations.CATA_GIL: lambda state: (
                self.has_all(
                    state,
                    Items.EYE_RED,
                    Items.EYE_BLUE,
                    Items.EYE_GREEN,
                    Items.STAR,
                    Items.ZEEK,
                    Items.CLAW,
                    Items.BELL,
                )
                and (self.has(state, Items.DOOR_RED_DEV_ROOM) if self.options.randomize_red_keys else True)
            ),
        }

    def region(self, name: Regions):
        return self.world.multiworld.get_region(name.value, self.player)

    def entrance(self, from_: Regions, to_: Regions):
        return self.world.multiworld.get_entrance(f"{from_.value} -> {to_.value}", self.player)

    def location(self, name: Locations):
        return self.world.multiworld.get_location(name.value, self.player)

    def can_reach_zeek(self, state: CollectionState):
        if not self.region(Regions.MECH).can_reach(state):
            return False
        if self.options.randomize_red_keys:
            return state.has(Items.DOOR_RED_ZEEK.value, self.player)
        # what is reasonable to get a surplus of red keys with
        return state.has(Items.EYE_BLUE.value, self.player) or state.has_all(
            [Items.EYE_GREEN.value, Items.STAR.value], self.player
        )

    def has_zeek(self, state: CollectionState):
        if self.options.start_with_zeek:
            return True
        return self.can_reach_zeek(state)

    def can_reach_bram(self, state: CollectionState):
        # if switch rando is implemented, may need to check for blue eye specifically
        return self.region(Regions.TR).can_reach(state)

    def has_bram(self, state: CollectionState):
        if self.options.start_with_bram:
            return True
        return self.can_reach_bram(state)

    def has(self, state: CollectionState, item: Items, *, count: int = 1):
        if item == Items.CYCLOPS:
            # item is not yet randomized
            return self.can_reach_zeek(state)
        if item == Items.ZEEK:
            return self.has_zeek(state)
        if item == Items.BRAM:
            return self.has_bram(state)
        if item == Items.BLOCK and not self.has_zeek(state):
            return False
        if item == Items.STAR and not self.has_bram(state):
            return False
        return state.has(item.value, self.player, count=count)

    def has_all(self, state: CollectionState, *items: Items):
        # cover extra logic instead of calling state.has_all
        for item in items:
            if not self.has(state, item):
                return False
        return True

    def has_any(self, state: CollectionState, *items: Items):
        # cover extra logic instead of calling state.has_any
        for item in items:
            if self.has(state, item):
                return True
        return False

    def hotp_backdoor(self, state: CollectionState):
        # kyuli with claw+beam could do this
        if not self.has(state, Items.CLAW):
            return False
        return self.has_any(state, Items.CLOAK, Items.ICARUS)

    def central_hotp(self, state: CollectionState):
        if self.hotp_backdoor(state):
            return True
        if not self.has(state, Items.BELL):
            return False
        return self.has_any(state, Items.STAR, Items.EYE_BLUE)

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

        # if self.options.randomize_white_keys:
        #     for location, rule in self.white_key_rules.items():
        #         set_rule(self.location(location), rule)

        # if self.options.randomize_blue_keys:
        #     for location, rule in self.blue_key_rules.items():
        #         set_rule(self.location(location), rule)

        if self.options.randomize_red_keys:
            for location, rule in self.red_key_rules.items():
                set_rule(self.location(location), rule)

        # if self.options.randomize_familiars:
        #     for location, rule in self.familiar_rules.items():
        #         set_rule(self.location(location), rule)
