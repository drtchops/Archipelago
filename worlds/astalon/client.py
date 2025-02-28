import asyncio
import urllib.parse
from collections import deque
from typing import TYPE_CHECKING, Dict, List, Optional

from CommonClient import get_base_parser, gui_enabled, logger, server_loop
from MultiServer import mark_raw
from Utils import get_intended_text

from .constants import GAME_NAME
from .regions import RegionName

if TYPE_CHECKING:
    from BaseClasses import CollectionState, Entrance, Location, MultiWorld, Region

    from .world import AstalonWorld

try:
    from worlds.tracker.TrackerClient import UT_VERSION, TrackerGameContext, updateTracker  # type: ignore
    from worlds.tracker.TrackerClient import TrackerCommandProcessor as ClientCommandProcessor

    tracker_loaded = True
except ImportError:
    from CommonClient import ClientCommandProcessor, CommonContext

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
            logger.info(p.name)
            if hasattr(p.access_rule, "__self__"):
                logger.info("    " + p.access_rule.__self__.serialize())  # type: ignore
            else:
                logger.info("    True")

        if goal_location:
            logger.info(f"-> {goal_location.name}")
            if hasattr(goal_location.access_rule, "__self__"):
                logger.info("    " + goal_location.access_rule.__self__.serialize())  # type: ignore
            else:
                logger.info("    True")

    if not tracker_loaded:
        del _cmd_route


class AstalonClientContext(TrackerGameContext):
    game = GAME_NAME
    command_processor = AstalonCommandProcessor

    def make_gui(self):
        ui = super().make_gui()  # before the kivy imports so kvui gets loaded first

        class AstalonManager(ui):
            # core appends ap version so this works
            base_title = f"Astalon Tracker with UT {UT_VERSION} for AP version"
            ctx: AstalonClientContext

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
