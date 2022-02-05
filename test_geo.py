#Max B Feb  2022

#Testing for the geo sub module

from sklearn.utils import assert_all_finite
from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
from floodsystem.station import MonitoringStation


stations = build_station_list()

#We again need a test object
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

def test_stations_by_distance():
    assert len(geo.stations_by_distance(stations, (0, 0))) >0
    assert round(geo.stations_by_distance(sacrificial_offering, (0,0)) [0][2]) == 16

def test_rivers_with_staiton():
    assert len(geo.rivers_with_station(stations)) >0
    assert geo.rivers_with_station(sacrificial_offering) == ['river_offering']

def test_stations_by_river():
    assert len(geo.stations_by_river(stations)) >  0
    assert len(geo.stations_by_river(stations)["River Thames"]) > 10
    assert geo.stations_by_river(sacrificial_offering) == {"river_offering": ["sacrificial_offering_1", "sacrificial_offering_2"]}

def test_stations_within_radius():
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1282), 0)) == 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1282), 10)) > 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1282), 500)) > len(geo.stations_within_radius(stations, (52.2053, 0.1282), 2))

def test_rivers_by_station_number():
    sacrifice_list  = geo.rivers_by_station_number(stations, 10)
    assert sacrifice_list[0][1] >= sacrifice_list[1][1]
    assert sacrifice_list [0][0] == "River Thames"
    