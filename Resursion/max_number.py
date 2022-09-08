#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:51:35 2022

@author: apple
"""

# find max number in array

def max_number(arr, i, max):
    if i == n:
        return max
    
    if arr[i] > max:
        max = arr[i]
        
    final_max = max_number(arr, i+1, max)
    return final_max

arr = [2, 5, 4, 7, 3]
n = len(arr)
print(max_number(arr, 0, arr[0]))


# find max number and its position in array

def max_number(arr, i, max, pos):
    if i == n:
        return max, pos
    
    if arr[i] > max:
        max = arr[i]
        pos = i
        
    final_max, pos = max_number(arr, i+1, max, pos)
    return final_max, pos

arr = [2, 5, 4, 7, 3, 10]
n = len(arr)
print(max_number(arr, 0, arr[0], 0))