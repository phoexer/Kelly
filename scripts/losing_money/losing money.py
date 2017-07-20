# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:52:00 2017

@author: phoexer

"""

import random
import numpy as np

def press(value):
    if(random.random() < 0.99):
        return value * 2
    else:
        return 0
    
def run():
    i = 0
    value = 1
    while True:
        i += 1
        newValue = press(value)
        if(newValue == 0):
            break
        else:
            value = newValue
    return (i,value)
    
narr = np.matrix([run() for j in range(1,1000)])
#for k in range(1,11):
#    i, value = run()
#    print("\nIt took " + str(i) + " presses")
#    print("You lost: $" + str(value))


