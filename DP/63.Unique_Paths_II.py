"""
 * LeetCode: 63 - Unique Paths II
 * Link: https://leetcode.com/problems/unique-paths-ii/
 * Difficulty: Medium
 * Time: O(m*n) where m and n are the dimensions of the input grid
 * Space: O(m*n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1: return 0
        ans=0
        R=[[0]*(n+1) for _ in range(m+1)]
        D=[[0]*(n+1) for _ in range(m+1)]
        R[0][0]=1
        for i in range(m):
            for j in range(n):
                r,d=R[i][j],D[i][j]
                if obstacleGrid[i][j]==0:
                    w=r+d
                    if i==m-1 and j==n-1: ans+=w
                    R[i][j+1]=(R[i][j+1]+w)
                    D[i+1][j]=(D[i+1][j]+w)
        return ans