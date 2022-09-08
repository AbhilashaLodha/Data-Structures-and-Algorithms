#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:24:15 2022

@author: apple
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:56:53 2022

@author: apple
"""

input = [".:?","abc","def","ghi","jkl","mno","pqrs","tur","wx","yz"]
data = "589" 
count=0

# def nokia_keypad(input,data,smallAns,count):
#     if count == 3:
#         print(smallAns)
#         return 1
        
#     for no in data:
#         smallAns = []
#         count = 0
#         for word in input[int(no)]:    
#             smallAns.append(word)
#             count += nokia_keypad(input,data,smallAns,count)
        
#     return count


def nokia_keypad(i):
    
    if i == len(data):
        return [""]
    
    digit = int(data[i])
    word = input[digit]
    n = len(word)
    
    rec_ans = nokia_keypad(i + 1)
    res = []
    
    for j in range(0, n):
        char = word[j]
        for r in rec_ans:
            res.append(char + r)
            
    return res
        
print(nokia_keypad(0))