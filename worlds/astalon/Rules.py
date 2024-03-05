from dataclasses import dataclass
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .Items import Items

if TYPE_CHECKING:
    from . import AstalonWorld


@dataclass
class AstalonRules:
    world: "AstalonWorld"

    def entrance(self, name: str):
        return self.world.multiworld.get_entrance(name, self.world.player)

    def location(self, name: str):
        return self.world.multiworld.get_location(name, self.world.player)

    def has_zeek(self, state: CollectionState):
        return self.world.options.start_with_zeek or self.has_all(Items.EYE_RED, Items.EYE_BLUE)(state)

    def has_bram(self, state: CollectionState):
        return self.world.options.start_with_bram or self.has_all(
            Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.CLAW, Items.VOID
        )(state)

    def has(self, item: Items, count: int = 1):
        def has_item(state: CollectionState):
            if item == Items.BLOCK and not self.has_zeek(state):
                return False
            if item == Items.STAR and not self.has_bram(state):
                return False
            return state.has(item.value, self.world.player, count=count)

        return has_item

    def has_all(self, *items: Items):
        def has_all_items(state: CollectionState):
            # cover zeek/bram logic instead of calling state.has_all
            for item in items:
                if not self.has(item)(state):
                    return False
            return True

        return has_all_items

    def has_any(self, *items: Items):
        def has_any_item(state: CollectionState):
            # cover zeek/bram logic instead of calling state.has_any
            for item in items:
                if self.has(item)(state):
                    return True
            return False

        return has_any_item

    def set_region_rules(self):
        set_rule(
            self.entrance("Gorgon Tomb -> Mechanism"),
            self.has(Items.EYE_RED),
        )
        set_rule(
            self.entrance("Gorgon Tomb -> The Apex"),
            self.has(Items.KEY_ASCENDANT),
        )
        set_rule(
            self.entrance("Mechanism -> Hall of the Phantoms"),
            self.has(Items.EYE_BLUE),
        )
        set_rule(
            self.entrance("Mechanism -> Cyclops Den"),
            self.has(Items.EYE_BLUE),
        )
        set_rule(
            self.entrance("Hall of the Phantoms -> Ruins of Ash"),
            self.has_all(Items.CLAW, Items.BELL),
        )
        set_rule(
            self.entrance("Hall of the Phantoms -> Cathedral"),
            self.has_all(Items.EYE_GREEN, Items.BOW, Items.BELL),
        )
        set_rule(
            self.entrance("Ruins of Ash -> The Apex"),
            self.has(Items.EYE_GREEN),
        )
        set_rule(
            self.entrance("Ruins of Ash -> Serpent Path"),
            self.has_all(Items.EYE_GREEN, Items.CLOAK, Items.BOW),
        )
        set_rule(
            self.entrance("The Apex -> Final Boss"),
            lambda state: self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.BELL)(state)
            and self.has_any(Items.KEY_ASCENDANT, Items.CLAW)(state),
        )
        set_rule(
            self.entrance("Catacombs -> Tower Roots"),
            self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.VOID, Items.CLAW),
        )

    def set_location_rules(self):
        set_rule(
            self.location("Gorgon Tomb - Ring of the Ancients"),
            self.has(Items.EYE_RED),
        )
        set_rule(
            self.location("Gorgon Tomb - Sword of Mirrors"),
            self.has(Items.EYE_RED),
        )
        set_rule(
            self.location("Gorgon Tomb - Void Charm"),
            self.has(Items.EYE_RED),
        )
        # set_rule(
        #     self.location("Gorgon Tomb - Monster Ball"),
        #     self.has(Items.EYE_RED),
        # )
        set_rule(
            self.location("Mechanism - Cloak of Levitation"),
            self.has(Items.EYE_BLUE),
        )
        set_rule(
            self.location("Hall of the Phantoms - Griffon Claw"),
            self.has(Items.BELL),
        )
        set_rule(
            self.location("Hall of the Phantoms - Dead Maiden's Ring"),
            self.has_all(Items.SWORD, Items.BANISH, Items.BELL, Items.CLAW),
        )
        set_rule(
            self.location("Hall of the Phantoms - Boreas Gauntlet"),
            self.has_all(Items.EYE_GREEN, Items.CLAW, Items.BELL),
        )
        set_rule(
            self.location("The Apex - Blood Chalice"),
            self.has_all(Items.KEY_ADORNED, Items.STAR),
        )
        set_rule(
            self.location("Catacombs - Lunarian Bow"),
            self.has(Items.EYE_RED),
        )
        set_rule(
            self.location("Tower Roots - Adorned Key"),
            self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN),
        )
        # set_rule(
        #     self.location("Catacombs - Gil"),
        #     self.has(Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.BLOCK),
        # )

        if self.world.options.randomize_attack_pickups:
            set_rule(
                self.location("Gorgon Tomb - Attack +1"),
                self.has(Items.EYE_GREEN),
            )
            set_rule(
                self.location("Mechanism - Attack +1 (Above Volantis)"),
                self.has_all(Items.CLAW, Items.BOW),
            )
            set_rule(
                self.location("Mechanism - Attack +1 (Morning Star Blocks)"),
                self.has(Items.STAR),
            )
            set_rule(
                self.location("Ruins of Ash - Attack +1"),
                self.has(Items.STAR),
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Item Chain Red)"),
                self.has(Items.EYE_RED),
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Item Chain Blue)"),
                self.has_all(Items.EYE_RED, Items.EYE_BLUE),
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Item Chain Green)"),
                self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN),
            )
            set_rule(
                self.location("Catacombs - Attack +1 (Poison Roots)"),
                self.has(Items.EYE_RED),
            )
            set_rule(
                self.location("Cathedral - Attack +1"),
                self.has(Items.BOW),  # double check
            )

        if self.world.options.randomize_health_pickups:
            set_rule(
                self.location("Gorgon Tomb - Max HP +1 (Ring of the Ancients)"),
                self.has_all(Items.EYE_RED, Items.SWORD),
            )
            set_rule(
                self.location("Gorgon Tomb - Max HP +5 (Ascendant Key)"),
                self.has(Items.CLAW),
            )
            set_rule(
                self.location("Mechanism - Max HP +1 (Morning Star Blocks)"),
                self.has(Items.STAR),
            )
            set_rule(
                self.location("Mechanism - Max HP +3 (Above Checkpoint)"),
                self.has(Items.CLAW),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +1 (Griffon Claw)"),
                self.has(Items.BELL),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +2 (Secret Ladder)"),
                self.has(Items.BELL),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +2 (Boreas Gauntlet)"),
                self.has_all(Items.EYE_GREEN, Items.CLAW),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +5 (Old Man)"),
                self.has_all(Items.EYE_GREEN, Items.BELL, Items.CLAW),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +5 (Teleport Maze)"),
                self.has_all(Items.EYE_GREEN, Items.BELL, Items.CLAW, Items.VOID, Items.CLOAK),
            )
            set_rule(
                self.location("Hall of the Phantoms - Max HP +5 (Above Start)"),
                self.has(Items.CLAW),
            )
            set_rule(
                self.location("Ruins of Ash - Max HP +2 (Right Side)"),
                self.has_any(Items.GAUNTLET, Items.STAR),
            )
            set_rule(
                self.location("Ruins of Ash - Max HP +5 (After Solaria)"),
                self.has(Items.EYE_GREEN),
            )
            set_rule(
                self.location("Catacombs - Max HP +1 (First Room)"),
                self.has(Items.BOW),
            )
            set_rule(
                self.location("Catacombs - Max HP +1 (Cyclops Arena)"),
                self.has(Items.SWORD),
            )
            set_rule(
                self.location("Catacombs - Max HP +1 (Above Poison Roots)"),
                self.has_all(Items.EYE_RED, Items.BOW),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Before Poison Roots)"),
                self.has_all(Items.EYE_RED, Items.BOW),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (After Poison Roots)"),
                self.has_all(Items.EYE_RED, Items.BOW),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Before Gemini Bottom)"),
                self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.CLAW),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Before Gemini Top)"),
                self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.CLAW),
            )
            set_rule(
                self.location("Catacombs - Max HP +2 (Above Gemini)"),
                self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.BOW, Items.GAUNTLET, Items.CLAW),
            )
            set_rule(
                self.location("Catacombs - Max HP +5 (Item Chain)"),
                self.has_all(Items.EYE_RED, Items.EYE_BLUE, Items.EYE_GREEN, Items.STAR),
            )
            set_rule(
                self.location("Tower Roots - Max HP +1 (Bottom)"),
                self.has(Items.EYE_BLUE),
            )
            set_rule(
                self.location("Tower Roots - Max HP +2 (Top)"),
                self.has(Items.EYE_BLUE),
            )
            set_rule(
                self.location("Cathedral - Max HP +2 (Left Climb)"),
                self.has(Items.CLAW),
            )
