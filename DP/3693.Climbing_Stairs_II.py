"""
 * LeetCode: 3693 - Climbing Stairs II
 * Link: https://leetcode.com/problems/climbing-stairs-ii/
 * Difficulty: Medium
 * Time: O(n)
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(n):
            for j in range(1,min(3,n-i)+1): dp[i+j]=min(dp[i+j],dp[i]+costs[i+j-1]+j*j)
        return int(dp[n])