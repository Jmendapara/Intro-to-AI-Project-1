import numpy as np
import random

def makeMatrix(size, densityProbability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    print (arr)


def main():
    mazeSize = 10
    densityProbability = .4
    makeMatrix(size, probability)


if __name__ == "__main__":
    main()