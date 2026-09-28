"""
 * LeetCode: 1584 - Min Cost to Connect All Points
 * Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
 * Difficulty: Medium
 * Time: O(n^2) for forming adj graph, and O(nlog(n)) for traversal, where n is number of points 
 * Space: O(n^2)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        adj=[[] for _ in range(n)]
        for i in range(n):
            x1=points[i][0]
            y1=points[i][1]
            for j in range(n):
                if i==j: continue
                x2=points[j][0]
                y2=points[j][1]
                adj[i].append((j,abs(x2-x1)+abs(y2-y1)))
        vis=[False]*n
        pq=[(0,0)]
        res=0
        visited=0
        while visited<n:
            wt,node=heapq.heappop(pq)
            if vis[node]: continue
            vis[node]=True
            res+=wt
            visited+=1
            for adjNode,weight in adj[node]:
                if not vis[adjNode]: heapq.heappush(pq,(weight,adjNode))
        return res