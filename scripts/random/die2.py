# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:29:23 2017

@author: michael

how long would it table to roll a million times? 
Around 15 seconds on my machine.
There should be a faster way of doing this, I'll look into that.
"""

#import numpy as np
import matplotlib.pyplot as plt
import random
import time

start_time = time.clock()
#out = random.choice(range(1,7))

def roll_dice():
    return random.choice(range(1,7))


rolls = [sum([roll_dice() for i in range(10)]) for k in range(1000000)]

plt.hist(rolls);#, bins = np.linspace(5,65, 11));

end_time = time.clock()

print("Time Taken")
print(end_time - start_time)