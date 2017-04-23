import astar
import cv2
import numpy as np

grid = cv2.imread('bin_small.png')[:,:,0];

maze = astar.getMaze(grid)
astar.fillPath(maze)

for i, line in enumerate(maze):
    for j, cell in enumerate(line):
        grid[i][j] = cell.val

cv2.imwrite('astar.png',np.array(grid))