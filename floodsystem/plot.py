# Lewis Clark and Max Bowler Jan/Feb 2022

from floodsystem.analysis import polyfit
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, datetime, timedelta

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels, label=station.name)
    plt.xlabel("date")
    plt.ylabel("Water level(m)")
    plt.xticks(rotation=45)
    plt.title("Water level data readings taken from", station)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station,dates,levels,p):                          #LC Task 2F
    poly, d0 = polyfit(dates,levels,p)                                          #generates polynomial
    dates = matplotlib.dates.date2num(dates)                                    #converts dates into usable form
    dates = dates - d0                                                          #shifts dates
    x1 = np.linspace(dates[0],dates[-1],30)
    
    plt.plot(dates, levels, '.')
    plt.plot(x1, poly(x1),"-m", label = "Fitted polynomial")
    plt.plot(x1, np.linspace(station.typical_range[0],station.typical_range[0],30),"-r", label="Typical Max/Min")
    plt.plot(x1, np.linspace(station.typical_range[1],station.typical_range[1],30),"-r")
    
    plt.xlabel("Number of Days ago")
    plt.ylabel("Water level")
    plt.title("Water level for last {} days for {}".format(round(abs(dates[-1]),1),station.name))
    plt.legend(loc="lower right")

    plt.grid(which = 'major', alpha = 0.1)

    plt.show()
