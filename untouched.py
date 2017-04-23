#!/bin/python2.6

import sys
from math import sqrt

class Tile:
    def __init__(self, char, x, y):
        self.char = char
        self.g = 0
        self.h = 0
        self.x = x
        self.y = y
        self.parent = None
        self.setReachable()

    def setReachable(self):
        self.reachable = True
        if self.char in ['-', '+', '|']:
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

def getMaze():
    maze = []
    for i ,line in enumerate(sys.stdin):
        line = list (line.rstrip("\r\n"))
        row = []
        for j in range(len(line)):
            row.append(Tile(line[j], j, i))
        maze.append(row)
    return maze

def fillPath(maze):
    aStar = AStar(maze)
    for tile in aStar.search(maze[1][0], maze[-2][-1]):
        maze[tile.y][tile.x].char = "#"

def printMaze(maze):
    for row in maze:
        for tile in row:
            sys.stdout.write(tile.char)
        print

if __name__ == "__main__":

    maze = getMaze()
    # print(len(maze))
    print(maze)
    fillPath(maze)
    printMaze(maze)