#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 13:34:35 2022

@author: apple
"""

# Knight's tour

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

n=8
grid = [[0] * 8,
        [0] * 8,
        [0] * 8,
        [0] * 8,
        [0] * 8,
        [0] * 8,
        [0] * 8,
        [0] * 8]



def KnightTour(r,c,steps):
    grid[r][c] = steps # mark the step
    
    if steps == n * n: # base case
        return True
    
    
    for i in range(0,n): # try moves
        x = r + move_x[i]
        y = c + move_y[i]
        
        if x >= 0 and y >= 0 and x < n and y < n and grid[x][y] == 0: # check for safety
            solvable = KnightTour(x,y,steps+1)
            if solvable: # if current moves results to an answer then return True
                return True
        
    grid[r][c] = 0 # if no moves possible then unmark and return False
    return False



KnightTour(0, 0, 1)
print(grid)
    
    