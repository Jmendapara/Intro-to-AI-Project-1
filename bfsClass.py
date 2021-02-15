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
 
    def shortestPath(self, start, end, showPathFinderAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        queue = collections.deque([[start]])
        seen = set([start])

        while queue:

            path = queue.popleft()
            x, y = path[-1]

            if(x == end[0] and y == end[1]):
                
                Utils.showFinalPlot(self.arr, start, end, path)
                return path

            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):

                if 0 <= x2 < mazeSize and 0 <= y2 < mazeSize and arr[y2][x2] != 1 and (x2, y2) not in seen:
                    
                    arr[y2,x2] = -1

                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))

            if(showPathFinderAnimation):
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
    
        return False


# Driver code
def main():

    mazeSize = 10
    densityProbability = .05
    array = Utils.makeMatrix(mazeSize, densityProbability)

    mat = np.array([[ 0, 0, 0, 0, 0, 1, 0, 1, 1, 1 ],
                    [ 1, 0, 0, 0, 0, 1, 1, 0, 1, 1 ], 
                    [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ], 
                    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ], 
                    [ 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ], 
                    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
                    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ], 
                    [ 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ], 
                    [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ], 
                    [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 0 ]])


    print(array)

    startPosition = (0, 0)
    endPosition = (9, 9)

    BFSTest = bfsClass(mat)

    showPathFinderAnimation = True

    path = BFSTest.shortestPath(startPosition, endPosition, showPathFinderAnimation)

    if path != False:
        print("Shortest Path is", path)
    else:
        print("Shortest path doesn't exist")


main()