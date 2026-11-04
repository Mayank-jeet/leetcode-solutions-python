"""
 * LeetCode: 64 - Minimum Path Sum
 * Link: https://leetcode.com/problems/minimum-path-sum/
 * Difficulty: Medium
 * Time: O(m*n) where m and n are the dimensions of the grid
 * Space: O(m*n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        cost=[[float('inf')]*n for _ in range(m)]
        cost[0][0]=grid[0][0]
        pq=[]
        heapq.heappush(pq,(grid[0][0],0,0))
        dx=[0,1]
        dy=[1,0]
        while pq:
            c,x,y=heapq.heappop(pq)
            for i in range(2):
                newX=x+dx[i]
                newY=y+dy[i]
                if newX>=m or newY>=n:
                    continue
                newCost=c+grid[newX][newY]
                if cost[newX][newY]<=newCost:
                    continue
                heapq.heappush(pq,(newCost,newX,newY))
                cost[newX][newY]=newCost
        return cost[m-1][n-1]