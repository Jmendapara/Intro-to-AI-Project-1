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


    def executeSimulation(self, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(self.arr)
        mazeSize = self.mazeSize

        #Get a random fire start location and verify that a path exists from the start position to the fire 
        fireToStartPathExists = (-1,-1)
        while (fireToStartPathExists != False):
            fireCoordinates = Utils.getRandomFireStartPosition(arr) 
            fireToStartPathExists = self.getShortestPathExists(arr, startPosition, fireCoordinates, False, False)
        arr[fireCoordinates[0]][fireCoordinates[1]] = 2

        path = self.getShortestPathExists(arr, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation)

        #There does not exist a path from start to end, so return -1
        if(path == False):
            return -1

        #While there is a path from current position to end
        while(path != False):

            arr = Utils.updateFireMaze(arr, self.fireRate)

            currentPosition = path[0]

            #If the agent is currently on a fire block, return False 
            if(arr[currentPosition[0]][currentPosition[1]] == 2):
                #print("Peppa caught on fire and died :( RIP")
                return False

            #If we reach the goal, return True
            if(currentPosition == endPosition):
                #print("Peppa made it across the maze without catching on fire!")
                return True  

            #Move the agent to the next best coordinate 
            nextStep = path[1]
                
            x = nextStep[0]
            y = nextStep[1]

            if(showCharacterAnimation):
                arr[x][y] = -1
                plt.imshow(arr, interpolation='none')
                plt.pause(0.00001)
                plt.clf()
                arr[x][y] = 0

            path = self.getShortestPathExists(arr, nextStep, endPosition, showPathFinderAnimation, showCharacterAnimation)

        #There is no path from current position to goal
        #print("Peppa could not find a path and died!")
        return False


    def getShortestPathExists(self, array, startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation):

        arr = deepcopy(array)
        tempAStar = AStar(arr)

        path = tempAStar.getShortestPath(startPosition, endPosition, showPathFinderAnimation, False)
        if(path != False):
            return path
        else:
            return False
            #print('Path does not exist from start to end')


def graph():
    

    #PARAMETERS YOU CAN CHANGE

    mazeSize = 20
    densityProbability = .3
    #fireRate = .03
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

            tempMaze = strategy2(array, fireRate)

            returnValue = tempMaze.executeSimulation(startPosition, endPosition, showPathFinderAnimation, showCharacterAnimation)

            #If there exists a path
            if(returnValue != -1): 
                currentTrial += 1
                if(returnValue == True):
                    successes += 1
            else:
                continue
        
            print('Trial = ' + str(currentTrial) + " Flammability Rate = "+ str(fireRate))

        y.append(successes/totalTrials)

   
    print('Total probability = ' + str(np.sum(y)))
    print(y)

    plt.plot(fireRates, y)
    plt.ylabel('Probability of agent reaching goal')
    plt.xlabel('Flammability Rate')
    plt.title('Strategy 2')
    plt.show()


if __name__ == "__main__":
    graph()