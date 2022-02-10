# Lewis Clark Jan 2022
# Task 2F
#

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)    

    highest_relative_level_stations = stations_highest_rel_level(stations, 6)          #chooses the 5 stations with the highest relative level

    for item in highest_relative_level_stations:                
        station = item[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2)) #fetches dates and levels using datafectcher
        plot_water_level_with_fit(station, dates, levels,4)                                     #plots using a polynomial of degree 4

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()