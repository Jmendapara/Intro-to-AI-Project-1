import numpy as np
import collections
from collections import deque
from utils import Utils
from copy import copy, deepcopy
import matplotlib.pyplot as plt
import time

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

            for i, j in dir:

                neighborX = x + i
                neighborY = y + j

                if 0 <= neighborX < mazeSize and 0 <= neighborY < mazeSize: 
                    if arr[neighborX][neighborY] != 1 and (neighborX, neighborY) not in visitedSet:
                    
                        arr[neighborX,neighborY] = -1

                        queue.append(currentPath + [(neighborX, neighborY)])
                        visitedSet.add((neighborX, neighborY))

            if(showPathFinderAnimation):
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
    
        return False, arr


# Driver code
def main():

    mazeSize = 20
    densityProbability = .3

    startPosition = (0, 0)
    endPosition = (mazeSize-1, mazeSize-1)

    showPathFinderAnimation = True

    #start_time = time.time()



    mazeSize = 100
    densityProbability = .3

    startPosition = (0, 0)
    endPosition = (mazeSize-1, mazeSize-1)

    showPathFinderAnimation = False
    
    obstacleDensities = np.linspace(0, 1, 11)

    totalTrials = 50

    #######################################################################################################################

    #plotting probabaility of path existing vs. density 
    y = []

    for obstacleDensity in obstacleDensities:

        visitedBlocks = 0
        currentTrial = 0

        while (currentTrial < totalTrials):

            array = Utils.makeMatrix(mazeSize, obstacleDensity)

            bfsTest = bfsClass(array)

            path, arr = bfsTest.getshortestPath(startPosition, endPosition, showPathFinderAnimation)

            print(arr)

            #print("--- %s seconds ---" % (time.time() - start_time))
            for k in range(bfsTest.mazeSize):
                for u in range(bfsTest.mazeSize):
                    if(arr[k][u] == -1):
                        visitedBlocks += 1
            print('Trial = ' + str(currentTrial))
            currentTrial += 1

        
        y.append(visitedBlocks/totalTrials)

   
    print('Total Nodes = ' + str(np.sum(y)))
    print(y)

    plt.plot(obstacleDensities, y)
    plt.ylabel('Average Number of Nodes Visited')
    plt.xlabel('Obstacle Density')
    plt.title('BFS (Obstacle Density vs. # of Nodes Visited)')
    plt.show()


if __name__ == "__main__":
    main()