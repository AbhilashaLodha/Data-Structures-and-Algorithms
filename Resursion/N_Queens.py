#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:57:53 2022

@author: apple
"""

N = 4

# boxes = [[False] * N] * N
boxes = [[False] * 4,
         [False] * 4,
         [False] * 4,
         [False] * 4]

dir = [[0, -1], [-1, 0], [-1, -1], [-1, 1]]


def isSafe_1(r, c):
    for d in dir:
        for rad in range(1, N + 1):  # rad is radius (1 unit, 2 unit and so on)
            x = r + rad * d[0]
            y = c + rad * d[1]
            #bounding conditions
            if x >= 0 and y >= 0 and x < N and y < N:
                # if queen is already in boxes[x][y], then that particular row, col and diagonals are not safe!!!
                if boxes[x][y] == True:
                    return False
            else:
                break
    
    return True

# ************** METHOD 1 ****************

# i :: box
# q :: queen
def N_Queens_1(i, q, ans):
    
    if q == N:
        print(ans)
        return 1
    
    count = 0
    
    r = int(i / N)
    c = i % N
    
    safe = isSafe_1(r, c)
    
    if i < N * N and safe:
        boxes[r][c] = True
        count += N_Queens_1(i + 1, q + 1, ans + "q" + str(q) + "(" + str(r) + "," + str(c) + ") ")
        boxes[r][c] = False
        
    if i < N * N:
        count += N_Queens_1(i + 1, q, ans)
        
    return count


# print(N_Queens_1(0, 0, ""))



# ************** METHOD 2 ****************

row = [False] * N
col = [False] * N
diagonal = [False] * (N + N - 1)
anti_diagonal = [False] * (N +  N - 1)


def N_Queens_2(i, q, ans):
    if q == N:
        print(ans)
        return 1
    
    count = 0
    
    r = int(i / N)
    c = i % N
    
    
    if i < N * N:
        if(row[r] == False and
           col[c] == False and
           diagonal[r + c] == False and
           anti_diagonal[r - c + N - 1] == False):
            
            row[r] = True
            col[c] = True
            diagonal[r + c] = True
            anti_diagonal[r - c + N - 1] = True
            
            count += N_Queens_2(i + 1, q + 1, ans + "q" + str(q) + "(" + str(r) + "," + str(c) + ") ")
            # If permutations required
            # count += N_Queens_2(0, q + 1, ans + "q" + str(q) + "(" + str(r) + "," + str(c) + ") ")
            
            row[r] = False
            col[c] = False
            diagonal[r + c] = False
            anti_diagonal[r - c + N - 1] = False
        
    if i < N * N:
        count += N_Queens_2(i + 1, q, ans)
        
    return count

# print(N_Queens_2(0, 0, ""))
    


# ************** METHOD 3 ****************

col = [False] * N
diagonal = [False] * (N + N - 1)
anti_diagonal = [False] * (N + N - 1)


def N_Queens_3(r, c, q, ans):
    
    
    if q == N:
        print(ans)
        return 1
    
    count = 0
    
    if r < N and c < N:
        if(col[c] == False and
           diagonal[r + c] == False and
           anti_diagonal[r - c + N - 1] == False):
            
            col[c] = True
            diagonal[r + c] = True
            anti_diagonal[r - c + N - 1] = True
            
            count += N_Queens_3(r + 1, 0, q + 1, ans + "q" + str(q) + "(" + str(r) + "," + str(c) + ") ")
            # If permutations required
            # count += N_Queens_2(0, q + 1, ans + "q" + str(q) + "(" + str(r) + "," + str(c) + ") ")
            
            col[c] = False
            diagonal[r + c] = False
            anti_diagonal[r - c + N - 1] = False
        
    if r < N and c < N:
        count += N_Queens_3(r, c + 1, q, ans)
        
    return count

print(N_Queens_3(0, 0, 0, ""))
    