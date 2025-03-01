import asyncio
import urllib.parse
from collections import deque
from typing import TYPE_CHECKING, Dict, List, Optional

from CommonClient import CommonContext, get_base_parser, gui_enabled, logger, server_loop
from MultiServer import mark_raw
from Utils import get_intended_text

from .constants import GAME_NAME
from .items import item_table
from .locations import location_table
from .regions import RegionName

if TYPE_CHECKING:
    from BaseClasses import CollectionState, Entrance, Location, MultiWorld, Region
    from NetUtils import JSONMessagePart

    from .logic import RuleInstance
    from .world import AstalonWorld

try:
    from worlds.tracker.TrackerClient import UT_VERSION, TrackerGameContext, updateTracker  # type: ignore
    from worlds.tracker.TrackerClient import TrackerCommandProcessor as ClientCommandProcessor

    tracker_loaded = True
except ImportError:
    from CommonClient import ClientCommandProcessor

    class TrackerGameContextMixin:
        """Expecting the TrackerGameContext to have these methods."""

        multiworld: "MultiWorld"
        player_id: int

        def build_gui(self, manager): ...

        def run_generator(self): ...

        def load_kv(self): ...

    class TrackerGameContext(CommonContext, TrackerGameContextMixin):
        pass

    tracker_loaded = False
    UT_VERSION = "Not found"


class AstalonCommandProcessor(ClientCommandProcessor):  # type: ignore
    ctx: "AstalonClientContext"

    def _print_rule(self, rule: "Optional[RuleInstance]"):
        if rule:
            if self.ctx.ui:
                messages: List[JSONMessagePart] = [{"type": "text", "text": "    "}]
                messages.extend(rule.explain())
                self.ctx.ui.print_json(messages)
            else:
                logger.info("    " + rule.serialize())
        else:
            if self.ctx.ui:
                messages: List[JSONMessagePart] = [
                    {"type": "text", "text": "    "},
                    {"type": "color", "color": "green", "text": "True"},
                ]
                self.ctx.ui.print_json(messages)
            else:
                logger.info("    True")

    @mark_raw
    def _cmd_route(self, input_text: str = ""):
        """Explain the route to get to a location or region"""
        world = self.ctx.get_world()
        if not world:
            return

        goal_location: Location | None = None
        goal_region: Region | None = None
        region_name = ""
        location_name, usable, response = get_intended_text(input_text, world.location_names)
        if usable:
            goal_location = world.get_location(location_name)
            goal_region = goal_location.parent_region
            if not goal_region:
                logger.warning(f"Location {location_name} has no parent region")
                return
        else:
            region_name, usable, _ = get_intended_text(
                input_text,
                [r.name for r in world.multiworld.get_regions(world.player)],
            )
            if usable:
                goal_region = world.get_region(region_name)
            else:
                logger.warning(response)
                return

        state = get_updated_state(self.ctx)
        if goal_location and not goal_location.can_reach(state):
            logger.warning(f"Location {goal_location.name} cannot be reached")
            return
        if goal_region and not goal_region.can_reach(state):
            logger.warning(f"Region {goal_region.name} cannot be reached")
            return

        start = world.get_region(RegionName.GT_ENTRANCE.value)
        visited: Dict[Region, Optional[Region]] = {start: None}
        q: deque[Region] = deque()
        q.append(start)

        found = False
        region = None
        while q:
            region = q.popleft()
            if region == goal_region:
                found = True
                break

            for entrance in region.get_exits():
                exit_region: Region = entrance.connected_region
                if exit_region and exit_region not in visited and entrance.can_reach(state):
                    visited[exit_region] = region
                    q.append(exit_region)

        if not found:
            logger.warning(f"Could not find path to {location_name or region_name}")

        path: List[Entrance] = []
        prev = None
        while region:
            if prev:
                entrance = world.get_entrance(f"{region.name} -> {prev.name}")
                path.append(entrance)
            prev = region
            region = visited[region]
        path.reverse()
        for p in path:
            if self.ctx.ui:
                self.ctx.ui.print_json(
                    [{"type": "entrance_name", "text": p.name, "player": self.ctx.player_id}]
                )
            else:
                logger.info(p.name)
            self._print_rule(getattr(p.access_rule, "__self__", None))

        if goal_location:
            if self.ctx.ui:
                self.ctx.ui.print_json(
                    [
                        {"type": "text", "text": "-> "},
                        {"type": "location_name", "text": goal_location.name, "player": self.ctx.player_id},
                    ]
                )
            else:
                logger.info(f"-> {goal_location.name}")
            self._print_rule(getattr(goal_location.access_rule, "__self__", None))

    if not tracker_loaded:
        del _cmd_route


