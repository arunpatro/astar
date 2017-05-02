import astar
import cv2
import numpy as np

grid = cv2.imread('bin_tiny.png')[:,:,0];

maze = astar.getMaze(grid)
aStar = astar.AStar(maze)
for tile in aStar.search(maze[2][1], maze[3][5]):
    maze[tile.y][tile.x].val = 127

for i, line in enumerate(maze):
    for j, cell in enumerate(line):
        grid[i][j] = cell.val

cv2.imwrite('astar.png',np.array(grid))
b = cv2.resize( np.array(grid).astype('float'), ( 1500, 1000 ), interpolation = cv2.INTER_NEAREST )
cv2.imwrite('astar_big.png',b)
for i in aStar.search(maze[2][1], maze[3][5]):
    print (i.x, i.y)