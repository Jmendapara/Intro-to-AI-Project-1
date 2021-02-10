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

            if(showCharacterAnimation):
                arr[x][y] = -1
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
                plt.clf()
                arr[x][y] = 0

        #Utils.showFinalPlot(arr, startPosition, endPosition, path)
        print("Peppa made it across the maze without catching on fire!")
        return True

    def pathExists(self, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(self.arr)
        tempAStar = AStar(arr)

        path = tempAStar.getShortestPath(startPosition, endPosition, showPathFinderAnimation)
        if(path != False):
            return path
        else:
            return False
            print('Path does not exist from start to end')


def main():
    
    mazeSize = 25
    densityProbability = .3
    #fireRate = .1
    showPathFinderAnimation = False
    showCharacterAnimation = False

    startPosition = (0,0)
    endPosition = (mazeSize-1,mazeSize-1)

    #plotting probabaility of peppe reaching goal vs fire rate

    fireRates = np.linspace(0, 1, 21)
    y = []

    totalTrials = 20

    for fireRate in fireRates:

        successes = 0
        
        currentTrial = 0
        while (currentTrial < totalTrials):

            array = Utils.makeMatrix(mazeSize, densityProbability)

            tempMaze = strategy1(array, fireRate)

            path = tempMaze.pathExists(startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation)
            if (path == False):
                continue
            else:
                currentTrial += 1
                survived = tempMaze.executeShortestPath(path, startPosition, endPosition, showCharacterAnimation)
                if(survived == True):
                    successes += 1

        y.append(successes/totalTrials)

 
    plt.plot(fireRates, y)
    plt.ylabel('Probability of Peppa reaching goal')
    plt.xlabel('Fire Rate')

    plt.show()


    


if __name__ == "__main__":
    main()