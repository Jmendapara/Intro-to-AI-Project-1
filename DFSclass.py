import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from utils import Utils
import time

class dfsClass: 

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]

    def pathExists(self, startPosition, endPosition, showPathFinderAnimation):
    
        mazeSize = self.mazeSize
        arr = deepcopy(self.arr)
        
        #print('mazesize='+str(mazeSize))

        stack = []

        #directions
        dir = np.array([[0,1], [0,-1], [1,0], [-1,0]])
        
        #queue 
        stack.append(startPosition)

        while(len(stack)>0):

            currentPosition = stack.pop()

            currentX = currentPosition[0]
            currentY = currentPosition[1]

            #mark as visited
            arr[currentX, currentY] = -1

            #destination is reached
            if( sorted(currentPosition) == sorted(endPosition)):
                return True

            #check all four directions
            for i in range(0, 4):
            
                #using the direction array
                a = currentX + dir[i][0]
                b = currentY + dir[i][1]
                
                #not blocked and valid
                if(a>=0 and b>=0 and a<mazeSize and b<mazeSize and arr[a][b]!=-1 and arr[a][b]!=1):
                
                    stack.append((a,b))

            if(showPathFinderAnimation):
                plt.imshow(arr)
                plt.pause(0.00000001)
                plt.clf()

        return False

def graph():

    #PARAMETERS YOU CAN CHANGE

    mazeSize = 100
    densityProbability = .3

    startPosition = (0, 0)
    endPosition = (mazeSize-1, mazeSize-1)

    showPathFinderAnimation = False
    
    obstacleDensities = np.linspace(0, 1, 11)

    totalTrials = 50

    #plotting probabaility of path existing vs. obstacle density 
    #######################################################################################################################
    
    y = []

    for obstacleDensity in obstacleDensities:

        successes = 0
        currentTrial = 0

        while (currentTrial < totalTrials):

            array = Utils.makeMatrix(mazeSize, obstacleDensity)

            dfsTest = dfsClass(array)

            returnValue = dfsTest.pathExists(startPosition, endPosition, showPathFinderAnimation)

            if(returnValue == True):
                successes += 1
                currentTrial += 1
            else:
                currentTrial += 1

            print('Trial = ' + str(currentTrial) + " Obstacle Density = "+ str(obstacleDensity))
        
        y.append(successes/totalTrials)

   
    print('Total probability = ' + str(np.sum(y)))
    print(y)

    plt.plot(obstacleDensities, y)
    plt.ylabel('Probability the S can be reached from G')
    plt.xlabel('Obstacle Density')
    plt.title('DFS (Obstacle Density vs. Probability of Path Existing)')
    plt.show()

def largestMatrixMinute():
    mazeSize = 3075
    densityProbability = .3

    startPosition = (0, 0)
    endPosition = (mazeSize-1, mazeSize-1)

    showPathFinderAnimation = False

    array = Utils.makeMatrix(mazeSize, densityProbability)

    dfsTest = dfsClass(array)

    start_time = time.time()

    if(array[0][0] == 1 or array[mazeSize-1][mazeSize-1] == 1):
        return 

    returnValue = dfsTest.pathExists(startPosition, endPosition, showPathFinderAnimation)

    print("DFS with maze size of " + str(mazeSize) +" x "+ str(mazeSize) + " --- %s seconds ---" % (time.time() - start_time))

    print("Path Exists: " + str(returnValue))


if __name__ == "__main__":
    #largestMatrixMinute()
    graph()