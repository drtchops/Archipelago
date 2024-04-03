from test.bases import WorldTestBase

from .. import AstalonWorld


class AstalonTestBase(WorldTestBase):
    game = "Astalon"
    world: AstalonWorld
