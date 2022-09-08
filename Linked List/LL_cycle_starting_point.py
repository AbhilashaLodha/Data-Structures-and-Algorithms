#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:30:55 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next;
        fast = fast.next.next;
        if slow == fast:
            break;

    if slow != fast:
        return None;

    slow = head;
    while slow != fast:

        slow = slow.next;
        fast = fast.next;

    return slow;