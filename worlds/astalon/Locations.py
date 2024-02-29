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

    "Gorgon Tomb - Attack +1": AstalonLocationData("Gorgon Tomb"),
    "Mechanism - Attack +1 (1)": AstalonLocationData("Mechanism"),
    "Mechanism - Attack +1 (2)": AstalonLocationData("Mechanism"),
    "Ruins of Ash - Attack +1": AstalonLocationData("Ruins of Ash"),
    "Catacombs - Attack +1 (1)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (2)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (3)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (4)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (5)": AstalonLocationData("Catacombs"),
    "Cyclops Den - Attack +1": AstalonLocationData("Cyclops Den"),
    "Cathedral - Attack +1": AstalonLocationData("Cathedral"),
    "Serpent Path - Attack +1": AstalonLocationData("Serpent Path"),

    "Gorgon Tomb - Max HP +1": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Max HP +5": AstalonLocationData("Gorgon Tomb"),
    "Mechanism - Max HP +1": AstalonLocationData("Mechanism"),
    "Mechanism - Max HP +3": AstalonLocationData("Mechanism"),
    "Hall of the Phantoms - Max HP +1 (1)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +1 (2)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +2 (1)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +2 (2)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +5 (1)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +5 (2)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +5 (3)": AstalonLocationData("Hall of the Phantoms"),
    "Ruins of Ash - Max HP +1": AstalonLocationData("Ruins of Ash"),
    "Ruins of Ash - Max HP +2": AstalonLocationData("Ruins of Ash"),
    "Ruins of Ash - Max HP +5": AstalonLocationData("Ruins of Ash"),
    "The Apex - Max HP +1": AstalonLocationData("The Apex"),
    "The Apex - Max HP +5": AstalonLocationData("The Apex"),
    "Catacombs - Max HP +1 (1)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +1 (2)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +1 (3)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (1)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (2)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (3)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (4)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +5": AstalonLocationData("Catacombs"),
    "Tower Roots - Max HP +1": AstalonLocationData("Tower Roots"),
    "Tower Roots - Max HP +2": AstalonLocationData("Tower Roots"),
    "Cyclops Den - Max HP +1": AstalonLocationData("Cyclops Den"),
    "Cathedral - Max HP +1 (1)": AstalonLocationData("Cathedral"),
    "Cathedral - Max HP +1 (2)": AstalonLocationData("Cathedral"),
    "Cathedral - Max HP +2": AstalonLocationData("Cathedral"),
    "Cathedral - Max HP +5": AstalonLocationData("Cathedral"),
    "Serpent Path - Max HP +1": AstalonLocationData("Serpent Path"),
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
