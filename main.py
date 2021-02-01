import numpy as np
import random
from matplotlib import pyplot
from matplotlib import colors
from DFSclass import DFS


def makeMatrix(size, probability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    return arr


def main():
    
    mazeSize = 20
    densityProbability = .3
    array = makeMatrix(mazeSize, densityProbability)


    startPosition = (2,10)
    endPosition = (18,19)

    DFStest = DFS(array)

    pathExists = DFStest.pathExistsDFS(startPosition, endPosition, True)

    print(pathExists)


if __name__ == "__main__":
    main()