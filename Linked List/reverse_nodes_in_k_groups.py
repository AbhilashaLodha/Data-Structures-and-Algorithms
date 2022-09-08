#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:11:56 2022

@author: apple
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def size(self, node):
    curr = node
    
    count = 0
    
    while curr :
        curr = curr.next
        count += 1
    
    return count

def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    
    # final answer's head and tail
    oh = None # original head
    ot = None # original tail

    # used to reverse groups one by one
    th = None # temp head
    tt = None # temp tail
    
    size = self.size(head)
   
    if k > size: 
        return head
   
    K = k
    curr = head
   
    while size >= k:
        
        while K > 0: # reversing nodes of a group size k
            temp = curr.next
            curr.next = None
           
            # add first
            if th is None:
                th = curr
                tt = curr
            else:
                curr.next = th
                th = curr
                
            curr = temp
            
            K -= 1
       
        if oh is None: # joining first reversed group to the answer
            oh = th
            ot = tt
        else: # joining rest of the reversed groups to the answer
            ot.next = th
            ot = tt
        
        th = None
        tt = None
       
        size -= k
        K = k
    
   
    ot.next = curr
   
    return oh