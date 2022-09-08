#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:58:03 2022

@author: apple
"""

class Heap:
    heap = []
    
    def __init__(self, arr):
        self.construct_heap(arr)
        
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
        
    def construct_heap(self, arr):
        self.heap = arr[:]
        
        n = len(self.heap)
        
        for i in range (n - 1, -1, -1):
            self.down_heapify(i)
        
    def down_heapify(self, pi):
        
        min_idx = pi
        left_child_idx = 2 * pi + 1
        right_child_idx = 2 * pi + 2
        
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
            min_idx = left_child_idx

        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
            min_idx = right_child_idx
        
        if min_idx != pi:
            self.swap(pi, min_idx)
            self.down_heapify(min_idx)
            
    def upheapify(self, ci):
        pi = (ci - 1) // 2
        
        if pi >= 0 and self.heap[pi] > self.heap[ci]:
            self.swap(pi, ci)
            self.upheapify(pi)
            
    def add(self, data):
        self.heap.append(data)
        
        idx = len(self.heap) - 1
        
        self.upheapify(idx)
        
    def pop(self):
        self.swap(0,len(self.heap)-1)
        ans = self.heap.pop()
        self.down_heapify(0)
        
        return ans
    
    def peek(self):
        return self.heap[0]
        
             

arr = [10, 20, 30, -2, -3, -4, 5, 6, 7, 8, 9, 22, 11, 13]

min_heap = Heap(arr)

print(min_heap.heap)

min_heap.add(1)
print(min_heap.heap)

print(min_heap.pop())
print(min_heap.heap)

print(min_heap.peek())
