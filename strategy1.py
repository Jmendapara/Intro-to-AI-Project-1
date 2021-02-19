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


    def executeSimulation(self, path, startPosition, endPosition, showCharacterAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        #Get a random fire start location and verify that a path exists from the start position to the fire 
        fireToStartPathExists = (-1,-1)
        while (fireToStartPathExists != False):
            fireCoordinates = Utils.getRandomFireStartPosition(arr) 
            fireToStartPathExists = self.getShortestPathExists(startPosition, fireCoordinates, False, False)
        arr[fireCoordinates[0]][fireCoordinates[1]] = 2

        for step in path:

            arr = Utils.updateFireMaze(arr, self.fireRate)

            #Current position's x and y values
            x = step[0]
            y = step[1]

            #If the current position is on fire, return False 
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

    def getShortestPathExists(self, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(self.arr)
        tempAStar = AStar(arr)

        path = tempAStar.getShortestPath(startPosition, endPosition, showPathFinderAnimation, False)
        if(path != False):
            return path
        else:
            return False
            print('Path does not exist from start to end')


def graph():

    #PARAMETERS YOU CAN CHANGE
    
    mazeSize = 20
    densityProbability = .3
    #fireRate = .1
    showPathFinderAnimation = False
    showCharacterAnimation = False

    startPosition = (0,0)
    endPosition = (mazeSize-1,mazeSize-1)

    #Total trials for each fireRate
    totalTrials = 50
    fireRates = np.linspace(0, 1, 11)


    #Plotting probabaility of agent reaching goal vs fire rate
    #######################################################################################################################
    
    y = []

    for fireRate in fireRates:

        successes = 0
        
        currentTrial = 0
        while (currentTrial < totalTrials):


            array = Utils.makeMatrix(mazeSize, densityProbability)


            tempMaze = strategy1(array, fireRate)

            path = tempMaze.getShortestPathExists(startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation)

            if (path == False):
                continue
            else:
                currentTrial += 1
                survived = tempMaze.executeSimulation(path, startPosition, endPosition, showCharacterAnimation)
                if(survived == True):
                    successes += 1
            
            print('Trial = ' + str(currentTrial) + " Flammability Rate = "+ str(fireRate))

        y.append(successes/totalTrials)

    print('Total probability = ' + str(np.sum(y)))
    print(y)

    plt.plot(fireRates, y)
    plt.ylabel('Average  Strategy  Success  Rate')
    plt.xlabel('Flammability Rate')
    plt.title('Strategy 1')

    plt.show()


if __name__ == "__main__":
    graph()