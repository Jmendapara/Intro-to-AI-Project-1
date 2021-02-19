import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq
from utils import Utils
from random import randrange

class AStar: 

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]
    
    
    def getShortestPath(self, startPosition, endPosition, showPathFinderAnimation, returnArray):
    
        mazeSize = self.mazeSize
        arr = deepcopy(self.arr)

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        closed = set()

        parent = {}

        startToCurrentCost = {startPosition:0}

        currentToEndCost = {startPosition:self.heuristic(startPosition, endPosition)}

        priorityQueue = []

        heapq.heappush(priorityQueue, (currentToEndCost[startPosition], startPosition))

        while priorityQueue:

            current = heapq.heappop(priorityQueue)[1]

            currentX = current[0]
            currentY = current[1]

            arr[currentX, currentY] = -1

            if current == endPosition:

                path = []

                while current in parent:

                    path.append(current)

                    current = parent[current]

                path = path + [startPosition]

                path = path[::-1]

                #Utils.showFinalPlot(self.arr, startPosition, endPosition, currentPath)
                if(returnArray == True):
                    return path, arr
                return path

            closed.add(current)

            for i, j in dir:

                neighbor = current[0] + i, current[1] + j

                tempStartToCurrent = startToCurrentCost[current] + self.heuristic(current, neighbor)

                neighborX = neighbor[0]
                neighborY = neighbor[1]

                #If index is out of bounds, do not do anything
                if ((0 <= neighbor[0] < mazeSize) and (0 <= neighbor[1] < mazeSize)):
                    if arr[neighbor[0]][neighbor[1]] == 1 or arr[neighbor[0]][neighbor[1]] == 2 or arr[neighbor[0]][neighbor[1]] == 3:
                        continue

                else:
                    continue
    

                if neighbor in closed and tempStartToCurrent >= startToCurrentCost.get(neighbor, 0):

                    continue
    

                if  tempStartToCurrent < startToCurrentCost.get(neighbor, 0) or neighbor not in [i[1]for i in priorityQueue]:

                    parent[neighbor] = current

                    startToCurrentCost[neighbor] = tempStartToCurrent

                    currentToEndCost[neighbor] = tempStartToCurrent + self.heuristic(neighbor, endPosition)

                    heapq.heappush(priorityQueue, (currentToEndCost[neighbor], neighbor))

            if(showPathFinderAnimation):
                    plt.imshow(arr)
                    plt.pause(0.01)
                    plt.clf()

        if(returnArray == True):
            return False, arr
        return False

    def heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def graph():
    
    #PARAMETERS YOU CAN CHANGE

    mazeSize = 100
    densityProbability = .3

    showPathFinderAnimation = False
    
    obstacleDensities = np.linspace(0, 1, 11)

    totalTrials = 50

    #######################################################################################################################

    #plotting probabaility of path existing vs. density 
    y = []

    for obstacleDensity in obstacleDensities:

        visitedBlocks = 0
        currentTrial = 0

        while (currentTrial < totalTrials):

            array = Utils.makeMatrix(mazeSize, obstacleDensity)

            aStarTest = AStar(array)

            startPosition = (randrange(mazeSize), randrange(mazeSize))
            endPosition = (randrange(mazeSize), randrange(mazeSize))

            path, arr = aStarTest.getShortestPath(startPosition, endPosition, showPathFinderAnimation, True)

            for k in range(aStarTest.mazeSize):
                for u in range(aStarTest.mazeSize):
                    if(arr[k][u] == -1):
                        visitedBlocks += 1
            print('Trial = ' + str(currentTrial))
            currentTrial += 1

        
        y.append(visitedBlocks/totalTrials)

   
    print('Total Nodes = ' + str(np.sum(y)))
    print(y)

    plt.plot(obstacleDensities, y)
    plt.ylabel('Average Number of Nodes Visited')
    plt.xlabel('Obstacle Density')
    plt.title('A* (Obstacle Density vs. # of Nodes Visited)')
    plt.show()


if __name__ == "__main__":
    graph()