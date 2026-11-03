"""
 * LeetCode: 213 - House Robber II
 * Link: https://leetcode.com/problems/house-robber-ii/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the input list
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def rob(self, nums: list[int]) -> int:
        m=len(nums)
        if m==1: return nums[0]
        def find(arr: list[int]) -> int:
            n=len(arr)
            dp=[0]*n
            dp[0]=arr[0]
            for i in range(1,n):
                take=arr[i]
                if i>1: take+=dp[i-2]
                notTake=dp[i-1]
                dp[i]=max(take,notTake)
            return dp[n-1]
        return max(find(nums[0:m-1]),find(nums[1:m]))