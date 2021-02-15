import numpy as np
import collections
from collections import deque
from utils import Utils
from copy import copy, deepcopy
import matplotlib.pyplot as plt

class bfsClass:

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]
 
    def shortestPath(self, startPosition, endPosition, showPathFinderAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        if(arr[startPosition[0]][startPosition[1]] == 1):
            return False

        queue = collections.deque([[startPosition]])
        visitedSet = set([startPosition])

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        while queue:

            currentPath = queue.popleft()
            x, y = currentPath[-1]

            if(x == endPosition[0] and y == endPosition[1]):
                
                Utils.showFinalPlot(self.arr, startPosition, endPosition, currentPath)
                return currentPath

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
    
        return False


# Driver code
def main():

    mazeSize = 10
    densityProbability = .3
    array = Utils.makeMatrix(mazeSize, densityProbability)
    print(array)

    startPosition = (0, 0)
    endPosition = (mazeSize-1, mazeSize-1)

    BFSTest = bfsClass(array)

    showPathFinderAnimation = True

    path = BFSTest.getshortestPath(startPosition, endPosition, showPathFinderAnimation)

    if path != False:
        print("Shortest Path is", path)
    else:
        print("Shortest path doesn't exist")


if __name__ == "__main__":
    main()