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

arr = [2, 3, 6, 8, 10]
n = len(arr)
array_print(arr,0)