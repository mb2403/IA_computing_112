# Max Bowler jan 2022
# Task 1C
#

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    list_within_radius = stations_within_radius(stations, (52.2053,0.1218), 10)
    print(list_within_radius)

if __name__ == "__main__":
    print("*** Task1C: CUED Part IA Flood  Warning System ***")
    run()