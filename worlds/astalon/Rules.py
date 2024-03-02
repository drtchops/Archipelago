from dataclasses import dataclass
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import KeyItem

if TYPE_CHECKING:
    from . import AstalonWorld


@dataclass
class AstalonRules:
    world: "AstalonWorld"

    def entrance(self, name: str):
        return self.world.multiworld.get_entrance(name, self.world.player)

    def location(self, name: str):
        return self.world.multiworld.get_location(name, self.world.player)

    def has_red_eye(self, state: CollectionState):
        return state.has(KeyItem.EYE_RED, self.world.player)

    def has_blue_eye(self, state: CollectionState):
        return state.has(KeyItem.EYE_BLUE, self.world.player)

    def has_green_eye(self, state: CollectionState):
        return state.has(KeyItem.EYE_GREEN, self.world.player)

    def has_two_eyes(self, state: CollectionState):
        return self.has_red_eye(state) and self.has_blue_eye(state)

    def has_three_eyes(self, state: CollectionState):
        return self.has_two_eyes(state) and self.has_green_eye(state)

    def has_elevators(self, state: CollectionState):
        return state.has(KeyItem.KEY_ASCENDANT, self.world.player)

    def has_claw(self, state: CollectionState):
        return state.has(KeyItem.CLAW, self.world.player)

    def has_bell(self, state: CollectionState):
        return state.has(KeyItem.BELL, self.world.player)

    def has_cloak(self, state: CollectionState):
        return state.has(KeyItem.CLOAK, self.world.player)

    def has_sword(self, state: CollectionState):
        return state.has(KeyItem.SWORD, self.world.player)

    def has_bow(self, state: CollectionState):
        return state.has(KeyItem.BOW, self.world.player)

    def has_block(self, state: CollectionState):
        return state.has(KeyItem.BLOCK, self.world.player)

    def has_star(self, state: CollectionState):
        return state.has(KeyItem.STAR, self.world.player)

    def has_gauntlet(self, state: CollectionState):
        return state.has(KeyItem.GAUNTLET, self.world.player)

    def has_adorned_key(self, state: CollectionState):
        return state.has(KeyItem.KEY_ADORNED, self.world.player)

    def has_void(self, state: CollectionState):
        return state.has(KeyItem.VOID, self.world.player)

    def has_items(self, state: CollectionState, items: list[KeyItem]):
        return state.has_all(items, self.world.player)

    def set_region_rules(self):
        set_rule(
            self.entrance("Gorgon Tomb -> Mechanism"),
            self.has_red_eye,
        )
        set_rule(
            self.entrance("Gorgon Tomb -> The Apex"),
            self.has_elevators,
        )
        set_rule(
            self.entrance("Mechanism -> Hall of the Phantoms"),
            self.has_blue_eye,
        )
        set_rule(
            self.entrance("Mechanism -> Cyclops Den"),
            self.has_blue_eye,
        )
        set_rule(
            self.entrance("Hall of the Phantoms -> Ruins of Ash"),
            lambda state: self.has_claw(state) and self.has_bell(state),
        )
        set_rule(
            self.entrance("Hall of the Phantoms -> Cathedral"),
            lambda state: self.has_items(state, [KeyItem.EYE_GREEN, KeyItem.BOW, KeyItem.BELL]),
        )
        set_rule(
            self.entrance("Ruins of Ash -> The Apex"),
            self.has_green_eye,
        )
        set_rule(
            self.entrance("Ruins of Ash -> Serpent Path"),
            lambda state: self.has_items(state, [KeyItem.EYE_GREEN, KeyItem.CLOAK, KeyItem.BOW]),
        )
        set_rule(
            self.entrance("The Apex -> Final Boss"),
            lambda state: (
                self.has_three_eyes(state)
                and self.has_bell(state)
                and (self.has_elevators(state) or self.has_claw(state))
            ),
        )
        set_rule(
            self.entrance("Catacombs -> Tower Roots"),
            lambda state: self.has_red_eye(state) and self.has_bow(state) and self.has_void(state),
        )

    def set_location_rules(self):
        set_rule(
            self.location("Gorgon Tomb - Ring of the Ancients"),
            self.has_red_eye,
        )
        set_rule(
            self.location("Gorgon Tomb - Sword of Mirrors"),
            self.has_red_eye,
        )
        set_rule(
            self.location("Gorgon Tomb - Void Charm"),
            self.has_red_eye,
        )
        # set_rule(
        #     self.location("Gorgon Tomb - Monster Ball"),
        #     self.has_red_eye,
        # )
        set_rule(
            self.location("Mechanism - Cloak of Levitation"),
            self.has_blue_eye,
        )
        set_rule(
            self.location("Hall of the Phantoms - Griffon Claw"),
            self.has_bell,
        )
        set_rule(
            self.location("Hall of the Phantoms - Dead Maiden's Ring"),
            self.has_sword,
        )
        set_rule(
            self.location("Hall of the Phantoms - Boreas Gauntlet"),
            lambda state: self.has_items(state, [KeyItem.EYE_GREEN, KeyItem.CLAW, KeyItem.BELL]),
        )
        set_rule(
            self.location("The Apex - Blood Chalice"),
            lambda state: self.has_items(state, [KeyItem.KEY_ADORNED, KeyItem.STAR]),
        )
        set_rule(
            self.location("Catacombs - Lunarian Bow"),
            self.has_red_eye,
        )
        set_rule(
            self.location("Tower Roots - Adorned Key"),
            self.has_three_eyes,
        )
        # set_rule(
        #     self.location("Catacombs - Gil"),
        #     lambda state: self.has_three_eyes(state) and self.has_block(state),
        # )

        if self.world.options.randomize_attack_pickups:
            set_rule(
                self.location("Gorgon Tomb - Attack +1"),
                self.has_green_eye,
            )
            set_rule(
                self.location("Mechanism - Attack +1 (Above Volantis)"),
                lambda state: self.has_claw(state) and self.has_bow(state),
            )
            set_rule(
                self.location("Mechanism - Attack +1 (Morning Star Blocks)"),
                self.has_star,
            )
            set_rule(
                self.location("Ruins of Ash - Attack +1"),
                self.has_star,
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Item Chain Red)"),
                self.has_red_eye,
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Item Chain Blue)"),
                self.has_two_eyes,
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Item Chain Green)"),
                self.has_three_eyes,
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Climbable Root)"),
                self.has_red_eye,
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Poison Roots)"),
                self.has_red_eye,
            )
            set_rule(
                self.location("Cathedral - Attack +1"),
                self.has_bow,  # double check
            )

        if self.world.options.randomize_health_pickups:
            set_rule(
                self.location("Gorgon Tomb - Max HP +1 (Ring of the Ancients)"),
                lambda state: self.has_red_eye(state) and self.has_sword(state),
            )
            set_rule(
                self.location("Gorgon Tomb - Max HP +5 (Ascendant Key)"),
                self.has_claw,
            )
            set_rule(
                self.location("Mechanism - Max HP +1 (Morning Star Blocks)"),
                self.has_star,
            )
            set_rule(
                self.location("Mechanism - Max HP +3 (Above Checkpoint)"),
                self.has_claw,
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +1 (Griffon Claw)"),
                self.has_bell,
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +2 (Secret Ladder)"),
                self.has_bell,
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +2 (Boreas Gauntlet)"),
                lambda state: self.has_claw(state) and self.has_green_eye(state),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +5 (Old Man)"),
                lambda state: self.has_items(
                    state, [KeyItem.EYE_GREEN, KeyItem.BELL, KeyItem.CLAW]
                ),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +5 (Teleport Maze)"),
                lambda state: self.has_items(
                    state,
                    [KeyItem.EYE_GREEN, KeyItem.BELL, KeyItem.CLAW, KeyItem.VOID, KeyItem.CLOAK],
                ),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +5 (Above Start)"),
                self.has_claw,
            )
            set_rule(
                self.location("Ruins of Ash - Max HP +2 (Right Side)"),
                lambda state: self.has_gauntlet(state) or self.has_star(state),
            )
            set_rule(
                self.location("Ruins of Ash - Max HP +5 (After Solaria)"),
                self.has_green_eye,
            )
            set_rule(
                self.location("Catacombs - Max HP +1 (First Room)"),
                self.has_bow,
            )
            set_rule(
                self.location("Catacombs - Max HP +1 (Cyclops Arena)"),
                self.has_sword,
            )
            set_rule(
                self.location("Catacombs - Max HP +1 (Above Poison Roots)"),
                self.has_red_eye,
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Before Poison Roots)"),
                self.has_red_eye,
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (After Poison Roots)"),
                self.has_red_eye,
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Before Gemini Bottom)"),
                lambda state: self.has_red_eye(state) and self.has_bow(state),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Before Gemini Top)"),
                lambda state: self.has_red_eye(state) and self.has_bow(state),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Above Gemini)"),
                lambda state: self.has_red_eye(state)
                and self.has_gauntlet(state)
                and self.has_claw(state),
            )
            set_rule(
                self.location("Catacombs - Max HP +5 (Item Chain)"),
                lambda state: self.has_three_eyes(state) and self.has_star(state),
            )
            set_rule(
                self.location("Tower Roots - Max HP +1 (Bottom)"),
                self.has_blue_eye,
            )
            set_rule(
                self.location("Tower Roots - Max HP +2 (Top)"),
                self.has_blue_eye,
            )
            set_rule(
                self.location("Cathedral - Max HP +2 (Left Climb)"),
                self.has_claw,
            )
