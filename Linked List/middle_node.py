#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:11:18 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

# Question is to find just the middle node
def middleNode(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    slow = head
    fast = head
    
    # 1->2->3->4->5->6 mein we need to pick 4
    # even and odd
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow


# When we need to use this function as an utility
def middleNode_1(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    slow = head
    fast = head
    
    # 1->2->3->4->5->6 mein we need to pick 3
    # odd and even
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
        