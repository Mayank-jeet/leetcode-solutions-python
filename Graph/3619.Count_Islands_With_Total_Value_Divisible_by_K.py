"""
 * LeetCode: 3619 - Count Islands With Total Value Divisible by K
 * Link: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
 * Difficulty: Medium
 * Time: O(m·n) where m is number of rows and n is number of columns
 * Space: O(m·n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional,NamedTuple
import heapq
class Solution:
    def bfs(self,grid:List[List[int]],vis:List[List[int]],x:int,y:int)->int:
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        q=deque([(x,y)])
        vis[x][y]=1
        total=grid[x][y]
        m,n=len(grid),len(grid[0])
        while q:
            xCorr,yCorr=q.popleft()
            for i in range(4):
                newX,newY=xCorr+dx[i],yCorr+dy[i]
                if newX<0 or newY<0 or newX>=m or newY>=n or vis[newX][newY] or grid[newX][newY]==0:
                    continue
                vis[newX][newY]=1
                total+=grid[newX][newY]
                q.append((newX,newY))
        return total
    def countIslands(self,grid:List[List[int]],k:int)->int:
        m,n=len(grid),len(grid[0])
        vis=[[0]*n for _ in range(m)]
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0 and not vis[i][j]:
                    total=self.bfs(grid,vis,i,j)
                    if total%k==0:
                        ans+=1
        return ans