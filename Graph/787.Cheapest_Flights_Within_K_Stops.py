"""
 * LeetCode: 787 - Cheapest Flights Within K Stops
 * Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
 * Difficulty: Medium
 * Time: O((E+V)logV) where E is number of edges and V is number of vertices in graph
 * Space: O(V+E)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for el in flights: adj[el[0]].append((el[1],el[2]))
        dist=[[float('inf')]*(k+2) for _ in range(n)]
        pq=[(0,src,k+1)]
        dist[src][k+1]=0
        while pq:
            cost,node,stops=heapq.heappop(pq)
            if node==dst: return cost
            if stops==0: continue
            for adjNode,w in adj[node]:
                newCost=cost+w
                if stops==1 and adjNode!=dst: continue
                if newCost<dist[adjNode][stops-1]:
                    dist[adjNode][stops-1]=newCost
                    heapq.heappush(pq,(newCost,adjNode,stops-1))
        return -1