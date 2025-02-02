from dataclasses import dataclass

from Options import PerGameCommonOptions, StartInventoryPool, Toggle, Visibility


class IncludeAchievements(Toggle):
    """Include achievements as locations."""

    display_name = "Include Achievements"
    default = 0
    visibility = Visibility.none


class IncludeBasto(Toggle):
    """Include the post-game section Basto."""

    display_name = "Include Basto"
    default = 0
    visibility = Visibility.none


@dataclass
class ToemOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    include_achievements: IncludeAchievements
    include_basto: IncludeBasto
