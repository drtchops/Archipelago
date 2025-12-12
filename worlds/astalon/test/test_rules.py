from typing_extensions import override

from rule_builder import And, OptionFilter, Or, True_

from ..items import BlueDoor, Crystal
from ..logic.custom_rules import Has, HasAll, HasBlue, HasSwitch
from ..logic.main_campaign import has_arias, has_block, has_bram, has_star
from ..options import Difficulty, RandomizeCharacters
from .bases import AstalonTestBase


class RuleHashTest(AstalonTestBase):
    auto_construct = False

    @property
    @override
    def run_default_tests(self) -> bool:
        return False

    def test_same_rules_have_same_hash(self) -> None:
        rule1 = Has.Resolved("Item", player=1)
        rule2 = Has.Resolved("Item", player=1)
        self.assertEqual(hash(rule1), hash(rule2))

    def test_different_rules_have_different_hashes(self) -> None:
        rule1 = Has.Resolved("Item", player=1)
        rule2 = Has.Resolved("Item", player=2)
        self.assertNotEqual(hash(rule1), hash(rule2))

        rule3 = Has.Resolved("Item1", player=1)
        rule4 = Has.Resolved("Item2", player=1)
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
    @override
    def run_default_tests(self) -> bool:
        return False

    def test_upper_path_rule_easy(self) -> None:
        rule = Or(
            HasSwitch(Crystal.GT_ROTA),
            Or(
                True_(options=[OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla)]),
                Or(
                    has_arias | has_bram,
                    options=[OptionFilter(RandomizeCharacters, RandomizeCharacters.option_vanilla, operator="gt")],
                ),
                options=[OptionFilter(Difficulty, Difficulty.option_hard)],
            ),
            And(has_star, HasBlue(BlueDoor.GT_RING, otherwise=True)),
            has_block,
        )
        expected = Or.Resolved(
            (
                HasAll.Resolved(
                    ("Blue Door (Gorgon Tomb - Ring of the Ancients)", "Bram", "Morning Star"),
                    player=self.player,
                ),
                HasAll.Resolved(("Magic Block", "Zeek"), player=self.player),
                Has.Resolved("Crystal (Gorgon Tomb - RotA)", player=self.player),
            ),
            player=self.player,
        )
        instance = rule.resolve(self.world)
        self.assertEqual(instance, expected, f"\n{instance}\n{expected}")
