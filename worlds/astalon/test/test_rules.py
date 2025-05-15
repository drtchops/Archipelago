from ..items import BlueDoor, Character, Crystal, KeyItem
from ..logic.factories import And, Has, HasAny, HasBlue, HasSwitch, Or, True_
from ..logic.instances import HasAllInstance, HasInstance, OrInstance
from .bases import AstalonTestBase


class RuleHashTest(AstalonTestBase):
    auto_construct = False

    @property
    def run_default_tests(self) -> bool:
        return False

    def test_same_rules_have_same_hash(self) -> None:
        rule1 = HasInstance("Item", player=1)
        rule2 = HasInstance("Item", player=1)
        self.assertEqual(hash(rule1), hash(rule2))

    def test_different_rules_have_different_hashes(self) -> None:
        rule1 = HasInstance("Item", player=1)
        rule2 = HasInstance("Item", player=2)
        self.assertNotEqual(hash(rule1), hash(rule2))

        rule3 = HasInstance("Item1", player=1)
        rule4 = HasInstance("Item2", player=1)
        self.assertNotEqual(hash(rule3), hash(rule4))


class RuleResolutionTest(AstalonTestBase):
    options = {  # noqa: RUF012
        "difficulty": "easy",
        "randomize_characters": "trio",
        "randomize_key_items": "true",
        "randomize_health_pickups": "true",
        "randomize_attack_pickups": "true",
        "randomize_white_keys": "true",
        "randomize_blue_keys": "true",
        "randomize_red_keys": "true",
        "randomize_shop": "true",
        "randomize_elevator": "true",
        "randomize_switches": "true",
    }

    @property
    def run_default_tests(self) -> bool:
        return False

    def test_upper_path_rule_easy(self) -> None:
        rule = Or(
            HasSwitch(Crystal.GT_ROTA),
            Or(
                True_(opts=(("randomize_characters", 0),)),
                HasAny(Character.ARIAS, Character.BRAM, opts=(("randomize_characters__ge", 1),)),
                opts=(("difficulty", 1),),
            ),
            And(Has(KeyItem.STAR), HasBlue(BlueDoor.GT_RING, otherwise=True)),
            Has(KeyItem.BLOCK),
        )
        expected = OrInstance(
            (
                HasAllInstance(
                    ("Bram", "Morning Star", "Blue Door (Gorgon Tomb - Ring of the Ancients)"),
                    player=self.player,
                ),
                HasAllInstance(("Zeek", "Magic Block"), player=self.player),
                HasInstance("Crystal (Gorgon Tomb - RotA)", player=self.player),
            ),
            player=self.player,
        )
        instance = rule.resolve(self.world)
        self.assertEqual(instance, expected)
