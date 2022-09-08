#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 21:42:04 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def swapPairs(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head;
   
    dummy = ListNode();
    prev = dummy;
    curr = head;
   
    while curr and curr.next:
        forw = curr.next.next;
       
        curr.next.next = curr;
        prev.next = curr.next;
        curr.next = forw;
       
        prev = curr;
        curr = forw;
    
   
    return dummy.next;