class AstalonClientContext(TrackerGameContext):
    game = GAME_NAME
    command_processor = AstalonCommandProcessor

    def make_gui(self):
        ui = super().make_gui()  # before the kivy imports so kvui gets loaded first
        from kvui import KivyJSONtoTextParser

        class AstalonJSONtoTextParser(KivyJSONtoTextParser):
            ctx: "CommonContext"

            def _handle_item_name(self, node: "JSONMessagePart"):
                flags = node.get("flags", 0)
                item_types = []
                if flags & 0b001:  # advancement
                    item_types.append("progression")
                if flags & 0b010:  # useful
                    item_types.append("useful")
                if flags & 0b100:  # trap
                    item_types.append("trap")
                if not item_types:
                    item_types.append("normal")
                tooltip = "Item Class: " + ", ".join(item_types)

                player = node.get("player", 0)
                slot_info = self.ctx.slot_info.get(player)
                item_name = node.get("text", "")
                metadata = item_table.get(item_name)
                if slot_info and slot_info.game == GAME_NAME and metadata and metadata.description:
                    tooltip += f"<br>{metadata.description}"

                node.setdefault("refs", []).append(tooltip)  # type: ignore
                return super(KivyJSONtoTextParser, self)._handle_item_name(node)

            def _handle_location_name(self, node: "JSONMessagePart"):
                player = node.get("player", 0)
                slot_info = self.ctx.slot_info.get(player)
                location_name = node.get("text", "")
                metadata = location_table.get(location_name)
                if slot_info and slot_info.game == GAME_NAME and metadata:
                    parts = []
                    if metadata.room:
                        parts.append(f"{metadata.area.value} ({metadata.room})")
                    else:
                        parts.append(metadata.area.value)
                    parts.append(f"Region: {metadata.region.value}")
                    if metadata.description:
                        parts.append(metadata.description)
                    node.setdefault("refs", []).append("<br>".join(parts))  # type: ignore
                return super()._handle_location_name(node)

        class AstalonManager(ui):
            # core appends ap version so this works
            base_title = f"Astalon Tracker with UT {UT_VERSION} for AP version"
            ctx: "AstalonClientContext"

            def __init__(self, ctx: "CommonContext"):
                super().__init__(ctx)
                self.json_to_kivy_parser = AstalonJSONtoTextParser(ctx)

            def build(self):
                container = super().build()
                if not tracker_loaded:
                    logger.info("To enable the tracker page, install Universal Tracker.")

                return container

        return AstalonManager

    def get_world(self) -> "Optional[AstalonWorld]":
        if self.player_id is None:
            logger.warning("Internal logic was not able to load, check your yamls and relaunch.")
            return

        if self.game != GAME_NAME:
            logger.warning(f"Please connect to a slot with explainable logic (not {self.game}).")
            return

        return self.multiworld.worlds[self.player_id]  # type: ignore


def get_updated_state(ctx: "TrackerGameContext") -> "CollectionState":
    return updateTracker(ctx).state  # type: ignore


async def main(args):
    ctx = AstalonClientContext(args.connect, args.password)

    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if tracker_loaded:
        ctx.run_generator()
    else:
        logger.warning("Could not find Universal Tracker.")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()


def launch(*args):
    parser = get_base_parser(description="Gameless Archipelago Client, for text interfacing.")
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    asyncio.run(main(args))
