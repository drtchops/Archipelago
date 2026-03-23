from typing import Any

from worlds.LauncherComponents import Component, Type, components
from worlds.LauncherComponents import launch as launch_component  # pyright: ignore[reportUnknownVariableType]


def launch_client(*args: Any):
    from .client import run

    launch_component(run, name="Proxy Client", args=args)


components.append(Component("Proxy Client", func=launch_client, component_type=Type.CLIENT))
