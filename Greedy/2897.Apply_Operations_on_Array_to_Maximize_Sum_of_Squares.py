"""
 * LeetCode: 2897 - Apply Operations on Array to Maximize Sum of Squares
 * Link: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
 * Difficulty: Hard
 * Time: O(30(n+k)) where n is the size of nums and k is the number of operations
 * Space: O(30) for bits vector
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits=[0]*30
        for x in nums:
            for i in range(30):
                if x&(1<<i): bits[i]+=1
        ans=0
        MOD=1000000007
        for i in range(k):
            el=0
            for j in range(29,-1,-1):
                if bits[j]>0:
                    el|=(1<<j)
                    bits[j]-=1
            ans=(ans+el*el)%MOD
        return ans