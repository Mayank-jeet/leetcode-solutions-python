""" 
 * LeetCode: 1015 - Smallest Integer Divisible by K
 * Link: https://leetcode.com/problems/smallest-integer-divisible-by-k/
 * Difficulty: Medium
 * Time: O(k)
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k==1: return 1
        if k%2==0 or k%5==0: return -1
        rem=0
        for i in range(1,k+1):
            rem=(rem*10+1)%k
            if rem==0: return i
        return -1