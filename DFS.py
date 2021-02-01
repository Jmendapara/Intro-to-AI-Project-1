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

            print('looking at:' + str(a) + ' ' + str(b))

             
            #not blocked and valid
            if(a>=0 and b>=0 and a<mazeSize and b<mazeSize and arr[a][b]!=-1 and arr[a][b]!=1):
            
                stack.append((a,b))


    return False
    
