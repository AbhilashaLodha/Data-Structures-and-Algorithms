#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:01:46 2022

@author: apple
"""

code = "51234"
n = len(code)

# print(int(code[0]))

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encoding(code, i, ans):
    if i == n:
        print(ans)
        return 1 
    
    idx = int(code[i])
    if idx == '0':
        return 0
    
    count = 0
    
    count += encoding(code, i + 1, ans + alphabets[idx - 1])
    
    if i < n - 1:
        idx2 = int(code[i + 1])
        index = idx * 10 + idx2
        if index >= 10 and index <= 26:
            count += encoding(code, i + 2, ans + alphabets[index - 1])
        
    return count


print(encoding(code, 0, ""))