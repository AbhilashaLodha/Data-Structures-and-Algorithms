#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:31:07 2022

@author: apple
"""

# fibbonacci

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    a = fibonacci(n-1)
    b = fibonacci(n-2)
    
    return a+b

print(fibonacci(5))