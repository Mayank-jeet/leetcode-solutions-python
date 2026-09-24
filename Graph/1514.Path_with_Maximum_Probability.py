"""
 * LeetCode: 1514 - Path with Maximum Probability
 * Link: https://leetcode.com/problems/path-with-maximum-probability/
 * Difficulty: Medium
 * Time: O((V+E)log(V)) where V is number of vertices and E is number of edges
 * Space: O(V+E)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj=[[] for _ in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1],succProb[i]))
            adj[edges[i][1]].append((edges[i][0],succProb[i]))
        prob=[0]*n
        prob[start_node]=1
        pq=[(-1,start_node)]
        while pq:
            currProb,node=heapq.heappop(pq)
            currProb=-currProb
            for adjNode,adjNodeProb in adj[node]:
                newProb=currProb*adjNodeProb
                if prob[adjNode]<newProb:
                    prob[adjNode]=newProb
                    heapq.heappush(pq,(-newProb,adjNode))
        return prob[end_node]