# Max Bowler Feb 2022
# Task 2G
#

import numpy
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key
from numpy import gradient
from floodsystem.analysis import polyfit
from floodsystem.geo import stations_by_river
from collections import defaultdict


def run():

    stations = build_station_list()

#List of stations in each town for later
    def stations_by_town():
        dictionary = defaultdict(list)                                      # creates a dictionary where the values are of type list
        for item in stations:
            dictionary[item.town].append(item.name)                        # dictionary keys: rivers, values: (station1, station2 ...)
    
        return dictionary
    
    town_set = stations_by_town(stations)

    N =  len(stations)
    g = N/5
    h = 2*N/5
    j = 3*N/5
    k = 4*N/5


    current_rel_risk = stations_highest_rel_level(stations, N)

#Need to find a way to find the current gradient of the measured height curve
    future_rel_risk = []

    levels = []
    for station in stations:
        height = station.measure_id
        levels.append(height)

    for station in stations:
        current_grad = numpy.gradient(polyfit(0, levels, 10))
        float(current_grad)
        future_rel_risk.append(current_grad)


    combined_rel_risk = []

    for i in range(N):
        product = current_rel_risk[i][1]*future_rel_risk[i][1]
        combined_rel_risk.append(product)

    stations.append(combined_rel_risk)

    stations = sorted_by_key(stations, 1, reverse=True)

#The below was writen when I thought we first needed to find a ranking of risks based on station
    """print("The following stations are at severe risk level:")
    for i in range(0, g):
        print(stations[i][0], stations[i][1])
    print("The following stations are at high risk level:")
    for i in range(g, h):
        print(stations[i][0], stations[i][1])
    print("The following stations are at moderate risk level:")
    for i in range(h, j):
        print(stations[i][0], stations[i][1])
    print("The following stations are at low risk level:")
    for i in range(j, k):
        print(stations[i][0], stations[i][1])
    print("The  following stations should not be considered a threat")
    for i in range(k, N):
        print(stations[i][0], stations[i][1])"""


#Making a sum of the relative risks at all the stations within a town, and assigning that to a town
    tot_town_risk = 0
    for station in stations:   
        for i in town_set:
            if town_set[station.name] == stations[i][0]:
                tot_town_risk += stations[i][1]
        town_set.append(tot_town_risk)

    town_set = sorted_by_key(town_set, 1, reverse=True)

    print("List of towns in order of highest to lowest risk relaitve to eachother:")
    for i in range(len(town_set)):
        print(town_set[i][0], town_set[i][1])



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()