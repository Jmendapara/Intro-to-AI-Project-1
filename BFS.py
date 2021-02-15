# Python program to find the shortest
# path between a given source cell 
# to a destination cell.

from collections import deque
from utils import Utils
from copy import copy, deepcopy
import matplotlib.pyplot as plt

ROW = 9
COL = 10


# To store matrix cell cordinates
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source

# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell 
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

class AStar:

    def __init__(self, arr):
        self.arr = arr
        self.mazeSize = arr.shape[0]


# Function to find the shortest path between
# a given source cell to a destination cell. 
    def getShortestPath(self, src: Point, dest: Point, showPathFinderAnimation):
        # check source and destination cell
        # of the matrix have value 1

        mazeSize = self.mazeSize
        arr = deepcopy(self.arr)

        if arr[src.x][src.y] != 1 or arr[dest.x][dest.y] != 1:
            return -1

        visited = [[False for i in range(COL)]
                   for j in range(ROW)]

        # Mark the source cell as visited
        visited[src.x][src.y] = True

        # Create a queue for BFS
        q = deque()

        # Distance of source cell is 0
        s = queueNode(src, 0)
        q.append(s)  # Enqueue source cell

        # Do a BFS starting from source cell
        while q:

            curr = q.popleft()  # Dequeue the front cell

            # If we have reached the destination cell,
            # we are done
            pt = curr.pt
            if pt.x == dest.x and pt.y == dest.y:
                return curr.dist

            # Otherwise enqueue its adjacent cells
            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]

                # if adjacent cell is valid, has path
                # and not visited yet, enqueue it.
                if (isValid(row, col) and
                        arr[row][col] == 1 and
                        not visited[row][col]):
                    visited[row][col] = True
                    Adjcell = queueNode(Point(row, col),
                                        curr.dist + 1)
                    q.append(Adjcell)

                if (showPathFinderAnimation):
                    plt.imshow(arr)
                    plt.pause(0.01)
                    plt.clf()
        # Return -1 if destination cannot be reached
        return -1


# Driver code
def main():
    # mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    #        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    #        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    #        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    #        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    #        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    #        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
    source = Point(5, 5)
    dest = Point(4, 4)

    mazeSize = 10
    densityProbability = .0
    array = Utils.makeMatrix(mazeSize, densityProbability)

    #print(array)

    startPosition = (1, 1)
    endPosition = (9, 9)

    BFSTest = AStar(array)

    showPathFinderAnimation = True

    dist=BFSTest.getShortestPath(source, dest, showPathFinderAnimation)

    if dist != None:
        print("Shortest Path is", dist)
    else:
        print("Shortest Path doesn't exist")


main()