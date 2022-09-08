#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:16:48 2022

@author: apple
"""


def sum(n):
    if(n == 1):
        return 1
    
    smallSum = sum(n-1)
    print(smallSum)
    return n + smallSum
    
    
# print(sum(5))



#********** sum of an array *******


def sum_array(arr, i, small_sum):
    if i == n:
        return small_sum
    
    small_sum += arr[i]
    total_sum = sum_array(arr, i+1, small_sum)
    return total_sum

# arr = [2, 5, 7, 3]
# n = len(arr)
# print(sum_array(arr, 0, 0))
    
    
#************ sum of n-natural numbers

def sum_n(i, small_sum):
    if i > n:
        return small_sum
    
    small_sum += i
    total_sum = sum_n(i+1, small_sum)
    
    return total_sum

n = 4
print(sum_n(1,0))
