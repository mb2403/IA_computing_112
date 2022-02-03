# Max Bowler Jan 2022
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
import matplotlib.pyplot as  plot

def run():
    stations = build_station_list()
    N = 5 
    names_high_rel = stations_highest_rel_level(stations, N)

    data_list = []
    for station in stations:
        for i in range(len(names_high_rel)):
            if station.name == names_high_rel[i][0]:
                data_list.append(station)
        

    dt = 10
    dates = np.empty(N, dtype=object)
    levels = [None, None, None, None, None, None, None, None, None, None]
    for i in range(len(data_list)):
        dates[i], levels[i] = fetch_measure_levels(data_list[i].measure_id, dt = datetime.timedelta(days = dt))

        plot_water_levels(data_list[i], dates[i], levels[i])
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()