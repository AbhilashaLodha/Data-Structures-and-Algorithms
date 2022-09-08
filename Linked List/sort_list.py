#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 13:27:31 2022

@author: apple
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        l1 = list1
        l2 = list2
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        temp_head = ListNode(-1)
        temp_tail = temp_head
        
        while l1 and l2:
            if l1.val <= l2.val:
                temp_tail.next = l1
                l1 = l1.next
            else:
                temp_tail.next = l2
                l2 = l2.next
                
            temp_tail = temp_tail.next
                    
        if l1:
            temp_tail.next = l1
        if l2:
            temp_tail.next = l2
                
        return temp_head.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        mid = self.middleNode(head)
        
        first = head
        second = mid.next
        mid.next = None
        
        sorted_first = self.sortList(first)
        sorted_second = self.sortList(second)
        
        sorted_head = self.merge(sorted_first, sorted_second)
        
        return sorted_head
        