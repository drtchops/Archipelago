from test.bases import WorldTestBase

from .. import AstalonWorld
from ..constants import GAME_NAME


class AstalonTestBase(WorldTestBase):
    game = GAME_NAME
    world: AstalonWorld  # type: ignore

    def tearDown(self) -> None:
        if getattr(self, "world", None) and getattr(self.world, "rules", None):
            self.world.rules.clear_cache()
        return super().tearDown()
