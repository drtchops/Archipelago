from ..Items import Items
from ..Locations import Locations
from ..Regions import Regions
from . import AstalonTestBase


class VanillaCharacterTest(AstalonTestBase):
    options = {
        "randomize_characters": "vanilla",
        "randomize_white_keys": "false",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
    }

    def test_star_needs_bram_access(self) -> None:
        location = Locations.GT_HP_1_RING.value
        self.collect_all_but([Items.VOID.value, Items.DOOR_BLUE_GT_RING.value])
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(Items.VOID.value)
        self.assertTrue(self.can_reach_location(location))

    def test_block_needs_zeek_access(self) -> None:
        location = Locations.CATH_BLOCK.value
        self.collect_all_but(Items.DOOR_RED_ZEEK.value)
        self.assertFalse(self.can_reach_region(Regions.MECH_ZEEK.value))
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(Items.DOOR_RED_ZEEK.value)
        self.assertTrue(self.can_reach_region(Regions.MECH_ZEEK.value))
        self.assertTrue(self.can_reach_location(location))


class AllCharacterTest(AstalonTestBase):
    options = {
        "randomize_characters": "all",
        "randomize_white_keys": "false",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
    }

    def test_starting_with_bram_only_needs_star(self) -> None:
        location = Locations.GT_HP_1_RING.value
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(Items.STAR.value)
        self.assertTrue(self.can_reach_location(location))


class SoloCharacterTest(AstalonTestBase):
    options = {
        "randomize_characters": "solo",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
    }
