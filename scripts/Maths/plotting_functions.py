a# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:40:35 2017

@author: michael

Simple script that draws the graph of a function
I was figuring this out as I went along, just to see if I can do it.

"""

import matplotlib.pyplot as plt
import numpy as np
import math

#Constants
a = 1
b = 8
c = 5#10
d = 6
#plt.plot([2,4,6,8],[1,2,3,4],'ro')
#plt.ylabel('Some Numbers')

def sinFunc(x):
    """f(x) = sin(x)"""
    return math.sin(x) 

def quadraticFunc(x):
    """y = ax^2 + bx + c,"""
    return a*x**2 + b*x + c

def powerFunc(x):
    """y = ax^c"""
    return a*x**c

def polinomialFunc(x):
    """y = x^5 -8x^3 +10x + 6"""
    return a*x**5 - b*x**3 + c*x + d

def someFunc(x):
    """y = 1/x"""
    return 1/x

x = np.arange(-3., 3., .2) 

sy = [someFunc(y) for y in x]
qy = [quadraticFunc(y) for y in x]
py = [powerFunc(y) for y in x]
ply = [polinomialFunc(y) for y in x]

#T = np.matrix(t)

plt.subplot(2,2,1)
plt.plot(x, sy,'r-.')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(x,qy,'b-.')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(x,py,'g-.')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(x,ply,'y-.')
plt.grid(True)

plt.show()