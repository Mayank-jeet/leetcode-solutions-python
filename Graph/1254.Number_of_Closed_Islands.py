"""
 * LeetCode: 1254 - Number of Closed Islands
 * Link: https://leetcode.com/problems/number-of-closed-islands/
 * Difficulty: Medium
 * Time: O(m·n) where m is number of rows, n is number of columns
 * Space: O(m·n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        vis=[[0]*n for _ in range(m)]
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        def bfs(sx,sy):
            closed=True
            q=deque([(sx,sy)])
            vis[sx][sy]=1
            while q:
                x,y=q.popleft()
                if x==0 or y==0 or x==m-1 or y==n-1:
                    closed=False
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    if nx<0 or ny<0 or nx>=m or ny>=n:
                        continue
                    if grid[nx][ny]==0 and not vis[nx][ny]:
                        vis[nx][ny]=1
                        q.append((nx,ny))
            return closed
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and not vis[i][j]:
                    if bfs(i,j):
                        ans+=1
        return ans