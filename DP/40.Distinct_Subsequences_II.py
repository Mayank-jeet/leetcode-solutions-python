"""
 * LeetCode: 40 - Distinct Subsequences II
 * Link: https://leetcode.com/problems/distinct-subsequences-ii/
 * Difficulty: Hard
 * Time: O(n) where n is the length of input string s
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    MOD=10**9+7
    def distinctSubseqII(self, s: str) -> int:
        tot=0
        dp=[0]*26
        for c in s:
            c=ord(c)-97
            new=tot+1-dp[c]
            tot=(tot+new)%self.MOD
            dp[c]=(dp[c]+new)%self.MOD
        return tot