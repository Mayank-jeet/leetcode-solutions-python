"""
 * LeetCode: 3310 - Remove Methods From Project
 * Link: https://leetcode.com/problems/remove-methods-from-project/
 * Difficulty: Medium
 * Time: O((V+E)log(V)) in worst case, where V is number of vertices and E is number of edges
 * Space: O(V+E)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        for a,b in invocations:
            adj[a].append(b)
        vis=[False]*n
        vis[k]=True
        q=deque([k])
        while q:
            node=q.popleft()
            for nxt in adj[node]:
                if not vis[nxt]:
                    vis[nxt]=True
                    q.append(nxt)
        for a,b in invocations:
            if vis[b] and not vis[a]:
                return list(range(n))
        return [i for i in range(n) if not vis[i]]