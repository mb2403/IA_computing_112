
from floodsystem.analysis import issue_warnings
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    towns_and_risks = issue_warnings(stations)
    #print(towns_and_risks)
    towns_and_risks2 = sorted(towns_and_risks.items(), key = lambda x: x[1], reverse=True)
    for item in towns_and_risks2:
        print("Town: {} Risk level: {}".format(item[0],item[1]))

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()