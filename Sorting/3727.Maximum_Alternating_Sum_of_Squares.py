"""
 * LeetCode: 3727 - Maximum Alternating Sum of Squares
 * Link: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
 * Difficulty: Medium
 * Time: O(nlog(n)) where n is number of elements in input vector
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]<0: nums[i]*=-1
        nums.sort(reverse=True)
        ans=0
        for i in range(n//2): ans+=nums[i]*nums[i]-nums[n-1-i]*nums[n-1-i]
        if n%2!=0: ans+=nums[n//2]*nums[n//2]
        return ans