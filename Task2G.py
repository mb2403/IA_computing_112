
from floodsystem.analysis import issue_warnings
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

def run():
    stations = build_station_list()
    update_water_levels(stations)

    towns_and_risks = issue_warnings(stations)

    towns_and_risks = sorted_by_key(towns_and_risks,1)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()