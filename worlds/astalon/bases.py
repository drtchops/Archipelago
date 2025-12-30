from typing import ClassVar

from BaseClasses import MultiWorld
from rule_builder.cached_world import CachedRuleBuilderWorld

from .items import Character
from .options import AstalonOptions
from .settings import AstalonSettings


class AstalonWorldBase(CachedRuleBuilderWorld):
    options_dataclass = AstalonOptions
    settings: ClassVar[AstalonSettings]  # pyright: ignore[reportIncompatibleVariableOverride]

    options: AstalonOptions  # pyright: ignore[reportIncompatibleVariableOverride]
    starting_characters: list[Character]
    extra_gold_eyes: int = 0

    def __init__(self, multiworld: MultiWorld, player: int) -> None:
        super().__init__(multiworld, player)
        self.starting_characters = []
