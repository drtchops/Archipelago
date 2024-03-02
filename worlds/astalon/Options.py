from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, StartInventoryPool, Toggle


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


class RandomizeItems(Toggle):
    """
    Choose whether to randomize inventory items like gorgon eyes and griffon claw.
    """

    display_name = "Randomize Items"
    default = 1


class RandomizeHealthPickups(Toggle):
    """
    Choose whether to randomize the + Max HP pickups found in the world.
    Does not affect shop upgrades.
    """

    display_name = "Randomize Max HP Pickups"
    default = 1


class RandomizeAttackPickups(Toggle):
    """
    Choose whether to randomize the + Attack pickups found in the world.
    Does not affect shop upgrades.
    """

    display_name = "Randomize Attack Pickups"
    default = 1


class RandomizeWhiteKeys(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize white keys and locked white doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize White Keys"
    default = 0


class RandomizeBlueKeys(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize blue keys and locked blue doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize Blue Keys"
    default = 0


class RandomizeRedKeys(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize red keys and locked red doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize Red Keys"
    default = 0


class SkipCutscenes(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to skip or shorten cutscenes.
    """

    display_name = "Skip Cutscenes"
    default = 1


@dataclass
class AstalonOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    # campaign: Campaign
    # randomize_items: RandomizeItems
    randomize_health_pickups: RandomizeHealthPickups
    randomize_attack_pickups: RandomizeAttackPickups
    # randomize_white_keys: RandomizeWhiteKeys
    # randomize_blue_keys: RandomizeBlueKeys
    # randomize_red_keys: RandomizeRedKeys
    # skip_cutscenes: SkipCutscenes
    death_link: DeathLink
