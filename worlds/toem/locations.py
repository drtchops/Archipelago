from dataclasses import dataclass
from enum import Enum
from itertools import groupby
from typing import Dict, Set

from BaseClasses import Location

from .constants import BASE_ID, GAME_NAME, Area
from .regions import RegionName


class LocationGroup(str, Enum):
    QUEST = "Quest"
    COMPENDIUM = "Compendium"
    ITEM = "Item"
    ACHIEVEMENT = "Achievement"


class LocationName(str, Enum):
    # Homelanda
    QUEST_PHOTO_OF_NANA = "Quest - Take a photo of Nana!"
    QUEST_HIDDEN_GIFT = "Quest - A hidden gift"
    QUEST_EXPERIENCE_TOEM = "Quest - Experience TOEM"

    COMP_COW = "Compendium - Cow"
    COMP_FLIES = "Compendium - Flies"
    COMP_HOME_BIRD = "Compendium - Home bird"
    COMP_TATO = "Compendium - Tato"

    ITEM_BACKPACK = "Item - Backpack"
    ITEM_CASSETTE_PLAYER = "Item - Cassette Player"
    ITEM_ALBUM = "Item - Album"
    ITEM_CAMERA = "Item - Camera"
    ITEM_CLOGS = "Item - Clogs"

    TAPE_PHOTO_OF_HOME = "Casette - Jamal Green - Photo of Home"

    CHEEVO_BEGINNING = "Achievement - The beginning"
    CHEEVO_HOME_SWEET_HOME = "Achievement - Home sweet home"

    # Oaklaville
    QUEST_SUS_FOREST = "Quest - Suspicious activity - forest"
    QUEST_MONSTERS = "Quest - Monster spotting"
    QUEST_SOCKS = "Quest - Missing socks"
    QUEST_SCOUTS = "Quest - Become a scout"
    QUEST_HIDE_AND_SEEK = "Quest - Hide-and-seek"
    QUEST_LOG_JAM = "Quest - Log blocking a path"
    QUEST_CHALLENGE_1 = "Quest - Photo challenge #1"
    QUEST_CHALLENGE_2 = "Quest - Photo challenge #2"
    QUEST_PAPARAZZI = "Quest - Become a paparazzi"
    QUEST_CAPTURE_HOTEL = "Quest - Capture the hotel's beauty"
    QUEST_HOTEL_CHEF = "Quest - Hotel chef"
    QUEST_STALLION = "Quest - A courageous stallion"
    QUEST_GHOST_HELPER = "Quest - Ghost helper!"
    QUEST_CUP_CHAMP = "Quest - Cup champion"
    QUEST_FLOWER = "Quest - Become a flower"

    COMP_ANT = "Compendium - Ant"
    COMP_BEEHIVE = "Compendium - Beehive"
    COMP_BUTTERFLY = "Compendium - Butterfly"
    COMP_OSKAR = "Compendium - Oskar"
    COMP_SERO = "Compendium - Sero"
    COMP_FOREST_BIRD = "Compendium - Forest bird"
    COMP_LADYBUG = "Compendium - Ladybug"
    COMP_TOM = "Compendium - Tom"
    COMP_NESTWORM = "Compendium - Nestworm"
    COMP_PET_ROCK = "Compendium - Pet rock"
    COMP_SNAIL = "Compendium - Snail"
    COMP_SQUIRREL = "Compendium - Squirrel"
    COMP_STAG_BEETLE = "Compendium - Stag beetle"
    COMP_TATO_BUG = "Compendium - Tato bug"
    COMP_TATO_FLY = "Compendium - Tato fly"

    ITEM_FINGER = "Item - Foam finger"
    ITEM_TRIPOD = "Item - Tripod"
    ITEM_COWBOY_HAT = "Item - Cowboy hat"
    ITEM_LOST_SOCK = "Item - Lost sock"
    ITEM_FJALLBJORN_HAT = "Item - Fjällbjörn hat"
    ITEM_GHOST_GLASSES = "Item - Ghost glasses"
    ITEM_SOAKED_SOCK = "Item - Soaked sock"
    ITEM_MONSTER_MASK = "Item - Monster mask"

    TAPE_SQUIRREL_PHOTO = "Launchable Socks - Squirrel Photography"

    CHEEVO_CALM_FOREST = "Achievement - The calm forest"
    CHEEVO_MAJESTIC_HOTEL = "Achievement - A majestic hotel"
    CHEEVO_SLOW_AND_STEADY = "Achievement - Slow and steady"
    CHEEVO_NATURE_SHOWSTOPPER = "Achievement - Nature's show-stopper"
    CHEEVO_STRONG_AS_AN_OAK = "Achievement - Strong as an oak"
    CHEEVO_CALMED_DOWN = "Achievement - Calmed down"
    CHEEVO_JUST_A_SOCK = "Achievement - Just a sock"
    CHEEVO_YOU_FOUND_US = "Achievement - You found us!"

    # Stanhamn
    QUEST_KING_FISH = "Quest - The king of fishes"
    QUEST_GOOD_SPOT = "Quest - A good spot with no sun"
    QUEST_SUS_HARBOR = "Quest - Suspicious activity - harbor"
    QUEST_PAPER_HATS = "Quest - Queen of paper hats"
    QUEST_CHALLENGE_3 = "Quest - Photo challenge #3"
    QUEST_CHALLENGE_4 = "Quest - Photo challenge #4"
    QUEST_FRAMES_FILTERS = "Quest - Frames & filters!"
    QUEST_TAKE_A_BATH = "Quest - Make someone take a bath"
    QUEST_LOST_DOG = "Quest - A lost dog"
    QUEST_POWER = "Quest - Power shortage?!"
    QUEST_CHAOS = "Quest - Solve the chaos"
    QUEST_FLAME = "Quest - Scorching flame?"
    QUEST_SANDWICH = "Quest - Supreme deluxe sandwich?!"
    QUEST_GARBAGE = "Quest - Ocean garbage"
    QUEST_WHISTLING = "Quest - A whistling dilemma"
    QUEST_MELODY = "Quest - A layered melody"

    COMP_BUBBLE_FLY = "Compendium - Bubble fly"
    COMP_FIA = "Compendium - Fia"
    COMP_FRAS = "Compendium - Fräs"
    COMP_WILLEMIJN = "Compendium - Willemijn"
    COMP_CRAB = "Compendium - Crab"
    COMP_DRAGONFLY = "Compendium - Dragonfly"
    COMP_HAPPY_CARP = "Compendium - Happy carp"
    COMP_JELLYFISH = "Compendium - Jellyfish"
    COMP_KING_FISH = "Compendium - King fish"
    COMP_SEAGULL = "Compendium - Seagull"
    COMP_SEAHORSE = "Compendium - Seahorse"
    COMP_SUNDAY_SWAN = "Compendium - Sunday swan"
    COMP_TATO_SCUBA = "Compendium - Tato scuba"
    COMP_TATO_SWIM = "Compendium - Tato swim"
    COMP_TOAD = "Compendium - Toad"

    ITEM_FRAMES_FILTERS = "Item - Frames & filters"
    ITEM_FISHING_HAT = "Item - Fishing hat"
    ITEM_HONK_ATTACHMENT = "Item - Honk attachment"
    ITEM_UMBRELLA = "Item - Umbrella"
    ITEM_OLD_KEY = "Item - Old key"
    ITEM_HARD_HAT = "Item - Hard hat"
    ITEM_DIVING_HELMET = "Item - Diving helmet"
    ITEM_RUBBER_BOOTS = "Item - Rubber boots"
    ITEM_FISHERMAN_WHISTLE = "Item - Fisherman's whisle"
    ITEM_SANDWICH = "Item - Supreme deluxe sandwich"
    ITEM_PIRATE_HAT = "Item - Pirate hat"
    ITEM_PAPER_HAT = "Item - Paper hat"
    ITEM_FLAG = "Item - Photo challenger flag"

    CHEEVO_SET_SAIL = "Achievement - Set sail for good weather"
    CHEEVO_VOYAGE_UNDERWATER = "Achievement - A voyage underwater"
    CHEEVO_EMPLOYEE_OF_THE_MONTH = "Achievement - Employee of the month"
    CHEEVO_CALM_AS_SEA = "Achievement - Calm as the sea"
    CHEEVO_SEAWORTHY = "Achievement - Seaworthy"
    CHEEVO_FLIGHT_READY = "Achievement - Flight ready"
    CHEEVO_SPARKLING_JUMP = "Achievement - A sparkling jump"
    CHEEVO_GOOD_BOY = "Achievement - Who's a good boy?!"

    # Logcity
    QUEST_SUS_CITY = "Quest - Suspicious activity - city"
    QUEST_RATSKULLZ = "Quest - Ratskullz crew"
    QUEST_PUNK_ROCKER = "Quest - Punk rocker bread crumbs"
    QUEST_CHALLENGE_5 = "Quest - Photo challenge #5"
    QUEST_CHALLENGE_6 = "Quest - Photo challenge #6"
    QUEST_NEWS = "Quest - Press-ing news"
    QUEST_SEWER = "Quest - Sewer stumble!"
    QUEST_HOTBEAN = "Quest - Super Hotbean Bros."
    QUEST_HANG_IN_THERE = "Quest - Hang in there, buddy"
    QUEST_SCARY_CITY = "Quest - Spooky scary city"
    QUEST_DATE = "Quest - A ghostly date"
    QUEST_ART = "Quest - Art exhibition"
    QUEST_INFLUENCER = "Quest - Young and inspiring!"
    QUEST_FASHION = "Quest - A design problem"
    QUEST_CLEANING = "Quest - Cleaning away the stress"
    QUEST_GRANNY = "Quest - Always tumbled granny"
    QUEST_MICE = "Quest - A mouse bakery"
    QUEST_CROW = "Quest - A thieving crow"

    COMP_BUSINESS_PIGEON = "Compendium - Business pigeon"
    COMP_PORTILLO = "Compendium - Portillo"
    COMP_MOUSE = "Compendium - Mouse"
    COMP_PIGEON = "Compendium - Pigeon"
    COMP_PUNK_PARROT = "Compendium - Punky parrot"
    COMP_TATO_SKATEBOARD = "Compendium - Tato skateboard"
    COMP_TATO_TOURIST = "Compendium - Tato tourist"
    COMP_TURTLE = "Compendium - Turtle"

    ITEM_HOTBEAN_HAT = "Item - Hotbean hat"
    ITEM_REPORTER_HAT = "Item - Reporter hat"
    ITEM_MUDDY_CAMERA = "Item - Muddy camera"
    ITEM_SNEAKERS = "Item - Sneakers"
    ITEM_CINNAMON_BUN = "Item - Cinnamon bun"
    ITEM_FRISBEE = "Item - Frisbee"

    CHEEVO_BIG_CITY = "Achievement - The big city"
    CHEEVO_CLOCKTOWER = "Achievement - The grand clock tower"
    CHEEVO_PROFESSIONAL = "Achievement - City professional"
    CHEEVO_BUSINESS = "Achievement - Business executed"
    CHEEVO_FOLLOWERS = "Achievement - 100 followers!"
    CHEEVO_NEW_JOB = "Achievement - A new job"

    # Kiiruberg
    QUEST_YETI_CUTE = "Quest - Yeti cuteness"
    QUEST_ICE_WIZARD = "Quest - Ice wizard's research"
    QUEST_MILITARY_SUS = "Quest - Military suspicions"
    QUEST_ASTRONAUT = "Quest - Play astronaut"
    QUEST_CHALLENGE_7 = "Quest - Photo challenge #7"
    QUEST_CHALLENGE_8 = "Quest - Photo challenge #8"
    QUEST_ASTEROID = "Quest - Locating an asteroid"
    QUEST_GOAT_CHOIR = "Quest - Listen to the goat choir"
    QUEST_SNOWBALL = "Quest - Snowball memories"
    QUEST_BIRTHDAY = "Quest - Birthday in distress"
    QUEST_PAINTINGS = "Quest - Ancient paintings"
    QUEST_BECOME_YETI = "Quest - Become a yeti"
    QUEST_SNOWMAN = "Quest - Assemble a snowman"

    COMP_MIKEE = "Compendium - Mikée"
    COMP_NARIKO = "Compendium - Nariko"
    COMP_COSMO_DEER = "Compendium - Cosmo deer"
    COMP_TEDDY = "Compendium - Teddy"
    COMP_FLUFF = "Compendium - Fluff ball"
    COMP_HEDGEHOG = "Compendium - Hedgehog"
    COMP_METEOPAL = "Compendium - Meteopal"
    COMP_GOAT = "Compendium - Mountain goat"
    COMP_OWL = "Compendium - Owl"
    COMP_SNOW_BIRD = "Compendium - Snow bird"
    COMP_TATO_ALIEN = "Compendium - Tato alien"
    COMP_TATO_SKI = "Compendium - Tato ski"

    ITEM_CLIMBING_BOOTS = "Item - Climbing boots"
    ITEM_PUFFER_HAT = "Item - Puffer hat"
    ITEM_SCARF = "Item - Scarf"
    ITEM_SKI_GOGGLES = "Item - Ski goggles"
    ITEM_SPACE_HELMET = "Item - Space helmet"

    CHEEVO_SNOWY_PEAKS = "Achievement - Snowy peaks"
    CHEEVO_GEARED_UP = "Achievement - All geared up"
    CHEEVO_HURDLE = "Achievement - The biggest hurdle"
    CHEEVO_FIGHTER = "Achievement - Ice fighter"
    CHEEVO_YOUTH = "Achievement - Happy youth"
    CHEEVO_STORY = "Achievement - A great story"

    # Mountain Top
    CHEEVO_CLOSE = "Achievement - So close now!"
    CHEEVO_TOEM = "Achievement - Experience TOEM"

    # Overall
    CHEEVO_CUTIES = "Achievement - Look at those cuties"
    CHEEVO_COLLECT_EM_ALL = "Achievement - Collect them all"
    CHEEVO_GOING_LONG = "Achievement - Going long!"
    CHEEVO_COSPLAYER = "Achievement - Cosplayer"
    CHEEVO_COMPLETIONIST = "Achievement - A true completionist"

    # Basto
    QUEST_BALLOONS = "Quest - Basto's hidden balloons"
    QUEST_ARTHUR = "Quest - Arthur hunter"
    QUEST_BAD_HAIR_DAY = "Quest - Bad hair day"
    QUEST_TAKE_A_NAP = "Quest - Take a nap!"
    QUEST_SPOOKY_STORIES = "Quest - Spooky stories"
    QUEST_PORTRAITS = "Quest - Painterly portrait"
    QUEST_CINEMA = "Quest - Night-time cinema"
    QUEST_NIGHT_LIGHTS = "Quest - Night lights"
    QUEST_JET_SKI = "Quest - Jet-ski tricks"
    QUEST_FRUITS = "Quest - Fruit shortage"
    QUEST_BRAIN_FREEZE = "Quest - Brain freeze"
    QUEST_SWEET_TOOTH = "Quest - Sweet tooth"
    QUEST_IN_YOUR_FACE = "Quest - In your face"
    QUEST_BROKEN_DREAMS = "Quest - Broken dreams"
    QUEST_DRY_SEASON = "Quest - Dry season"
    QUEST_MUSCLES = "Quest - Dehydrated muscles"
    QUEST_SAND_CASTLE = "Quest - Sand castle competition"
    QUEST_CARNIVAL = "Quest - Play a carnival game"
    QUEST_BATS = "Quest - Book of bats"
    QUEST_BITLING = "Quest - Bitling collector"

    COMP_BAT = "Compendium - Bat"
    COMP_SNAKE = "Compendium - Beach snake"
    COMP_BEAK_BIRD = "Compendium - Beak bird"
    COMP_BITLING_FROG = "Compendium - Bitling frog"
    COMP_BITLING_MOUSE = "Compendium - Bitling mouse"
    COMP_BITLING_SNAIL = "Compendium - Bitling snail"
    COMP_BITLING_TATO = "Compendium - Bitling tato"
    COMP_COCO_CRAB = "Compendium - Coco crab"
    COMP_DAY_LIZARD = "Compendium - Day lizard"
    COMP_DRILL_MOLE = "Compendium - Drill mole"
    COMP_EGGERT = "Compendium - Eggert"
    COMP_FIRE_FLY = "Compendium - Fire fly"
    COMP_GLOW_WORM = "Compendium - Glow worm"
    COMP_ITSY_BITSY = "Compendium - Itsy bitsy"
    COMP_MUD_FROG = "Compendium - Mud frog"
    COMP_NIGHT_LIZARD = "Compendium - Night lizard"
    COMP_SNOUT_BUG = "Compendium - Snout bug"
    COMP_TATO_COCO = "Compendium - Tato coco"
    COMP_TATO_KING = "Compendium - Tato king"
    COMP_WATER_STRIDER = "Compendium - Water strider"

    ITEM_WATERGUN = "Item - Water popper attachment"
    ITEM_SUN_HAT = "Item - Sun hat"
    ITEM_MELONEAR = "Item - Melonear"
    ITEM_BANAKIN = "Item - Banakin"
    ITEM_ORANGANAS = "Item - Oranganas"
    ITEM_BEANUT = "Item - Beanut"
    ITEM_PICKAXE = "Item - Pickaxe"
    ITEM_SUN_CAP = "Item - Sun cap"
    ITEM_FLIP_FLOPS = "Item - Flip-flops"
    ITEM_ICE_CREAM = "Item - Ice cream"
    ITEM_ROYAL_CAPE = "Item - Royal cape"
    ITEM_MINIGAME_TICKET = "Item - minigame ticket"
    ITEM_LEI = "Item - Lei"
    ITEM_VACATION_SHIRT = "Item - Vacation shirt"
    ITEM_ROYAL_CANE = "Item - Royal cane"
    ITEM_EMPTY_BOTTLE = "Item - Empty bottle"
    ITEM_WATER_BOTTLE = "Item - Water bottle"
    ITEM_VIKING_HELMET = "Item - Viking helmet"
    ITEM_FOOT_CAST = "Item - Foot cast"
    ITEM_BERET = "Item - Beret"


