#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:33:26 2022

@author: apple
"""

# print an array using recusrion 

def array_print(arr,i):
    if i == n:
        return
    
    print(arr[i])
    array_print(arr, i+1)
    return

# arr = [2, 3, 6, 8, 10]
# n = len(arr)
# array_print(arr,0)


# print array in reversed form using recursion

def reverse_array(arr,i):
    if i == n:
        return
    
    reverse_array(arr, i+1)
    print(arr[i])
    return

# arr = [2, 3, 6, 8, 10]
# n = len(arr)
# reverse_array(arr,0)


# reverse array and store in a list

def reverse_array_lst(arr,i):
    if i == n:
        return []
    
    smallAns = reverse_array_lst(arr, i+1)
    smallAns.append(arr[i])
    return smallAns

arr = [2, 3, 6, 8, 10]
n = len(arr)
print(reverse_array_lst(arr,0))


