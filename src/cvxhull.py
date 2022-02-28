import numpy as np

def getAboveOrBelow(point, startPt, endPt):
    xS, yS = startPt; xE, yE = endPt; xP, yP = point
    det = (xS*yE + xP*yS + xE*yP - xP*yE - xE*yS - xS*yP) 
    # ^Determinant formula to check whether xP,yP is above/below the line created by xS,yS and xE,yE

    if(det > 10**(-10)):
        return "ABOVE"
    elif(det < 0):
        return "BELOW"
# Obtain the location(above/below) of a point from a line (xP -> yP)
    
def getFarthest(arr,tailPt,headPt):
    curFarthestPoint = []; curDist = 0
    for point in arr:
        if(getDistance(point,tailPt,headPt) >= curDist):
            curDist = getDistance(point,tailPt,headPt)
            curFarthestPoint = point
    return curFarthestPoint
# Obtain the farthest point from a line (tailPt -> headPt)

def getDistance(point,tailPt,headPt):
    tailPt = np.asfarray(tailPt); headPt = np.asfarray(headPt); point = np.asfarray(point)
    distance = (np.linalg.norm(np.cross(headPt-tailPt, tailPt-point))/np.linalg.norm(headPt-tailPt))
    # ^Distance formula

    return distance
# Obtain the distance between a point and a line (tailPt -> headPt)

def isArrEmpty(arr):
    if len(arr) == 0:
        return "Empty"

def getConvexHullPt(location, ptArr, startPt, endPt):
    #ptArr is either ptAbove or ptBelow
    #startPt is the starting point of the line, either ptLeft or ptRight
    #endPt is the end point of the line, either ptLeft or ptRight
    #location can be TOP or BOTTOM depends on ptArr
    
    #BASIS
    if(isArrEmpty(ptArr) == "Empty"):
        if(location =="A"):
            cvxHullPtAbove.extend([startPt])
            cvxHullPtAbove.extend([endPt])
        else:
            cvxHullPtBelow.extend([startPt])
            cvxHullPtBelow.extend([endPt])
    # The basis of the algorithm will assign 2 points that made the line as convex hull point if there's no point found above/below the line 

    #RECURSIVE
    else:
        furthestPoint = getFarthest(ptArr,startPt,endPt)
    
        ptAbove_leftLine=[]
        # Array for storing points that's above the line (ptLeft -> furthestPoint)

        ptAbove_rightLine=[]
        # Array for storing points that's above the line (furthestPoint -> ptRight)

        for point in ptArr:
            if(getAboveOrBelow(point,startPt,furthestPoint) == "ABOVE"):
                ptAbove_leftLine.extend([point])

        for point in ptArr:
            if(getAboveOrBelow(point,furthestPoint,endPt) == "ABOVE"):
                ptAbove_rightLine.extend([point])
        getConvexHullPt(location, ptAbove_leftLine,startPt,furthestPoint)
        getConvexHullPt(location, ptAbove_rightLine,furthestPoint,endPt)
        # Recursive until there's no point above/below the line
# Obtain the convex hull points using recursive 

def myConvexHull(arr):
    sortedArr = np.array(sorted(arr , key=lambda x:[x[0], x[1]])) 

    global cvxHullPtAbove
    global cvxHullPtBelow 
    cvxHullPtAbove = []
    cvxHullPtBelow = []
    # Assign empty array for storing convex hull points above and below the line created by the ptLeft and ptRight point

    ptAbove = []
    ptBelow = []
    # Assign empty array for storing points from above and below the line created by ptLeft and ptRight

    ptLeft = sortedArr[0]
    ptRight = sortedArr[-1]
    # Obtain the first and last point of the dataset

    for point in sortedArr:
        checkPos = getAboveOrBelow(point,ptLeft,ptRight)
        if checkPos == "ABOVE":
            ptAbove.append(point)
        else:
            ptBelow.append(point)
    # Divide the points from the array to 2 sides by checking their location (above or below the line) and append it to ptAbove/ptBelow
 
    getConvexHullPt("A",ptAbove,ptLeft,ptRight)
    getConvexHullPt("B",ptBelow,ptRight,ptLeft)
    sortedHullAbove = sorted(cvxHullPtAbove , key=lambda x:[x[0], x[1]])
    # Obtain a sorted dataset (axis first then ordinate) in ascending order

    sortedHullBelow = sorted(cvxHullPtBelow , key=lambda x:[x[0], x[1]], reverse = True)
    # Obtain a sorted dataset (axis first then ordinate) in descending order

    finalConvexHull = np.concatenate((sortedHullAbove, sortedHullBelow), axis=0) 
    # Obtain the final convex hull through merging these 2 arrays

    return(finalConvexHull)