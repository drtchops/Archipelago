from dataclasses import dataclass
from itertools import groupby

from BaseClasses import Location


class AstalonLocation(Location):
    game = "Astalon"


@dataclass
class AstalonLocationData:
    region: str
    item_group: str = ""


location_table: dict[str, AstalonLocationData] = {
    "Gorgon Tomb - Gorgonheart": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Ring of the Ancients": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Sword of Mirrors": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Linus' Map": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Ascendant Key": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Banish Spell": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Void Charm": AstalonLocationData("Gorgon Tomb", "items"),
    # "Gorgon Tomb - Monster Ball": AstalonLocationData("Gorgon Tomb", "items"),
    "Gorgon Tomb - Gorgon Eye (Red)": AstalonLocationData("Gorgon Tomb", "items"),
    "Mechanism - Talaria Boots": AstalonLocationData("Mechanism", "items"),
    "Mechanism - Cloak of Levitation": AstalonLocationData("Mechanism", "items"),
    # "Mechanism - Cyclops Idol": AstalonLocationData("Mechanism", "items"),
    "Mechanism - Gorgon Eye (Blue)": AstalonLocationData("Mechanism", "items"),
    "Hall of the Phantoms - Athena's Bell": AstalonLocationData("Hall of the Phantoms", "items"),
    "Hall of the Phantoms - Amulet of Sol": AstalonLocationData("Hall of the Phantoms", "items"),
    "Hall of the Phantoms - Griffon Claw": AstalonLocationData("Hall of the Phantoms", "items"),
    "Hall of the Phantoms - Boreas Gauntlet": AstalonLocationData("Hall of the Phantoms", "items"),
    "Hall of the Phantoms - Dead Maiden's Ring": AstalonLocationData("Hall of the Phantoms", "items"),
    "Ruins of Ash - Icarus Emblem": AstalonLocationData("Ruins of Ash", "items"),
    "Ruins of Ash - Gorgon Eye (Green)": AstalonLocationData("Ruins of Ash", "items"),
    "The Apex - Blood Chalice": AstalonLocationData("The Apex", "items"),
    "Catacombs - Lunarian Bow": AstalonLocationData("Catacombs", "items"),
    # "Catacombs - Gil": AstalonLocationData("Catacombs", "items"),
    "Tower Roots - Adorned Key": AstalonLocationData("Tower Roots", "items"),
    # "Cyclops Den - Prince's Crown": AstalonLocationData("Cyclops Den", "items"),
    "Cathedral - Magic Block": AstalonLocationData("Cathedral", "items"),
    "Serpent Path - Morning Star": AstalonLocationData("Serpent Path", "items"),
    "Gorgon Tomb - Attack +1": AstalonLocationData("Gorgon Tomb", "attack"),
    "Mechanism - Attack +1 (Above Volantis)": AstalonLocationData("Mechanism", "attack"),
    "Mechanism - Attack +1 (Morning Star Blocks)": AstalonLocationData("Mechanism", "attack"),
    "Ruins of Ash - Attack +1": AstalonLocationData("Ruins of Ash", "attack"),
    "Catacombs - Attack +1 (Item Chain Red)": AstalonLocationData("Catacombs", "attack"),
    "Catacombs - Attack +1 (Item Chain Blue)": AstalonLocationData("Catacombs", "attack"),
    "Catacombs - Attack +1 (Item Chain Green)": AstalonLocationData("Catacombs", "attack"),
    "Catacombs - Attack +1 (Climbable Root)": AstalonLocationData("Catacombs", "attack"),
    "Catacombs - Attack +1 (Poison Roots)": AstalonLocationData("Catacombs", "attack"),
    "Cyclops Den - Attack +1": AstalonLocationData("Cyclops Den", "attack"),
    "Cathedral - Attack +1": AstalonLocationData("Cathedral", "attack"),
    "Serpent Path - Attack +1": AstalonLocationData("Serpent Path", "attack"),
    "Gorgon Tomb - Max HP +1 (Ring of the Ancients)": AstalonLocationData("Gorgon Tomb", "health"),
    "Gorgon Tomb - Max HP +5 (Ascendant Key)": AstalonLocationData("Gorgon Tomb", "health"),
    "Mechanism - Max HP +1 (Secret Switch)": AstalonLocationData("Mechanism", "health"),
    "Mechanism - Max HP +1 (Morning Star Blocks)": AstalonLocationData("Mechanism", "health"),
    "Mechanism - Max HP +3 (Above Checkpoint)": AstalonLocationData("Mechanism", "health"),
    "Hall of the Phantoms - Max HP +1 (Griffon Claw)": AstalonLocationData("Hall of the Phantoms", "health"),
    "Hall of the Phantoms - Max HP +2 (Secret Ladder)": AstalonLocationData("Hall of the Phantoms", "health"),
    "Hall of the Phantoms - Max HP +2 (Boreas Gauntlet)": AstalonLocationData("Hall of the Phantoms", "health"),
    "Hall of the Phantoms - Max HP +5 (Old Man)": AstalonLocationData("Hall of the Phantoms", "health"),
    "Hall of the Phantoms - Max HP +5 (Teleport Maze)": AstalonLocationData("Hall of the Phantoms", "health"),
    "Hall of the Phantoms - Max HP +5 (Above Start)": AstalonLocationData("Hall of the Phantoms", "health"),
    "Ruins of Ash - Max HP +1 (Left of Ascent)": AstalonLocationData("Ruins of Ash", "health"),
    "Ruins of Ash - Max HP +2 (Right Side)": AstalonLocationData("Ruins of Ash", "health"),
    "Ruins of Ash - Max HP +5 (After Solaria)": AstalonLocationData(
        "The Apex", "health"
    ),  # this is visually RoA but logically Apex
    "Darkness - Max HP +4": AstalonLocationData("Darkness", "health"),
    "The Apex - Max HP +1 (Blood Chalice)": AstalonLocationData("The Apex", "health"),
    "The Apex - Max HP +5 (After Heart)": AstalonLocationData("The Apex", "health"),
    "Catacombs - Max HP +1 (First Room)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +1 (Cyclops Arena)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +1 (Above Poison Roots)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +2 (Before Poison Roots)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +2 (After Poison Roots)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +2 (Before Gemini Bottom)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +2 (Before Gemini Top)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +2 (Above Gemini)": AstalonLocationData("Catacombs", "health"),
    "Catacombs - Max HP +5 (Item Chain)": AstalonLocationData("Catacombs", "health"),
    "Tower Roots - Max HP +1 (Bottom)": AstalonLocationData("Tower Roots", "health"),
    "Tower Roots - Max HP +2 (Top)": AstalonLocationData("Tower Roots", "health"),
    "Cyclops Den - Max HP +1": AstalonLocationData("Cyclops Den", "health"),
    "Cathedral - Max HP +1 (Top Left)": AstalonLocationData("Cathedral", "health"),
    "Cathedral - Max HP +1 (Top Right)": AstalonLocationData("Cathedral", "health"),
    "Cathedral - Max HP +2 (Left Climb)": AstalonLocationData("Cathedral", "health"),
    "Cathedral - Max HP +5 (Bell)": AstalonLocationData("Cathedral", "health"),
    "Serpent Path - Max HP +1": AstalonLocationData("Serpent Path", "health"),
}

base_id = 333000
location_name_to_id: dict[str, int] = {name: base_id + i for i, name in enumerate(location_table)}


def get_location_group(location_name: str) -> str:
    return location_table[location_name].region


location_name_groups: dict[str, set[str]] = {
    group: set(location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
