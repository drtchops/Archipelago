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
    # "Gorgon Tomb - Monster Ball": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Gorgon Eye (Red)": AstalonLocationData("Gorgon Tomb"),
    "Mechanism - Talaria Boots": AstalonLocationData("Mechanism"),
    "Mechanism - Cloak of Levitation": AstalonLocationData("Mechanism"),
    # "Mechanism - Cyclops Idol": AstalonLocationData("Mechanism"),
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
    # "Catacombs - Gil": AstalonLocationData("Catacombs"),
    "Tower Roots - Adorned Key": AstalonLocationData("Tower Roots"),
    # "Cyclops Den - Prince's Crown": AstalonLocationData("Cyclops Den"),
    "Cathedral - Magic Block": AstalonLocationData("Cathedral"),
    "Serpent Path - Morning Star": AstalonLocationData("Serpent Path"),
    "Gorgon Tomb - Attack +1": AstalonLocationData("Gorgon Tomb"),
    "Mechanism - Attack +1 (Above Volantis)": AstalonLocationData("Mechanism"),
    "Mechanism - Attack +1 (Morning Star Blocks)": AstalonLocationData("Mechanism"),
    "Ruins of Ash - Attack +1": AstalonLocationData("Ruins of Ash"),
    "Catacombs - Attack +1 (Item Chain Red)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (Item Chain Blue)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (Item Chain Green)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (Climbable Root)": AstalonLocationData("Catacombs"),
    "Catacombs - Attack +1 (Poison Roots)": AstalonLocationData("Catacombs"),
    "Cyclops Den - Attack +1": AstalonLocationData("Cyclops Den"),
    "Cathedral - Attack +1": AstalonLocationData("Cathedral"),
    "Serpent Path - Attack +1": AstalonLocationData("Serpent Path"),
    "Gorgon Tomb - Max HP +1 (Ring of the Ancients)": AstalonLocationData("Gorgon Tomb"),
    "Gorgon Tomb - Max HP +5 (Ascendant Key)": AstalonLocationData("Gorgon Tomb"),
    "Mechanism - Max HP +1 (Secret Switch)": AstalonLocationData("Mechanism"),
    "Mechanism - Max HP +1 (Morning Star Blocks)": AstalonLocationData("Mechanism"),
    "Mechanism - Max HP +3 (Above Checkpoint)": AstalonLocationData("Mechanism"),
    "Hall of the Phantoms - Max HP +1 (Griffon Claw)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +2 (Secret Ladder)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +2 (Boreas Gauntlet)": AstalonLocationData(
        "Hall of the Phantoms"
    ),
    "Hall of the Phantoms - Max HP +5 (Old Man)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +5 (Teleport Maze)": AstalonLocationData("Hall of the Phantoms"),
    "Hall of the Phantoms - Max HP +5 (Above Start)": AstalonLocationData("Hall of the Phantoms"),
    "Ruins of Ash - Max HP +1 (Left of Ascent)": AstalonLocationData("Ruins of Ash"),
    "Ruins of Ash - Max HP +2 (Right Side)": AstalonLocationData("Ruins of Ash"),
    "Ruins of Ash - Max HP +5 (After Solaria)": AstalonLocationData("Ruins of Ash"),
    "Darkness - Max HP +4": AstalonLocationData("Darkness"),
    "The Apex - Max HP +1 (Blood Chalice)": AstalonLocationData("The Apex"),
    "The Apex - Max HP +5 (After Heart)": AstalonLocationData("The Apex"),
    "Catacombs - Max HP +1 (First Room)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +1 (Cyclops Arena)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +1 (Above Poison Roots)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (Before Poison Roots)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (After Poison Roots)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (Before Gemini Bottom)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (Before Gemini Top)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +2 (Above Gemini)": AstalonLocationData("Catacombs"),
    "Catacombs - Max HP +5 (Item Chain)": AstalonLocationData("Catacombs"),
    "Tower Roots - Max HP +1 (Bottom)": AstalonLocationData("Tower Roots"),
    "Tower Roots - Max HP +2 (Top)": AstalonLocationData("Tower Roots"),
    "Cyclops Den - Max HP +1": AstalonLocationData("Cyclops Den"),
    "Cathedral - Max HP +1 (Top Left)": AstalonLocationData("Cathedral"),
    "Cathedral - Max HP +1 (Top Right)": AstalonLocationData("Cathedral"),
    "Cathedral - Max HP +2 (Left Climb)": AstalonLocationData("Cathedral"),
    "Cathedral - Max HP +5 (Bell)": AstalonLocationData("Cathedral"),
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
