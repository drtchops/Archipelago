from functools import cached_property
from typing import Any, ClassVar, Final, cast

from typing_extensions import override

from BaseClasses import CollectionRule, CollectionState, Entrance, Location, Region
from NetUtils import JSONMessagePart
from Options import Option
from rule_builder.rules import Rule
from Utils import get_fuzzy_results, get_intended_text  # pyright: ignore[reportUnknownVariableType]

from .bases import AstalonWorldBase
from .items import Character, Events, item_table
from .locations import location_table
from .logic.custom_rules import FastTravel
from .options import ShuffleVoidPortals, StartingLocation
from .regions import RegionName, astalon_regions


def map_page_index(data: Any, *_: Any, **__: Any) -> int:
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

CAMPFIRE_WARPS: Final[dict[int, tuple[RegionName, str]]] = {
    6696: (RegionName.GT_ENTRANCE, "Tutorial"),
    18: (RegionName.GT_BOTTOM, "GT Bottom"),
    292: (RegionName.GT_LEFT, "GT Left"),
    293: (RegionName.GT_BOSS, "GT Boss"),
    1140: (RegionName.MECH_START, "Mechanism Start"),
    1556: (RegionName.MECH_SWORD_CONNECTION, "Mechanism Sword"),
    813: (RegionName.MECH_BOTTOM_CAMPFIRE, "Mechanism Bottom"),
    712: (RegionName.MECH_BK, "Mechanism Shortcut"),
    3547: (RegionName.MECH_RIGHT, "Mechanism Right"),
    1634: (RegionName.MECH_TOP, "Mechanism Top"),
    819: (RegionName.MECH_BOSS, "Mechanism Boss"),
    7507: (RegionName.CD_START, "CD 1"),
    7577: (RegionName.CD_MIDDLE, "CD 2"),
    7703: (RegionName.CD_CAMPFIRE_3, "CD 3"),
    7774: (RegionName.CD_TOP, "CD 4"),
    5019: (RegionName.HOTP_EPIMETHEUS, "HotP Epimetheus"),
    6421: (RegionName.HOTP_BELL_CAMPFIRE, "HotP Bell"),
    3207: (RegionName.HOTP_CLAW_CAMPFIRE, "HotP Claw"),
    2904: (RegionName.HOTP_BOSS_CAMPFIRE, "HotP Boss"),
    10203: (RegionName.CATH_CAMPFIRE_1, "Cathedral 1"),
    10260: (RegionName.CATH_CAMPFIRE_2, "Cathedral 2"),
    3726: (RegionName.ROA_START, "RoA Start"),
    7088: (RegionName.ROA_LEFT_ASCENT, "RoA Left"),
    7086: (RegionName.ROA_MIDDLE, "RoA Middle"),
    4685: (RegionName.ROA_ELEVATOR, "RoA Elevator"),
    10026: (RegionName.ROA_BOSS, "RoA Boss"),
    7436: (RegionName.SP_CAMPFIRE_1, "SP 1"),
    8243: (RegionName.SP_CAMPFIRE_2, "SP 2"),
    4635: (RegionName.APEX, "The Apex"),
    7109: (RegionName.CAVES_LOWER, "Catacombs Upper"),
    2524: (RegionName.CATA_BOW_CAMPFIRE, "Catacombs Bow"),
    2610: (RegionName.CATA_ROOTS_CAMPFIRE, "Catacombs Roots"),
    2669: (RegionName.CATA_BOSS, "Catacombs Boss"),
    9056: (RegionName.TR_START, "Tower Roots"),
    9161: (RegionName.CATA_DEV_ROOM, "Dev Room"),
}
ELEVATORS: Final[dict[int, tuple[RegionName, str]]] = {
    6629: (RegionName.GT_ENTRANCE, "Gorgon Tomb 1"),
    248: (RegionName.GT_BOSS, "Gorgon Tomb 2"),
    3947: (RegionName.MECH_ZEEK_CONNECTION, "Mechanism 1"),
    803: (RegionName.MECH_BOSS, "Mechanism 2"),
    10535: (RegionName.HOTP_ELEVATOR, "Hall of the Phantoms"),
    1080: (RegionName.HOTP_BOSS, "Ruins of Ash 1"),
    8771: (RegionName.ROA_ELEVATOR, "Ruins of Ash 2"),
    4109: (RegionName.APEX, "The Apex"),
    61: (RegionName.CATA_ELEVATOR, "Catacombs 1"),
    2574: (RegionName.CATA_BOSS, "Catacombs 2"),
    2705: (RegionName.TR_START, "Tower Roots"),
}
PORTAL_REGIONS: Final[dict[int, RegionName]] = {
    1099: RegionName.GT_ENTRANCE,
    186: RegionName.GT_VOID,
    877: RegionName.MECH_LOWER_VOID,
    1315: RegionName.MECH_UPPER_VOID,
    879: RegionName.HOTP_LOWER_VOID,
    3264: RegionName.HOTP_UPPER_VOID,
    7056: RegionName.HOTP_CATH_VOID,
    7272: RegionName.CATA_START,
    7437: RegionName.ROA_LOWER_VOID,
    4094: RegionName.ROA_UPPER_VOID,
    3795: RegionName.CATA_VOID_R,
    4336: RegionName.CATA_VOID_L,
}

