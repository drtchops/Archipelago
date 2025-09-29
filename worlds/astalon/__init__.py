from worlds.LauncherComponents import (
    Component,
    Type,
    components,
    icon_paths,
    launch_subprocess,  # pyright: ignore[reportUnknownVariableType]
)

from .world import AstalonWorld


def launch_client() -> None:
    from .client import launch

    launch_subprocess(launch, name="Astalon Tracker")


components.append(Component("Astalon Tracker", func=launch_client, component_type=Type.CLIENT, icon="astalon"))

icon_paths["astalon"] = f"ap:{__name__}/images/pil.png"

__all__ = ("AstalonWorld",)
