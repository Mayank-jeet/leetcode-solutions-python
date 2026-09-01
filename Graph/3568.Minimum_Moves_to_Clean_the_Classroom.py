"""
 * LeetCode:  3568 - Minimum Moves to Clean the Classroom
 * Link: https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/
 * Difficulty: Medium
 * Time: O(m*n*2^L) where m is number of rows, n is number of columns and L is number of lockers
 * Space: O(m*n*2^L)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m=len(classroom)
        n=len(classroom[0])
        sr=-1
        sc=-1
        cnt=0
        id=[[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    sr=i
                    sc=j
                if classroom[i][j]=='L':
                    id[i][j]=cnt
                    cnt+=1
        masks=1<<cnt
        fullMask=masks-1
        best=[[[-1]*masks for _ in range(n)] for _ in range(m)]
        q=deque()
        q.append((sr,sc,0,energy,0))
        best[sr][sc][0]=energy
        dr=[-1,1,0,0]
        dc=[0,0,-1,1]
        while q:
            r,c,mask,en,dist=q.popleft()
            if mask==fullMask:
                return dist
            if en==0:
                continue
            for d in range(4):
                nr=r+dr[d]
                nc=c+dc[d]
                if nr<0 or nc<0 or nr>=m or nc>=n:
                    continue
                if classroom[nr][nc]=='X':
                    continue
                newEn=en-1
                newMask=mask
                if classroom[nr][nc]=='L':
                    newMask|=(1<<id[nr][nc])
                if classroom[nr][nc]=='R':
                    newEn=energy
                if best[nr][nc][newMask]>=newEn:
                    continue
                best[nr][nc][newMask]=newEn
                q.append((nr,nc,newMask,newEn,dist+1))
        return -1