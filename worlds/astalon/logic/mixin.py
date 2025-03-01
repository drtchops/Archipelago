from typing import TYPE_CHECKING, Dict

from worlds.AutoWorld import LogicMixin

from ..constants import GAME_NAME

if TYPE_CHECKING:
    from BaseClasses import CollectionState, MultiWorld
else:
    CollectionState = object


class AstalonLogicMixin(LogicMixin, CollectionState):
    multiworld: "MultiWorld"

    _astalon_rule_results: Dict[int, Dict[int, bool]]

    def init_mixin(self, multiworld: "MultiWorld") -> None:
        players = multiworld.get_game_players(GAME_NAME)
        self._astalon_rule_results = {player: {} for player in players}

    def copy_mixin(self, new_state: "AstalonLogicMixin") -> "AstalonLogicMixin":
        new_state._astalon_rule_results = {
            player: rule_results.copy() for player, rule_results in self._astalon_rule_results.items()
        }
        return new_state
