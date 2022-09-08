#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:38:50 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def length(self, node):
        len = 0
        while node:
            len += 1
            node = node.next
            
        return len
    
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if head is None:
        return None
    
    length = self.length(head)
    index = length-n
    
    if index == 0:
        return head.next
    
    temp = head
        
    i = 0
    while i < index - 1:
        temp = temp.next
        i += 1

    temp.next = temp.next.next
    
    return head