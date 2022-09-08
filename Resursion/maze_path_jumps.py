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

def maze_path_obstacle_jump(cr, cc, tr, tc):   # cr=current row, cc=current column, tr=target row, tc=target column
    if(cr == tr and cc == tc):
        return 1
    
    paths = 0
    
    for i in range(1, m):
        if(cc + i <= tc and matrix[cr][cc + i] != 1):  # right
            paths += maze_path_obstacle_jump(cr, cc + i, tr, tc)
            
    for j in range(1, n):
        if(cr + j <= tr and matrix[cr + j][cc] != 1): # down
            paths += maze_path_obstacle_jump(cr + j, cc, tr , tc)
        
    return paths


print(maze_path_obstacle_jump(0, 0, 3, 3))