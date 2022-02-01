# Lewis Clark + Max Bowler Jan/Feb 2022
#

from floodsystem.station import MonitoringStation
from .utils import sorted_by_key    

def stations_level_over_threshold(stations,tol):                                                            #LC task 2B
    stations_list = []
    relatives_list = []

    for item in stations:
        if (item.typical_range_consistent() == False) or (item.relative_water_level() == None):             #checks if data is valid
            pass
        elif (item.relative_water_level() > tol):                                                           #if data > tol then add to list.
            stations_list.append(item)
            relatives_list.append(item.relative_water_level())
            
    combined_list = zip(stations_list,relatives_list)                                                       #combines two lists into a list of tuples
    
    return sorted_by_key(combined_list,1)                                                                   #returns a list sorted by relative level

def stations_highest_rel_level(stations, N):                                                                #MB
    stations_list = []
    relatives_list = []
    
    for item in stations:
        if (item.typical_range_consistent() == False) or (item.relative_water_level() == None):             #checks if data is valid
            pass
        else:                                                           #if data > tol then add to list.
            stations_list.append(item)
            relatives_list.append(item.relative_water_level())
            
    combined_list = zip(stations_list,relatives_list)                                                       #combines two lists into a list of tuples
    
    combined_list = sorted_by_key(combined_list, 1, reverse=True)

    return combined_list[:N]