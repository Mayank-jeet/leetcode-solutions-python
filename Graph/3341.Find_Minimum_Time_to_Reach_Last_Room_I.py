"""
 * LeetCode: 3341 - Find Minimum Time to Reach Last Room I
 * Link: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/
 * Difficulty: Medium
 * Time: O(m*n*log(m*n)) where m is the number of rows and n is the number of columns in moveTime
 * Space: O(m*m) for the distance matrix and priority queue
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional,NamedTuple
import heapq
class Schema(NamedTuple):
    cost:int
    coordinate:tuple
class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        m,n=len(moveTime),len(moveTime[0])
        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=0
        startNode=Schema(0,(0,0))
        pq=[startNode]
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        while pq:
            curr=heapq.heappop(pq)
            cost=curr.cost
            currX,currY=curr.coordinate
            if cost>dist[currY][currX]: continue
            for i in range(4):
                newX=currX+x[i]
                newY=currY+y[i]
                if newX<0 or newX>=n or newY<0 or newY>=m: continue
                newCost=max(cost,moveTime[newY][newX])+1
                if dist[newY][newX]>newCost:
                    dist[newY][newX]=newCost
                    heapq.heappush(pq,Schema(newCost,(newX,newY)))