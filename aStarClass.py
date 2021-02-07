import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq


class AStar: 

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]
    
    def showFinalPlot(self, startPosition, endPosition, path):

        arr = deepcopy(self.arr)

        for i in (range(0,len(path))):

            x = path[i][0]

            y = path[i][1]

            arr[x][y] = 2

        startX = startPosition[0]
        startY = startPosition[1]

        arr[startX, startY] = 3

        endX = endPosition[0]
        endY = endPosition[1]

        arr[endX, endY] = 4

        plt.imshow(arr)
        plt.show()


    def getShortestPath(self, startPosition, endPosition, showGraph):
    
        mazeSize = self.mazeSize
        arr = deepcopy(self.arr)

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        close_set = set()

        came_from = {}

        gscore = {startPosition:0}

        fscore = {startPosition:self.heuristic(startPosition, endPosition)}

        oheap = []

        heapq.heappush(oheap, (fscore[startPosition], startPosition))

        startX = startPosition[0]
        startY = startPosition[1]

        arr[startX, startY] = 2
    

        while oheap:

            current = heapq.heappop(oheap)[1]

            currentX = current[0]
            currentY = current[1]

            arr[currentX, currentY] = -1

            if current == endPosition:

                data = []

                while current in came_from:

                    data.append(current)

                    current = came_from[current]

                data = data + [startPosition]

                data = data[::-1]

                self.showFinalPlot(startPosition, endPosition, data)

                return data

            close_set.add(current)

            for i, j in dir:

                neighbor = current[0] + i, current[1] + j

                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)

                if 0 <= neighbor[0] < arr.shape[0]:

                    if 0 <= neighbor[1] < arr.shape[1]:                

                        if arr[neighbor[0]][neighbor[1]] == 1:

                            continue

                    else:

                        # array bound y walls

                        continue

                else:

                    # array bound x walls

                    continue
    

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):

                    continue
    

                if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:

                    came_from[neighbor] = current

                    gscore[neighbor] = tentative_g_score

                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, endPosition)

                    heapq.heappush(oheap, (fscore[neighbor], neighbor))

            if(showGraph):
                    plt.imshow(arr)
                    plt.pause(0.01)
                    plt.clf()

        return False

    def heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)



def makeMatrix(size, probability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    return arr


def main():
    
    mazeSize = 300
    densityProbability = .4
    array = makeMatrix(mazeSize, densityProbability)


    startPosition = (280,200)
    endPosition = (145,0)

    AStarTest = AStar(array)

    path = AStarTest.getShortestPath(startPosition, endPosition, False)

    print(path)


if __name__ == "__main__":
    main()