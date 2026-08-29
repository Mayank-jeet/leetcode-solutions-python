"""
 * LeetCode: 98 - Validate Binary Search Tree
 * Link: https://leetcode.com/problems/validate-binary-search-tree/
 * Difficulty: Medium
 * Time: O(n) where n is the number of nodes in the tree
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def dfs(self,root,maxLimit,minLimit,ans):
        if not root or not ans[0]:
            return
        if root.val<minLimit or root.val>maxLimit:
            ans[0]=False
        self.dfs(root.left,root.val-1,minLimit,ans)
        self.dfs(root.right,maxLimit,root.val+1,ans)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[True]
        self.dfs(root.left,root.val-1,float('-inf'),ans)
        self.dfs(root.right,float('inf'),root.val+1,ans)
        return ans[0]