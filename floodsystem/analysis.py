# Lewis Clark Jan 2022

import numpy as np
import matplotlib

def polyfit(dates,levels,p):                                    #LC Task 2F
    x = matplotlib.dates.date2num(dates)                        #converts into days since the year 0001
    d0 = x[0]                                                   #shift of graph
    x = x - d0                                      
    y = levels

    p_coeff = np.polyfit(x,y,p)                                 #coefficients of polynomial of order p
    poly = np.poly1d(p_coeff)                                   #converts to the right form for numpy to use

    return poly, d0                                             #returns the polynomial expression and shift

def current_gradient(poly):
    der = np.poly1d.deriv(poly)
    return np.polyval(der,0)