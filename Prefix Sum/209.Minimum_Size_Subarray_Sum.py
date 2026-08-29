"""
 * LeetCode: 209 - Minimum Size Subarray Sum
 * Link: https://leetcode.com/problems/minimum-size-subarray-sum/
 * Difficulty: Medium
 * Time: O(n) where n is size of input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=0
        total=0
        leftSum=0
        n=len(nums)
        i=0
        j=-1
        while i<n:
            total+=nums[i]
            if (total-leftSum)>=target:
                while(j+1)<i and (total-(leftSum+nums[j+1]))>=target:
                    j+=1
                    leftSum+=nums[j]
                if ans==0: ans=i-j
                else: ans=min(ans,i-j)
            i+=1
        return ans