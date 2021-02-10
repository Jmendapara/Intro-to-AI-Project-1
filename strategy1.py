import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq
from random import randrange
from aStarClass import AStar
from utils import Utils

class strategy1: 

    def __init__(self, arr, fireRate):
        self.arr = arr
        self.mazeSize = arr.shape[0]
        self.fireRate = fireRate
    
    def updateFireMaze(self, arr):

        newMaze = deepcopy(arr)
        fireRate = self.fireRate
        mazeSize = self.mazeSize
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        for x in range(0, mazeSize):
            for y in range(0, mazeSize):

                totalNeighborsOnFire = 0

                if(arr[x][y] == 0 or arr[x][y] == 3 and arr[x][y] != 1):
                
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


    def executeShortestPath(self, path, startPosition, endPosition, showCharacterAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        randomFireX = randrange(mazeSize)
        randomFireY = randrange(mazeSize)

        while arr[randomFireX][randomFireY] != 1 :
            randomFireX = randrange(mazeSize)
            randomFireY = randrange(mazeSize)

        arr[randomFireX][randomFireY] = 2

        for step in path:

            arr = self.updateFireMaze(arr)

            x = step[0]
            y = step[1]

            if(arr[x][y] == 2):
                print("Peppa caught on fire and died :( RIP")
                return False

            arr[x][y] = -1

            if(showCharacterAnimation):
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
                plt.clf()

            
            arr[x][y] = 0

        Utils.showFinalPlot(arr, startPosition, endPosition, path)
        print("Peppa made it across the maze without catching on fire!")
        return True

    def runSimulation(self, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(self.arr)
        tempAStar = AStar(arr)

        path = tempAStar.getShortestPath(startPosition, endPosition, showPathFinderAnimation)
        if(path != False):
            self.executeShortestPath(path, startPosition, endPosition, showCharacterAnimation)
        else:
            print('Path does not exist from start to end')


def makeMatrix(size, probability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    return arr


def main():
    
    mazeSize = 10
    densityProbability = .1
    fireRate = .1
    showPathFinderAnimation = True
    showCharacterAnimation = True

    startPosition = (8,9)
    endPosition = (0,0)

    array = Utils.makeMatrix(mazeSize, densityProbability)

    strategy1Test = strategy1(array, fireRate)
    strategy1Test.runSimulation(startPosition, endPosition , showPathFinderAnimation, showCharacterAnimation )


if __name__ == "__main__":
    main()