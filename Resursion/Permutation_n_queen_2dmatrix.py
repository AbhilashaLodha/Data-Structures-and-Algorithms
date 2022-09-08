#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:15:13 2022

@author: apple
"""

'''
Permutation - place 3 queens q0,q1,q2 in 2-D marix based boxes

[[0,1,2]
[3,4,5]
[6,7,8]]


here 2 refers to (0,1)
similarly 5 refers to (1,2) which we can calculate as

x-value : int(5/(total no. of col)) = 1
y-value : 5%(total no. of col) = 2

hence the value (1,2) for 5
'''



def permutation_queens_2D(b,q,ans,vis):
    if q==tq:
        print(ans)
        return 1
    
    count=0
    if b<=total_boxes - 1 and vis[b]==False:
        
        r = int(b / m)
        c = b % m
        
        vis[b]=True
        count+=permutation_queens_2D(0,q+1,ans+"bx"+str(r)+"by"+str(c)+"q"+str(q)+" ",vis)
        vis[b]=False
        
    if b<=8:
        count+=permutation_queens_2D(b+1,q,ans,vis)
        
    return count

tq = 3
n = 3
m = 3
total_boxes = n * m


print(permutation_queens_2D(0,0,"",[False]*total_boxes))