# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


#from types import NoneType
#from sqlalchemy import Float, true


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):                                 # LC Task 1F
        if self.typical_range == None:                                  # typical range none
            return False
        elif self.typical_range[0] > self.typical_range[1]:             # lower bound of range higher than upper bound
            return False
        else:
            return True

    def relative_water_level(self):                                     # LC Task 2B
        if (self.typical_range_consistent() == False) or (self.latest_level == None):
            return None                                                 # returns none if typical values are not consistent, or if data for latest level is not available
        else:                                                           # returns the relative water level using formula (level - typical min)/(typical max - typical min)
            return ((self.latest_level)-(self.typical_range[0]))/((self.typical_range[1])-(self.typical_range[0]))

    def latest_level_consistent(self):                                  #LC Task 2G
        if self.latest_level is None:
            return False

        if not isinstance(self.latest_level, float):
            return False  
            
        else:
            return True
            
            
def inconsistent_typical_range_stations(stations):                      # LC Task 1F
    incon_list=[]
    for item in stations:
        if item.typical_range_consistent() == False:
            incon_list.append(item.name)
    return (incon_list)