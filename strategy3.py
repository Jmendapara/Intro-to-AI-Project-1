import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq
from random import randrange
from aStarClass import AStar
from utils import Utils
from scipy.spatial import distance

class strategy3: 

    def __init__(self, arr, fireRate):
        self.arr = arr
        self.mazeSize = arr.shape[0]
        self.fireRate = fireRate


    #Update fire maze with fire and new predictions    
    def updateFireMaze(self, arr, fireRate, currentPosition, endPosition, onFireSet):

        newMaze = deepcopy(arr)
        mazeSize = arr.shape[0]
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        #"Expand" the fire
        for x in range(mazeSize):
            for y in range(mazeSize):

                totalNeighborsOnFire = 0

                if((arr[x][y] == 0 and arr[x][y] != 1) or arr[x][y] == 3):
                
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
                        onFireSet.add((x,y))
                    
        path = False
            
        #Prediction distance. Large prediction distance will force agent to be further from the fire 
        futurePredictionDistance = self.getfirePredictionDistance()

        #Update predictions of where the fire will be in the next few updates
        while (path == False):

            for k in range(self.mazeSize):
                for u in range(self.mazeSize):
                    if(newMaze[k][u] == 3):
                        newMaze[k][u] = 0

            if (futurePredictionDistance == 0):
                return newMaze

            #For each location of a fire block, create prediction blocks of how the fire will expand
            for fireCoordinates in onFireSet:
                
                        point = [fireCoordinates[0],fireCoordinates[1]]
                        valid_points = []
                        for x in range(self.mazeSize):
                            for y in range(self.mazeSize):

                                if ( (abs(x - point[0]) + abs(y - point[1])) <= futurePredictionDistance ):
                                    valid_points.append((x,y))

                        for coordinate in valid_points:
                            x = coordinate[0]
                            y = coordinate[1]
                            if(newMaze[x][y] != 1 and newMaze[x][y] != 2):
                                newMaze[x][y] = 3

            path = self.getShortestPathExists(newMaze, currentPosition, endPosition, False, False)
            futurePredictionDistance -= 1

        return newMaze


    #Get a prediction distance based on the fireRate
    def getfirePredictionDistance(self):

        if (self.fireRate < .2):
            return 1

        if (self.fireRate < .5):
            return 2

        if (self.fireRate < 1):
            return 3

        return 4


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

        onFireSet = set()

        #While there is a path from current position to end
        while(path != False):

            currentPosition = path[0]

            arr = self.updateFireMaze(arr, self.fireRate, currentPosition, endPosition, onFireSet)

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
            print('Path does not exist from start to end')
        


def graph():

    #PARAMETERS YOU CAN CHANGE
    
    mazeSize = 20
    densityProbability = .3
    fireRate = .3
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

            tempMaze = strategy3(array, fireRate)

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
    plt.title('Strategy 3')
    plt.show()


if __name__ == "__main__":
    graph()