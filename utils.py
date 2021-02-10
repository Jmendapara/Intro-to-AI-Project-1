import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq

class Utils: 

    #-3 = end of path
    #-2 = start of path
    #-1 = shortest path
    #0 = open 
    #1 = blocks
    #2 = fire
    #3 = searched


    @staticmethod
    def showFinalPlot(arr, startPosition, endPosition, path):

        arr = deepcopy(arr)

        for i in (range(0,len(path))):

            x = path[i][0]

            y = path[i][1]

            arr[x][y] = -1

        startX = startPosition[0]
        startY = startPosition[1]

        arr[startX, startY] = -2

        endX = endPosition[0]
        endY = endPosition[1]

        arr[endX, endY] = -3

        plt.imshow(arr)
        plt.show()

    @staticmethod
    def makeMatrix(size, probability):
        arr = np.zeros((size, size))

        for x in range(0, size):
            for y in range(0, size):
                if (random.random() < probability): 
                    arr[x,y] = 1
        return arr
