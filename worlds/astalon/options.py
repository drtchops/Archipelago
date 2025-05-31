from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    DefaultOnToggle,
    NamedRange,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
    Visibility,
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

    visibility = Visibility.none
    display_name = "Campaign"
    option_tears_of_the_earth = 0
    option_new_game_plus = 1
    option_black_knight = 2
    option_monster_mode = 3
    default = 0


class Goal(Choice):
    """
    Select what requirements must be completed before you can finish your goal.
    Vanilla: Acquire the red, blue, and green gorgon eyes and defeat Medusa
    Eye Hunt: Acquire a configurable number of gorgon eyes before you can confront Medusa
    """

    display_name = "Goal"
    option_vanilla = 0
    option_eye_hunt = 1
    default = 0


class AdditionalEyesRequired(Range):
    """
    How many additional gorgon eyes are required to confront Medusa when playing Eye Hunt.
    These are on top of the red, blue, and green gorgon eyes, which are always required.
    """

    display_name = "Additional Eyes Required"
    range_start = 1
    range_end = 30
    default = 6


class ExtraEyes(Range):
    """
    How many extra gorgon eyes are added to the item pool, as a percentage of the goal amount.
    """

    display_name = "Extra Eyes"
    range_start = 0
    range_end = 100
    default = 33


class RandomizeCharacters(Choice):
    """
    Choose how the 5 characters are randomized.
    Vanilla: Start with the default 3 characters and unlock Zeek and Bram in-game as normal
    Trio: Start with the default 3 characters and receive Zeek and Bram as items
    Solo: Start with one random character and receive the rest as items
    All: Start with all 5 characters
    Random Selection: Start with a random selection of the characters and receive the rest as items
    Algus: Start with just Algus and receive the rest as items
    Arias: Start with just Arias and receive the rest as items
    Kyuli: Start with just Kyuli and receive the rest as items
    Bram: Start with just Bram and receive the rest as items
    Zeek: Start with just Zeek and receive the rest as items
    """

    display_name = "Randomize Characters"
    option_vanilla = 0
    option_trio = 1
    option_solo = 2
    option_all = 3
    option_random_selection = 4
    option_algus = 5
    option_arias = 6
    option_kyuli = 7
    option_bram = 8
    option_zeek = 9
    default = 1


