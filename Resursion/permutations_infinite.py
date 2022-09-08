#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:30:29 2022

@author: apple
"""

# ********** TREE 1 ***********


arr = [2, 3, 5, 7]
t = 10

res = []

# output os list of string

def permutation_infinte(target, ans):
    if(target == 0):
        res.append(ans)
        return 1
    
    count = 0
    
    for i in range (0, len(arr)):
        if(target - arr[i] >= 0):
            count += permutation_infinte(target - arr[i], ans + str(arr[i]))
            
    
    return count


# print(permutation_infinte(t, ""))
# print(res)



# output is list of list

import copy
def permutation_infinte_1(target, ans):
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    for i in range (0, len(arr)):
        if(target - arr[i] >= 0):
            ans.append(arr[i])
            count += permutation_infinte_1(target - arr[i], ans)
            ans.pop()
            
    
    return count

# ans=[]
# print(permutation_infinte_1(t, ans))
# print(res)



# ************* TREE 7 ***************

arr = [2, 3, 5, 7]
n = len(arr)
t = 10

res = []

def permutation_infinite_tree7(target, ans, i):
    
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    # choose
    if(i < n and target - arr[i] >= 0):
        ans.append(arr[i])
        count += permutation_infinite_tree7(target - arr[i], ans, 0)
        ans.pop()
    
    # not choose
    if(i < n):
        count += permutation_infinite_tree7(target, ans, i + 1)
    
    return count

ans=[]
print(permutation_infinite_tree7(t, ans, 0))
print(res)