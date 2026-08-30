import json
from typing import TypedDict

from .locations import ALL_LOCATIONS


class LocationDict(TypedDict):
    name: str
    sections: list[dict[str, str]]
    map_locations: list[dict[str, str | int]]


MAPS = (
    ("World Map", "A1", "ZZ61"),
    ("The Apex", "M58", "T61"),
    ("Catacombs", "J6", "U20"),
    ("Cathedral", "A31", "E42"),
    ("Cyclops Den", "S36", "Z45"),
    ("Dev Room", "U13", "ZZ15"),
    ("Gorgon Tomb", "G17", "S28"),
    ("Hall of Phantoms", "D27", "S44"),
    ("Mechanism", "K21", "W38"),
    ("Ruins of Ash", "I41", "Q60"),
    ("Serpent Path", "C40", "K53"),
    ("Tower Roots", "J1", "S9"),
)
PURCHASES = (
    ("Gift", 283, 508),
    ("Knowledge", 73, 508),
    ("Mercy", 374, 666),
    ("Orb Seeker", 177, 508),
    ("Cartographer", 91, 666),
    ("Death Orb", 179, 666),
    ("Death Point", 283, 666),
    ("Titan's Ego", 374, 508),
    ("Arcanist", 619, 128),
    ("Shock Field", 711, 128),
    ("Meteor Rain", 811, 128),
    ("Gorgonslayer", 619, 276),
    ("Last Stand", 711, 276),
    ("Lionheart", 811, 276),
    ("Assassin Strike", 619, 418),
    ("Bullseye", 711, 418),
    ("Shining Ray", 811, 418),
    ("Junkyard Hunt", 619, 560),
    ("Orb Monger", 711, 560),
    ("Bigger Loot", 811, 560),
    ("Golden Axe", 619, 704),
    ("Monster Hunter", 711, 704),
    ("Whiplash", 811, 704),
)

OFFSETS = (60, 40)


def room_to_coords(room: str) -> tuple[int, int]:
    if room.startswith("ZZ"):
        x = 26
        start = 2
    else:
        x = ord(room[0]) - 65
        start = 1
    y = int(room[start:]) - 1
    return (x, y)


def build() -> None:
    rooms: dict[str, LocationDict] = {}

    for data in ALL_LOCATIONS:
        if not data.room:
            continue

        if data.room not in rooms:
            room_data: LocationDict = {
                "name": f"{data.area.value} {data.room}",
                "sections": [],
                "map_locations": [],
            }
            pos = room_to_coords(data.room)
            for map_name, bottom_left, top_right in MAPS:
                bl = room_to_coords(bottom_left)
                tr = room_to_coords(top_right)
                if bl[0] <= pos[0] <= tr[0] and bl[1] <= pos[1] <= tr[1]:
                    room_data["map_locations"].append(
                        {
                            "map": map_name,
                            "x": int(((pos[0] - bl[0]) * OFFSETS[0]) + (OFFSETS[0] * 1.5)),
                            "y": int(((tr[1] - pos[1]) * OFFSETS[1]) + (OFFSETS[1] * 1.5)),
                        }
                    )
            rooms[data.room] = room_data

        rooms[data.room]["sections"].append({"name": data.name.value})

    children = list(rooms.values())
    children.append(
        {
            "name": "Epimetheus Shop",
            "sections": [{"name": f"{name} Purchase"} for name, _, _ in PURCHASES],
            "map_locations": [
                {
                    "map": "World Map",
                    "x": 330,
                    "y": 2125,
                }
            ],
        }
    )
    for name, x, y in PURCHASES:
        children.append(
            {
                "name": f"{name} Purchase",
                "sections": [{"name": f"{name} Purchase"}],
                "map_locations": [
                    {
                        "map": "Shop",
                        "x": x,
                        "y": y,
                    },
                ],
            }
        )

    locations = [
        {
            "name": "World Map",
            "children": children,
        }
    ]
    with open("worlds/astalon/tracker/locations.json", "w") as f:
        json.dump(locations, f, indent=2)
