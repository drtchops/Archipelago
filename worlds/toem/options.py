from dataclasses import dataclass

from Options import PerGameCommonOptions, StartInventoryPool, Toggle


class RandomizeThing(Toggle):
    display_name = "Randomize Thing"
    default = 1


@dataclass
class ToemOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    randomize_thing: RandomizeThing
