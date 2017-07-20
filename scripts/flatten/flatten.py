# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:14:21 2017

@author: phoexer

This is my answer to the question 
"Write some code, that will flatten an array of arbitrarily nested 
arrays of integers into a flat array of integers. 
e.g. [[1,2,[3]],4] -> [1,2,3,4]. "

"""
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

l = [[1,2,[3]],4]


def flatten(a):
    """Recursively flattens a list of arbitrarily nested lists of integers
        into a flat list of integers. 
        e.g. [[1,2,[3]],4] -> [1,2,3,4]."""
    try:
        if(iter(a)):
            logging.debug("Flattening:\t" + str(a))
            ar = []
            for i in a:
                ar += flatten(i)
            return ar
    except TypeError:
        logging.error(str(a) + " is not iterable.")
        return [a]

flatList = flatten(l)
logging.debug('flat list:\t' + str(flatList))