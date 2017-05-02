import astar
import cv2
import numpy as np

grid = cv2.imread('bin2.png')[:,:,0];

maze = astar.getMaze(grid)
astar.fillPath(maze)

for i, line in enumerate(maze):
    for j, cell in enumerate(line):
        grid[i][j] = cell.val

cv2.imwrite('astar.png',np.array(grid))
b = cv2.resize( np.array(grid).astype('float'), ( 1500, 1000 ), interpolation = cv2.INTER_NEAREST )
cv2.imwrite('astar_big.png',b)