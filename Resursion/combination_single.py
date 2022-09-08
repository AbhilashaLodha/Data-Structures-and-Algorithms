#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:14:33 2022

@author: apple
"""

# ************ TREE 4 *************

arr = [2, 3, 5, 7]
t = 10

res = []

import copy
def combination_single(target, ans, i):
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    for j in range (i, len(arr)):
        if(target - arr[j] >= 0):
            ans.append(arr[j])
            count += combination_single(target - arr[j], ans, j + 1)
            ans.pop()
            
    
    return count

# ans=[]
# print(combination_single(t, ans, 0))
# print(res)




# ************* TREE 5 ***************

arr = [2, 3, 5, 7]
n = len(arr)
t = 10

res = []

def combination_single_tree5(target, ans, i):
    
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    # choose
    if(i < n and target - arr[i] >= 0):
        ans.append(arr[i])
        count += combination_single_tree5(target - arr[i], ans, i + 1)
        ans.pop()
    
    # not choose
    if(i < n):
        count += combination_single_tree5(target, ans, i + 1)
    
    return count

ans=[]
print(combination_single_tree5(t, ans, 0))
print(res)


