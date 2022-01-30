# Lewis Clark Jan 2022
# Task 1F

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    inconsistent_stations.sort()
    print("The stations with inconsistent typical range data are: {}".format(inconsistent_stations))
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
