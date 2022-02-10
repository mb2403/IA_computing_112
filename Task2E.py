# Max Bowler/Lewis Clark Jan/Feb 2022
# Task 2E
#
#%%
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import numpy as np
import matplotlib.pyplot as  plt

def run():

    stations = build_station_list()
    update_water_levels(stations)    

    highest_relative_level_stations = stations_highest_rel_level(stations, 6)          #chooses the 5 stations with the highest relative level

    for item in highest_relative_level_stations:                
        station = item[0]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))  #fetches dates and levels using datafectcher
        #print (levels) 
        #print (dates)                                                                           #make sure that it prints exactly 5!!
        plot_water_levels(station, dates, levels)
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()