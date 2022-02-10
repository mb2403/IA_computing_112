#  TEST for  flood submodule
#Max B/LC Feb 2022
#Testing subroutines in the "Flood" submodule

from cgi import test
from  floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


stations = build_station_list()
update_water_levels(stations)
#Need to create  an object to test as an input

sacrificial_offering_1 = MonitoringStation(
                station_id=1,
                measure_id=10,
                label='sacrificial_offering_1',
                coord=(float(0.1), float(0.1)),
                typical_range= (1.2, 1.5),
                river='river_offering',
                town='town_offering')

sacrificial_offering_2 = MonitoringStation(
                station_id=2,
                measure_id=20,
                label='sacrificial_offering_2',
                coord=(float(50), float(0)),
                typical_range= (15, 2),
                river='river_offering',
                town='town_offering')

sacrificial_offering = [sacrificial_offering_1, sacrificial_offering_2]

def test_stations_highest_rel_level():
    sacrificial_offering[0].latest_level = 1.4
    sacrificial_offering[1].latest_level = 255
    assert stations_highest_rel_level(sacrificial_offering, 1) == [(sacrificial_offering_1,0.6666666666666664)]
    
def test_stations_over_threshold():
    sacrificial_offering_1.latest_level = 10
    sacrificial_offering_2.latest_level = 10
    assert stations_level_over_threshold(sacrificial_offering, 0.8) == sacrificial_offering_1()
