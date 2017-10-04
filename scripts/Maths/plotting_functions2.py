# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:40:35 2017

@author: michael

Simple script that draws the graph of a function
I was figuring this out as I went along, just to see if I can do it.

"""

import matplotlib.pyplot as plt
import numpy as np
import math

def someFunc(x):
    """y = |x| """
    if x != 3 and x != -2:
        return (x+3)/(x**2 -x -6)
    #return (16-2*x)*(30-2*x)*x
    #if x<=1:
    #    return .5*x -3
    #else:
    #    return 4*x+3
    #return x/ (x**2+4)
    #return (x+3)/(x**2 - x -6)   
    #if x <= 2: 
    #    return math.sqrt(4 - x**2)
    
x = np.arange(-5, 5, .25) 

y = [someFunc(y) for y in x  ]


#
##T = np.matrix(t)
##plt.figure(figsize=(100,100))
#plt.xlim((-6,6))
#plt.ylim((-10,10))
#plt.plot(x, y,'r-.')
#plt.grid(True)
#
#
#
#plt.show()