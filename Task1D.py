# Lewis Clark Jan 2022
# Task 1D
#

from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)
    rivers_list = (list(rivers_set))
    rivers_list.sort()

    print("{0} stations. First 10 - {1}".format(len(rivers_list),rivers_list[:10])) #prints the number of stations as well as the first and last 10 alphabetically
    
    aire = (stations_by_river(stations))["River Aire"]  #makes a list of all the stations with key: river name
    cam = (stations_by_river(stations))["River Cam"]
    thames = (stations_by_river(stations))["River Thames"]
    
    aire.sort()
    cam.sort()
    thames.sort()

    print("Stations along the river Aire - {}".format(aire))
    print("Stations along the River Cam - {}".format(cam))
    print("Stations along the River Thames - {}".format(thames))
    
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()



