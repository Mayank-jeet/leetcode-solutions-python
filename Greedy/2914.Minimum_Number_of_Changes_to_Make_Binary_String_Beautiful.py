"""
 * LeetCode: 2914 -Minimum Number of Changes to Make Binary String Beautiful
 * Link: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minChanges(self, s: str) -> int:
        n,ans=len(s),0
        for i in range(0,n,2):
            if s[i]!=s[i+1]: ans+=1
        return ans