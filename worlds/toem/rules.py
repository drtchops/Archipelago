from enum import Enum
from functools import partial
from typing import TYPE_CHECKING, Callable, Dict, Tuple

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

from .items import ItemName
from .locations import LocationName
from .regions import RegionName

if TYPE_CHECKING:
    from . import ToemWorld


class EventName(str, Enum):
    VICTORY = "TOEM Experienced"


Rule = Callable[[int, CollectionState], bool]

ENTRANCE_RULES: Dict[Tuple[RegionName, RegionName], Rule] = {
    (RegionName.HOMELANDA, RegionName.OAKLAVILLE): lambda player, state: (
        state.has(ItemName.HOMELANDA_STAMP.value, player, 2)
    ),
    (RegionName.OAKLAVILLE, RegionName.STANHAMN): lambda player, state: (
        state.has(ItemName.OAKLAVILLE_STAMP.value, player, 8)
    ),
    (RegionName.STANHAMN, RegionName.LOGCITY): lambda player, state: (
        state.has(ItemName.STANHAMN_STAMP.value, player, 8)
    ),
    (RegionName.LOGCITY, RegionName.KIIRUBERG): lambda player, state: (
        state.has(ItemName.LOGCITY_STAMP.value, player, 8)
    ),
    (RegionName.KIIRUBERG, RegionName.MOUNTAIN_TOP): lambda player, state: (
        state.has(ItemName.KIIRUBERG_STAMP.value, player, 8)
    ),
}

LOCATION_RULES: Dict[LocationName, Rule] = {
    LocationName.QUEST_EXPERIENCE_TOEM: lambda player, state: (
        state.can_reach_region(RegionName.MOUNTAIN_TOP.value, player)
    ),
    LocationName.QUEST_MONSTERS: lambda player, state: state.can_reach_region(RegionName.KIIRUBERG.value, player),
    LocationName.QUEST_GHOST_HELPER: lambda player, state: state.can_reach_region(RegionName.LOGCITY.value, player),
    LocationName.QUEST_PAINTINGS: lambda player, state: state.can_reach_region(RegionName.MOUNTAIN_TOP.value, player),
}


def set_region_rules(world: "ToemWorld"):
    for (from_, to_), rule in ENTRANCE_RULES.items():
        set_rule(world.get_entrance(f"{from_.value} -> {to_.value}"), partial(rule, world.player))


def set_location_rules(world: "ToemWorld"):
    for location_name, rule in LOCATION_RULES.items():
        set_rule(world.get_location(location_name.value), partial(rule, world.player))
