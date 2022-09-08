#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:01:52 2022

@author: apple
"""

class Int:
    
    def __init__(self, x):
        self.x = x
    
    def __lt__(self, other):
        # print(self.nums)
        # print("comparing " + str(self.x) + " and " + str(other.x))
        return self.x < other.x

    # def __gt__(self, other):
    #     return self.x < other.x

def sorting(nums):
    
    print(sorted(nums))
    
    l = []
    for a in nums:
        int_ = Int(a)
        l.append(int_)
    
    l.sort()
    for a in l:
        print(a.x)


class Freq_Array:
    def __init__(self, k, v):
        self.k = k
        self.v = v
    
    def __lt__(self, other):
        return self.v < other.v
        
    
                
def frequencySort(nums):
    dic = {}
    for ele in nums:
        if ele in dic:
            dic[ele] = dic[ele] + 1
        else:
            dic[ele] = 1
            
    # print(dic)
    
    key_values = []
    for k in dic:
        key_value = Freq_Array(k,dic[k])
        key_values.append(key_value)
    
    
    for i in key_values:
        print(str(i.k) + ", " + str(i.v))
        
    key_values1 = sorted(key_values)
    print("=============")
    
    for i in key_values1:
        print(str(i.k) + ", " + str(i.v))
    # for i in key_values:
    #     print(i.k)

frequencySort([10, 10, 10, 5, 6, 7, 1, 5, 5, 0, 0, -1, 20, 20, 6, 7])
        
    
    