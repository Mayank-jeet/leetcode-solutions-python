"""
 * LeetCode: 2368. Reachable Nodes With Restrictions
 * Link: https://leetcode.com/problems/reachable-nodes-with-restrictions/
 * Difficulty: Medium
 * Time: O(n) where n is the number of nodes in the graph
 * Space: O(n) for adjecency list, set and deque
 """
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj=[[] for _ in range(n)]
        for el in edges:
            adj[el[0]].append(el[1])
            adj[el[1]].append(el[0])
        u_set=set()
        for el in restricted: u_set.add(el)
        q=deque()
        q.append((0,-1))
        ans=1
        while len(q)!=0:
            curr=q[0]
            q.popleft()
            currNode=curr[0]
            parentNode=curr[1]
            for i in range(len(adj[currNode])):
                if adj[currNode][i]==parentNode or adj[currNode][i] in u_set: continue
                q.append((adj[currNode][i],currNode))
                ans+=1
        return ans