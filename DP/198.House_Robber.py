"""
 * LeetCode: 198 - House Robber
 * Link: https://leetcode.com/problems/house-robber/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the input list
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            take=nums[i]
            if i>1: take+=dp[i-2]
            notTake=dp[i-1]
            dp[i]=max(take,notTake)
        return dp[n-1]