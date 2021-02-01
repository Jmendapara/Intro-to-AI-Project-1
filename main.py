import numpy as np
import random
from DFS import pathExistsDFS

def makeMatrix(size, probability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    return arr


def main():
    mazeSize = 10
    densityProbability = .3
    array = makeMatrix(mazeSize, densityProbability)

    print(array)

    startPosition = (1,1)
    endPosition = (8,8)

    pathExists = pathExistsDFS(array, startPosition, endPosition)

    print(array)


    print(pathExists)


if __name__ == "__main__":
    main()