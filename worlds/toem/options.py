from dataclasses import dataclass

from Options import PerGameCommonOptions, StartInventoryPool


@dataclass
class ToemOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