class ToemLocation(Location):
    game = GAME_NAME


@dataclass(frozen=True)
class LocationData:
    region: RegionName
    group: LocationGroup
    area: Area


location_table: Dict[str, LocationData] = {
    LocationName.QUEST_PHOTO_OF_NANA.value: LocationData(RegionName.HOMELANDA, LocationGroup.QUEST, Area.HOMELANDA),
    LocationName.QUEST_HIDDEN_GIFT.value: LocationData(RegionName.HOMELANDA, LocationGroup.QUEST, Area.HOMELANDA),
    LocationName.QUEST_EXPERIENCE_TOEM.value: LocationData(RegionName.HOMELANDA, LocationGroup.QUEST, Area.HOMELANDA),
    LocationName.COMP_COW.value: LocationData(RegionName.HOMELANDA, LocationGroup.COMPENDIUM, Area.HOMELANDA),
    LocationName.COMP_FLIES.value: LocationData(RegionName.HOMELANDA, LocationGroup.COMPENDIUM, Area.HOMELANDA),
    LocationName.COMP_HOME_BIRD.value: LocationData(RegionName.HOMELANDA, LocationGroup.COMPENDIUM, Area.HOMELANDA),
    LocationName.COMP_TATO.value: LocationData(RegionName.HOMELANDA, LocationGroup.COMPENDIUM, Area.HOMELANDA),
    LocationName.ITEM_BACKPACK.value: LocationData(RegionName.HOMELANDA, LocationGroup.ITEM, Area.HOMELANDA),
    LocationName.ITEM_CAMERA.value: LocationData(RegionName.HOMELANDA, LocationGroup.ITEM, Area.HOMELANDA),
    LocationName.ITEM_CLOGS.value: LocationData(RegionName.HOMELANDA, LocationGroup.ITEM, Area.HOMELANDA),
    LocationName.CHEEVO_BEGINNING.value: LocationData(RegionName.HOMELANDA, LocationGroup.ACHIEVEMENT, Area.HOMELANDA),
    LocationName.CHEEVO_HOME_SWEET_HOME.value: LocationData(
        RegionName.HOMELANDA, LocationGroup.ACHIEVEMENT, Area.HOMELANDA
    ),
    LocationName.QUEST_SUS_FOREST.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_MONSTERS.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_SOCKS.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_SCOUTS.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_HIDE_AND_SEEK.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_LOG_JAM.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_CHALLENGE_1.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_CHALLENGE_2.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_PAPARAZZI.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_CAPTURE_HOTEL.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_HOTEL_CHEF.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_STALLION.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_GHOST_HELPER.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_CUP_CHAMP.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.QUEST_FLOWER.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.QUEST, Area.OAKLAVILLE),
    LocationName.COMP_ANT.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_BEEHIVE.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_BUTTERFLY.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_OSKAR.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_SERO.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_FOREST_BIRD.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_LADYBUG.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_TOM.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_NESTWORM.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_PET_ROCK.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_SNAIL.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_SQUIRREL.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_STAG_BEETLE.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_TATO_BUG.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.COMP_TATO_FLY.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.COMPENDIUM, Area.OAKLAVILLE),
    LocationName.ITEM_FINGER.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_TRIPOD.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_COWBOY_HAT.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_LOST_SOCK.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_FJALLBJORN_HAT.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_GHOST_GLASSES.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_SOAKED_SOCK.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.ITEM_MONSTER_MASK.value: LocationData(RegionName.OAKLAVILLE, LocationGroup.ITEM, Area.OAKLAVILLE),
    LocationName.CHEEVO_CALM_FOREST.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_MAJESTIC_HOTEL.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_SLOW_AND_STEADY.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_NATURE_SHOWSTOPPER.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_STRONG_AS_AN_OAK.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_CALMED_DOWN.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_JUST_A_SOCK.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.CHEEVO_YOU_FOUND_US.value: LocationData(
        RegionName.OAKLAVILLE, LocationGroup.ACHIEVEMENT, Area.OAKLAVILLE
    ),
    LocationName.QUEST_KING_FISH.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_GOOD_SPOT.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_SUS_HARBOR.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_PAPER_HATS.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_CHALLENGE_3.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_CHALLENGE_4.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_FRAMES_FILTERS.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_TAKE_A_BATH.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_LOST_DOG.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_POWER.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_CHAOS.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_FLAME.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_SANDWICH.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_GARBAGE.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_WHISTLING.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.QUEST_MELODY.value: LocationData(RegionName.STANHAMN, LocationGroup.QUEST, Area.STANHAMN),
    LocationName.COMP_BUBBLE_FLY.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_FIA.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_FRAS.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_WILLEMIJN.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_CRAB.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_DRAGONFLY.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_HAPPY_CARP.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_JELLYFISH.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_KING_FISH.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_SEAGULL.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_SEAHORSE.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_SUNDAY_SWAN.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_TATO_SCUBA.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_TATO_SWIM.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.COMP_TOAD.value: LocationData(RegionName.STANHAMN, LocationGroup.COMPENDIUM, Area.STANHAMN),
    LocationName.ITEM_FRAMES_FILTERS.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_FISHING_HAT.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_HONK_ATTACHMENT.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_UMBRELLA.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_OLD_KEY.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_HARD_HAT.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_DIVING_HELMET.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_RUBBER_BOOTS.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_FISHERMAN_WHISTLE.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_SANDWICH.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_PIRATE_HAT.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_PAPER_HAT.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.ITEM_FLAG.value: LocationData(RegionName.STANHAMN, LocationGroup.ITEM, Area.STANHAMN),
    LocationName.CHEEVO_SET_SAIL.value: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN),
    LocationName.CHEEVO_VOYAGE_UNDERWATER.value: LocationData(
        RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN
    ),
    LocationName.CHEEVO_EMPLOYEE_OF_THE_MONTH.value: LocationData(
        RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN
    ),
    LocationName.CHEEVO_CALM_AS_SEA.value: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN),
    LocationName.CHEEVO_SEAWORTHY.value: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN),
    LocationName.CHEEVO_FLIGHT_READY.value: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN),
    LocationName.CHEEVO_SPARKLING_JUMP.value: LocationData(
        RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN
    ),
    LocationName.CHEEVO_GOOD_BOY.value: LocationData(RegionName.STANHAMN, LocationGroup.ACHIEVEMENT, Area.STANHAMN),
    LocationName.QUEST_SUS_CITY.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_RATSKULLZ.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_PUNK_ROCKER.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_CHALLENGE_5.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_CHALLENGE_6.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_NEWS.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_SEWER.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_HOTBEAN.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_HANG_IN_THERE.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_SCARY_CITY.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_DATE.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_ART.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_INFLUENCER.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_FASHION.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_CLEANING.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_GRANNY.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_MICE.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.QUEST_CROW.value: LocationData(RegionName.LOGCITY, LocationGroup.QUEST, Area.LOGCITY),
    LocationName.COMP_BUSINESS_PIGEON.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_PORTILLO.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_MOUSE.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_PIGEON.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_PUNK_PARROT.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_TATO_SKATEBOARD.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_TATO_TOURIST.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.COMP_TURTLE.value: LocationData(RegionName.LOGCITY, LocationGroup.COMPENDIUM, Area.LOGCITY),
    LocationName.ITEM_HOTBEAN_HAT.value: LocationData(RegionName.LOGCITY, LocationGroup.ITEM, Area.LOGCITY),
    LocationName.ITEM_REPORTER_HAT.value: LocationData(RegionName.LOGCITY, LocationGroup.ITEM, Area.LOGCITY),
    LocationName.ITEM_MUDDY_CAMERA.value: LocationData(RegionName.LOGCITY, LocationGroup.ITEM, Area.LOGCITY),
    LocationName.ITEM_SNEAKERS.value: LocationData(RegionName.LOGCITY, LocationGroup.ITEM, Area.LOGCITY),
    LocationName.ITEM_CINNAMON_BUN.value: LocationData(RegionName.LOGCITY, LocationGroup.ITEM, Area.LOGCITY),
    LocationName.ITEM_FRISBEE.value: LocationData(RegionName.LOGCITY, LocationGroup.ITEM, Area.LOGCITY),
    LocationName.CHEEVO_BIG_CITY.value: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT, Area.LOGCITY),
    LocationName.CHEEVO_CLOCKTOWER.value: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT, Area.LOGCITY),
    LocationName.CHEEVO_PROFESSIONAL.value: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT, Area.LOGCITY),
    LocationName.CHEEVO_BUSINESS.value: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT, Area.LOGCITY),
    LocationName.CHEEVO_FOLLOWERS.value: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT, Area.LOGCITY),
    LocationName.CHEEVO_NEW_JOB.value: LocationData(RegionName.LOGCITY, LocationGroup.ACHIEVEMENT, Area.LOGCITY),
    LocationName.QUEST_YETI_CUTE.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_ICE_WIZARD.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_MILITARY_SUS.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_ASTRONAUT.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_CHALLENGE_7.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_CHALLENGE_8.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_ASTEROID.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_GOAT_CHOIR.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_SNOWBALL.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_BIRTHDAY.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_PAINTINGS.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_BECOME_YETI.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.QUEST_SNOWMAN.value: LocationData(RegionName.KIIRUBERG, LocationGroup.QUEST, Area.KIIRUBERG),
    LocationName.COMP_MIKEE.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_NARIKO.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_COSMO_DEER.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_TEDDY.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_FLUFF.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_HEDGEHOG.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_METEOPAL.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_GOAT.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_OWL.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_SNOW_BIRD.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_TATO_ALIEN.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.COMP_TATO_SKI.value: LocationData(RegionName.KIIRUBERG, LocationGroup.COMPENDIUM, Area.KIIRUBERG),
    LocationName.ITEM_CLIMBING_BOOTS.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ITEM, Area.KIIRUBERG),
    LocationName.ITEM_PUFFER_HAT.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ITEM, Area.KIIRUBERG),
    LocationName.ITEM_SCARF.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ITEM, Area.KIIRUBERG),
    LocationName.ITEM_SKI_GOGGLES.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ITEM, Area.KIIRUBERG),
    LocationName.ITEM_SPACE_HELMET.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ITEM, Area.KIIRUBERG),
    LocationName.CHEEVO_SNOWY_PEAKS.value: LocationData(
        RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT, Area.KIIRUBERG
    ),
    LocationName.CHEEVO_GEARED_UP.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT, Area.KIIRUBERG),
    LocationName.CHEEVO_HURDLE.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT, Area.KIIRUBERG),
    LocationName.CHEEVO_FIGHTER.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT, Area.KIIRUBERG),
    LocationName.CHEEVO_YOUTH.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT, Area.KIIRUBERG),
    LocationName.CHEEVO_STORY.value: LocationData(RegionName.KIIRUBERG, LocationGroup.ACHIEVEMENT, Area.KIIRUBERG),
    LocationName.CHEEVO_CLOSE.value: LocationData(
        RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP
    ),
    LocationName.CHEEVO_TOEM.value: LocationData(RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP),
    LocationName.CHEEVO_CUTIES.value: LocationData(
        RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP
    ),
    LocationName.CHEEVO_COLLECT_EM_ALL.value: LocationData(
        RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP
    ),
    LocationName.CHEEVO_GOING_LONG.value: LocationData(
        RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP
    ),
    LocationName.CHEEVO_COSPLAYER.value: LocationData(
        RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP
    ),
    LocationName.CHEEVO_COMPLETIONIST.value: LocationData(
        RegionName.MOUNTAIN_TOP, LocationGroup.ACHIEVEMENT, Area.MOUNTAIN_TOP
    ),
    LocationName.QUEST_BALLOONS.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_ARTHUR.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_BAD_HAIR_DAY.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_TAKE_A_NAP.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_SPOOKY_STORIES.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_PORTRAITS.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_CINEMA.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_NIGHT_LIGHTS.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_JET_SKI.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_FRUITS.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_BRAIN_FREEZE.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_SWEET_TOOTH.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_IN_YOUR_FACE.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_BROKEN_DREAMS.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_DRY_SEASON.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_MUSCLES.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_SAND_CASTLE.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_CARNIVAL.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_BATS.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.QUEST_BITLING.value: LocationData(RegionName.BASTO, LocationGroup.QUEST, Area.BASTO),
    LocationName.COMP_BAT.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_SNAKE.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_BEAK_BIRD.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_BITLING_FROG.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_BITLING_MOUSE.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_BITLING_SNAIL.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_BITLING_TATO.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_COCO_CRAB.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_DAY_LIZARD.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_DRILL_MOLE.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_EGGERT.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_FIRE_FLY.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_GLOW_WORM.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_ITSY_BITSY.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_MUD_FROG.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_NIGHT_LIZARD.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_SNOUT_BUG.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_TATO_COCO.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_TATO_KING.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.COMP_WATER_STRIDER.value: LocationData(RegionName.BASTO, LocationGroup.COMPENDIUM, Area.BASTO),
    LocationName.ITEM_WATERGUN.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_SUN_HAT.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_MELONEAR.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_BANAKIN.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_ORANGANAS.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_BEANUT.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_PICKAXE.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_SUN_CAP.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_FLIP_FLOPS.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_ICE_CREAM.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_ROYAL_CAPE.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_MINIGAME_TICKET.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_LEI.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_VACATION_SHIRT.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_ROYAL_CANE.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_EMPTY_BOTTLE.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_WATER_BOTTLE.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_VIKING_HELMET.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_FOOT_CAST.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
    LocationName.ITEM_BERET.value: LocationData(RegionName.BASTO, LocationGroup.ITEM, Area.BASTO),
}


location_name_to_id: Dict[str, int] = {name: i for i, name in enumerate(location_table, start=BASE_ID)}


def get_location_group(location_name: str) -> LocationGroup:
    return location_table[location_name].group


def get_location_area(location_name: str) -> Area:
    return location_table[location_name].area


location_name_groups: Dict[str, Set[str]] = {
    group.value: set(location for location in location_names)
    for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group)
}
location_name_groups.update(
    {
        group.value: set(location for location in location_names)
        for group, location_names in groupby(sorted(location_table, key=get_location_area), get_location_area)
    }
)
