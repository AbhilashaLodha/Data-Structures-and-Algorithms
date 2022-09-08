#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:28:45 2022

@author: apple
"""

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def rowValid(x, i): # checks if putting "i" in "xth" row is safe or not
    for j in range(0, 9):
        if grid[x][j] == i:
            return False
        
    return True

def colValid(y, i): # checks if putting "i" in "yth" col is safe or not
    for j in range(0, 9):
        if grid[j][y] == i:
            return False
        
    return True

def boxValid(x, y, i): # checks if putting "i" in that box is safe or not
    
    row = int((x / 3)) * 3
    col = int((y / 3)) * 3
    
    for j in range(row, row + 3):
        for k in range(col, col + 3):
            if grid[j][k] == i:
                return False
        
    return True



def Sudoku(c): # c = cell number
    if c >= 81:
        return True
    
    x = int(c / 9)
    y = c % 9
    
    if grid[x][y] == 0: # if current cell is 0
        for i in range(1, 10):
            if (rowValid(x, i) and
               colValid(y, i) and
               boxValid(x, y, i)):
                   
                   grid[x][y] = i
                   
                   solvable = Sudoku(c + 1)
                   
                   if solvable: # we try to put numbers from 1 to 9 and recurse to new state to check if the selected number results to answer
                       return True
                   else: # if not then we try further numbers
                       grid[x][y] = 0
    else: # if current cell is not 0
        solvable = Sudoku(c + 1) # we move forward to next cell and check if that lead to answer or not
        return solvable
    
    return False # if not solvable at all we return False to the previous state form where this current state was called


Sudoku(0)

print(grid)