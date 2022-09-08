#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:32:07 2022

@author: apple
"""

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w
        
def addEdge(graph, u, v, w):
    graph[u].append(Edge(v ,w))
    graph[v].append(Edge(u ,w))

def constructGraph(n):
    graph = []
    for i in range(0, n):
        graph.append([])
    
    addEdge(graph, 0, 3, 10)
    addEdge(graph, 0, 1, 10)
    addEdge(graph, 1, 2, 10)
    addEdge(graph, 3, 2, 10)
    addEdge(graph, 3, 4, 10)
    addEdge(graph, 4, 5, 10)
    addEdge(graph, 4, 6, 10)
    addEdge(graph, 5, 6, 10)
    
    # for i in range(0, n):
    #     print(str(i) + "->")
    #     for edge in graph[i]:
    #         print("(" + str(edge.v) + "," + str(edge.w) + ")")
    return graph

def hasPath(graph, vis, src, des, path):
    if src == des:
        print(path + str(des))
        return True
    
    vis[src] = True
    res = False
    for edge in graph[src]:
        v = edge.v
        if vis[v] == False:
            res = res or hasPath(graph, vis, v, des, path + str(src))
    
    return res
    
def allPaths(graph, vis, src, des, path):
    if src == des:
        print(path + str(des))
        return 1
    
    count = 0    
    vis[src] = True                                                                                
    for edge in graph[src]:
        v = edge.v
        if vis[v] == False:
            count += allPaths(graph, vis, v, des, path + str(src))
            
    vis[src] = False
    return count

import copy

def allPaths_returnType(graph, vis, src, des, ans, smallAns):
    if src == des:
        base = copy.deepcopy(smallAns)
        base.append(des)
        ans.append(base)
        return 1
    
    count = 0    
    vis[src] = True
    smallAns.append(src)                                                                                
    for edge in graph[src]:
        v = edge.v
        if vis[v] == False:
            count += allPaths_returnType(graph, vis, v, des, ans, smallAns)
            
    vis[src] = False
    smallAns.pop()
    return count
    

graph = constructGraph(7)
# hasPath(graph, [False]*7, 0, 6, "")
# print(allPaths(graph, [False]*7, 0, 6, ""))

ans = []
smallAns = []
print(allPaths_returnType(graph, [False]*7, 0, 6, ans, smallAns))
print(ans)
    