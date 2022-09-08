#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 00:38:50 2022

@author: apple
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        temp_head = ListNode(-1)
        temp_tail = temp_head
        
        qo = 0
        
        while l1 or l2 or qo:
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
                
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
                
            sum = l1_val + l2_val + qo

            temp_tail.next = ListNode(sum)
            temp_tail = temp_tail.next

            if temp_tail.val > 9:
                qo = int(temp_tail.val/10)
                rem = temp_tail.val % 10

                temp_tail.val = rem
            else:
                qo = 0
                
            if l1:        
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            
        return temp_head.next


