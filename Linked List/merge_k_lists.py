#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:38:27 2022

@author: apple
"""


import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge2SortedLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
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
    
def mergeLists(self, lists, li, ri):
    if li == ri:
        return lists[li]
    
    mid = int((li + ri) / 2)
    
    l1 = self.mergeLists(lists, li, mid)
    l2 = self.mergeLists(lists, mid + 1, ri)
    
    final_list = self.merge2SortedLists(l1, l2)
    
    return final_list

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if len(lists) == 0:
        return None
    
    ans = self.mergeLists(lists, 0, len(lists) - 1)
    
    return ans