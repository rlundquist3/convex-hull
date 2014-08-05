'''
Convex Hull Class
Author: Riley Lundquist
Creation Date: January 31, 2013
    Last Modified: February 13, 2013

A solution to the Convex Hull Problem.

The Convex Hull class finds the convex hull of 
a given set of points using a divide and conquer
algorithm. 

@author: Riley Lundquist
'''
from Point import *
from Hull import *

''' The findHull method finds the convex hull of a list of points. It
splits the set in half, then calls itself on these halves. The base case
is a list of size 3 or less.
@param arr: the list for which the convex hull is desired
@return: the set of points which makes up the convex hull '''
def findHull(arr):
    #Handles base cases
    if len(arr) <= 3:
        ccw = []
        if len(arr) == 1:
            ccw.append(arr[0])
        elif len(arr) == 2:
            if arr[0].clockwise(arr[1]) == 1:
                ccw.append(arr[0]); ccw.append(arr[1])
            else:
                ccw.append(arr[1]); ccw.append(arr[0])
        else:
            if arr[0].clockwiseTurn(arr[1], arr[2]) == 1:
                ccw.append(arr[0]); ccw.append(arr[2]); ccw.append(arr[1])
            else:
                ccw.append(arr[0]); ccw.append(arr[1]); ccw.append(arr[2])
        return Hull(ccw)
    #Splits into sub-hulls
    mid = len(arr)//2
    left = findHull(arr[0:mid])
    right = findHull(arr[mid:len(arr)])
    return mergeHulls(left, right)

''' The mergeHulls method merges two sub-hulls together into one convex
hull. It finds the upper and lower tangent lines, then removes points no
longer in the hull and combines the halves. 
@param left: the left sub-hull
@param right: the right sub-hull
@return: the merged hull '''
def mergeHulls(left, right):
    '''Prevents the case where points in a hull are in the same vertical
    line from causing an infinite loop.'''
    if len(left) == 2 and vertical(left):
        leftIndex = left.index(max(left, key=getY))
        rightIndex = right.index(leftmost(right))
        topLine = [leftIndex, rightIndex]
        while not upperTangentRight(left[leftIndex], right, rightIndex):
            if rightIndex == 0:
                rightIndex = len(right)-1
            else:
                rightIndex -= 1
            topLine = [leftIndex, rightIndex]
        leftIndex = left.index(min(left, key=getY))
        rightIndex = right.index(leftmost(right))
        bottomLine = [leftIndex, rightIndex]
        while not lowerTangentRight(left[leftIndex], right, rightIndex):
            if rightIndex == len(right)-1:
                rightIndex = 0
            else:
                rightIndex += 1
            bottomLine = [leftIndex, rightIndex]
        rightStart = right[rightIndex]
    elif len(right) == 2 and vertical(right):
        leftIndex = left.index(rightmost(left))
        rightIndex = right.index(max(right, key=getY))
        topLine = [leftIndex, rightIndex]
        while not upperTangentLeft(right[rightIndex], left, leftIndex):
            if leftIndex == len(left)-1:
                leftIndex = 0
            else:
                leftIndex += 1
            topLine = [leftIndex, rightIndex]
        while not lowerTangentLeft(right[rightIndex], left, leftIndex):
            if leftIndex == 0:
                leftIndex = len(left)-1
            else:
                leftIndex -= 1
            bottomLine = [leftIndex, rightIndex]
        rightStart = right[rightIndex]
            
    else:
        #Finds the line upper tangent to both sub-hulls
        leftIndex = left.index(rightmost(left))
        rightIndex = right.index(leftmost(right))
        topLine = [leftIndex, rightIndex]
        while not upperTangentLeft(right[rightIndex], left, leftIndex) or not upperTangentRight(left[leftIndex], right, rightIndex):
            while not upperTangentLeft(right[rightIndex], left, leftIndex):
                if leftIndex == len(left)-1:
                    leftIndex = 0
                else:
                    leftIndex += 1
                topLine = [leftIndex, rightIndex]
            while not upperTangentRight(left[leftIndex], right, rightIndex):
                if rightIndex == 0:
                    rightIndex = len(right)-1
                else:
                    rightIndex -= 1
                topLine = [leftIndex, rightIndex]
        
        #Finds the line lower tangent to both sub-hulls
        leftIndex = left.index(rightmost(left))
        rightIndex = right.index(leftmost(right))
        bottomLine = [leftIndex, rightIndex]
        while not lowerTangentLeft(right[rightIndex], left, leftIndex) or not lowerTangentRight(left[leftIndex], right, rightIndex):
            while not lowerTangentLeft(right[rightIndex], left, leftIndex):
                if leftIndex == 0:
                    leftIndex = len(left)-1
                else:
                    leftIndex -= 1
                bottomLine = [leftIndex, rightIndex]
            while not lowerTangentRight(left[leftIndex], right, rightIndex):
                if rightIndex == len(right)-1:
                    rightIndex = 0
                else:
                    rightIndex += 1
                bottomLine = [leftIndex, rightIndex]
        rightStart = right[rightIndex]
    
    #Removes points no longer in hull
    left.removeSlice(bottomLine[0]+1, topLine[0])
    right.removeSlice(topLine[1]+1, bottomLine[1])
    
    #Puts the hull together
    index = bottomLine[0]+1
    start = right.index(rightStart)
    size = len(left)+len(right)
    while len(left) < size:
        left.insert(index, right[start])
        index += 1
        start += 1
    return left

