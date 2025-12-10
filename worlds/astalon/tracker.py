from functools import cached_property
from typing import Any, ClassVar, Final

from typing_extensions import override

from BaseClasses import CollectionState, Entrance, Location, Region
from NetUtils import JSONMessagePart
from Options import Option
from rule_builder import Macro, Rule
from Utils import get_intended_text  # pyright: ignore[reportUnknownVariableType]
from worlds.generic.Rules import CollectionRule

from .bases import AstalonWorldBase
from .items import Character, Events
from .logic.custom_rules import CampfireWarp
from .regions import RegionName


def map_page_index(data: Any) -> int:
    """Converts the area id provided by the game mod to a map index."""
    if not isinstance(data, int):
        return 0
    if data in (1, 99):
        # tomb
        return 1
    if data in (2, 3, 7):
        # mechanism_and_hall
        return 2
    if data in (4, 19, 21):
        # catacombs
        return 3
    if data in (5, 6, 8, 13):
        # ruins
        return 4
    if data == 11:
        # cyclops
        return 5
    # world map
    return 0


CHARACTER_ICONS: Final[dict[int, str]] = {
    1: "algus",
    2: "arias",
    3: "kyuli",
    4: "bram",
    5: "zeek",
}

MAP_OFFSETS: Final[tuple[tuple[int, int], ...]] = (
    (-1800, 17180),  # world map
    (-4152, 25130),  # gt
    (-1560, 21080),  # mech and hotp
    (-5448 + 876, 26840),  # catacombs
    (-2424, 17000),  # ruins
    (-9336, 20840),  # cyclops
)
ROOM_WIDTH: Final[int] = 432
ROOM_HEIGHT: Final[int] = 240
MAP_SCALE_X: Final[float] = ROOM_WIDTH / 59.346
MAP_SCALE_Y: Final[float] = -ROOM_HEIGHT / 40.475

CAMPFIRE_WARPS: Final[dict[int, RegionName]] = {
    6696: RegionName.GT_ENTRANCE,
    18: RegionName.GT_BOTTOM,
    292: RegionName.GT_LEFT,
    293: RegionName.GT_BOSS,
    1140: RegionName.MECH_START,
    1556: RegionName.MECH_SWORD_CONNECTION,
    813: RegionName.MECH_BOTTOM_CAMPFIRE,
    712: RegionName.MECH_BK,
    3547: RegionName.MECH_RIGHT,
    1634: RegionName.MECH_TOP,
    819: RegionName.MECH_BOSS,
    7507: RegionName.CD_START,
    7577: RegionName.CD_MIDDLE,
    7703: RegionName.CD_CAMPFIRE_3,
    7774: RegionName.CD_TOP,
    5019: RegionName.HOTP_EPIMETHEUS,
    6421: RegionName.HOTP_BELL_CAMPFIRE,
    3207: RegionName.HOTP_CLAW_CAMPFIRE,
    2904: RegionName.HOTP_BOSS_CAMPFIRE,
    10203: RegionName.CATH_CAMPFIRE_1,
    10260: RegionName.CATH_CAMPFIRE_2,
    3726: RegionName.ROA_START,
    7088: RegionName.ROA_LEFT_ASCENT,
    7086: RegionName.ROA_MIDDLE,
    4685: RegionName.ROA_ELEVATOR,
    10026: RegionName.ROA_BOSS,
    7436: RegionName.SP_CAMPFIRE_1,
    8243: RegionName.SP_CAMPFIRE_2,
    4635: RegionName.APEX,
    7109: RegionName.CAVES_LOWER,
    2524: RegionName.CATA_BOW_CAMPFIRE,
    2610: RegionName.CATA_ROOTS_CAMPFIRE,
    2669: RegionName.CATA_BOSS,
    9056: RegionName.TR_START,
    9161: RegionName.CATA_DEV_ROOM,
}


def location_icon_coords(index: int | None, coords: dict[str, Any]) -> tuple[int, int, str] | None:
    """Converts player coordinates provided by the game mod into image coordinates for the map page."""
    if index is None or not coords:
        return None

    dx, dy = MAP_OFFSETS[index]
    x = int((coords.get("X", 0) + (ROOM_WIDTH / 2) + dx) / MAP_SCALE_X)
    y = int((coords.get("Y", 0) - (ROOM_HEIGHT / 2) + dy) / MAP_SCALE_Y)
    icon = CHARACTER_ICONS.get(coords.get("Character", 1), "algus")
    return x, y, f"images/icons/{icon}.png"


def rule_to_json(rule: CollectionRule | None, state: CollectionState) -> list[JSONMessagePart]:
    if isinstance(rule, Rule.Resolved):
        return [
            {"type": "text", "text": "    "},
            *rule.explain_json(state),
        ]
    return [
        {"type": "text", "text": "    "},
        {"type": "color", "color": "green", "text": "True"},
    ]


