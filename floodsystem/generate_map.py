#LC Jan/Feb 2022
# This module is part of the extensions to the project. Its purpose is to create a map of stations and relative water levels.
# This module is WIP

# Suggestions LC:

# Maybe try to implement importing directly to a pandas dataframe and stations?
# Maybe try to implement using a 'bubble map' with sliders for last x days
# Maybe try and change colour depending on flood risk - could wait for 2G to be done to do this
# Option to not view stations which have invalid ranges
# Option to not view stations with a relative water level below the tolerance

from turtle import pd
from numpy import integer
import pandas as pd
import plotly.express as px 

from floodsystem.flood import stations_level_over_threshold

def generate_layer_map(stations, tol=0, colour = "black"):

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

    fig = px.scatter_mapbox(stations_data_frame, lat = 'Latitude', lon = 'Longitude', hover_name = 'Station Name', hover_data = ['Relative Level', 'Town'], color_discrete_sequence=[colour],)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

def generate_bubble_map(stations, tol=0, colour = "black"):
    station_names = []
    locations = []
    relative_levels = []
    lats=[]
    longs = []
    towns = []


    for item in stations:
        if type(relative_levels) != integer:
            pass
        elif item.relative_water_level() < 0:
            pass
        else: 
            station_names.append(item.name)
            locations.append(item.coord)
            relative_levels.append(item.relative_water_level())
            towns.append(item.town)

    for item in locations:
        lats.append(item[0])
        longs.append(item[1])

    d = {'Station Name': station_names, 'Latitude' : lats, 'Longitude' : longs, 'Relative Level': relative_levels, 'Town': towns }
    stations_data_frame = pd.DataFrame(data=d)

    fig = px.scatter_geo(stations_data_frame, lat = 'Latitude', lon = 'Longitude', locationmode = 'UK', hover_name = 'Station Name', size = 'Relative Level', hover_data = ['Relative Level', 'Town'], color_discrete_sequence=[colour],)
    fig.show()