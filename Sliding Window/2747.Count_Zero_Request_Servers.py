"""
 * LeetCode: 2747 - Count Zero Request Servers
 * Link: https://leetcode.com/problems/count-zero-request-servers/
 * Difficulty: Medium
 * Time: Time: O(LlogL+QlogQ+L+Q) where L is number of logs, Q is number of queries, n is number of servers
 * Space: O(n+Q) where n is freq array, Q is qs array and ans array
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        q=len(queries)
        l=len(logs)
        logs.sort(key=lambda a:a[1])
        qs=[]
        for i in range(q):
            qs.append((queries[i],i))
        qs.sort()
        ans=[0]*q
        freq=[0]*(n+1)
        active=0
        i=0
        j=0
        for k in range(q):
            time=qs[k][0]
            idx=qs[k][1]
            start=time-x
            end=time
            while j<l and logs[j][1]<=end:
                id=logs[j][0]
                freq[id]+=1
                if freq[id]==1:
                    active+=1
                j+=1
            while i<l and logs[i][1]<start:
                id=logs[i][0]
                freq[id]-=1
                if freq[id]==0:
                    active-=1
                i+=1
            ans[idx]=n-active
        return ans 