from dataclasses import dataclass

from Options import (
    Choice,
    DeathLink,
    DefaultOnToggle,
    NamedRange,
    PerGameCommonOptions,
    StartInventoryPool,
    Toggle,
)


class Campaign(Choice):
    """
    NOT CURRENTLY SUPPORTED
    Set which campaign you wish to play through.
    """

    display_name = "Campaign"
    option_tears_of_the_earth = 0
    option_new_game_plus = 1
    option_black_knight = 2
    option_monster_mode = 3
    default = 0


class RandomizeHealthPickups(DefaultOnToggle):
    """
    Choose whether to randomize the + Max HP pickups found in the world.
    Does not affect shop upgrades.
    """

    display_name = "Randomize Max HP Pickups"


class RandomizeAttackPickups(DefaultOnToggle):
    """
    Choose whether to randomize the + Attack pickups found in the world.
    Does not affect shop upgrades.
    """

    display_name = "Randomize Attack Pickups"


class RandomizeWhiteKeys(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize white keys and locked white doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize White Keys"


class RandomizeBlueKeys(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize blue keys and locked blue doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize Blue Keys"


class RandomizeRedKeys(Toggle):
    """
    Choose whether to randomize red keys and locked red doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize Red Keys"


class RandomizeFamiliars(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize familiar pickups and upgrades.
    This includes all three Old Man checks and Gil in the secret dev room.
    """

    display_name = "Randomize Familiars"


class SkipCutscenes(DefaultOnToggle):
    """
    Choose whether to skip or shorten cutscenes.
    """

    display_name = "Skip Cutscenes"


class StartWithZeek(Toggle):
    """
    Choose whether to start the game with Zeek unlocked.
    """

    display_name = "Start With Zeek"


class StartWithBram(Toggle):
    """
    Choose whether to start the game with Bram unlocked.
    """

    display_name = "Start With Bram"


class StartWithQOL(DefaultOnToggle):
    """
    Choose whether to start the game with various QoL shop upgrades.
    Includes Knowledge, Orb Seeker, Map Reveal, Cartography, Gift, and Titan's Ego.
    """

    display_name = "Start With QoL"


class FreeApexElevator(DefaultOnToggle):
    """
    Choose whether to automatically unlock The Apex elevator when getting Ascendant Key as the vanilla game does.
    Disabling this means you'll have to ascend the whole tower and defeat all normally required bosses.
    """

    display_name = "Free Apex Elevator"


class CostMultiplier(NamedRange):
    """
    NOT YET SUPPORTED
    Set a multiplier for how many orbs shop purchases cost.
    50 means purchases will cost 50% or half the amount of orbs.
    """

    display_name = "Cost Multiplier"
    range_start = 0
    range_end = 200
    default = 100

    special_range_names = {
        "zero": 0,
        "tenth": 10,
        "quarter": 25,
        "half": 50,
        "normal": 100,
        "double": 200,
    }


@dataclass
class AstalonOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    # campaign: Campaign
    randomize_health_pickups: RandomizeHealthPickups
    randomize_attack_pickups: RandomizeAttackPickups
    # randomize_white_keys: RandomizeWhiteKeys
    # randomize_blue_keys: RandomizeBlueKeys
    randomize_red_keys: RandomizeRedKeys
    # randomize_familiars: RandomizeFamiliars
    skip_cutscenes: SkipCutscenes
    start_with_zeek: StartWithZeek
    start_with_bram: StartWithBram
    start_with_qol: StartWithQOL
    free_apex_elevator: FreeApexElevator
    # cost_multiplier: CostMultiplier
    death_link: DeathLink