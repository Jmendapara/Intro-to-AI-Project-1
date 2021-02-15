# Python program to find the shortest
# path between a given source cell 
# to a destination cell.
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
 
    def getshortestPath(self, start, end, showPathFinderAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        queue = collections.deque([[start]])
        visited = set([start])

        dir = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])

        while queue:

            currentPosition = queue.popleft()
            currentX = currentPosition[0]
            currentY = currentPosition[1]
            arr[currentX, currentY] = -1

            if(currentX == end[0] and currentY == end[1]):

                Utils.showFinalPlot(self.arr, start, end, currentPosition)
                return currentPosition

            #for i in range(0, 4):
            for x2, y2 in ((currentX+1,currentY), (currentX-1,currentY), (currentX,currentY+1), (currentX,currentY-1)):

                if 0 <= x2 < mazeSize and 0 <= y2 < mazeSize and arr[y2][x2] != 1 and (x2, y2) not in visited:

                    arr[y2,x2] = -1

                    queue.append(currentPosition + [(x2, y2)])
                    visited.add((x2, y2))

            if(showPathFinderAnimation):
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
    
        return False


# Driver code
def main():

    mazeSize = 10
    densityProbability = .05
    array = Utils.makeMatrix(mazeSize, densityProbability)

    # mat = np.array([[ 0, 0, 0, 0, 0, 1, 0, 1, 1, 1 ],
    #                 [ 1, 0, 0, 0, 0, 1, 1, 0, 1, 1 ],
    #                 [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ],
    #                 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    #                 [ 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ],
    #                 [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    #                 [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    #                 [ 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ],
    #                 [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    #                 [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 0 ]])


    print(array)

    startPosition = (0, 0)
    endPosition = (9, 9)

    BFSTest = bfsClass(array)

    showPathFinderAnimation = True

    path = BFSTest.getshortestPath(startPosition, endPosition, showPathFinderAnimation)

    if path != False:
        print("Shortest Path is", path)
    else:
        print("Shortest path doesn't exist")


main()