class RandomizeKeyItems(DefaultOnToggle):
    """
    Choose whether to randomize key items that appear in your inventory.
    Does not include Monster Ball or Gift.
    """

    display_name = "Randomize Key Items"


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
    Choose whether to randomize all ground switches, magic crystals, and face switches in the world.
    Activating a switch will complete a check and the corresponding doors or blocks
    will toggle from a received item.
    """

    display_name = "Randomize Switches"


class RandomizeElevator(Toggle):
    """
    Choose whether to randomize the elevator destinations.
    Finding elevators will complete checks and you will unlock elevator destinations as items.
    """

    display_name = "Randomize Elevator"


class RandomizeCandles(Toggle):
    """
    Choose whether to randomize the reward gained from breaking candles.
    Breaking a candle the first time will complete a check,
    restoring and breaking it subsequent times will restore health as normal.
    """

    display_name = "Randomize Candles"


class RandomizeOrbRocks(Toggle):
    """
    Choose whether to randomize the reward gained from breaking orb rocks.
    """

    visibility = Visibility.none
    display_name = "Randomize Orb Rocks"


class RandomizeFamiliars(Toggle):
    """
    NOT YET SUPPORTED
    Choose whether to randomize familiar pickups and upgrades.
    This includes all three Old Man checks and Gil in the secret dev room.
    """

    visibility = Visibility.none
    display_name = "Randomize Familiars"


class RandomizeMinibossRewards(Toggle):
    """
    NOT YET SUPPORTED
    """

    visibility = Visibility.none
    display_name = "Randomize Miniboss Rewards"


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


class StartWithAscendantKey(Toggle):
    """
    Choose whether to start the seed with Ascendant Key already acquired.
    """

    display_name = "Start With Ascendant Key"


class StartWithBell(Toggle):
    """
    Choose whether to start the seed with Athena's Bell already acquired.
    """

    display_name = "Start With Bell"


class ApexElevator(Choice):
    """
    Choose how The Apex elevator is unlocked.
    Vanilla: available as soon as you get Ascendant Key
    Included: available when received as an item or reached normally if elevators aren't randomized
    Removed: will not be available for the whole seed
    """

    display_name = "Apex Elevator"
    option_vanilla = 0
    option_included = 1
    option_removed = 2
    default = 0


class CostMultiplier(NamedRange):
    """
    Set a multiplier for how many orbs shop purchases cost.
    """

    display_name = "Cost Multiplier"
    range_start = 0
    range_end = 200
    default = 50

    special_range_names = {  # noqa: RUF012
        "zero": 0,
        "tenth": 10,
        "quarter": 25,
        "half": 50,
        "normal": 100,
        "double": 200,
    }


class FastBloodChalice(Choice):
    """
    Choose when the Blood Chalice health regeneration rate is 5x faster.
    Off: Regen is always at the vanilla speed
    Campfires: Regen is faster when near campfires
    Not Bosses: Regen is faster when not inside a boss room
    Always: Regen is always at the faster speed
    """

    display_name = "Fast Blood Chalice"
    option_off = 0
    option_campfires = 1
    option_not_bosses = 2
    option_always = 3
    default = 1


class CampfireWarp(DefaultOnToggle):
    """
    Allows you to warp to any campfire you've previously visited.
    """

    display_name = "Campfire Warp"


class AllowBlockWarping(Toggle):
    """
    Allows Zeek to continue carrying a block when using campfire warp.
    This may allow you to get to things out of logic.
    """

    display_name = "Allow Block Warping"


class OpenEarlyDoors(DefaultOnToggle):
    """
    Opens some Gorgon Tomb doors by default when using key or switch rando to give you a bigger sphere 1.
    Has no effect when not using white key, blue key, or switch rando.
    """

    display_name = "Open Early Doors"


class CheapKyuliRay(Toggle):
    """
    Makes Kyuli's Shining Ray only cost 50 orbs.
    Recommended when using hard logic and character rando as it can activate crystals.
    """

    display_name = "Cheap Kyuli Ray"


class AlwaysRestoreCandles(Toggle):
    """
    Restores all candles on every death for free.
    """

    display_name = "Always Restore Candles"


class ScaleCharacterStats(DefaultOnToggle):
    """
    Scales character starting attack and defense based on which sphere they're found in.
    """

    display_name = "Scale Character Stats"


class TrapPercentage(NamedRange):
    """
    Set what percentage of the filler in the item pool will be replaced by trap items.
    Has no effect if no filler items need to be created.
    """

    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 10

    special_range_names = {  # noqa: RUF012
        "none": 0,
        "tenth": 10,
        "quarter": 25,
        "half": 50,
        "all": 100,
    }


class TagLink(Toggle):
    """
    Determines if the Tag Link is enabled.
    If enabled, if you have another player's character you will tag to that charater as well.
    If you don't have that character, you will randomly tag to another character.
    If you only have one character, nothing will happen.
    """

    display_name = "Tag Link"


@dataclass
class AstalonOptions(DeathLinkMixin, PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    difficulty: Difficulty
    # campaign: Campaign
    goal: Goal
    additional_eyes_required: AdditionalEyesRequired
    extra_eyes: ExtraEyes
    randomize_characters: RandomizeCharacters
    randomize_key_items: RandomizeKeyItems
    randomize_health_pickups: RandomizeHealthPickups
    randomize_attack_pickups: RandomizeAttackPickups
    randomize_white_keys: RandomizeWhiteKeys
    randomize_blue_keys: RandomizeBlueKeys
    randomize_red_keys: RandomizeRedKeys
    randomize_shop: RandomizeShop
    randomize_elevator: RandomizeElevator
    randomize_switches: RandomizeSwitches
    randomize_candles: RandomizeCandles
    # randomize_orb_rocks: RandomizeOrbRocks
    # randomize_familiars: RandomizeFamiliars
    # randomize_miniboss_rewards: RandomizeMinibossRewards
    skip_cutscenes: SkipCutscenes
    start_with_qol: StartWithQOL
    start_with_ascendant_key: StartWithAscendantKey
    start_with_bell: StartWithBell
    apex_elevator: ApexElevator
    cost_multiplier: CostMultiplier
    fast_blood_chalice: FastBloodChalice
    campfire_warp: CampfireWarp
    allow_block_warping: AllowBlockWarping
    open_early_doors: OpenEarlyDoors
    cheap_kyuli_ray: CheapKyuliRay
    always_restore_candles: AlwaysRestoreCandles
    scale_character_stats: ScaleCharacterStats
    trap_percentage: TrapPercentage
    tag_link: TagLink
