"""
 * LeetCode: 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum
 * Link: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
 * Difficulty: Medium
 * Time: O(n) where n is size of input vector
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr)
        res,tot,i=n+1,0,0
        dp=[n]*(n+1)
        for j in range(n):
            tot+=arr[j]
            while tot>target:
                tot-=arr[i]
                i+=1
            dp[j+1]=dp[j]
            if tot==target:
                Len=j-i+1
                res=min(res,Len+dp[i])
                dp[j+1]=min(dp[j],Len)        
        return -1 if res==n+1 else res