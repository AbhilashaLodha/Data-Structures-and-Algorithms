#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:13:13 2022

@author: apple
"""

matrix = [[0, 0, 0, 1],
          [0, 0, 1, 0],
          [1, 0, 1, 0],
          [0, 0, 0, 0]]

n = 4
m = 4

def maze_path_obstacle(cr, cc, tr, tc):   # cr=current row, cc=current column, tr=target row, tc=target column
    if(cr == tr and cc == tc):
        return 1
    
    paths = 0
    if(cc + 1 <= tc and matrix[cr][cc + 1] != 1):  # right
        paths += maze_path_obstacle(cr, cc + 1, tr, tc)
    
    if(cr + 1 <= tr and matrix[cr + 1][cc] != 1): # down
        paths += maze_path_obstacle(cr + 1, cc, tr , tc)
        
    return paths


print(maze_path_obstacle(0, 0, 3, 3))