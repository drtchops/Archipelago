from itertools import groupby
from typing import NamedTuple

from BaseClasses import Location


class AstalonLocation(Location):
    game = "Astalon"


class AstalonLocationData(NamedTuple):
    region: str


location_table: dict[str, AstalonLocationData] = {
    "Gorgon Tomb - Gorgonheart": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Ring of the Ancients": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Sword of Mirrors": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Linus' Map": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Ascendant Key": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Banish Spell": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Void Charm": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Monster Ball": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Gorgon Eye (Red)": AstalonLocationData("Gorgon Tomb"),
    "Mechanism - Talaria Boots": AstalonLocationData("Mechanism"),
    "Mechanism - Cape of Levitation": AstalonLocationData("Mechanism"),
    "Mechanism - Cyclops Idol": AstalonLocationData("Mechanism"),
    "Mechanism - Gorgon Eye (Blue)": AstalonLocationData("Mechanism"),
    "Hall of the Phantoms - Athena's Bell": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Amulet of Sol": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Griffon Claw": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Boreas Gauntlet": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Dead Maiden's Ring": AstalonLocationData("Hall of the Phantoms"),
    "Ruins of Ash - Icarus Emblem": AstalonLocationData("Ruins of Ash"),
    "Ruins of Ash - Gorgon Eye (Green)": AstalonLocationData("Ruins of Ash"),
    "The Apex - Blood Chalice": AstalonLocationData("The Apex"),
    "Catacombs - Lunarian Bow": AstalonLocationData("Catacombs"),
    "Catacombs - Gil": AstalonLocationData("Catacombs"),
    "Tower Roots - Adorned Key": AstalonLocationData("Tower Roots"),
    "Cyclops Den - Prince's Crown": AstalonLocationData("Cyclops Den"),
    "Cathedral - Magic Block": AstalonLocationData("Cathedral"),
    "Serpent Path - Morning Star": AstalonLocationData("Serpent Path"),
}

location_name_to_id: dict[str, int] = {name: 1000 + i for i, name in enumerate(location_table)}


def get_location_group(location_name: str) -> str:
    return location_table[location_name].region


location_name_groups: dict[str, set[str]] = {
    group: set(location_names)
    for group, location_names in groupby(
        sorted(location_table, key=get_location_group), get_location_group
    )
}
