import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq
from random import randrange
from aStarClass import AStar
from utils import Utils

class strategy2: 

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


    def executeSimulation(self, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        randomFireX = randrange(mazeSize)
        randomFireY = randrange(mazeSize)

        while arr[randomFireX][randomFireY] != 1 :
            randomFireX = randrange(mazeSize)
            randomFireY = randrange(mazeSize)

        arr[randomFireX][randomFireY] = 2

        path = self.pathExists(arr, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation)

        if(path == False):
            return -1

        while(path != False):

            arr = self.updateFireMaze(arr)

            step = path[1]

            if(step == endPosition):
                print("Peppa made it across the maze without catching on fire!")
                return True  
                
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

            path = self.pathExists(arr, step, endPosition, showPathFinderAnimation, showCharacterAnimation)

            
        if(path == False): 
            print("Peppa could not find a path and died!")
            return False

        #Utils.showFinalPlot(arr, startPosition, endPosition, path)
        

    def pathExists(self, array, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(array)
        tempAStar = AStar(arr)

        path = tempAStar.getShortestPath(startPosition, endPosition, showPathFinderAnimation)
        if(path != False):
            return path
        else:
            return False
            print('Path does not exist from start to end')


def main():
    
    mazeSize = 20
    densityProbability = .3
    #fireRate = .03
    showPathFinderAnimation = False
    showCharacterAnimation = False

    startPosition = (0,0)
    endPosition = (mazeSize-1,mazeSize-1)


    #plotting probabaility of peppe reaching goal vs fire rate

    fireRates = np.linspace(0, 1, 41)
    y = []

    totalTrials = 20

    for fireRate in fireRates:

        successes = 0
        
        currentTrial = 0
        while (currentTrial < totalTrials):

            array = Utils.makeMatrix(mazeSize, densityProbability)


            tempMaze = strategy2(array, fireRate)

            returnValue = tempMaze.executeSimulation(startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation)

            if(returnValue != -1): #if there exists a path
                currentTrial += 1
                if(returnValue == True):
                    successes += 1
            else:
                continue
        

        y.append(successes/totalTrials)

 
    plt.plot(fireRates, y)
    plt.ylabel('Probability of Peppa reaching goal')
    plt.xlabel('Fire Rate')
    plt.show()


if __name__ == "__main__":
    main()