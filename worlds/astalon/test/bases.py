from test.bases import WorldTestBase

from .. import AstalonWorld
from ..constants import GAME_NAME


class AstalonTestBase(WorldTestBase):
    game = GAME_NAME
    world: AstalonWorld  # type: ignore
