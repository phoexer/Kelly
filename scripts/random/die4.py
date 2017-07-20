# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:32:22 2017

@author: michael

"""

import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.clock()
T = (1000000,10)

X = np.random.randint(1,7,T)

#Get sums of each of the ten rolls 
Y = np.sum(X, axis=1)

print(X)
print(Y)

#plt.hist(Y)

end_time = time.clock()

print("Time Taken")
print(end_time - start_time)