from functools import cached_property
from typing import Any, ClassVar

from typing_extensions import override

from BaseClasses import CollectionState, Entrance, Location, Region
from NetUtils import JSONMessagePart
from Options import Option
from rule_builder import Rule
from Utils import get_intended_text  # pyright: ignore[reportUnknownVariableType]
from worlds.generic.Rules import CollectionRule

from .bases import AstalonWorldBase
from .items import Character, Events


def map_page_index(data: Any) -> int:
    """Converts the area id provided by the game mod to a map index."""
    if not isinstance(data, int):
        return 0
    if data in (1, 99):
        # tomb
        return 1
    if data in (2, 3, 7):
        # mechanism_and_hall
        return 2
    if data in (4, 19, 21):
        # catacombs
        return 3
    if data in (5, 6, 8, 13):
        # ruins
        return 4
    if data == 11:
        # cyclops
        return 5
    # world map
    return 0


CHARACTER_ICONS = {
    1: "algus",
    2: "arias",
    3: "kyuli",
    4: "bram",
    5: "zeek",
}

MAP_OFFSETS = (
    (-1800, 17180),  # world map
    (-4152, 25130),  # gt
    (-1560, 21080),  # mech and hotp
    (-5448 + 876, 26840),  # catacombs
    (-2424, 17000),  # ruins
    (-9336, 20840),  # cyclops
)
ROOM_WIDTH = 432
ROOM_HEIGHT = 240
MAP_SCALE_X = ROOM_WIDTH / 59.346
MAP_SCALE_Y = -ROOM_HEIGHT / 40.475


def location_icon_coords(index: int | None, coords: dict[str, Any]) -> tuple[int, int, str] | None:
    """Converts player coordinates provided by the game mod into image coordinates for the map page."""
    if index is None or not coords:
        return None

    dx, dy = MAP_OFFSETS[index]
    x = int((coords.get("X", 0) + (ROOM_WIDTH / 2) + dx) / MAP_SCALE_X)
    y = int((coords.get("Y", 0) - (ROOM_HEIGHT / 2) + dy) / MAP_SCALE_Y)
    icon = CHARACTER_ICONS.get(coords.get("Character", 1), "algus")
    return x, y, f"images/icons/{icon}.png"


def rule_to_json(rule: CollectionRule | None, state: CollectionState) -> list[JSONMessagePart]:
    if isinstance(rule, Rule.Resolved):
        return [
            {"type": "text", "text": "    "},
            *rule.explain_json(state),
        ]
    return [
        {"type": "text", "text": "    "},
        {"type": "color", "color": "green", "text": "True"},
    ]


class AstalonUTWorld(AstalonWorldBase):
    tracker_world: ClassVar[dict[str, Any]] = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": "locations/locations.json",
        "map_page_setting_key": "{player}_{team}_astalon_area",
        "map_page_index": map_page_index,
        "location_setting_key": "{player}_{team}_astalon_coords",
        "location_icon_coords": location_icon_coords,
    }
    ut_can_gen_without_yaml: ClassVar[bool] = True
    glitches_item_name: ClassVar[str] = Events.FAKE_OOL_ITEM.value

    @cached_property
    def is_ut(self) -> bool:
        return getattr(self.multiworld, "generation_is_fake", False)

    @override
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Option[Any] | None = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

            if "starting_characters" in slot_data:
                self.starting_characters = [Character(c) for c in slot_data["starting_characters"]]
            if "extra_gold_eyes" in slot_data:
                self.extra_gold_eyes = slot_data["extra_gold_eyes"]

    def get_logical_path(self, dest_name: str, state: CollectionState) -> list[JSONMessagePart]:
        if not dest_name:
            return [{"type": "text", "text": "Provide a location or region to route to using /route [name]"}]

        goal_location: Location | None = None
        goal_region: Region | None = None
        region_name = ""
        location_name, usable, response = get_intended_text(dest_name, [loc.name for loc in self.get_locations()])
        if usable:
            try:
                goal_location = self.get_location(location_name)
            except KeyError:
                return [{"type": "text", "text": f"Location {location_name} not found in this multiworld"}]
            goal_region = goal_location.parent_region
            if not goal_region:
                return [{"type": "text", "text": f"Location {location_name} has no parent region"}]
        else:
            region_name, usable, _ = get_intended_text(
                dest_name,
                [reg.name for reg in self.get_regions()],
            )
            if usable:
                goal_region = self.get_region(region_name)
            else:
                return [{"type": "text", "text": response}]

        if goal_location and not goal_location.can_reach(state):
            return [{"type": "text", "text": f"Location {goal_location.name} cannot be reached"}]
        if goal_region and goal_region not in state.path:
            return [{"type": "text", "text": f"Region {goal_region.name} cannot be reached"}]

        path: list[Entrance] = []
        name, connection = state.path[goal_region]
        while connection != ("Menu", None) and connection is not None:
            name, connection = connection
            if "->" in name and "Menu" not in name:
                path.append(self.get_entrance(name))

        messages: list[JSONMessagePart] = []
        path.reverse()
        for p in path:
            messages.extend(
                [
                    {"type": "entrance_name", "text": p.name, "player": self.player},
                    {"type": "text", "text": "\n"},
                    *rule_to_json(p.access_rule, state),
                    {"type": "text", "text": "\n"},
                ]
            )

        if goal_location:
            messages.extend(
                [
                    {"type": "text", "text": "-> "},
                    {
                        "type": "location_name",
                        "text": goal_location.name,
                        "player": self.player,
                    },
                    {"type": "text", "text": "\n"},
                    *rule_to_json(goal_location.access_rule, state),
                ]
            )

        return messages
