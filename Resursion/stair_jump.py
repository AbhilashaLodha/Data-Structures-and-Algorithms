#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:11:08 2022

@author: apple
"""

n=3
def stair_jump(i,ans):
    if i == n:
        print(ans)
        return 1
    
    count = 0
    
    count += stair_jump(i+1, ans + str(i + 1))
    
    if i < n-1:
        count += stair_jump(i+2, ans + str(i + 2))
        
    return count
    
    
    
print(stair_jump(0,"0"))



def stair_jump_1(i):
    
    if i == n:
        # print(ans)
        return 1
    
    count = 0
    
    if i + 1 <= n:
        count += stair_jump(i+1)
    
    if i + 2 <= n:
        count += stair_jump(i+2)
        
    return count


def stair_jump_2(i):
    
    if i > n:
        return 0
    
    if i == n:
        # print(ans)
        return 1
    
    count = 0
    
    
    count += stair_jump(i+1)


    count += stair_jump(i+2)
        
    return count
