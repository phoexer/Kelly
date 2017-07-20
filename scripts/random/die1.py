# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:29:23 2017

@author: michael

Roll a die 1000 times and draw a histogram 
"""

#import numpy as np
import matplotlib.pyplot as plt
import random

#out = random.choice(range(1,7))
rolls = [random.choice(range(1,7)) for i in range(1000)]

plt.hist(rolls, bins = np.linspace(0.5,6.5, 7));