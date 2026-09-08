"""
 * LeetCode:  2477 - Minimum Fuel Cost to Report to the Capital
 * Link: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
 * Difficulty: Medium
 * Time: O(E+V) where E is number of edges and V is number of vertices
 * Space: O(V)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans=0
        def dfs(adj: List[List[int]],prev: int,index: int,seats: int):
            nonlocal ans
            passangers=1
            n=len(adj[index])
            for i in range(n):
                if adj[index][i]==prev: continue
                passangers+=dfs(adj,index,adj[index][i],seats)
            if index>0: ans+=(passangers+seats-1)//seats
            return passangers
        n=len(roads)+1
        adj=[[] for _ in range(n)]
        for el in roads:
            adj[el[0]].append(el[1])
            adj[el[1]].append(el[0])
        dfs(adj,-1,0,seats)
        return ans