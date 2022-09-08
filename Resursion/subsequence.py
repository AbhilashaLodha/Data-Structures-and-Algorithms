#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:10:03 2022

@author: apple
"""

# Subsequence
# input =["a","b","c"]
# output = ["","a","b","c","ab","ac","bc","abc"]

# Method 1

def f(arr,i):
    if i==n:
        return [""]
    rA=f(arr,i+1)
    level=[]
    level.extend(rA)
    for x in rA:
        level.append(arr[i]+x)
        print(level)
    return level


# Method 2
def f2(arr,i,ans, ls):
    if i == n:
        ls.append(ans)
        print(ans)
        return 1
    
    count = 0
    count += f2(arr, i + 1, ans + arr[i], ls)
    count += f2(arr, i + 1, ans, ls)
    
    return count

arr=["a","b","c"]
n=len(arr)
# print(f(arr,0))

# call to second method

ls = []
print(f2(arr, 0, "",ls))
print(ls)