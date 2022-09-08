#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 00:13:40 2022

@author: apple
"""

# idx = position of box
# qp = current queen we are talking about
# tq = total queen
# ans = forming the answer

# tries to place Queen Number "QP" from index "idx" to 6
def Queens3_Boxes6_Combination(box, idx, qp, tq, ans):
    if qp == tq:
        print(ans)
        return 1
    
    count = 0
    
    # this loop places Queen Number "QP" at "j" index,
    # and then calls the recursive function to place "QP + 1" queen in the further indexes
    
    for j in range(idx, len(box)):
        count += Queens3_Boxes6_Combination(box, j + 1, qp + 1, tq, 
                                            ans + "b" + str(j) + "q" + str(qp) + " ")
        
    
    return count

print(Queens3_Boxes6_Combination([False] * 6, 0, 0, 3, ""))




# Subsequence Method
def Queens3_Boxes6_Combination_SubSequence(box, idx, qp, tq, ans):
    if qp == tq:
        print(ans)
        return 1
    
    count = 0
    if(idx < len(box) and qp < tq):
        count += Queens3_Boxes6_Combination_SubSequence(box, idx + 1, qp + 1, tq, ans + "b" + str(idx) + "q" + str(qp) + " ")
    
    if(idx < len(box)):
        count += Queens3_Boxes6_Combination_SubSequence(box, idx + 1, qp, tq, ans)
        
    return count

# print(Queens3_Boxes6_Combination_SubSequence([False] * 6, 0, 0, 3, ""))
