'''
Hull Class
Author: Riley Lundquist
Creation Date: February 5, 2013
    Last Modified: February 8, 2013

The Hull class is based on a Circular List
implementation in Python by Chris Lawlor.

This class stores the points on a convex hull
in a circular list. This eliminates
indexing issues when traversing a hull to find 
upper and lower tangent lines and remove points.

@author: Riley Lundquist
'''
from Point import *
import math

class Hull(list):
    ''' The __getitem__ method of Python list is
    modified here to allow for circular indexing.
    Indices beyond the bounds of the array are handled
    with modulo arithmetic. Index __len__() returns 
    the element at index 0, __len__()+1 returns the 
    element at index 1, and so on. 
    @param key: the index of the desired element '''
    def __getitem__(self, key):
        try:
            return super(Hull, self).__getitem__(key)
        except IndexError:
            pass
        try:
            index = int(key)
            index = index % self.__len__()
            return super(Hull, self).__getitem__(index)
        except ValueError:
            raise TypeError
    
    ''' The removeSlice method is allows for the
    removal of "slices" (sections of a list) from the 
    hull (circular list).
    @param start: the starting index of the slice to be removed
    @param end: the end index of the slice to be removed (the
    element at this index is not removed) '''
    def removeSlice(self, start, end):
        start %= self.__len__()
        stopAt = self[end]
        stop = False
        if self[start] == stopAt:
            stop = True
        copy = Hull()
        for p in self:
            copy.append(p)
        while not stop:
            self.remove(copy[start])
            start += 1
            if copy[start] == stopAt:
                stop = True








