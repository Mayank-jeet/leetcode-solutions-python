"""
 * LeetCode: 921 - Minimum Add to Make Parentheses Valid
 * Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
 * Difficulty: Medium
 * Time: O(n) where n is length of input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        close=0
        for el in s:
            if el=='(': open+=1
            else:
                if open>0: open-=1
                else: close+=1
        return open+close