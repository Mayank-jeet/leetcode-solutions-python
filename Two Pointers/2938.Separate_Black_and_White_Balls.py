"""
 * LeetCode: 2938 - Separate Black and White Balls
 * Link: https://leetcode.com/problems/separate-black-and-white-balls/
 * Difficulty: Medium
 * Time: O(n) where n is the size of the input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minimumSteps(self, s: str) -> int:
        swap=0
        black=0
        n=len(s)
        for i in range(n):
            if s[i]=='0': swap+=black
            else: black+=1
        return swap