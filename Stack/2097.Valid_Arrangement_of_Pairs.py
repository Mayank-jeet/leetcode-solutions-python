"""
 * LeetCode: 2097 - Valid Arrangement of Pairs
 * Link: https://leetcode.com/problems/valid-arrangement-of-pairs/
 * Difficulty: Hard
 * Time: O(n) where n is number of pairs
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        adj=defaultdict(list)
        deg=defaultdict(int)
        for p in pairs:
            adj[p[0]].append(p[1])
            deg[p[0]]+=1
            deg[p[1]]-=1
        start=pairs[0][0]
        for node,d in deg.items():
            if d==1:
                start=node
                break
        st=[start]
        pair=[start]
        while len(st)!=0:
            curr=st[-1]
            if len(adj[curr])!=0:
                v=adj[curr][-1]
                adj[curr].pop()
                st.append(v)
            else:
                pair.append(curr)
                st.pop()
        ans=[]
        for i in range(len(pair)-1,1,-1):
            ans.append([pair[i],pair[i-1]])
        return ans