"""
 * LeetCode: 2090 - K Radius Subarray Averages
 * Link: https://leetcode.com/problems/k-radius-subarray-averages/
 * Difficulty: Medium
 * Time: O(n) where n is size of input vector
 * Space: O(n) for storing answer vector, otherwise O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        sum=0
        for i in range(k):
            if i>=n: break
            sum+=nums[i]
        ans=[]
        for i in range(n):
            if i-k-1>=0: sum-=nums[i-k-1]
            if i+k<n: sum+=nums[i+k]
            if i-k<0 or i+k>=n: ans.append(-1)
            else: ans.append(int(sum/(2*k+1)))
        return ans