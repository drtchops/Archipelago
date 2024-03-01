from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import AstalonWorld


eye_red = "Gorgon Eye (Red)"
eye_blue = "Gorgon Eye (Blue)"
eye_green = "Gorgon Eye (Green)"
key_elevator = "Ascendant Key"
# key_cyclops = "Cyclops Idol"
key_chalice = "Adorned Key"
claw = "Griffon Claw"
bow = "Lunarian Bow"
mirror_sword = "Sword of Mirrors"
break_blocks = "Morning Star"
magic_block = "Magic Block"
cloak = "Cloak of Levitation"
bell = "Athena's Bell"


def set_region_rules(world: "AstalonWorld"):
    set_rule(
        world.multiworld.get_entrance("Gorgon Tomb -> Mechanism", world.player),
        lambda state: state.has(eye_red, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Gorgon Tomb -> The Apex", world.player),
        lambda state: state.has(key_elevator, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Mechanism -> Hall of the Phantoms", world.player),
        lambda state: state.has(eye_blue, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Mechanism -> Cyclops Den", world.player),
        lambda state: state.has(eye_blue, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Hall of the Phantoms -> Ruins of Ash", world.player),
        lambda state: state.has(claw, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Hall of the Phantoms -> Cathedral", world.player),
        lambda state: state.has(eye_blue, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Ruins of Ash -> The Apex", world.player),
        lambda state: state.has(eye_green, world.player),
    )
    set_rule(
        world.multiworld.get_entrance("Ruins of Ash -> Serpent Path", world.player),
        lambda state: state.has_any([eye_green, cloak], world.player),
    )
    set_rule(
        world.multiworld.get_entrance("The Apex -> Final Boss", world.player),
        lambda state: (
            state.has_all([eye_red, eye_blue, eye_green], world.player)
            and (state.has(key_elevator, world.player) or state.has_all([claw, bell], world.player))
        ),
    )
    set_rule(
        world.multiworld.get_entrance("Catacombs -> Tower Roots", world.player),
        lambda state: state.has(bow, world.player),
    )


def set_location_rules(world: "AstalonWorld"):
    set_rule(
        world.multiworld.get_location("Gorgon Tomb - Ring of the Ancients", world.player),
        lambda state: state.has(eye_red, world.player),
    )
    set_rule(
        world.multiworld.get_location("Gorgon Tomb - Sword of Mirrors", world.player),
        lambda state: state.has(eye_red, world.player),
    )
    set_rule(
        world.multiworld.get_location("Gorgon Tomb - Void Charm", world.player),
        lambda state: state.has(eye_red, world.player),
    )
    # set_rule(
    #     world.multiworld.get_location("Gorgon Tomb - Monster Ball", world.player),
    #     lambda state: state.has(eye_red, world.player),
    # )
    set_rule(
        world.multiworld.get_location("Mechanism - Cloak of Levitation", world.player),
        lambda state: state.has(eye_blue, world.player),
    )
    set_rule(
        world.multiworld.get_location("Hall of the Phantoms - Dead Maiden's Ring", world.player),
        lambda state: state.has(mirror_sword, world.player),
    )
    set_rule(
        world.multiworld.get_location("The Apex - Blood Chalice", world.player),
        lambda state: state.has_all([key_chalice, break_blocks], world.player),
    )
    # set_rule(
    #     world.multiworld.get_location("Catacombs - Gil", world.player),
    #     lambda state: state.has_all([eye_red, eye_blue, eye_green, magic_block], world.player),
    # )
    set_rule(
        world.multiworld.get_location("Tower Roots - Adorned Key", world.player),
        lambda state: state.has_all([eye_red, eye_blue, eye_green], world.player),
    )
