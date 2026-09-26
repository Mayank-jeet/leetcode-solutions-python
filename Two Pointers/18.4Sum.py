"""
 * LeetCode: 18 - 4Sum
 * Link: https://leetcode.com/problems/4sum/
 * Difficulty: Medium
 * Time: O(n^3) where n is size of input list
 * Space: O(n) for answer list
 """
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n-3):
            if i!=0 and nums[i]==nums[i-1]: continue
            for j in range(i+1,n-2):
                if j!=i+1 and nums[j]==nums[j-1]: continue
                k=j+1
                l=n-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum>target: l-=1
                    elif sum<target: k+=1
                    else:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]: k+=1
                        while k<l and nums[l]==nums[l+1]: l-=1
        return ans