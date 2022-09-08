#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 01:26:44 2022

@author: apple
"""

# Leetcode 328

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head
        
        
        # odd linked list
        odd_head = None
        odd_tail = None
        
        # even linked list
        even_head = None
        even_tail = None
        
        i = 1
        
        curr = head
        
        while curr is not None:
            if(i % 2 == 1):
                if odd_head is None:
                    odd_head = curr
                    odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = curr
            else:
                if even_head is None:
                    even_head = curr
                    even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = curr
                    
            curr = curr.next
            i += 1
        
        even_tail.next = None
        odd_tail.next = even_head
        
        return odd_head