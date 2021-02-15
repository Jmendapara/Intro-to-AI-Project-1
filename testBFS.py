import collections
from collections import deque
from utils import Utils

def bfs(grid, start, end):

    mazeSize = grid.shape[0]
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if(x == end[0] and y == end[1]):
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < mazeSize and 0 <= y2 < mazeSize and grid[y2][x2] != 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
 
    return False
    
if __name__ == '__main__':
 
    mazeSize = 10
    densityProbability = .1
    
    array = Utils.makeMatrix(mazeSize, densityProbability)

    path = bfs(array, (0, 0), (9,9))

    print(path)