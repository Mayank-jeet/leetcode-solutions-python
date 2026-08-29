"""
 * LeetCode: 33 - Search in Rotated Sorted Array
 * Link: https://leetcode.com/search-in-rotated-sorted-array/
 * Difficulty: Medium
 * Time: O(nlog(n)) where n is the size of input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int(low+(high-low)/2)
            if nums[mid]==target: return mid
            elif target>nums[mid]:
                if nums[mid]<=nums[low]:
                    if nums[high]>=target: low=mid+1
                    else: high=mid-1
                else: low=mid+1
            elif target<nums[mid]:
                if nums[mid]>=nums[low]:
                    if nums[low]<=target: high=mid-1
                    else: low=mid+1
                else: high=mid-1
        return -1