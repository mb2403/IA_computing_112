# Lewis Clark + Max Bowler Jan/Feb 2022
#

from floodsystem.station import MonitoringStation
from .utils import sorted_by_key    

def stations_level_over_threshold(stations,tol):
    names_list = []
    relatives_list = []

    for item in stations:
        if (item.typical_range_consistent() == False) or (item.relative_water_level() == None):
            pass
        elif (item.relative_water_level() > tol):
            names_list.append(item.name)
            relatives_list.append(item.relative_water_level())
    names_and_relatives = zip(names_list,relatives_list)
    

    return sorted_by_key(names_and_relatives,1)

