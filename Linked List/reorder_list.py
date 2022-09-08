#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:46:04 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    prev = None
    curr = head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    head = prev
    return head

def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head is None or head.next is None:
        return
    
    mid_node = self.middleNode(head)
    
    first = head
    second = mid_node.next
    mid_node.next = None # breaking the link
    
    second = self.reverseList(second)
    
    while first and second:
        # saving the next nodes
        temp1 = first.nexts
        temp2 = second.next
        
        # reordering the list (making connections)
        first.next = second
        second.next = temp1
        
        # traversing forward
        first = temp1
        second = temp2