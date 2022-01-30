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
from collections import defaultdict                                     # helps formatting dictionary values as lists

def stations_by_distance(stations,p):                                   # LC Task 1B
    distance_list = []
    for item in stations:                                               # generates list of distances from p 
        distance_list.append(haversine(item.coord,p))   
    
    names_list = []
    for item in stations:                                               # generates list of names from p 
        names_list.append(item.name)
    
    names_and_distance_list = list(zip(names_list,distance_list))       # combines lists into a list of tuples (name,distance)
    return(sorted_by_key(names_and_distance_list,1))                    # returns the sorted list using sorted_by_key (sorts by distance)

def rivers_with_station(stations):                                      # LC Task 1D
    rivers_set = set()                                                  # a set it used here to avoid duplicate entries
    for item in stations:
        rivers_set.add(item.river)

    return rivers_set

def stations_by_river(stations):                                        # LC Task 1D
    dictionary = defaultdict(list)                                      # creates a dictionary where the values are of type list
    for item in stations:
        dictionary[item.river].append(item.name)                        # dictionary keys: rivers, values: (station1, station2 ...)
    
    return dictionary
