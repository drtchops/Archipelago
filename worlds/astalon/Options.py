from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, StartInventoryPool


class Campaign(Choice):
    display_name = "Campaign"
    option_tears_of_the_earth = 0
    option_black_knight = 1
    option_monster_mode = 2
    default = 0


@dataclass
class AstalonOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    campaign: Campaign
