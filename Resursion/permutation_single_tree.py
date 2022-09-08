#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 16:18:18 2022

@author: apple
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:56:53 2022

@author: apple
"""

# **************** TREE 3 ******************

import copy

res = []
small_ans = []

arr = [2, 3, 5, 7]
target = 10
n = len(arr)

def permutations_single_tree3(target, vis):
    if target == 0:
        base = copy.deepcopy(small_ans)
        res.append(base)
        return 1
    
    c = 0
    
    for i in range(0, n):
        if not vis[i]:
            small_ans.append(arr[i])
            vis[i] = True  # mark
            
            c += permutations_single_tree3(target - arr[i], vis) # visiting all neighbours
            
            # backtracking -> going to prevous state; with the help of unmark, we got to explore that state again
            small_ans.pop()  # unmark
            vis[i] = False
    
    return c


# print(permutations_single_tree3(target, [False] * n))
# print(res)




# ************* TREE 8 ***************

arr = [2, 3, 5, 7]
n = len(arr)
t = 10

res = []

def permutation_single_tree8(target, ans, i, vis):
    
    if(target == 0):
        small_ans = copy.deepcopy(ans)
        res.append(small_ans)
        return 1
    
    count = 0
    
    # choose
    if(i < n and target - arr[i] >= 0 and not vis[i]):
        ans.append(arr[i])
        vis[i] = True
        
        count += permutation_single_tree8(target - arr[i], ans, 0, vis)
        
        vis[i] = False
        ans.pop()
    
    # not choose
    if(i < n):
        count += permutation_single_tree8(target, ans, i + 1, vis)
    
    return count

ans=[]
print(permutation_single_tree8(t, ans, 0, [False] * n))
print(res)