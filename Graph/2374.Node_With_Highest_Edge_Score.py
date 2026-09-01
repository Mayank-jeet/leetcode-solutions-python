"""
 * LeetCode: 2374 - Node With Highest Edge Score
 * Link: https://leetcode.com/problems/node-with-highest-edge-score/
 * Difficulty: Medium
 * Time: O(n) where n is size of input list edges
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n=len(edges)
        score=[0]*n
        for i in range(n): score[edges[i]]+=i
        return max(range(n),key=lambda i:score[i])