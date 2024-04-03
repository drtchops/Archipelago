from ..Items import Items
from ..Locations import Locations
from . import AstalonTestBase


class NoCharacterStartTest(AstalonTestBase):
    options = {
        "start_with_zeek": "false",
        "start_with_bram": "false",
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
        location = Locations.HOTP_MAIDEN_RING.value
        self.collect_all_but(
            [
                Items.SWORD.value,
                Items.DOOR_RED_SP.value,
                Items.DOOR_RED_ZEEK.value,
            ]
        )
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(Items.DOOR_RED_ZEEK.value)
        self.assertTrue(self.can_reach_location(location))


class AllCharacterStartTest(AstalonTestBase):
    options = {
        "start_with_zeek": "true",
        "start_with_bram": "true",
        "randomize_white_keys": "false",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
    }

    def test_starting_with_bram_only_needs_star(self) -> None:
        location = Locations.GT_HP_1_RING.value
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(Items.STAR.value)
        self.assertTrue(self.can_reach_location(location))
