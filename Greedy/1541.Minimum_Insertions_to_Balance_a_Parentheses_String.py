"""
 * LeetCode: 1541 - Minimum_Insertions_to_Balance_a_Parentheses_String
 * Link: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
 * Difficulty: Medium
 * Time: O(n) where n is length of input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minInsertions(self, s: str) -> int:
        balance=0
        ans=0
        n=len(s)
        i=0
        while i<n:
            if s[i]=='(':
                balance+=1
            else:
                if i==n-1 or s[i+1]!=')':
                    ans+=1
                else:
                    i+=1
                balance-=1
                if balance<0:
                    ans+=abs(balance)
                    balance=0
            i+=1
        return ans+balance*2