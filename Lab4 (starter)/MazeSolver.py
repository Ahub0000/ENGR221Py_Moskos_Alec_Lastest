"""
# Filename: Lab 4
# Author Alec M
# Created: 2026-02-28-26
# Description: 
# This program creates a Stack and a Queue and uses them to
# solve a maze. It finds a path from the start (S) to the
# goal (G) and prints the solution.
"""

import sys, os 
sys.path.append(os.path.dirname(__file__))

from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:

    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object (Stack or Queue)

    def tileIsVisitable(self, row, col):
        # 1) check if row/col are inside maze boundries
        if row < 0  or row >= self.maze.num_rows:           # Write your tileIsVisitable() implementation here
            return False
        if col < 0 or col >= self.maze.num_cols:
            return False
        
        tile = self.maze.contents[row][col]

        #2 Get the title at the position
        if tile.getIsWall():
            return False        
        
        #4 Check is it is a wall
        if tile.isVisited():
            return False
        
        return True
    
    def solve(self):
        # Add start tile to the search structure 
        self.ss.add(self.maze.start)

        while not self.ss.isEmpty():

            current = self.ss.remove()

            #Skip if already visited
            if current.isVisited():
                continue

            current.visit()

            #If goal reached, return it
            if current == self.maze.goal:
                return current
            
            r = current.getRow()
            c = current.getCol()

            #Neighbor directions (N, S, E, W)
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                if self.tileIsVisitable(new_row, new_col):
                    neighbor = self.maze.contents[new_row][new_col]
                    neighbor.setPrevious(current)  # use Tile method 
                    self.ss.add(neighbor)

        # No path found
        return None

        # ~~~~~~~~


    def getPath(self):
        # If goal was never reached, no solution
        if self.maze.goal.getPrevious() is None and self.maze.goal != self.maze.start:
            return []

        path = []
        current = self.maze.goal

     # Follow previous pointers back to start
        while current is not None:
            path.append(current)
            current = current.getPrevious()

    # Reverse so it goes Start -> Goal
        path.reverse()
        return path

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
    # Get the solution path (list of Tiles)
        solution = self.getPath()
    # Get a printable maze (list of lists of characters)
        output_string = self.maze.makeMazeBase()

    # Mark the solution path with '*'
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'

    # Put S and G back (so they don't get overwritten)
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

    # Print each row
        for row in output_string:
         print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()