from collections import deque
from utils import Utils
# from utils import showFinalPlot
# from utils import makeMatrix
import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import heapq

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Arr:

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]


class Node:

    def __init__(self, pt: Point, dist: int):
        self.pt=pt
        self.dist=dist

    def __repr__(self):
        return str((self.x, self.y))


row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


def isValid(x, y):
    return (0 <= x < N) and (0 <= y < N)


def findPath(array, x, y):
    q = deque()
    src = Node(startPosition, y, None)
    Dest=Node()
    q.append(src)

    visited = set()

    key = (src.x, src.y)
    visited.add(key)

    while q:

        curr = q.popleft()
        i = curr.startPosition
        j = curr.endPosition

        if i == N - 1 and j == N - 1:
            return curr

        n = array[i][j]

        for k in range(4):

            x = i + row[k] * n
            y = j + col[k] * n

            if isValid(x, y):

                next = Node(x, y, curr)
                key = (next.x, next.y)

                if key not in visited:
                    q.append(next)
                    visited.add(key)

    return None


def printPath(node):
    if node is None:
        return 0

    length = printPath(node.parent)
    print(node, end=' ')
    return length + 1


if __name__ == '__main__':

    """matrix = [
        [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
        [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
        [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
        [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
        [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
        [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
        [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
        [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
        [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
        [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
    ]"""

    # N = len(matrix)

    mazeSize = 20
    densityProbability = .3
    array = Utils.makeMatrix(mazeSize, densityProbability)

    startPosition = (2, 10)
    endPosition = (18, 19)

    bfsTest = Arr(array)

    # pathExists = bfsTest.pathExists(startPosition, endPosition, True)

    # print(pathExists)

    # Find a route in the matrix from source cell `(0, 0)` to
    # destination cell `(N-1, N-1)`
    node = findPath(array, 0, 0, 3, 4)

    if node:
        print("The shortest path is ", end='')
        length = printPath(node) - 1
        print("\nThe shortest path length is", length)
    else:
        print("Destination is not found")
