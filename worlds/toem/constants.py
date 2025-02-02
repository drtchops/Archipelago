from enum import Enum
from typing import Final

GAME_NAME: Final[str] = "TOEM"
BASE_ID: Final[int] = 678356000


class Area(str, Enum):
    HOMELANDA = "Homelanda"
    OAKLAVILLE = "Oaklaville"
    STANHAMN = "Stanhamn"
    LOGCITY = "Logcity"
    KIIRUBERG = "Kiiruberg"
    MOUNTAIN_TOP = "Mountain Top"
    BASTO = "Basto"
