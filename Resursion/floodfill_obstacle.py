#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:33:29 2022

@author: apple
"""
matrix = [[0, 0, 2, 0],
          [0, 0, 2, 0],
          [2, 2, 0, 0],
          [0, 0, 0, 0]]

m = 4
n = 4


# DFS Algo:
#     1. Mark source
#     2. Visit/Explore all unvisited/unmark neighbours
#     3. Unmark source

directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]

def floodfill(cr, cc, er, ec, matrix):
    if(cr == er and cc == ec):
        return 1
    
    matrix[cr][cc] = 1 # mark
    
    count = 0
    # explore unvisited neighbors
    for d in directions:
        x = cr + d[0]
        y = cc + d[1]
        
        # check for validity
        if(x >= 0 and y >=  0 and x < m and y < n and matrix[x][y] != 1 and matrix[x][y] != 2):
            count += floodfill(x, y, er, ec, matrix)
    
    matrix[cr][cc] = 0 # unmark

    return count


print(floodfill(0, 0, 2, 2, matrix))            