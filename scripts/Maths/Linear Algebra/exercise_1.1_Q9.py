# -*- coding: utf-8 -*-

def check_tuple(values):
    x1,x2,x3 = values
    try:
        assert (2*x1 - 4*x2 -x3) == 1
        assert (x1 - 3 * x2 + x3) == 1
        assert (3*x1 - 5*x2 - 3*x3) == 1
    except:    
        return False
    return True        



a = (3,1,1,)
b = (3,-1,1)
c = (13,5,2)
d = (13/2,5/2,2)
e = (17,7,5)

print(check_tuple(a))
print(check_tuple(b))
print(check_tuple(c))
print(check_tuple(d))
print(check_tuple(e))