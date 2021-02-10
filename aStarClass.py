import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq
from utils import Utils

class AStar: 

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]
    
    
    def getShortestPath(self, startPosition, endPosition, showPathFinderAnimation):
    
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

                #Utils.showFinalPlot(self.arr, startPosition, endPosition, path)

                return path

            closed.add(current)

            for i, j in dir:

                neighbor = current[0] + i, current[1] + j

                tempStartToCurrent = startToCurrentCost[current] + self.heuristic(current, neighbor)

                neighborX = neighbor[0]
                neighborY = neighbor[1]

                if ((0 <= neighbor[0] < mazeSize) and (0 <= neighbor[1] < mazeSize)):
                    if arr[neighbor[0]][neighbor[1]] == 1:
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

        return False

    def heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def main():
    
    mazeSize = 300
    densityProbability = .3
    array = Utils.makeMatrix(mazeSize, densityProbability)


    startPosition = (280,200)
    endPosition = (145,0)

    AStarTest = AStar(array)

    showPathFinderAnimation = False

    path = AStarTest.getShortestPath(startPosition, endPosition, showPathFinderAnimation)

    print(path)


if __name__ == "__main__":
    main()