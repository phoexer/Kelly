# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:44:35 2018

@author: michael
"""

def check_tuple(values):
    x,y,z = values
    try:
        assert (x + 2*y - 2*z) == 3
        assert (3*x - y + z) == 1
        assert (-x + 5*y - 5*z) == 5
    except:    
        return False
    return True        



a = (5/7,8/7,1)
b = (5/7,8/7,0)
c = (5,8,1)
d = (5/7,10/7,2/7)
e = (5/7,22/7,2)

print(check_tuple(a))
print(check_tuple(b))
print(check_tuple(c))
print(check_tuple(d))
print(check_tuple(e))