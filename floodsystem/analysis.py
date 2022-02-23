# Lewis Clark Jan/Feb 2022

import numpy as np
from numpy import linalg as LA
import matplotlib
import matplotlib.dates
import datetime
from alive_progress import alive_bar

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import inconsistent_typical_range_stations 

def polyfit(dates,levels,p):                                    #LC Task 2F
    x = matplotlib.dates.date2num(dates)                        #converts into days since the year 0001
    d0 = x[0]                                                   #shift of graph
    x = x - d0                                      
    y = levels

    try:
        p_coeff = np.polyfit(x,y,p)  
        poly = np.poly1d(p_coeff)                                   #converts to the right form for numpy to use
        return poly, d0                                #coefficients of polynomial of order p
    except(LA):
        return np.poly1d(0), d0                                     #returns the polynomial expression and shift

def issue_warnings(stations, p=4, dt=1):
    
    def risk_definition(risk):                                  #define the boundaries for risks 
        boundaries = (0, 0.8, 1.5, 2)                           #these can be changed based on results
        if risk == None:
            return "unknown"
        if risk < boundaries[1]:
            return "low"
        if risk < boundaries[2]:
            return "moderate"
        if risk < boundaries[3]:
            return "high"
        else:
            return "severe"

    stations_by_risk = []
    risk_of_towns = {}
    first_deriv_weight, second_deriv_weight = (5, 0.1)                      #weighting of the derivatives, can be changed 
    count = 0 

    inconsistent_stations = inconsistent_typical_range_stations(stations)
    unsafe_stations_name = stations_level_over_threshold(stations, 0.8)     #0.8 can be changed as desired
    unsafe_stations = [station for station in stations for name, level in unsafe_stations_name if station.name == name]
    with alive_bar(len(stations)) as bar:
        for station in stations:
            if station in inconsistent_stations:
                pass
            if not station.latest_level_consistent():
                inconsistent_stations.append(station)                           #gets rid of inconsistent stations
            if station not in unsafe_stations:
                stations_by_risk.append((station, station.relative_water_level(), risk_definition(station.relative_water_level())))

            try:
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))       #fetched plotting data
            except (KeyError):
                inconsistent_stations.append(station)

            try:
                levels = np.array(levels)
                levels = (levels - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])
            except (TypeError, ValueError):                                     #makes sure bad data doenst break the program
                inconsistent_stations.append(station)

            try:
                poly, d0 = polyfit(dates,levels,p)
            
            except (IndexError, ValueError, TypeError):
                inconsistent_stations.append(station)

            first_deriv = poly.deriv()
            second_deriv = poly.deriv(2)
            risk_value = poly(0)
            risk_value += first_deriv(0) * first_deriv_weight
            risk_value += second_deriv(0) * second_deriv_weight             #

            if (risk_value is None) or (station.relative_water_level() is None):
                inconsistent_stations.append(station)
            elif risk_value < station.relative_water_level():
                risk_value = station.relative_water_level()
        

            stations_by_risk.append((station, risk_value, risk_definition(risk_value)))

            if (station.town not in risk_of_towns.keys()) or (risk_value > risk_of_towns[station.town]):
                risk_of_towns[station.town] = risk_value
            else:
                stations_by_risk.append((station, 0, risk_definition(0)))

            count = count + 1
            bar()
            #if count > 100:
            #    break

        return risk_of_towns