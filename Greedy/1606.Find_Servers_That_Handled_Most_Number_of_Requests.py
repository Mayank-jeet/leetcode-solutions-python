"""
 * LeetCode: 1606 - Find Servers That Handled Most Number of Requests
 * Link: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
 * Difficulty: Medium
 * Time: O(nlogk) where n is the length of input vector and k is the number of servers
 * Space: O(k)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        handle=[0]*k
        busy=[]
        free=list(range(k))
        n=len(arrival)
        for i in range(n):
            while busy and busy[0][0]<=arrival[i]:
                time,node=heapq.heappop(busy)
                heapq.heappush(free,i+(node-i)%k)
            while free and free[0]<i:
                j=heapq.heappop(free)
                heapq.heappush(free,j+((i-j+k-1)//k)*k)
            if not free: continue
            j=heapq.heappop(free)
            node=j%k
            heapq.heappush(busy,(arrival[i]+load[i],node))
            handle[node]+=1
        maxLoad=max(handle)
        return [i for i in range(k) if handle[i]==maxLoad]