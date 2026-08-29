"""
 * LeetCode: 990 - Satisfiability of Equality Equations
 * Link: https://leetcode.com/satisfiability-of-equality-equations/
 * Difficulty: Medium
 * Time: O(n) where n is size of input vector
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent=[]
        for i in range(26): parent.append(i)
        def find(x):
            if x!=parent[x]: parent[x]=find(parent[x])
            return parent[x]
        for s in equations:
            if s[1]=='=':
                parent[find(ord(s[0])-ord('a'))]=find(ord(s[3])-ord('a'))
        for s in equations:
            if s[1]=='!' and find(ord(s[0])-ord('a'))==find(ord(s[3])-ord('a')):
                return False
        return True