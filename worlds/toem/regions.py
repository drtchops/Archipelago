from enum import Enum
from typing import Dict, Tuple


class RegionName(str, Enum):
    MENU = "Menu"
    HOMELANDA = "Homelanda"
    OAKLAVILLE = "Oaklaville"
    STANHAMN = "Stanhamn"
    LOGCITY = "Logcity"
    KIIRUBERG = "Kiiruberg"
    MOUNTAIN_TOP = "Mountain Top"
    BASTO = "Basto"


toem_regions: Dict[RegionName, Tuple[RegionName, ...]] = {
    RegionName.MENU: (RegionName.HOMELANDA,),
    RegionName.HOMELANDA: (RegionName.OAKLAVILLE,),
    RegionName.OAKLAVILLE: (RegionName.STANHAMN,),
    RegionName.STANHAMN: (RegionName.LOGCITY,),
    RegionName.LOGCITY: (RegionName.KIIRUBERG,),
    RegionName.KIIRUBERG: (RegionName.MOUNTAIN_TOP,),
    RegionName.MOUNTAIN_TOP: (RegionName.BASTO,),
    RegionName.BASTO: (),
}
