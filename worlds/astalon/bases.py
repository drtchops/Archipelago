from typing import ClassVar

from BaseClasses import MultiWorld
from worlds.AutoWorld import World

from .items import Character, EarlyItems
from .options import AstalonOptions
from .settings import AstalonSettings


class AstalonWorldBase(World):
    options_dataclass = AstalonOptions
    settings: ClassVar[AstalonSettings]  # pyright: ignore[reportIncompatibleVariableOverride]

    options: AstalonOptions  # pyright: ignore[reportIncompatibleVariableOverride]
    starting_characters: list[Character]
    extra_gold_eyes: int = 0
    early_items: EarlyItems
    portal_pairs: tuple[tuple[str, str], ...] = ()

    def __init__(self, multiworld: MultiWorld, player: int) -> None:
        super().__init__(multiworld, player)
        self.starting_characters = []
        self.early_items = EarlyItems()
