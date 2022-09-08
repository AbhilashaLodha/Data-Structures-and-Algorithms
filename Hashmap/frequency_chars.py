#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 00:56:42 2022

@author: apple
"""

def frequency(name):
    freq_map = {}
    
    for char in name:
        if char in freq_map:
            freq_map[char] = freq_map[char] + 1
        else:
            freq_map[char] = 1
        
    return freq_map


print(frequency("My name is Abhilasha"))