''' Determines if a hull of size two is two points in a vertical line.
@param hull: the hull being checked
@return: true if the points are in a vertical line, false otherwise. 
'''
def vertical(hull):
    return hull[0].x == hull[1].x
    
''' The rightmost method finds the rightmost point in a hull.
@param hull: the hull for which the rightmost is to be found
@return: the rightmost point '''
def rightmost(hull):
    return max(hull, key=getX)

''' The leftmost method finds the leftmost point in a hull.
@param hull: the hull for which the leftmost is to be found
@return: the leftmost point '''
def leftmost(hull):                                             
    return min(hull, key=getX)
  
''' The upperTangentLeft method tests if a line is upper tangent to the left sub-hull.
@param rightPoint: the end point of the line in the right sub-hull
@param left: the left sub-hull
@param leftIndex: the index of the end point of the line in the left sub-hull
@return: True if the line is upper tangent to the left sub-hull, False otherwise '''
def upperTangentLeft(rightPoint, left, leftIndex):
    return not rightPoint.clockwiseTurn(left[leftIndex], left[leftIndex-1]) and not rightPoint.clockwiseTurn(left[leftIndex], left[leftIndex+1])

''' The upperTangentRight method tests if a line is upper tangent to the right sub-hull.
@param leftPoint: the end point of the line in the left sub-hull
@param right: the right sub-hull
@param rightIndex: the index of the end point of the line in the right sub-hull
@return: True if the line is upper tangent to the right sub-hull, False otherwise '''
def upperTangentRight(leftPoint, right, rightIndex):
    return leftPoint.clockwiseTurn(right[rightIndex], right[rightIndex+1]) and leftPoint.clockwiseTurn(right[rightIndex], right[rightIndex-1])

''' The lowerTangentLeft method tests if a line is lower tangent to the left sub-hull.
@param rightPoint: the end point of the line in the right sub-hull
@param left: the left sub-hull
@param leftIndex: the index of the end point of the line in the left sub-hull
@return: True if the line is lower tangent to the left sub-hull, False otherwise '''
def lowerTangentLeft(rightPoint, left, leftIndex):
    return rightPoint.clockwiseTurn(left[leftIndex], left[leftIndex-1]) and rightPoint.clockwiseTurn(left[leftIndex], left[leftIndex+1])

''' The lowerTangentRight method tests if a line is lower tangent to the right sub-hull.
@param leftPoint: the end point of the line in the left sub-hull
@param right: the right sub-hull
@param rightIndex: the index of the end point of the line in the right sub-hull
@return: True if the line is lower tangent to the right sub-hull, False otherwise '''
def lowerTangentRight(leftPoint, right, rightIndex):
    return not leftPoint.clockwiseTurn(right[rightIndex], right[rightIndex+1]) and not leftPoint.clockwiseTurn(right[rightIndex], right[rightIndex-1])

''' The data input and sorting are done here. Then the method 
for finding the hull is called.'''
#Opens the data file containing the points, stores coordinates as
#a list of Point objects
name = raw_input('Enter name of file containing data set (e.g. test.txt, or points.dat):\n')
dataFile = open(name)
data = dataFile.read().split()
points = []
index = 0
while index < len(data):
    points.append(Point(data[index], data[index+1]))
    index += 2 

#Sorts the list of Point objects by their x-coordinates
#Python's list sort method is a modified mergesort: O(n*lg(n))
points.sort(key = lambda point: float(point.x))

#Finds and prints the convex hull for the set of points
for p in findHull(points):
    print (float(p.x), float(p.y))

