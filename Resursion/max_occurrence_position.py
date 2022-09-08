#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:03:18 2022

@author: apple
"""
# not a good method
def max_occurrence_pos(arr, i, lst):
    if i == n:
        return lst
    
    if arr[i] == 2:
        lst.append(i)
        
    final_lst = max_occurrence_pos(arr, i+1, lst)
    return final_lst


# arr = [3, 4, 9, 2, 2, 4, 2, 8]
# n = len(arr)
# print(max_occurrence_pos(arr, 0, []))



# good method - faith that smaller inputs would do their work

def max_occ(arr, i):
    if i == n:
        return []
    
    level = []
    if arr[i] == 2:
        level.append(i)
        
    recAns = max_occ(arr, i+1)
    if len(recAns) > 0:
        level.extend(recAns)
        
    return level

# arr = [3, 4, 9, 2, 2, 4, 2, 8]
# n = len(arr)
# print(max_occ(arr, 0))



# printing would be in reverse order


def max_occ_1(arr, i):
    if i == n:
        return []
        
    recAns = max_occ_1(arr, i+1)
    
    level = []
    if len(recAns) > 0:
        level.extend(recAns)
        
    if arr[i] == 2:
        level.append(i)
        
    return level

arr = [3, 4, 9, 2, 2, 4, 2, 8]
n = len(arr)
print(max_occ_1(arr, 0))

