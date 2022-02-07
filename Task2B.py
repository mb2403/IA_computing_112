# Lewis Clark Jan 2022
# Task 2B
#

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    stations_over = stations_level_over_threshold(stations,0.8)                        #defines the list stations_over as any (valid data) station where the recent relative level is over 0.8
    print("The stations currently above the tolerance are:")
    for i in range(len(stations_over)):
        print((stations_over[i][0]).name, (stations_over[i][0].relative_water_level()))#prints the station name and relative water level

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()