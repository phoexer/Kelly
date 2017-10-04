P# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:54:37 2017

@author: michael
"""

import matplotlib.pyplot as plt


t = [0,0.5,1.,1.5,2.]
d = [0,4,16,36,64]

plt.plot(t,d,'b-.')
plt.xlabel("Time")
plt.ylabel("Distance")
plt.xlim(0,3)
plt.ylim(0,100)
plt.grid(True)
plt.show();