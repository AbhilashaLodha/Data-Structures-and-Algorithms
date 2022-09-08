#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:20:04 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        if head is None:
            return head
        
        fakeHead = ListNode(-1);
        fakeHead.next = head;
        
        prev = fakeHead;
        curr = fakeHead.next;
        
        i = 1;
        # reaching the node at left index
        while i < left:
            prev = curr;
            curr = curr.next;
            i += 1;
        
        # reversing nodes from left index to right index
        node = prev;
        while i <= right:
            tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
            i += 1;
        
        # connecting rest of the list
        node.next.next = curr;
        node.next = prev;
        
        return fakeHead.next;