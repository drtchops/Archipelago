from typing import TYPE_CHECKING, Dict, Set

from worlds.AutoWorld import LogicMixin

from ..constants import GAME_NAME

if TYPE_CHECKING:
    from BaseClasses import MultiWorld


class AstalonLogicMixin(LogicMixin):
    multiworld: "MultiWorld"

    _astalon_computed_rules: Dict[int, Set[int]]

    def init_mixin(self, multiworld: "MultiWorld") -> None:
        players = multiworld.get_game_players(GAME_NAME)
        self._astalon_computed_rules = {player: set() for player in players}

    # Don't copy cache so playthrough treats everything as stale
    # def copy_mixin(self, new_state: "CollectionState") -> "CollectionState":
    #     new_state._astalon_computed_rules = {  # type: ignore
    #         player: rule_ids.copy() for player, rule_ids in self._astalon_computed_rules.items()
    #     }
    #     return new_state
