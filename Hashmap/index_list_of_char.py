#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:29:39 2022

@author: apple
"""

def index_list_of_char(input_):
    dict_ = {}
    i = 0
    for char in input_:
        if char not in dict_:
            lst = []
            dict_[char] = lst
            
        
        dict_[char].append(i)
        
        i += 1
        
    return dict_
    
    
    
    
    
    
print(index_list_of_char("abhilasha is best"))