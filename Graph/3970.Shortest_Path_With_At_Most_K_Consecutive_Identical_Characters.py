"""
 * LeetCode: 3970 - Shortest Path With At Most K Consecutive Identical Characters
 * Link: https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
 * Difficulty: Medium
 * Time: O(E·k·log(V·k)) where V is the number of nodes (n), E is the number of edges (edges.size()), and k is the maximum allowed consecutive identical characters
 * Space: O(V·k+E)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional,NamedTuple
import heapq
class Solution:
    def shortestPath(self,n,edges,labels,k):
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
        m=[[float('inf')]*(k+1) for _ in range(n)]
        m[0][1]=0
        pq=[(0,0,1)]
        while pq:
            dist,node,run=heapq.heappop(pq)
            if dist>m[node][run]:
                continue
            if node==n-1:
                return dist
            for adjNode,wt in adj[node]:
                newRun=run+1 if labels[adjNode]==labels[node] else 1
                if newRun>k:
                    continue
                if dist+wt<m[adjNode][newRun]:
                    m[adjNode][newRun]=dist+wt
                    heapq.heappush(pq,(dist+wt,adjNode,newRun))
        return -1