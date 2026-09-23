"""
 * LeetCode: 1658 - Minimum Operations to Reduce X to Zero
 * Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
 * Difficulty: Medium
 * Time: O(n)
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        sum=0
        n=len(nums)
        left=-1
        right=n
        for i in range(n):
            if sum>=x: break
            sum+=nums[i]
            left+=1
        if left==n-1:
            if sum<x: return -1
            elif sum==x: return n
        ans=1e10
        while left>=0:
            if sum>x:
                while sum>x and left>=0:
                    sum-=nums[left]
                    left-=1
            if sum<x:
                while sum<x and right>left and right>0:
                    right-=1
                    sum+=nums[right]
            if sum==x:
                ans=min(ans,left+1+(n-right))
                if left>=0:
                    sum-=nums[left]
                    left-=1
        if ans==1e10: return -1
        return ans