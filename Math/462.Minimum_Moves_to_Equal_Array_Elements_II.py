""" 
 * LeetCode: 462 - Minimum Moves to Equal Array Elements II
 * Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
 * Difficulty: Medium
 * Time: O(nlog(n)) where n is the length of the input array
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med=nums[len(nums)//2]
        return sum(abs(x-med) for x in nums)