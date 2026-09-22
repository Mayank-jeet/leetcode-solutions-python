"""
 * LeetCode: 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance3568 - Minimum Moves to Clean the Classroom
 * Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
 * Difficulty: Medium
 * Time: O(n^3)
 * Space: O(n^2)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        cost=[[1e9]*n for _ in range(n)]
        for edge in edges:
            cost[edge[0]][edge[1]]=edge[2]
            cost[edge[1]][edge[0]]=edge[2]
        for i in range(n): cost[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if cost[i][k]==1e9 or cost[k][j]==1e9: continue
                    cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
        minCount=1e9
        ans=-1
        for i in range(n):
            count=0
            for j in range(n):
                if cost[i][j]<=distanceThreshold: count+=1
            if count<=minCount:
                minCount=count
                ans=i
        return ans