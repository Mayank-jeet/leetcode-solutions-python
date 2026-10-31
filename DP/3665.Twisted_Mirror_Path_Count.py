"""
 * LeetCode: 3665 - Twisted Mirror Path Count
 * Link: https://leetcode.com/problems/twisted-mirror-path-count/
 * Difficulty: Medium
 * Time: O(m*n) where m and n are the dimensions of the grid
 * Space: O(m*n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD=10**9+7
        m,n=len(grid),len(grid[0])
        ans=0

        R=[[0]*(n+1) for _ in range(m+1)]
        D=[[0]*(n+1) for _ in range(m+1)]
        R[0][0]=1

        for i in range(m):
            for j in range(n):
                r=R[i][j]%MOD
                d=D[i][j]%MOD
                if grid[i][j]==0:
                    w=(r+d)%MOD
                    if i==m-1 and j==n-1:
                        ans=(ans+w)%MOD
                    R[i][j+1]=(R[i][j+1]+w)%MOD
                    D[i+1][j]=(D[i+1][j]+w)%MOD
                else:
                    D[i+1][j]=(D[i+1][j]+r)%MOD
                    R[i][j+1]=(R[i][j+1]+d)%MOD
        return ans