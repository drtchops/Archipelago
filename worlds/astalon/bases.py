from abc import ABCMeta
from collections import defaultdict
from typing import TYPE_CHECKING, Any, ClassVar

from BaseClasses import MultiWorld
from worlds.AutoWorld import AutoWorldRegister, World

from .items import Character, EarlyItems
from .options import AstalonOptions
from .settings import AstalonSettings

if TYPE_CHECKING:
    from .logic.instances import RuleInstance


# TODO: remove once ap 0.6.6 is released
class AstalonWorldMetaclass(AutoWorldRegister, ABCMeta):
    def __new__(mcs, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> AutoWorldRegister:
        if name == "AstalonWorld":
            return super().__new__(mcs, name, bases, dct)
        return super(AutoWorldRegister, mcs).__new__(mcs, name, bases, dct)


class AstalonWorldBase(World, metaclass=AstalonWorldMetaclass):
    options_dataclass = AstalonOptions
    settings: ClassVar[AstalonSettings]  # pyright: ignore[reportIncompatibleVariableOverride]

    options: AstalonOptions  # pyright: ignore[reportIncompatibleVariableOverride]
    starting_characters: list[Character]
    extra_gold_eyes: int = 0
    early_items: EarlyItems
    portal_pairs: tuple[tuple[str, str], ...] = ()

    rule_cache: "dict[int, RuleInstance]"
    _rule_deps: dict[str, set[int]]

    def __init__(self, multiworld: MultiWorld, player: int) -> None:
        super().__init__(multiworld, player)
        self.starting_characters = []
        self.early_items = EarlyItems()
        self.rule_cache = {}
        self._rule_deps = defaultdict(set)