class AstalonUTWorld(AstalonWorldBase):
    tracker_world: ClassVar[dict[str, Any]] = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": "locations/locations.json",
        "map_page_setting_key": "{player}_{team}_astalon_area",
        "map_page_index": map_page_index,
        "location_setting_key": "{player}_{team}_astalon_coords",
        "location_icon_coords": location_icon_coords,
    }
    ut_can_gen_without_yaml: ClassVar = True
    glitches_item_name: ClassVar = Events.FAKE_OOL_ITEM.value
    found_entrances_datastorage_key: ClassVar = "Slot:{player}:campfires"

    @cached_property
    def is_ut(self) -> bool:
        return getattr(self.multiworld, "generation_is_fake", False)

    @override
    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data.get("options", {})
            for key, value in slot_options.items():
                opt: Option[Any] | None = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

            if "starting_characters" in slot_data:
                self.starting_characters = [Character(c) for c in slot_data["starting_characters"]]
            if "extra_gold_eyes" in slot_data:
                self.extra_gold_eyes = slot_data["extra_gold_eyes"]

    def get_logical_path(self, dest_name: str, state: CollectionState) -> list[JSONMessagePart]:
        if not dest_name:
            return [{"type": "text", "text": "Provide a location or region to route to using /route [name]"}]

        goal_location: Location | None = None
        goal_region: Region | None = None
        region_name = ""
        location_name, usable, response = get_intended_text(dest_name, [loc.name for loc in self.get_locations()])
        if usable:
            try:
                goal_location = self.get_location(location_name)
            except KeyError:
                return [{"type": "text", "text": f"Location {location_name} not found in this multiworld"}]
            goal_region = goal_location.parent_region
            if not goal_region:
                return [{"type": "text", "text": f"Location {location_name} has no parent region"}]
        else:
            region_name, usable, _ = get_intended_text(
                dest_name,
                [reg.name for reg in self.get_regions()],
            )
            if usable:
                goal_region = self.get_region(region_name)
            else:
                return [{"type": "text", "text": response}]

        if goal_location and not goal_location.can_reach(state):
            return [{"type": "text", "text": f"Location {goal_location.name} cannot be reached"}]
        if goal_region and goal_region not in state.path:
            return [{"type": "text", "text": f"Region {goal_region.name} cannot be reached"}]

        path: list[Entrance] = []
        name, connection = state.path[goal_region]
        while connection != ("Menu", None) and connection is not None:
            name, connection = connection
            if "->" in name and "Menu" not in name:
                path.append(self.get_entrance(name))

        messages: list[JSONMessagePart] = []
        path.reverse()
        for p in path:
            messages.extend(
                [
                    {"type": "entrance_name", "text": p.name, "player": self.player},
                    {"type": "text", "text": "\n"},
                    *rule_to_json(p.access_rule, state),
                    {"type": "text", "text": "\n"},
                ]
            )

        if goal_location:
            messages.extend(
                [
                    {"type": "text", "text": "-> "},
                    {
                        "type": "location_name",
                        "text": goal_location.name,
                        "player": self.player,
                    },
                    {"type": "text", "text": "\n"},
                    *rule_to_json(goal_location.access_rule, state),
                ]
            )

        return messages

    def explain_rule(self, dest_name: str, state: CollectionState) -> list[JSONMessagePart]:
        macro_name, usable, response = get_intended_text(dest_name, list(self.rule_macro_hashes))
        if not usable:
            return [{"type": "text", "text": response}]
        macro = self.rules_by_hash[self.rule_macro_hashes[macro_name]]
        assert isinstance(macro, Macro.Resolved)
        messages: list[JSONMessagePart] = [
            {"type": "color", "color": "green" if macro(state) else "salmon", "text": macro.name}
        ]
        if macro.description:
            messages.append({"type": "text", "text": f": {macro.description}"})
        messages.extend([{"type": "text", "text": "\n"}, *macro.child.explain_json(state)])
        return messages

    def reconnect_found_entrances(self, found_key: str, data_storage_value: Any) -> None:
        if (
            not self.options.campfire_warp
            or getattr(self.multiworld, "enforce_deferred_connections", None) == "off"
            or not isinstance(data_storage_value, list)
        ):
            return

        source_region = self.get_region(RegionName.GT_ENTRANCE.value)
        for campfire_id in data_storage_value:  # pyright: ignore[reportUnknownVariableType]
            dest_region = self.get_region(CAMPFIRE_WARPS[campfire_id].value)
            entrance_name = f"{source_region.name} -> {dest_region.name}"

            try:
                self.get_entrance(entrance_name)
                continue
            except KeyError:
                pass

            self.create_entrance(source_region, dest_region, rule=CampfireWarp())
