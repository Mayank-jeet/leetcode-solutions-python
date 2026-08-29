"""
 * LeetCode: 1823 - Find the Winner of the Circular Game
 * Link: https://leetcode.com/find-the-winner-of-the-circular-game/
 * Difficulty: Medium
 * Time: O(n)
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=deque()
        for i in range(1,n+1): q.append(i)
        while len(q)!=1:
            for i in range(1,k):
                if len(q)==1: return q[0]
                else:
                    q.append(q[0])
                    q.popleft()
            q.popleft()
        return q[0]