ACRONYMS = {
    "gt": "Gorgon's Tomb, the light blue starting area",
    "mech": "Mechanism, the yellow 2nd main area",
    "hotp": "Hall of the Phantoms, the purple 3rd main area",
    "roa": "Ruins of Ash, the orange last main area",
    "cata": "Catacombs, the blue area below the start",
    "tr": "Tower Roots, the blue area below Catacombs",
    "cd": "Cyclops Den, the blue side area off of Mechanism",
    "cath": "Cathedral, the orange side area off of Hall of the Phantoms",
    "sp": "Serpent Path, the pink side area off of Ruins of Ash",
}


def location_icon_coords(index: int | None, coords: dict[str, Any], *_: Any, **__: Any) -> tuple[int, int, str] | None:
    """Converts player coordinates provided by the game mod into image coordinates for the map page."""
    if index is None or not coords:
        return None

    dx, dy = MAP_OFFSETS[index]
    x = int((coords.get("X", 0) + (ROOM_WIDTH / 2) + dx) / MAP_SCALE_X)
    y = int((coords.get("Y", 0) - (ROOM_HEIGHT / 2) + dy) / MAP_SCALE_Y)
    icon = CHARACTER_ICONS.get(coords.get("Character", 1), "algus")
    return x, y, f"images/icons/{icon}.png"


def rule_to_json(
    rule: CollectionRule | Rule.Resolved | None,
    state: CollectionState,
    indent: str = "",
) -> list[JSONMessagePart]:
    messages: list[JSONMessagePart] = []
    if indent:
        messages.append({"type": "text", "text": indent})
    if isinstance(rule, Rule.Resolved):
        messages.extend(rule.explain_json(state))
    else:
        messages.append({"type": "color", "color": "green", "text": "True"})
    return messages


