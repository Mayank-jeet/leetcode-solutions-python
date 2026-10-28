"""
 * LeetCode: 3882 - Minimum XOR Path in a Grid
 * Link: https://leetcode.com/problems/minimum-xor-path-in-a-grid/
 * Difficulty: Hard
 * Time: O(m*n*V) where m and n are the dimensions of the grid and V is the number of possible XOR values
 * Space: O(m*n*V)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: continue
                v=grid[i][j]
                if i>0: dp[i][j]|={x^v for x in dp[i-1][j]}
                if j>0: dp[i][j]|={x^v for x in dp[i][j-1]}
        return min(dp[m-1][n-1])