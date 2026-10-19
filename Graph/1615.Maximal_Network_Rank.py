"""
 * LeetCode: 1615 - Maximal Network Rank
 * Link: https://leetcode.com/problems/maximal-network-rank/
 * Difficulty: Medium
 * Time: O(n^2) where n is number of nodes
 * Space: O(V+E) where V is number of nodes and E is number of edges
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads)==0: return 0
        elif len(roads)==1: return 1
        adj=[[] for _ in range(n)]
        for node in roads:
            adj[node[0]].append(node[1])
            adj[node[1]].append(node[0])
        maxEdge=0
        secondMaxEdge=0
        for i in range(n):
            edgeSize=len(adj[i])
            if edgeSize>maxEdge:
                secondMaxEdge=maxEdge
                maxEdge=edgeSize
            elif edgeSize>secondMaxEdge: secondMaxEdge=edgeSize
        for a in range(n):
            if len(adj[a])!=maxEdge: continue
            u_set=set(adj[a])
            for i in range(n):
                if i==a: continue
                if len(adj[i])==secondMaxEdge and i not in u_set: return maxEdge+secondMaxEdge
        return maxEdge+secondMaxEdge-1