class AstalonUTWorld(AstalonWorldBase):
    tracker_world: ClassVar = {
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
    found_entrances_datastorage_key: ClassVar = [
        "Slot:{player}:campfires",
        "Slot:{player}:portals",
        "Slot:{player}:elevators",
    ]

    @cached_property
    def is_ut(self) -> bool:
        return getattr(self.multiworld, "generation_is_fake", False)

    @cached_property
    def defer_connections(self) -> bool:
        return self.is_ut and getattr(self.multiworld, "enforce_deferred_connections", None) != "off"

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
            if "portal_pairs" in slot_data:
                self.portal_pairs = tuple(tuple(p) for p in slot_data["portal_pairs"])

    def get_logical_path(self, dest_name: str, state: CollectionState, *_: Any, **__: Any) -> list[JSONMessagePart]:
        if not dest_name:
            return [{"type": "text", "text": "Provide a location or region to route to using /get_logical_path [name]"}]

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
            region_name, usable, _resp = get_intended_text(
                dest_name,
                [reg.name for reg in self.get_regions()],
            )
            if usable:
                goal_region = self.get_region(region_name)
            else:
                return [{"type": "text", "text": response}]

        in_logic = True
        if (goal_location and not goal_location.can_reach(state)) or (
            goal_region not in state.path and goal_region.name != self.origin_region_name
        ):
            state.collect(self.create_item(self.glitches_item_name))
            in_logic = False

        if goal_location and not goal_location.can_reach(state):
            return [{"type": "text", "text": f"Location {goal_location.name} cannot be reached"}]
        if goal_region not in state.path and goal_region.name != self.origin_region_name:
            return [{"type": "text", "text": f"Region {goal_region.name} cannot be reached"}]

        messages: list[JSONMessagePart] = [
            {"type": "color", "color": "slateblue", "text": f"Start -> {self.origin_region_name}\n"},
            {"type": "color", "color": "green", "text": "    True\n"},
        ]
        if goal_region.name != self.origin_region_name:
            path: list[Entrance] = []
            name, connection = state.path[goal_region]
            while connection is not None:
                name, connection = connection
                if "->" in name or name.endswith(" Portal"):
                    path.append(self.get_entrance(name))

            path.reverse()
            for p in path:
                messages.extend(
                    [
                        {"type": "entrance_name", "text": p.name, "player": self.player},
                        {"type": "text", "text": "\n"},
                        *rule_to_json(p.access_rule, state, indent="    "),
                        {"type": "text", "text": "\n"},
                    ]
                )

        if goal_location:
            messages.extend(
                [
                    {"type": "text", "text": "-> "},
                    {
                        "type": "color",
                        "color": "green" if in_logic else "yellow",
                        "text": goal_location.name,
                    },
                    {"type": "text", "text": "\n"},
                    *rule_to_json(goal_location.access_rule, state, indent="    "),
                ]
            )

        return messages

    def explain_rule(self, dest_name: str, state: CollectionState, *_: Any, **__: Any) -> list[JSONMessagePart]:
        if not dest_name:
            return [{"type": "text", "text": "Enter a location, region, item, or acronym to get an explanation"}]
        if description := ACRONYMS.get(dest_name.lower()):
            return [{"type": "text", "text": description}]

        types_to_try = {
            "location": self._explain_location,
            "region": self._explain_region,
            "item": self._explain_item,
        }
        attempts = list(types_to_try.keys())
        parts = dest_name.split(maxsplit=1)
        if len(parts) == 2:
            first_word = parts[0].lower()
            for label in types_to_try.keys():
                if first_word == label:
                    attempts = [label]
                    break

        result = []
        usable = False
        best_guess = []
        max_confidence = 0
        confidence = 0
        for classification in attempts:
            result, usable, confidence = types_to_try[classification](dest_name, state)
            if usable:
                return result
            if confidence > max_confidence:
                best_guess = result
                max_confidence = confidence

        return best_guess

    def _explain_location(self, location_name: str, state: CollectionState) -> tuple[list[JSONMessagePart], bool, int]:
        all_location_names = set(self.multiworld.regions.location_cache[self.player])
        guess, usable, response = get_intended_text(location_name, all_location_names)
        if not usable:
            picks = get_fuzzy_results(location_name, all_location_names, limit=1)
            confidence = picks[0][1]
            return [{"type": "text", "text": response}], False, confidence

        location_name = guess
        location = self.get_location(location_name)
        location_data = location_table[location_name]
        messages: list[JSONMessagePart] = [
            {"type": "text", "text": "Location "},
            {"type": "color", "color": "green" if location.can_reach(state) else "salmon", "text": location_name},
        ]
        if location_data.description:
            messages.append({"type": "text", "text": f"\n{location_data.description}"})
        if location.parent_region:
            region = location.parent_region
            region_data = astalon_regions[RegionName(region.name)]
            messages.extend(
                [
                    {"type": "text", "text": "\nRegion "},
                    {"type": "color", "color": "green" if region.can_reach(state) else "salmon", "text": region.name},
                ]
            )
            if region_data.description:
                messages.append({"type": "text", "text": f": {region_data.description}"})
        if location_data.room:
            messages.append({"type": "text", "text": f"\nRoom: {location_data.area} {location_data.room}"})
        else:
            messages.append({"type": "text", "text": f"\nArea: {location_data.area}"})
        messages.extend(
            [
                {"type": "text", "text": f"\nGroup: {location_data.group}"},
                {"type": "text", "text": "\nLogic: "},
                *rule_to_json(location.access_rule, state),
            ]
        )
        return messages, True, 100

    def _explain_region(self, region_name: str, state: CollectionState) -> tuple[list[JSONMessagePart], bool, int]:
        all_region_names = set(self.multiworld.regions.region_cache[self.player])
        guess, usable, response = get_intended_text(region_name, all_region_names)
        if not usable:
            picks = get_fuzzy_results(region_name, all_region_names, limit=1)
            confidence = picks[0][1]
            return [{"type": "text", "text": response}], False, confidence

        region_name = guess
        region = self.get_region(region_name)
        region_data = astalon_regions[RegionName(region_name)]
        messages: list[JSONMessagePart] = [
            {"type": "text", "text": "Region "},
            {"type": "color", "color": "green" if region.can_reach(state) else "salmon", "text": region_name},
        ]
        if region_data.description:
            messages.append({"type": "text", "text": f"\n{region_data.description}"})
        tags: list[str] = []
        if region_data.boss:
            tags.append("Boss")
        if region_data.campfire:
            tags.append("Campfire")
        if region_data.elevator:
            tags.append("Elevator")
        if region_data.multiplier:
            tags.append("Orb Multiplier")
        if region_data.portal:
            tags.append("Void Portal")
        if region_data.statue:
            tags.append("Epimetheus Statue")
        if tags:
            messages.append({"type": "text", "text": f"\nTags: {', '.join(tags)}"})
        if region.entrances:
            messages.append({"type": "text", "text": "\nEntrances:"})
            for entrance in region.entrances:
                messages.extend(
                    [
                        {
                            "type": "text",
                            "text": f"\n  {entrance.parent_region.name if entrance.parent_region else entrance.name}\n",
                        },
                        *rule_to_json(entrance.access_rule, state, indent="    "),
                    ]
                )
        return messages, True, 100

    def _explain_item(self, item_name: str, state: CollectionState) -> tuple[list[JSONMessagePart], bool, int]:
        all_item_names = set(self.item_name_to_id.keys())
        guess, usable, response = get_intended_text(item_name, all_item_names)
        if not usable:
            picks = get_fuzzy_results(item_name, all_item_names, limit=1)
            confidence = picks[0][1]
            return [{"type": "text", "text": response}], False, confidence

        item_name = guess
        item_data = item_table[item_name]
        classification = (
            item_data.classification(self.options) if callable(item_data.classification) else item_data.classification
        )
        messages: list[JSONMessagePart] = [
            {"type": "text", "text": "Item "},
            {
                "type": "item_id",
                "flags": int(classification),
                "player": self.player,
                "text": str(self.item_name_to_id[item_name]),
            },
        ]
        if item_data.description:
            messages.append({"type": "text", "text": f"\n{item_data.description}"})
        count = state.count(item_name, self.player)
        messages.extend(
            [
                {"type": "text", "text": "\nCount: "},
                {"type": "color", "color": "green" if count else "salmon", "text": str(count)},
                {"type": "text", "text": f"\nGroup: {item_data.group}"},
            ]
        )
        return messages, True, 100

    def reconnect_found_entrances(self, found_key: str, data_storage_value: Any, *_: Any, **__: Any) -> None:
        if not self.defer_connections or not data_storage_value:
            return

        if found_key.endswith(":campfires") and self.options.campfire_warp and isinstance(data_storage_value, list):
            campfires = cast(list[int], data_storage_value)
            self._connect_campfire_warps(campfires)
        elif (
            found_key.endswith(":elevators")
            and not self.options.randomize_elevator
            and self.options.starting_location == StartingLocation.option_gorgon_tomb  # TODO: check if others work
            and isinstance(data_storage_value, list)
        ):
            elevators = cast(list[int], data_storage_value)
            self._connect_elevators(elevators)
        elif (
            found_key.endswith(":portals")
            and self.options.shuffle_void_portals
            and isinstance(data_storage_value, dict)
        ):
            portals = cast(dict[str, int], data_storage_value)
            self._connect_portals({int(k): v for k, v in portals.items()})

    def _connect_campfire_warps(self, campfire_ids: list[int]) -> None:
        source_region = self.get_region(self.origin_region_name)
        for campfire_id in campfire_ids:
            region_name, campfire_name = CAMPFIRE_WARPS[campfire_id]
            dest_region = self.get_region(region_name.value)
            if source_region == dest_region:
                continue
            entrance_name = f"{source_region.name} -> {dest_region.name}"

            try:
                self.get_entrance(entrance_name)
                continue
            except KeyError:
                pass

            self.create_entrance(source_region, dest_region, rule=FastTravel(f"Campfire Warp to {campfire_name}"))

    def _connect_elevators(self, elevator_ids: list[int]) -> None:
        source_region = self.get_region(self.origin_region_name)
        for elevator_id in elevator_ids:
            region_name, elevator_name = ELEVATORS[elevator_id]
            dest_region = self.get_region(region_name.value)
            if source_region == dest_region:
                continue
            entrance_name = f"{source_region.name} -> {dest_region.name}"

            try:
                self.get_entrance(entrance_name)
                continue
            except KeyError:
                pass

            self.create_entrance(source_region, dest_region, rule=FastTravel(f"Elevator to {elevator_name}"))

    def _connect_portals(self, portals: dict[int, int]) -> None:
        for source_portal, dest_portal in portals.items():
            if source_portal == dest_portal:
                continue
            source_region = self.get_region(PORTAL_REGIONS[source_portal].value)
            dest_region = self.get_region(PORTAL_REGIONS[dest_portal].value)
            entrance = self.get_entrance(f"{source_region.name} Portal")
            if entrance.connected_region is None:
                entrance.connect(dest_region)
            if self.options.shuffle_void_portals == ShuffleVoidPortals.option_coupled:
                coupled_entrance = self.get_entrance(f"{dest_region.name} Portal")
                if coupled_entrance.connected_region is None:
                    coupled_entrance.connect(source_region)
