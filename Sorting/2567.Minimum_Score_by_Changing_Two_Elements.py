"""
 * LeetCode: 2567 - Minimum Score by Changing Two Elements
 * Link: https://leetcode.com/problems/minimum-operations-to-sort-with-locked-indices/
 * Difficulty: Medium
 * Time: O(nlog(n)) where n is number of elements in input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        return min([nums[n-3]-nums[0],nums[n-2]-nums[1],nums[n-1]-nums[2]])