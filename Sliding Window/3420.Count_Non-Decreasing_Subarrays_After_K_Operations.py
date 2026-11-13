"""
 * LeetCode: 3420. Count Non-Decreasing Subarrays After K Operations
 * Link: https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
 * Difficulty: Medium
 * Time: O(n) where n is length of input vector
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n=len(nums); r=n-1
        dq=deque()
        ans=0; cost=0
        for l in range(n-1,-1,-1):
            x=nums[l]
            while dq and nums[dq[0]]<=x:
                s=dq.popleft()
                e=dq[0] if dq else r+1
                cost+=(x-nums[s])*(e-s)
            dq.appendleft(l)
            while cost>k:
                cost-=nums[dq[-1]]-nums[r]
                if dq[-1]==r: dq.pop()
                r-=1
            ans+=r-l+1
        return ans