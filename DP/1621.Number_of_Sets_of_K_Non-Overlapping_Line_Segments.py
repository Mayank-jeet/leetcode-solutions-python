"""
 * LeetCode: 1621 - Number of Sets of K Non-Overlapping Line Segments
 * Link: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
 * Difficulty: Medium
 * Time: O(n*k)
 * Space: O(n*k)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD=10**9 + 7
        dp=[[0]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
        for j in range(1,k+1):
            running_sum=0
            for i in range(1,n):
                running_sum =(running_sum +dp[i-1][j-1])%MOD
                dp[i][j]=(dp[i-1][j]+running_sum )%MOD
        return dp[n-1][k]