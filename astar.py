#!/bin/python2.6

import sys
from math import sqrt

class Tile:
    def __init__(self, val, x, y):
        self.val = val
        self.g = 0
        self.h = 0
        self.x = x
        self.y = y
        self.parent = None
        self.setReachable()

    def setReachable(self):
        self.reachable = True
        if self.val > 30:
            self.reachable = False

    def move_cost(self, other):
        if other.reachable:
            return 10
        else:
            return 1000

class AStar:

    def __init__(self, maze):
        self.maze = maze

    def getAdjacent(self, cell):
        mazeWidth = len(self.maze[0])
        mazeHeight = len(self.maze)
        ret = []
        if cell.y > 0:
            ret.append(self.getTileAtCoords(cell.x, cell.y - 1))
        if cell.x < mazeWidth - 1:
            ret.append(self.getTileAtCoords(cell.x + 1, cell.y))
        if cell.y < mazeHeight - 1:
            ret.append(self.getTileAtCoords(cell.x, cell.y + 1))
        if cell.x > 0:
            ret.append(self.getTileAtCoords(cell.x - 1, cell.y))
        return ret

    def heuristic(self, cell):
        return sqrt((self.end.x - cell.x)**2 + (self.end.y - cell.y)**2)

    def constructPath(self, current):
        path = []
        while current.parent:
            path.append(current)
            current = current.parent
        path.append(current)
        return path[::-1]

    def getTileAtCoords(self, x, y):
        try:
            return self.maze[y][x]
        except KeyError as e:
            print "Could not find tile at position x: {0} y: {1}".format(x, y)

    def search(self, current, end):
        self.end = end
        openset = set()
        closedset = set()
        openset.add(current)
        # print ('{0} {1}'.format(len(openset),len(closedset)))
        while len(openset):
            current = min(openset, key=lambda o:o.g + o.h)
            if current == end:
                return self.constructPath(current)
            openset.remove(current)
            closedset.add(current)
            for node in self.getAdjacent(current):
                if node in closedset:
                    continue
                if node in openset:
                    new_g = current.g + current.move_cost(node)
                    if node.g > new_g:
                        node.g = new_g
                        node.parent = current
                else:
                    node.g = current.g + current.move_cost(node)
                    node.h = self.heuristic(node)
                    node.parent = current
                    openset.add(node)

def fillPath(maze):
    aStar = AStar(maze)
    for tile in aStar.search(maze[0][0], maze[-1][-1]):
        maze[tile.y][tile.x].val = 127

def printMaze(maze):
    for row in maze:
        for tile in row:
            sys.stdout.write(str(tile.val))
        print

def getMaze(grid):
    maze = []
    for i ,line in enumerate(grid):
        row = []
        for j in range(len(line)):
            row.append(Tile(line[j], j, i))
        maze.append(row)
    return maze

if __name__ == "__main__":

    grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1],
            [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1],
            [1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1],
            [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1],
            [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    maze = getMaze(grid)
    fillPath(maze)
    for line in maze:
        print [i.val for i in line]
