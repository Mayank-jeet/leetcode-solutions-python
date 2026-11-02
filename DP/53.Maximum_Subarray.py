"""
 * LeetCode: 53 - Maximum Subarray
 * Link: https://leetcode.com/problems/maximum-subarray/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum=0
        res=-float('inf')
        n=len(nums)
        for i in range(n):
            sum+=nums[i]
            res=max(res,sum)
            if sum<0: sum=0
        return res