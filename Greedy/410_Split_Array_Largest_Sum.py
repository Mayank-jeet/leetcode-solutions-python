"""
 * LeetCode: 410 - Split Array Largest Sum
 * Link: https://leetcode.com/split-array-largest-sum/
 * Difficulty: Hard
 * Time: O(nlog(n)) where n is the size of input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def isPossible(nums: List[int],maxSum: int,k: int):
            n,count,sum=len(nums),0,0
            for i in range(n):
                if nums[i]+sum>maxSum:
                    sum=0
                    count+=1
                if count>=k: return False
                sum+=nums[i]
            return True
        low=max(nums,default=-1)
        high=0
        for el in nums:
            high+=el
        while low<=high:
            mid=low+(high-low)//2
            if isPossible(nums,mid,k): high=mid-1
            else: low=mid+1
        return low