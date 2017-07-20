# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:57:07 2017

@author: michael
the faster way of doing a million rolls
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.clock()

rolls = np.random.randint(1,7,1000000)

print(rolls)
plt.hist(rolls)

end_time = time.clock()

print("Time Taken")
print(end_time - start_time)