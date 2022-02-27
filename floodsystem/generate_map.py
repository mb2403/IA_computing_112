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

from floodsystem.stationdata import update_water_levels 

def generate_layer_map(stations, tol=0, colour = "black"):
    update_water_levels(stations)
    station_names = []
    locations = []
    relative_levels = []
    lats = []
    longs = []
    towns = []
    count = 0


    for station in stations:
        if station.relative_water_level() == None:
            stations.pop(count)
        elif (station.relative_water_level() > 5):
            stations.pop(count)
        elif (station.relative_water_level() < 0):
            stations.pop(count)
        count = count + 1
                
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

    fig = px.scatter_mapbox(stations_data_frame, lat = 'Latitude', lon = 'Longitude', hover_name = 'Station Name', hover_data = ['Relative Level', 'Town'], color = "Relative Level", color_continuous_scale=px.colors.sequential.Bluered, range_color = (0,3))
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(mapbox_style = "open-street-map")
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