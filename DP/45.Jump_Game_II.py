"""
 * LeetCode: 45 - Jump Game II
 * Link: https://leetcode.com/problems/jump-game-ii/
 * Difficulty: Medium
 * Time: O(n*max(nums)) where n is the length of the input array and max(nums) is the maximum jump length
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution: 
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[float('inf')]*n
        dp[0]=0
        for i in range(n):
            for j in range(1,nums[i]+1):
                if i+j>=n: break
                dp[i+j]=min(dp[i+j],dp[i]+1)
            if dp[n-1]!=float('inf'): return dp[n-1]
        return dp[n-1]