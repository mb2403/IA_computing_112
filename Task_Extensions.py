#LC and MB 2022

from floodsystem.generate_map import generate_layer_map, generate_bubble_map
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    generate_layer_map(stations)  
    #generate_bubble_map(stations)            
    
if __name__ == "__main__":
    print("***Extensions: CUED Part IA Flood Warning System ***")
    run()