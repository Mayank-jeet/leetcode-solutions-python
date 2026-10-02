"""
 * LeetCode: 2976 - Minimum Cost to Convert String I
 * Link: https://leetcode.com/problems/minimum-cost-to-convert-string-i/
 * Difficulty: Medium
 * Time: O(m+26^3+L), where m is length of original/changed/cost list and L is length of source/target string
 * Space: O(26^2) for dist vector
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional,NamedTuple
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF=float('inf')
        dist=[[INF]*26 for _ in range(26)]
        for i in range(len(original)):
            u=ord(original[i])-ord('a')
            v=ord(changed[i])-ord('a')
            dist[u][v]=min(dist[u][v],cost[i])
        for i in range(26): dist[i][i]=0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k]==INF or dist[k][j]==INF: continue
                    dist[i][j]=min(dist[i][k]+dist[k][j],dist[i][j])
        ans=0
        for i in range(len(source)):
            u=ord(source[i])-ord('a')
            v=ord(target[i])-ord('a')
            if dist[u][v]==INF: return -1
            ans+=dist[u][v]
        return ans