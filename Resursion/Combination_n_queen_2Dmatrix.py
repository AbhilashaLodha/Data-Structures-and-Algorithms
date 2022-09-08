#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:53:03 2022

@author: apple
"""

'''

'''

def combination_queens_2D(b,q,ans):
    if q==tq:
        print(ans)
        return 1
    
    count=0
    
    if b<=total_boxes - 1:
        
        r = int(b / m)
        c = b % m
        
        count+=combination_queens_2D(b+1,q+1,ans+"bx"+str(r)+"by"+str(c)+"q"+str(q)+" ")
        
    if b<=8:
        count+=combination_queens_2D(b+1,q,ans)
        
    return count


tq = 3
n = 3
m = 3
total_boxes = n * m

print(combination_queens_2D(0,0,""))
