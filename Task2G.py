
from floodsystem.analysis import issue_warnings
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    print(issue_warnings(stations))

    #stations_by_risk = issue_warnings(stations)

    #for station, riskv, risk in stations_by_risk:
    #    if risk == "severe" or risk == "high":
    #        print((s.name, riskv, risk), "\n")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()