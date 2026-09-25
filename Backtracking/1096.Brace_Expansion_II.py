"""
 * LeetCode: 1096 - Brace Expansion II
 * Link: https://leetcode.com/problems/brace-expansion-ii/
 * Difficulty: Medium
 * Time: O(K×L) where K is number of unique final strings, and L is length of each final string.
 * Space: O(K×L)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        ans=set()
        def dfs(s):
            r=s.find('}')
            if r==-1:
                ans.add(s)
                return
            l=s.rfind('{',0,r)
            left=s[:l]
            right=s[r+1:]
            inside=s[l+1:r]
            for part in inside.split(','):
                dfs(left+part+right)
        dfs(expression)
        return sorted(ans)