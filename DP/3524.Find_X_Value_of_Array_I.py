"""
 * LeetCode: 3524 - Find X Value of Array I
 * Link: https://leetcode.com/problems/find-x-value-of-array-i/
 * Difficulty: Medium
 * Time: O(n*k) where n is size of input list
 * Space: O(k)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans=[0]*k
        dp=[0]*k
        for num in nums:
            x=num%k
            nxt=[0]*k
            nxt[x]+=1
            for r in range(k):
                newR=(r*x)%k
                nxt[newR]+=dp[r]
            for r in range(k):
                ans[r]+=nxt[r]
            dp=nxt
        return ans