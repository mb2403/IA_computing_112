# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.datafetcher import fetch_station_data
from floodsystem.station import MonitoringStation           
from .utils import sorted_by_key                                        # allows sorting
from haversine import haversine, Unit                                   # calcuates the distance between two (latitude, longitude)s


def stations_by_distance(stations,p):                       
    distance_list = []
    for item in stations:                                               # generates list of distances from p 
        distance_list.append(haversine(item.coord,p))   
    
    names_list = []
    for item in stations:                                               # generates list of names from p 
        names_list.append(item.name)
    
    names_and_distance_list = list(zip(names_list,distance_list))       # combines lists into a list of tuples (name,distance)
    return(sorted_by_key(names_and_distance_list,1))                    # returns the sorted list using sorted_by_key (sorts by distance)