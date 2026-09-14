"""
 * LeetCode: 106 - Construct Binary Tree from Inorder and Postorder Traversal
 * Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
 * Difficulty: Medium
 * Time: O(n) where n is the number of nodes in the graph
 * Space: O(n) for adjecency list, set and deque
 """
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def formTree(inorder: List[int],postorder: List[int],postLeft: int,postRight: int,inLeft: int,inRight: int,u_map: dict):
            if postLeft>postRight or inLeft>inRight: return None
            root=TreeNode(postorder[postRight])
            index=u_map[root.val]
            dist=inRight-index
            root.right=formTree(inorder,postorder,postRight-dist,postRight-1,index+1,inRight,u_map)
            root.left=formTree(inorder,postorder,postLeft,postRight-dist-1,inLeft,index-1,u_map)
            return root
        u_map={}
        n=len(inorder)
        for i in range(n): u_map[inorder[i]]=i
        return formTree(inorder,postorder,0,len(postorder)-1,0,len(inorder)-1,u_map)