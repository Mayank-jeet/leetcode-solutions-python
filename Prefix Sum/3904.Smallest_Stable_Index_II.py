"""
 * LeetCode: 3904 - Smallest Stable Index II
 * Link: https://leetcode.com/problems/smallest-stable-index-ii/
 * Difficulty: Medium
 * Time: O(n) 
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minList=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            if len(minList)==0 or minList[-1]>nums[i]: minList.append(nums[i])
            else: minList.append(minList[-1])
        maxEl=-1e9
        for i in range(n):
            maxEl=max(maxEl,nums[i])
            if maxEl-minList[n-1-i]<=k: return i
        return -1