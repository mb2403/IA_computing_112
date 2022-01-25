# Lewis Clark Jan 2022
# Task 1F

from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    inconsistent_stations.sort()
    print(inconsistent_stations)
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
