from typing import ClassVar

from test.bases import WorldTestBase

from .. import ToemWorld
from ..constants import GAME_NAME


class ToemTestBase(WorldTestBase):
    game: ClassVar[str] = GAME_NAME
    world: ToemWorld  # pyright: ignore[reportIncompatibleVariableOverride]
