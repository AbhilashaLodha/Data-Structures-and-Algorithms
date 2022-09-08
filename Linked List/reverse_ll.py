#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:25:01 2022

@author: apple
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



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