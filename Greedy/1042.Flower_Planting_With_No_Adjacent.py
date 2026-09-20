"""
 * LeetCode: 1042 - Flower Planting With No Adjacent
 * Link: https://leetcode.com/problems/flower-planting-with-no-adjacent/
 * Difficulty: Medium
 * Time: O(n)
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        adj=[[] for _ in range(n)]
        for node in paths:
            adj[node[0]-1].append(node[1]-1)
            adj[node[1]-1].append(node[0]-1)
        ans=[0]*n
        for i in range(n):
            color=[0]*5
            for j in adj[i]: color[ans[j]]=1
            for k in range(4,0,-1):
                if color[k]==0: ans[i]=k
        return ans