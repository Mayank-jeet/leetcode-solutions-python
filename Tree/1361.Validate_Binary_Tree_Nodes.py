""" 
 * LeetCode: 1361 - Validate Binary Tree Nodes
 * Link: https://leetcode.com/problems/validate-binary-tree-nodes/
 * Difficulty: Medium
 * Time: O(n)
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        def countNodes(l: list[int],r: list[int],root: int) -> int:
            if root==-1: return 0
            return 1+countNodes(l,r,l[root])+countNodes(l,r,r[root])
        inDegree=[0]*n
        root=-1
        for i in range(n):
            if leftChild[i]!=-1:
                if inDegree[leftChild[i]]==1: return False
                inDegree[leftChild[i]]+=1
            if rightChild[i]!=-1:
                if inDegree[rightChild[i]]==1: return False
                inDegree[rightChild[i]]+=1
        for i in range(n):
            if inDegree[i]==0:
                if root==-1: root=i
                else: return False
        if root==-1: return False
        return countNodes(leftChild,rightChild,root)==n