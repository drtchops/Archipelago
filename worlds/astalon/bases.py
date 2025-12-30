from abc import ABCMeta
from typing import Any, ClassVar

from rule_builder import RuleWorldMixin
from worlds.AutoWorld import AutoWorldRegister, World

from .constants import GAME_NAME
from .items import Character
from .options import AstalonOptions
from .settings import AstalonSettings


class AstalonWorldMetaclass(AutoWorldRegister, ABCMeta):
    def __new__(mcs, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> AutoWorldRegister:
        if name == "AstalonWorld":
            return super().__new__(mcs, name, bases, dct)
        return super(AutoWorldRegister, mcs).__new__(mcs, name, bases, dct)


class AstalonWorldBase(RuleWorldMixin, World, metaclass=AstalonWorldMetaclass):  # pyright: ignore[reportUnsafeMultipleInheritance]
    game = GAME_NAME
    options_dataclass = AstalonOptions
    settings: ClassVar[AstalonSettings]  # pyright: ignore[reportIncompatibleVariableOverride]

    options: AstalonOptions  # pyright: ignore[reportIncompatibleVariableOverride]
    starting_characters: list[Character]
    extra_gold_eyes: int = 0
