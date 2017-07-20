# -*- coding: utf-8 -*-
"""
@author: michael
Learning functions. 
"""


import random
import math

def intersect(s1,s2):
    res = []
    for s in s1:
        if s in s2:
            res.append(s)
    return res

print(intersect([1,2,3], [3,4,5,6,7]))

def password(length):
    select_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([random.choice(select_text) for i in range(length)])

print(password(16))

def is_vowel(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in "aeiouy":
        return(True)
    else:
        return(False) 

print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel(4))



def factorial(n):
    if n == 0:
        return 1
    else:
        N = 1
        for i in range(1, n+1):
            N *= i #blank#
        return(N) 

print(math.factorial(15))
print(factorial(15))
