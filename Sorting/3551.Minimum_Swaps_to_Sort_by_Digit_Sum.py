"""
 * LeetCode: 3551 - Minimum Swaps to Sort by Digit Sum
 * Link: https://leetcode.com/minimum-swaps-to-sort-by-digit-sum/
 * Difficulty: Medium
 * Time: O(nlog(n)) where n is number of elements in input vector
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(el : int) -> int:
            sum=0
            while el>0:
                sum+=el%10
                el//=10
            return sum
        keyed=[]
        n=len(nums)
        for i in range(n):
            keyed.append((digitSum(nums[i]),nums[i],i))
        keyed.sort()
        home=[0]*n
        for pos in range(n):
            index=keyed[pos][2]
            home[index]=pos 
        count=0
        for i in range(n):
            while home[i]!=i:
                j=home[i]
                home[i],home[j]=home[j],home[i]
                count+=1
        return count