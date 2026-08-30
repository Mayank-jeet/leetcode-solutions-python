"""
 * LeetCode: 80 - Remove Duplicates from Sorted Array II
 * Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
 * Difficulty: Medium
 * Time: O(n) where n is size of input list
 * Space: O(1)
 """
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for el in nums:
            if i==0 or i==1 or nums[i-2]!=el:
                nums[i]=el
                i+=1
        return i