#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:20:23 2022

@author: apple
"""

# output = 2 4 6 7 5 3 1

def odd_even(i):
    if i > n:
        return
    
    if i % 2 != 0:
        odd_even(i+1)
        print(i)
        
    if i % 2 == 0:
        print(i)
        odd_even(i+1)
        
    return

n = 7
# odd_even(1)


# output = 7 5 3 1 2 4 6

def odd_even_1(n):
    if n == 0:
        return
    
    if n %2 ==0:
        odd_even_1(n-1)
        print(n)
        
    if n %2 !=0:
        print(n)
        odd_even_1(n-1)
        
    return

odd_even_1(7)