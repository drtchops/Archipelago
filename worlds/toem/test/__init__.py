from test.bases import WorldTestBase

from .. import ToemWorld


class ToemTestBase(WorldTestBase):
    game = "TOEM"
    world: ToemWorld  # type: ignore
