"""
 * LeetCode: 62 - Unique Paths
 * Link: https://leetcode.com/problems/unique-paths/
 * Difficulty: Medium
 * Time: O(m*n)
 * Space: O(m*n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R=[[0]*(n+1) for _ in range(m+1)]
        D=[[0]*(n+1) for _ in range(m+1)]
        R[0][0]=1
        ans=0
        for i in range(m):
            for j in range(n):
                r=R[i][j]
                d=D[i][j]
                w=r+d
                if i==m-1 and j==n-1: ans=ans+w
                R[i][j+1]=(R[i][j+1]+w)
                D[i+1][j]=(D[i+1][j]+w)
        return ans