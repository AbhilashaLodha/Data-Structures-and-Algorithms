#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:32:59 2022

@author: apple
"""

class LinkedList:
    def __init__(self): # head and tail are sort of nodes only
        self.head = None
        self.tail = None
        self.length = 0
        
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        self.length += 1
        
    def add_last(self, data):
        new_node1 = Node(data)
        self.tail.next = new_node1
        self.tail = new_node1
        
        self.length += 1
        
    def add_at(self, data, index):
        
        if index == 0:
            self.add_first(data)
        elif index == self.length:
            self.add_last(data)
        else:
            new_node = Node(data)
            
            temp = self.head
            
            i = 0
            while i < index - 1:
                temp = temp.next
                i += 1
                
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
    
    def delete_at(self, index):
        
        if index == 0:
            self.delete_first()
        elif index == self.length:
            self.delete_last()
        else:
            temp = self.head
            
            i = 0
            while i < index - 1:
                temp = temp.next
                i += 1
                
            temp.next = temp.next.next
            self.length -= 1
        
    
    def delete_first(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None        
    
        self.length -= 1
        
    def delete_last(self):
        temp = self.head
        i = 1
        while i < self.length - 1:
            # print(temp.data)
            temp = temp.next
            i += 1
        
        self.tail = temp
        self.tail.next = None   
        
        self.length -= 1
        
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
llist = LinkedList()
llist2 = LinkedList()

first_node = Node("a")


llist.head = first_node
llist.tail = first_node # initially both head and tail points the first node
# print(llist.head.data)

second_node = Node("b")

third_node = Node("c")

first_node.next = second_node

second_node.next = third_node

llist.tail = third_node

llist.length = 3

# traversal
llist.traverse()

print("\n")
# insertion at first 
llist.add_first("d")
llist.traverse()

print("\n")
# insertion at last
llist.add_last("ee")
llist.traverse() 

print("\n")
# delete from start
llist.delete_first()
llist.traverse() 

print("\n")
# delete from last
llist.delete_last()
llist.traverse()

print("\n")
# add at index
llist.add_at("f", 3)
llist.traverse()

print("\n")
# delete at index
llist.delete_at(3)
llist.traverse()

llist2.add_first("1")
llist2.traverse()

print("\n")
# print(llist.head.next.data)  
# print(llist.head.next.next.data) 