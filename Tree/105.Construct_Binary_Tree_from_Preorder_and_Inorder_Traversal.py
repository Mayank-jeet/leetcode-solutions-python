"""
 * LeetCode: 105 - Construct Binary Tree from Preorder and Inorder Traversal
 * Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def formTree(preorder,inorder,preLeft,preRight,inLeft,inRight,u_map):
            if preLeft>preRight or inLeft>inRight: return None
            root=TreeNode(preorder[preLeft])
            index=u_map[preorder[preLeft]]
            left=index-inLeft
            root.left=formTree(preorder,inorder,preLeft+1,preLeft+left,inLeft,index-1,u_map)
            root.right=formTree(preorder,inorder,preLeft+left+1,preRight,index+1,inRight,u_map)
            return root
        u_map={}
        n=len(inorder)
        for i in range(n): u_map[inorder[i]]=i
        return formTree(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1,u_map)