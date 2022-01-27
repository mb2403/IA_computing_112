#LC Jan/Feb 2022
#Maybe try to implement using a pandas dataframe and stations?


from turtle import pd
import pandas as pd
import plotly.express as px 


import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

#def generate_map(stations, colour = "yellow", tol=0, ):
def run(): 
    stations = build_station_list()
    update_water_levels(stations)

    
    station_names = []
    locations = []
    relative_levels = []
    lats=[]
    longs = []
    towns = []

    for item in stations:
        station_names.append(item.name)
        locations.append(item.coord)
        relative_levels.append(item.relative_water_level())
        towns.append(item.town)


    for item in locations:
        lats.append(item[0])
        longs.append(item[1])

    d = {'Station Name': station_names, 'Latitude' : lats, 'Longitude' : longs, 'Relative Level': relative_levels, 'Town': towns }
    stations_data_frame = pd.DataFrame(data=d)

    fig = px.scatter_mapbox(stations_data_frame, lat = 'Latitude', lon = 'Longitude', hover_name = 'Station Name', hover_data = ['Relative Level', 'Town'], color_discrete_sequence=["black"],)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()


if __name__ == "__main__":
    print("*** Generating Map...***")
    run()