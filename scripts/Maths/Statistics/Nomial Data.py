# -*- coding: utf-8 -*-
"""
    Working with nominal data, I first cleaned it a little in sublinme, just to put it all in one line
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw = [2, 8, 4, 5, 1, 1, 5, 1, 5, 8, 5, 1, 5, 4, 2, 2, 2, 1, 1, 5, 1, 5, 5, 1, 1, 5, 1, 1, 1, 2, 1, 7, 1, 5, 1, 7, 1, 1, 1, 2, 7, 1, 1, 5, 5, 8, 8, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 2, 5, 2, 5, 1, 1, 1, 7, 1, 1, 7, 4, 1, 4, 1, 5, 8, 1, 1, 1, 7, 6, 6, 5, 1, 2, 1, 1, 1, 1, 5, 7, 1, 1, 1, 7, 1, 1, 1, 7, 1, 2, 7, 1, 4, 7, 7, 1, 7, 1, 1, 5, 1, 7, 1, 6, 4, 1, 1, 5, 1, 7, 1, 5, 2, 5, 5, 1, 1, 5, 1, 4, 5, 1, 1, 1, 1, 6, 2, 1, 5, 2, 1, 2, 1, 2, 1, 5, 2, 1, 1]

labels = {
            1: "Working full-time",
            2: "Working part-time",
            3: "Temporarily not working",
            4: "Unemployed, laid off",
            5: "Retired",
            6: "School",
            7: "Keeping house",
            8: "Other",        
        }

d = {}

for i in range(1,9):
    d[str(i)] = 0

for i in raw:
    try:
        d[str(i)] = d[str(i)] + 1
    except:
        d[str(i)] = 1
    
plt.pie(d.values(), labels=labels.values())
plt.legend()
plt.show()
