# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:03:16 2017

@author: michael
"""
import math

def findDistance(p1,p2):
    """Finds the distance between two points on the Cartesian Plane
    the arguemensts are two tuples, each representing a point"""
    #unplack tuples
    x1,y1 = p1
    x2,y2 = p2
    
    #distance is squareroot of (x2-x1)^2 + (y2-y1)^2
    return math.sqrt( (x2-x1)**2 + (y2-y1)**2 ) 

a = (1, 2)
b = (3, 4)
c = (2, 6)

print("Distance from a to b", findDistance(a,b))
print("Distance from a to c", findDistance(a,c))
print("Distance from b to c", findDistance(b,c))