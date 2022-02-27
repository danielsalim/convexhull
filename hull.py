from asyncio.windows_events import NULL
import numpy as np
from cmath import sqrt

def isAboveLine(x1,y1,x2,y2,x3,y3):
    #is a point p(x3,y3) above line l(x2x1,y2y1)
    det = (x1*y2+x3*y1+x2*y3)-(x3*y2+x2*y1+x1*y3)
    if det > 0: 
        return "above"
    else:
        return "below"

def findFurthest(arr_points, lm, rm):
    x1, y1 = lm
    x2, y2 = rm
    a = y2 - y1
    b = x1 - x2
    c = (x2*y1) - (x1*y2)
    furthest_dist = -99
    furthest_point = None
    for points in arr_points:
        x3, y3 = points
        curr_dist = abs(a*x3 + b*y3 + c)/sqrt(a**2 + b**2)
        if curr_dist>furthest_dist:
            furthest_point = points
            furthest_dist = curr_dist
    return furthest_point

def divnconqHullabove(arr_points, lm, rm):
    if len(arr_points) == 0:
        return NULL
    else:
        furthest = findFurthest(arr_points, lm, rm)
        hullabove.append(furthest)

        above_left = []
        above_right = []
        x1,y1 = lm
        x2,y2 = rm
        x3,y3 = furthest
        for points in arr_points:
            x0,y0 = points
            if x0 != x3 and y0 != y3:
                to_check = isAboveLine(x1,y1,x3,y3,x0,y0)
                if to_check == "above":
                    above_left.append(points)
        for points in arr_points:
            x0,y0 = points
            if x0 != x3 and y0 != y3:
                to_check = isAboveLine(x3,y3,x2,y2,x0,y0)
                if to_check == "above":
                    above_right.append(points)
        
        divnconqHullabove(above_left, lm, furthest)
        divnconqHullabove(above_right, furthest, rm)
    
def divnconqHullbelow(arr_points, lm, rm):
    if len(arr_points) == 0:
        return NULL
    else:
        furthest = findFurthest(arr_points, rm, lm)
        hullbelow.append(furthest)

        below_left = []
        below_right = []
        x1,y1 = lm
        x2,y2 = rm
        x3,y3 = furthest
        for points in arr_points:
            x0,y0 = points
            if x0 != x3 and y0 != y3:
                to_check = isAboveLine(x1,y1,x3,y3,x0,y0)
                if to_check == "below":
                    below_left.append(points)
        for points in arr_points:
            x0,y0 = points
            if x0 != x3 and y0 != y3:
                to_check = isAboveLine(x3,y3,x2,y2,x0,y0)
                if to_check == "below":
                    below_right.append(points)
        
        divnconqHullbelow(below_left, lm, furthest)
        divnconqHullbelow(below_right, furthest, rm)

def myConvexHull(data):
    global hullSolution
    global hullabove
    global hullbelow
    hullSolution = []
    hullabove = []
    hullbelow = []
    data = np.array(sorted(data, key=lambda k: [k[0], k[1]]))
    lm = data[0]
    rm = data[-1]

    points_above = []
    points_below = []
    hullSolution.append(lm)
    # hullSolution.append(rm)

    x1, y1 = lm
    x2, y2 = rm
    for points in data:
        x3, y3 = points
        tocheck = isAboveLine(x1,y1,x2,y2,x3,y3)
        if tocheck == "above":  
            points_above.append(points)
        elif tocheck == "below":
            points_below.append(points)

    divnconqHullabove(points_above,lm,rm)
    divnconqHullbelow(points_below,lm,rm)
    hullabove = np.array(sorted(hullabove, key=lambda k: [k[0], k[1]]))
    hullbelow = np.array(sorted(hullbelow, reverse=True, key=lambda k: [k[0], k[1]]))
    hullSolution.extend(hullabove)
    hullSolution.append(rm)
    hullSolution.extend(hullbelow)
    hullSolution.append(lm)
    return hullSolution