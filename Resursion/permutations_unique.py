#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:56:53 2022

@author: apple
"""


import copy

res = []
small_ans = []

arr = [1, 2, 3]
n = len(arr)

def permutations_unique(arr, vis, count):
    if count == n:
        base = copy.deepcopy(small_ans)
        res.append(base)
        return 1
    
    c = 0
    
    for i in range(0, n):
        if not vis[i]:
            small_ans.append(arr[i])
            vis[i] = True  # mark
            
            c += permutations_unique(arr, vis, count + 1) # visiting all neighbours
            
            # backtracking -> going to prevous state; with the help of unmark, we got to explore that state again
            small_ans.pop()  # unmark
            vis[i] = False
    
    return c


print(permutations_unique(arr, [False] * n, 0))
print(res)

