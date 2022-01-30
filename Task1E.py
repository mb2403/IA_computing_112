# Max Bowler jan 2022
# Task 1E
#

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    list_rivers_by_number = rivers_by_station_number(stations, 9)
    print(list_rivers_by_number)

if __name__ == "__main__":
    print("*** Task1E: CUED Part IA Flood  Warning System ***")
    run()