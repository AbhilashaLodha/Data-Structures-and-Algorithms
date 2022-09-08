#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:31:28 2022

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

def isPalindrome(self, head: ListNode) -> bool:
    if head is None or head.next is None:
        return True
    
    mid_node = self.middleNode(head)
    
    first = head
    second = mid_node.next
    mid_node.next = None # breaking the link
    
    second = self.reverseList(second)
    
    while first and second:
        if first.val != second.val:
            return False
        
        first = first.next
        second = second.next
        
    
    return True