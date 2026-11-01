"""
 * LeetCode: 4099 - Minimum Operations to Sort With Locked Indices
 * Link: https://leetcode.com/problems/minimum-operations-to-sort-with-locked-indices/
 * Difficulty: Medium
 * Time: O(n^2) where n is number of elements in input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n=len(nums)
        unlock,maximum=0,0
        for i in range(n):
            maximum=max(maximum,nums[i])
            if locked[i]==1 and not (nums[i]==i+1 and maximum==i+1): unlock+=1
        if unlock>k: return -1
        swaps=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]: swaps+=1
        return swaps+unlock