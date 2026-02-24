from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import OPTION_GROUPS


class AstalonWebWorld(WebWorld):
    theme = "stone"
    tutorials = [  # noqa: RUF012
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up the Astalon randomizer.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["DrTChops"],
        )
    ]
    option_groups = OPTION_GROUPS
