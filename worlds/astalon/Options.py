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


class Difficulty(Choice):
    """
    Choose how difficult of a playthrough the logic expects.
    Hard difficulty expects extra jump height with Arias, sticking blocks in walls with Zeek,
    or hitting magic crystals with Kyuli or Bram.
    """

    display_name = "Difficulty"
    option_easy = 0
    option_hard = 1
    default = 0


class Campaign(Choice):
    """
    NOT YET SUPPORTED
    Set which campaign you wish to play through.
    """

    display_name = "Campaign"
    option_tears_of_the_earth = 0
    option_new_game_plus = 1
    option_black_knight = 2
    option_monster_mode = 3
    default = 0


class RandomizeCharacters(Choice):
    """
    Choose how the 5 characters are randomized.
    vanilla: Start with the default 3 characters and unlock Zeek and Bram in-game as normal
    trio: Start with the default 3 characters and receive Zeek and Bram as items
    solo: Start with one random character and receive the rest as items
    all: Start with all 5 characters
    random_selection: Start with a random selection of the characters and receive the rest as items
    """

    display_name = "Randomize Characters"
    option_vanilla = 0
    option_trio = 1
    option_solo = 2
    option_all = 3
    option_random_selection = 4
    default = 1


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
    Choose whether to randomize white keys and locked white doors.
    Keys are location checks and door unlocks are received as items.
    """

    display_name = "Randomize White Keys"


class RandomizeBlueKeys(Toggle):
    """
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


class RandomizeShop(Toggle):
    """
    Choose whether to randomize the purchases in Epimetheus's shop.
    All unique shop upgrades will be randomized, including the three special powers for each character.
    """

    display_name = "Randomize Shop"


class RandomizeSwitches(Toggle):
    """
    Choose whether to randomize all switches and magic crystals in the world.
    Activating a switch will complete a check and the corresponding doors or blocks will open from a received item.
    """

    display_name = "Randomize Switches"


class RandomizeElevator(Toggle):
    """
    Choose whether to randomize the elevator destinations.
    Finding elevators will complete checks and you will receive elevator destinations as items.
    """

    display_name = "Randomize Elevator"


class RandomizeFamiliars(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize familiar pickups and upgrades.
    This includes all three Old Man checks and Gil in the secret dev room.
    """

    display_name = "Randomize Familiars"


class RandomizeOrbCrates(Toggle):
    """
    NOT YET SUPPORTED
    """

    display_name = "Randomize Orb Crates"


class RandomizeBossOrbRewards(Toggle):
    """
    NOT YET SUPPORTED
    """

    display_name = "Randomize Boss Orb Rewards"


class RandomizeMinibossOrbRewards(Toggle):
    """
    NOT YET SUPPORTED
    """

    display_name = "Randomize Miniboss Orb Rewards"


class SkipCutscenes(DefaultOnToggle):
    """
    Choose whether to skip or shorten cutscenes.
    """

    display_name = "Skip Cutscenes"


class StartWithQOL(DefaultOnToggle):
    """
    Choose whether to start the game with various Quality of Life shop upgrades.
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
    Set a multiplier for how many orbs shop purchases cost.
    """

    display_name = "Cost Multiplier"
    range_start = 0
    range_end = 200
    default = 50

    special_range_names = {
        "zero": 0,
        "tenth": 10,
        "quarter": 25,
        "half": 50,
        "normal": 100,
        "double": 200,
    }


class FastBloodChalice(DefaultOnToggle):
    """
    Makes the Blood Chalice regeneration rate 5x faster so you spend less time standing around.
    """

    display_name = "Free Blood Chalice"


class CampfireWarp(DefaultOnToggle):
    """
    Allows you to warp to any campfire you've previously visited.
    """

    display_name = "Campfire Warp"


class OpenEarlyDoors(DefaultOnToggle):
    """
    Opens some Gorgon's Tomb doors by default when using key rando to give you a bigger sphere 1.
    Has no effect when not using white or blue key rando.
    """

    display_name = "Open Early Doors"


class CheapKyuliRay(Toggle):
    """
    Make's Kyuli's Shining Ray only cost 50 orbs. You still need to have at least 500 to fire it.
    Recommended when using hard logic as it can activate crystals.
    """

    display_name = "Cheap Kyuli Ray"


@dataclass
class AstalonOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    difficulty: Difficulty
    # campaign: Campaign
    randomize_characters: RandomizeCharacters
    randomize_health_pickups: RandomizeHealthPickups
    randomize_attack_pickups: RandomizeAttackPickups
    randomize_white_keys: RandomizeWhiteKeys
    randomize_blue_keys: RandomizeBlueKeys
    randomize_red_keys: RandomizeRedKeys
    randomize_shop: RandomizeShop
    randomize_elevator: RandomizeElevator
    randomize_switches: RandomizeSwitches
    # randomize_familiars: RandomizeFamiliars
    # randomize_orb_crates: RandomizeOrbCrates
    # randomize_boss_orb_rewards: RandomizeBossOrbRewards
    # randomize_miniboss_orb_rewards: RandomizeMinibossOrbRewards
    skip_cutscenes: SkipCutscenes
    start_with_qol: StartWithQOL
    free_apex_elevator: FreeApexElevator
    cost_multiplier: CostMultiplier
    fast_blood_chalice: FastBloodChalice
    campfire_warp: CampfireWarp
    open_early_doors: OpenEarlyDoors
    cheap_kyuli_ray: CheapKyuliRay
    death_link: DeathLink
