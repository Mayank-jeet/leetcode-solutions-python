"""
 * LeetCode: 743 - Network Delay Time
 * Link: https://leetcode.com/problems/network-delay-time/
 * Difficulty: Medium
 * Time: O((V+E)logV) where V is number of vertices and E is nuber of edges
 * Space: O(V+E)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for el in times: adj[el[0]].append((el[1],el[2]))
        pq=[]
        dist=[float('inf')]*(n+1)
        dist[0]=0
        dist[k]=0
        heapq.heappush(pq,(0,k))
        while len(pq)!=0:
            curr=pq[0]
            heapq.heappop(pq)
            distance=curr[0]
            node=curr[1]
            for i in range(len(adj[node])):
                adjNode=adj[node][i][0]
                newWeight=distance+adj[node][i][1]
                if newWeight<dist[adjNode]:
                    dist[adjNode]=newWeight
                    heapq.heappush(pq,(newWeight,adjNode))
        ans=max(dist)
        if ans==float('inf'): return -1
        return ans