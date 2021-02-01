import numpy as np
import random
from DFS import pathExistsDFS
from matplotlib import pyplot
from matplotlib import colors


def makeMatrix(size, probability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    return arr


def main():
    mazeSize = 20
    densityProbability = .05
    array = makeMatrix(mazeSize, densityProbability)

    print(array)

    startPosition = (2,10)
    endPosition = (18,19)

    pathExists = pathExistsDFS(array, startPosition, endPosition)

    print(array)


    print(pathExists)


if __name__ == "__main__":
    main()