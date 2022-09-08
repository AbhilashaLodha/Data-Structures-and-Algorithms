#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:03:43 2022

@author: apple
"""

# ************ TREE 2 *************

arr = [2, 3, 5, 7]
t = 10

res = []

import copy
def combination_infinte(target, ans, i):
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    for j in range (i, len(arr)):
        if(target - arr[j] >= 0):
            ans.append(arr[j])
            count += combination_infinte(target - arr[j], ans, j)
            ans.pop()
            
    
    return count

# ans=[]
# print(combination_infinte(t, ans, 0))
# print(res)


# ************* TREE 6 ***************

arr = [2, 3, 5, 7]
n = len(arr)
t = 10

res = []

def combination_single_tree6(target, ans, i):
    
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    # choose
    if(i < n and target - arr[i] >= 0):
        ans.append(arr[i])
        count += combination_single_tree6(target - arr[i], ans, i)
        ans.pop()
    
    # not choose
    if(i < n):
        count += combination_single_tree6(target, ans, i + 1)
    
    return count

ans=[]
print(combination_single_tree6(t, ans, 0))
print(res)
