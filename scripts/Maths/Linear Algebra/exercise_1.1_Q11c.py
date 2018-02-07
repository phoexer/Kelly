# -*- coding: utf-8 -*-
"""
    Graph of the system 
    x - 2y = 0
    x - 4y = 8
    
    I calculated solution as (-8,-4)
    
    graph agrees
"""
#%reset -f

import matplotlib.pyplot as plt

def get_x_i(y):
    """
        Returns x -2y = 0 solved for x
        i.e. x = 2y
    """
    return 2*y

def get_x_ii(y):
    """
        returns x -4y = 8 solved x
        i.e. x = 8 + 4y
    """
    return 8 + 4*y

y_i = range(-10,11)
y_ii = range(-10,11)

x_i = [get_x_i(y) for y in y_i]
x_ii = [get_x_ii(y) for y in y_ii]    
    
plt.plot(x_i,y_i,color="blue",label="x - 2y = 0")
plt.plot(x_ii,y_ii,color="red", label="x - 4y = 8")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, which='both')
plt.title("Graph of x - 2y = 0 and x - 4y = 8")

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()