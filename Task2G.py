# Max Bowler Jan 2022
# Task 2G
#

import numpy
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key
from numpy import gradient


def run():

    stations = build_station_list()

    N =  len(stations)
    g = N/5
    h = 2*N/5
    j = 3*N/5
    k = 4*N/5


    current_rel_risk = stations_highest_rel_level(stations, N)


#Need to find a way to find the current gradient of the measured height curve
    future_rel_risk = []
    for stations in range(len(stations)):
        current_grad = numpy.gradient(plot_water_level_with_fit(stations, 0, stations.measureid, p))
        future_rel_risk.append(current_grad)


    combined_rel_risk = []

    for i in range(N):
        product = current_rel_risk[i][1]*future_rel_risk[i][1]
        combined_rel_risk.append(product)

    stations.append(combined_rel_risk)

    stations = sorted_by_key(stations, 1, reverse=True)

    print("The following stations are at severe risk level:")
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
        print(stations[i][0], stations[i][1])


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()