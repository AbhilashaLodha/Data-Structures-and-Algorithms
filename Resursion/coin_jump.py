#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:36:37 2022

@author: apple
"""

### if given an array of coins, print the total number of ways, target is achieved
### eg. if we have 5,1,2,3 coins then ways to achieve target 10 (we can use one coin only once)

## seaparation of concern




def coin_jump(arr,i,ans,coins):
    
    if i == n:
        if ans == 10:
            coins = coins+1
            print(coins)
            return coins
        return 0
    
    # if(i + 1 < n):
    count = 0
    count += coin_jump(arr,i+1,ans+arr[i],coins)
    count += coin_jump(arr,i+1,ans,coins)
    
    return count
        
arr = [5,5,2,3]
n = len(arr)   
print(coin_jump(arr,0,0,0))






def coin_jump_1(arr,i,ans):
    
    
    if ans == 10:
        return 1
    
    count = 0
    if i + 1 <= n and ans + arr[i] <= 10:
        count += coin_jump_1(arr,i+1,ans+arr[i])
    
    if i + 1 <= n:    
        count += coin_jump_1(arr,i+1,ans)
        
    return count
        
arr = [5,5,2,3]
n = len(arr)   
# print(coin_jump_1(arr,0,0))