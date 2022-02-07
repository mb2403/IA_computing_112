#  TEST for  flood submodule
#Max B/LC Feb 2022
#Testing subroutines in the "Flood" submodule

from cgi import test
from  floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood


stations = build_station_list()
update_water_levels(stations)
#Need to create  an object to test as an input

sacrificial_offering = [MonitoringStation(
                station_id=1,
                measure_id=10,
                label='sacrificial_offering_1',
                coord=(float(0.1), float(0.1)),
                typical_range= (1.2, 1.5),
                river='river_offering',
                town='town_offering'),
                MonitoringStation(
                station_id=2,
                measure_id=20,
                label='sacrificial_offering_2',
                coord=(float(50), float(0)),
                typical_range= (15, 2),
                river='river_offering',
                town='town_offering')]


def test_stations_highest_rel_level():
    sacrificial_offering[0].latest_level = 1.4
    sacrificial_offering[1].latest_level = 255
    correct_output = [(sacrificial_offering[0])]
    assert flood.stations_highest_rel_level(sacrificial_offering,  1) == correct_output
    
