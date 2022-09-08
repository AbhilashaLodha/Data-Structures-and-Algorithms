#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 12:59:16 2022

@author: apple
"""

# Permutation n queens 6 boxes
# Placing queens (p) (p0,p1,p2) in boxes (b) ranging from 0 to 5.


tb=6
tp=3


def f(b,p,ans,vis):
    if p==tp:
        print(ans)
        return 1
    
    count=0
    if b<tb and not vis[b]:
        vis[b]=True
        count+=f(0,p+1,ans+"p"+str(p)+"b"+str(b)+" ",vis)
        vis[b]=False
        
    if b<tb:
        count+=f(b+1,p,ans,vis)
        
    return count

print(f(0,0,"",[False]*tb))       