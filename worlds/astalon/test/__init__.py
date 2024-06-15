from test.bases import WorldTestBase

from .. import AstalonWorld


class AstalonTestBase(WorldTestBase):
    game = "Astalon"
    world: AstalonWorld  # type: ignore

    def tearDown(self) -> None:
        if getattr(self, "world", None):
            self.world.rules.clear_cache()
        return super().tearDown()
