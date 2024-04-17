from ..Items import Items
from ..Locations import Locations
from . import AstalonTestBase


class LocationsTest(AstalonTestBase):
    options = {
        "difficulty": "hard",
        "randomize_characters": "vanilla",
        "randomize_white_keys": "false",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
    }

    def test_access_ring_hp_star(self) -> None:
        location = Locations.GT_HP_1_RING.value
        self.collect_by_name(Items.STAR.value)
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(
            [
                Items.DOOR_BLUE_CAVES.value,
                Items.EYE_RED.value,
                Items.EYE_BLUE.value,
                Items.BOW.value,
                Items.CLAW.value,
                Items.BELL.value,
                Items.BANISH.value,
                Items.VOID.value,
            ]
        )
        self.assertTrue(self.can_reach_location(location))

    def test_access_ring_hp_door(self) -> None:
        location = Locations.GT_HP_1_RING.value
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(Items.DOOR_BLUE_GT_RING.value)
        self.assertTrue(self.can_reach_location(location))

    def _test_bow(self, reverse_order: bool):
        location = Locations.CATA_BOW.value
        items = [Items.DOOR_BLUE_CATA_BOW.value, Items.DOOR_BLUE_CATA_SAVE.value]
        if reverse_order:
            items.reverse()
        precollect = [Items.EYE_RED.value, Items.DOOR_BLUE_CAVES.value]
        for item in precollect:
            self.collect_by_name(item)
        self.assertFalse(self.can_reach_location(location))

        self.collect_by_name(items[0])
        self.assertFalse(self.can_reach_location(location))
        self.collect_by_name(items[1])
        self.assertTrue(self.can_reach_location(location))

    def test_access_bow_needs_both_doors(self) -> None:
        self._test_bow(True)

    def test_access_bow_needs_both_doors_reversed(self) -> None:
        self._test_bow(False)
