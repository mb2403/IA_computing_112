# Lewis Clark Jan 2022
# Task 2B
#

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    for item in stations:
        print(item.relative_water_level())

    stations_over = stations_level_over_threshold(stations,0.8)
    for i in range(len(stations_over)):
        print(stations_over[i])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()