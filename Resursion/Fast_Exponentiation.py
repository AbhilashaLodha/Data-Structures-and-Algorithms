#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:33:39 2022

@author: apple
"""

# Given a and b, find a to the power b in O(log(b))

# ************* Method 1 *****************

def fast_exp(a, b, temp):
    if b == 1:
        return a * temp
    
    if b % 2 == 1:
        temp *= a
        
    rec = fast_exp(a * a, int(b / 2), temp)
    
    return rec


# print(fast_exp(10, 4, 1))

# ************* Method 2 *****************

def fast_exp_2(a, b):
    if b == 0:
        return 1
    
    rec = fast_exp_2(a, int(b / 2))
    print(rec)
    
    ans = 0
    
    if b % 2 == 1:
        ans = rec * rec * a
    else:
        ans = rec * rec
    
    return ans

print(fast_exp_2(3, 13))