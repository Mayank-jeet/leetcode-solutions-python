"""
 * LeetCode: 2267  Check if There Is a Valid Parentheses String Path
 * Link: https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
 * Difficulty: Hard
 * Time: O(m*n*(m+n)) where m and n are number of rows and columns in input grid respectively
 * Space: O(m*n*(m+n))
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==')' or (m+n-1)%2==1: return False
        q=deque([(1, 0, 0)])
        x=[0,1]
        y=[1,0]
        scoreMap=[[set() for _ in range(n)] for _ in range(m)]
        scoreMap[0][0].add(1)
        while len(q)!=0:
            score,xCord,yCord=q.popleft()
            if score>(m+n-1)/2: continue
            if xCord==m-1 and yCord==n-1 and score==0: return True
            for i in range(2):
                newX=x[i]+xCord
                newY=y[i]+yCord
                if newX<0 or newX>=m or newY<0 or newY>=n: continue
                change=1
                if grid[newX][newY]==')': change=-1
                newScore=score+change
                if newScore<0 or newScore in scoreMap[newX][newY]: continue
                scoreMap[newX][newY].add(newScore)
                q.append((newScore,newX,newY))
        return False