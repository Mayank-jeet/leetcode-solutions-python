"""
 * LeetCode: 15 - 3Sum
 * Link: https://leetcode.com/3sum/
 * Difficulty: Medium
 * Time: O(n^2) where n is size of input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]: continue
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<0: j+=1
                elif sum>0: k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    j+=1
                    k-=1
                    ans.append(temp)
                    while j<k and nums[j]==nums[j-1]: j+=1
                    while j<k and nums[k]==nums[k+1]: k-=1
        return ans