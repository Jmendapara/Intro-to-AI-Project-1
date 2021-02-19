import numpy as np
import random
from random import randrange
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
    #3 = future possible fire

    #Shows the final path
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

    #Make a random matrix
    @staticmethod
    def makeMatrix(size, probability):
        arr = np.zeros((size, size))

        for x in range(0, size):
            for y in range(0, size):
                if (random.random() < probability): 
                    arr[x,y] = 1
        return arr

    #"Expand" the fire
    @staticmethod
    def updateFireMaze(arr, fireRate):

        newMaze = deepcopy(arr)
        mazeSize = arr.shape[0]
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        for x in range(0, mazeSize):
            for y in range(0, mazeSize):

                totalNeighborsOnFire = 0

                if(arr[x][y] == 0 and arr[x][y] != 1):
                
                    for i, j in dir:

                        neighbor = x + i, y + j
                        neighborX = neighbor[0]
                        neighborY = neighbor[1]

                        if ((0 <= neighborX < mazeSize) and (0 <= neighborY < mazeSize)):

                            if(arr[neighborX][neighborY] == 2):
                                totalNeighborsOnFire += 1

                    prob = 1 - ((1-fireRate)**totalNeighborsOnFire)
                    if (random.random() <= prob): 
                        newMaze[x,y] = 2
                    
        return newMaze

    @staticmethod
    def getRandomFireStartPosition(arr):
        mazeSize = arr.shape[0]

        randomFireX = randrange(mazeSize)
        randomFireY = randrange(mazeSize)

        while arr[randomFireX][randomFireY] != 1 :
            randomFireX = randrange(mazeSize)
            randomFireY = randrange(mazeSize)

        return (randomFireX, randomFireY)


