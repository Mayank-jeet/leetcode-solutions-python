"""
 * LeetCode: 55 - Jump Game
 * Link: https://leetcode.com/problems/jump-game/
 * Difficulty: Medium
 * Time: O(n*max(nums)) where n is the length of the input array and max(nums) is the maximum jump length
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        dp=[False]*n
        dp[0]=True
        for i in range(n):
            if not dp[i]: continue
            for j in range(1,nums[i]+1):
                if i+j>=n: break
                dp[i+j]=True
            if dp[n-1]: return True
        return dp[n-1]