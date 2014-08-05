'''
Point Class
Author: Riley Lundquist
Creation Date: January 31, 2013
    Last Modified: January 31, 2013

Stores the x- and y-coordinates of a point.

The Point class stores the coordinates of a Cartesian
point as a pair. It contains methods which indicate whether
points and lines (represented as lists of points) are
(counter)clockwise from one another. 

@author: Riley Lundquist
'''

class Point:
    ''' The constructor for a point.
    @param xCoord: the x-coordinate of the point
    @param yCoord: the y-coordinate of the point '''
    def __init__(self, xCoord, yCoord):
        self.x = xCoord
        self.y = yCoord

    ''' The clockwise method indicates the relation of the point
    to another point.
    @param point2: the point with which this point is being compared
    @return: True if this point is clockwise from point2, False otherwise '''
    def clockwise(self, point2):
        cross = float(self.x)*float(point2.y) - float(point2.x)*float(self.y)
        #If cross is positive, this point is clockwise from point2.
        return cross > 0 

    ''' The clockwiseTurn method indicates the turn one line makes to another.
    @param point2: the point shared between the two lines
    @param point3: the end point of the second line segment
    @return: True if the line from this point to point2 makes a clockwise turn at
    point2 to the line from point2 to point3, False otherwise '''
    def clockwiseTurn(self, point2, point3):
        cross = (float(point3.x)-float(self.x))*(float(point2.y)-float(self.y)) - (float(point2.x)-float(self.x))*(float(point3.y)-float(self.y))
        #If cross is positive, the segments self-point2 and point2-point3 make a clockwise turn at point2
        return cross > 0

''' The getX method returns the y-coordinate of the point.
@param point: the desired point
@return: the x-coordinate '''
def getX(point):
    return float(point.x)
    
''' The getY method returns the y-coordinate of the point.
@param point: the desired point
@return: the y-coordinate '''
def getY(point):
    return float(point.y)