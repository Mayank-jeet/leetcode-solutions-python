"""
 * LeetCode: 3286 - Find a Safe Walk Through a Grid
 * Link: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
 * Difficulty: Medium
 * Time: O(m·n·log(m·n)) where m is the number of rows and n is the number of columns in the grid
 * Space: O(m·n) for the priority queue and life matrix
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional,NamedTuple
import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        life=[[-1]*n for _ in range(m)]
        if grid[0][0]==1: health-=1
        pq=[(-health,0,0)]
        life[0][0]=health
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        while len(pq)!=0:
            curr= heapq.heappop(pq)
            currCost=-curr[0]
            xCord=curr[1]
            yCord=curr[2]
            for i in range(4):
                newX=xCord+x[i]
                newY=yCord+y[i]
                if newX<0 or newX>=m or newY<0 or newY>=n: continue
                newCost=currCost
                if grid[newX][newY]==1: newCost-=1
                if newCost<=0 or life[newX][newY]>=newCost: continue
                life[newX][newY]=newCost
                heapq.heappush(pq,(-newCost,newX,newY))
        return life[m-1][n-1]>0