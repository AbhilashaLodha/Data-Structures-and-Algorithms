#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:04:04 2022

@author: apple
"""

def maze_path(i, j, m, n):
    if(i == m - 1 and j == n - 1):
        return 1
    
    paths = 0
    if(j + 1 < n):  # right
        paths += maze_path(i, j + 1, m, n)
    
    if(i + 1 < m): # down 
        paths += maze_path(i + 1, j, m , n)
        
    if(i + 1 < m and j + 1 < n): #diagonal path \
        paths += maze_path(i + 1, j + 1, m, n)
        
    return paths


print(maze_path(0, 0, 3, 3))