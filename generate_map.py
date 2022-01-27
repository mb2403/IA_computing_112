#LC Jan/Feb 2022
#Maybe try to implement using a pandas dataframe and stations?


from turtle import pd
import pandas as pd
import plotly.express as px 


import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)

    
    station_names = []
    locations = []
    relative_levels = []
    lats=[]
    longs = []
    print(stations[0])

    for item in stations:
        station_names.append(item.name)
        locations.append(item.coord)
        relative_levels.append(item.relative_water_level())

    for item in locations:
        lats.append(item[0])
        longs.append(item[1])

    d = {'Station Name': station_names, 'Latitude' : lats, 'Longitude' : longs, 'e': relative_levels }
    stations_data_frame = pd.DataFrame(data=d)
    print(stations_data_frame)

    fig = px.scatter_mapbox(stations_data_frame, lat = 'Latitude', lon = 'Longitude', hover_name = 'Station Name', hover_data = 'e')
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()


if __name__ == "__main__":
    print("*** Generating Map...***")
    run()