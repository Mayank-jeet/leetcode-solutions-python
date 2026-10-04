"""
 * LeetCode: 678 - Valid Parenthesis String
 * Link: https://leetcode.com/problems/valid-parenthesis-string/
 * Difficulty: Medium
 * Time: O(n) where n is length of input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum=0
        maximum=0
        for el in s:
            if el=='(':
                minimum+=1
                maximum+=1
            elif el==')':
                minimum-=1
                maximum-=1
            else:
                minimum-=1
                maximum+=1
            if maximum<0: return False
            minimum=max(minimum,0)
        return minimum==0