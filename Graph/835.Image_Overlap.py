"""
 * LeetCode: 835 - Image Overlap
 * Link: https://leetcode.com/problems/image-overlap/
 * Difficulty: Medium
 * Time: O(n^2+k1·k2) where n is the number of row or column in inuput matrix and k1 and k2 are the number of  1s in img1 and img2 respectively
 * Space: O(n^2)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        store1=[]
        store2=[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1: store1.append((i,j))
                if img2[i][j]==1: store2.append((i,j))
        ans=0
        coordMap=[[0]*(2*n) for _ in range(2*n)]
        for el1 in store1:
            for el2 in store2:
                delX=el1[0]-el2[0]+n
                delY=el1[1]-el2[1]+n
                coordMap[delX][delY]+=1
                ans=max(ans,coordMap[delX][delY])
        return ans