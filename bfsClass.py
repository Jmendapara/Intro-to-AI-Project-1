import numpy as np
import collections
from collections import deque
from utils import Utils
from copy import copy, deepcopy
import matplotlib.pyplot as plt
import time
from random import randrange

class bfsClass:

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]
 
    def getshortestPath(self, startPosition, endPosition, showPathFinderAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        if(arr[startPosition[0]][startPosition[1]] == 1):
            return False, arr

        queue = collections.deque([[startPosition]])
        visitedSet = set([startPosition])

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        while queue:

            currentPath = queue.popleft()
            x, y = currentPath[-1]

            if(x == endPosition[0] and y == endPosition[1]):
                
                #Utils.showFinalPlot(self.arr, startPosition, endPosition, currentPath)
                
                return currentPath, arr

            #For each neighbor
            for i, j in dir:

                neighborX = x + i
                neighborY = y + j

                if 0 <= neighborX < mazeSize and 0 <= neighborY < mazeSize: 

                    #If that neighbor has not been visited, add to queue and the current path
                    if arr[neighborX][neighborY] != 1 and (neighborX, neighborY) not in visitedSet:
                    
                        arr[neighborX,neighborY] = -1

                        queue.append(currentPath + [(neighborX, neighborY)])
                        visitedSet.add((neighborX, neighborY))

            if(showPathFinderAnimation):
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
    
        return False, arr


def graph():

    #PARAMETERS YOU CAN CHANGE

    mazeSize = 100
    densityProbability = .3

    showPathFinderAnimation = False
    
    obstacleDensities = np.linspace(0, 1, 11)

    totalTrials = 50

    #plotting probabaility of path existing vs. obstacle density 
    #######################################################################################################################
    
    y = []

    for obstacleDensity in obstacleDensities:

        visitedBlocks = 0
        currentTrial = 0

        while (currentTrial < totalTrials):

            array = Utils.makeMatrix(mazeSize, obstacleDensity)

            bfsTest = bfsClass(array)

            startPosition = (randrange(mazeSize), randrange(mazeSize))
            endPosition = (randrange(mazeSize), randrange(mazeSize))

            path, arr = bfsTest.getshortestPath(startPosition, endPosition, showPathFinderAnimation)

            for k in range(bfsTest.mazeSize):
                for u in range(bfsTest.mazeSize):
                    if(arr[k][u] == -1):
                        visitedBlocks += 1
            print('Trial = ' + str(currentTrial) + " Obstacle Density = "+ str(obstacleDensity))
            currentTrial += 1

        
        y.append(visitedBlocks/totalTrials)

   
    print('Total Nodes = ' + str(np.sum(y)))
    print(y)

    plt.plot(obstacleDensities, y)
    plt.ylabel('Average Number of Nodes Visited')
    plt.xlabel('Obstacle Density')
    plt.title('BFS (Obstacle Density vs. # of Nodes Visited)')
    plt.show()

def largestMatrixMinute():
    mazeSize = 1680
    densityProbability = .3

    startPosition = (0, 0)
    endPosition = (mazeSize-1, mazeSize-1)

    showPathFinderAnimation = False

    array = Utils.makeMatrix(mazeSize, densityProbability)

    bfsTest = bfsClass(array)

    start_time = time.time()

    if(array[0][0] == 1 or array[mazeSize-1][mazeSize-1] == 1):
        return 

    returnValue = bfsTest.getshortestPath(startPosition, endPosition, showPathFinderAnimation)

    print("BFS with maze size of " + str(mazeSize) +" x "+ str(mazeSize) + " --- %s seconds ---" % (time.time() - start_time))

    if(returnValue[0] != False):
        print("Path Exists: True")


if __name__ == "__main__":
    #largestMatrixMinute()
    graph()