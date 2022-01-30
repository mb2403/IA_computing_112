# Max  Bowler Jan 2022
# Task 2C
#

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    risk_station = stations_highest_rel_level(stations, 10)
    print("The stations posing the highest risk are:")
    for i in range(len(risk_station)):
        print((risk_station[i][0]).name, (risk_station[i][0].relative_water_level()))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()