"""
 * LeetCode: 115 - Distinct Subsequences
 * Link: https://leetcode.com/problems/distinct-subsequences/
 * Difficulty: Hard
 * Time: O(n*m) where n is the length of t and m is the length of s
 * Space: O(n*m)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        if n>m: return 0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1): dp[i][n]=1
        for i in range(m-1,-1,-1):
            sChar=s[i]
            for j in range(n-1,-1,-1):
                if t[j]==sChar: dp[i][j]=dp[i+1][j]+dp[i+1][j+1]
                else: dp[i][j]=dp[i+1][j]
        return dp[0][0]