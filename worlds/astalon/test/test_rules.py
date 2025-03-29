from ..logic.instances import HasInstance
from . import AstalonTestBase


class RuleHashTest(AstalonTestBase):
    auto_construct = False

    @property
    def run_default_tests(self) -> bool:
        return False

    def test_same_rules_have_same_hash(self) -> None:
        rule1 = HasInstance("Item", player=1)
        rule2 = HasInstance("Item", player=1)
        self.assertEquals(hash(rule1), hash(rule2))

    def test_different_rules_have_different_hashes(self) -> None:
        rule1 = HasInstance("Item", player=1)
        rule2 = HasInstance("Item", player=2)
        self.assertNotEquals(hash(rule1), hash(rule2))

        rule3 = HasInstance("Item1", player=1)
        rule4 = HasInstance("Item2", player=1)
        self.assertNotEquals(hash(rule3), hash(rule4))
