from typing import Any


def map_page_index(data: Any) -> int:
    if data in (1, 99):
        # tomb
        return 1
    elif data in (2, 3, 7):
        # mechanism_and_hall
        return 2
    elif data in (4, 19, 21):
        # catacombs
        return 3
    elif data in (5, 6, 8, 13):
        # ruins
        return 4
    elif data == 11:
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


def location_icon_coords(index: int, coords: dict[str, Any]) -> tuple[int, int, str] | None:
    if not coords:
        return None

    dx, dy = MAP_OFFSETS[index]
    x = int((coords.get("X", 0) + (ROOM_WIDTH / 2) + dx) / MAP_SCALE_X)
    y = int((coords.get("Y", 0) - (ROOM_HEIGHT / 2) + dy) / MAP_SCALE_Y)
    icon = CHARACTER_ICONS.get(coords.get("Character", 1), "algus")
    return x, y, f"images/icons/{icon}.png"


TRACKER_WORLD = {
    "map_page_folder": "tracker",
    "map_page_maps": "maps/maps.json",
    "map_page_locations": "locations/locations.json",
    "map_page_setting_key": "{player}_{team}_astalon_area",
    "map_page_index": map_page_index,
    "location_setting_key": "{player}_{team}_astalon_coords",
    "location_icon_coords": location_icon_coords,
}
