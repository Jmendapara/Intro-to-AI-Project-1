import numpy as np
import random


def pathExistsDFS(arr, startPosition, endPosition):

    mazeSize = arr.shape[0]



    print('mazesize='+str(mazeSize))

    stack = []

    #directions
    dir = np.array([[0,1], [0,-1], [1,0], [-1,0]])

    print(dir)
     
    #queue 
    stack.append(startPosition)

    print(stack)

    while(len(stack)>0):

        currentPosition = stack.pop()

        currentX = currentPosition[0]
        currentY = currentPosition[1]

        print('current element: ' + str(currentPosition))

        #mark as visited
        arr[currentX, currentY] = -1

        #destination is reached
        if( sorted(currentPosition) == sorted(endPosition) ):
            return True

        #check all four directions
        for i in range(0, 4):
        
            #using the direction array
            a = currentX + dir[i][0]
            b = currentY + dir[i][1]
             
            #not blocked and valid
            if(arr[a][b]!=-1 and arr[a][b]!=1 and a>=0 and b>=0 and a<mazeSize and b<mazeSize):

                print('adding:' + str(a) + ' ' + str(b))

            
                stack.append((a,b))


    return False
    


def makeMatrix(size, probability):
    arr = np.zeros((size, size))

    for x in range(0, size):
        for y in range(0, size):
            if (random.random() < probability): 
                arr[x,y] = 1
    return arr


def main():
    mazeSize = 10
    densityProbability = .4
    array = makeMatrix(mazeSize, densityProbability)

    print(array)

    startPosition = (1,1)
    endPosition = (5,5)

    pathExists = pathExistsDFS(array, startPosition, endPosition)

    print(array)

    print(pathExists)


if __name__ == "__main__":
    main()