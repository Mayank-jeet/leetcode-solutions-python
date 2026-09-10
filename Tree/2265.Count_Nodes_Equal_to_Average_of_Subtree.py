"""
 * LeetCode: 2265 - Count Nodes Equal to Average of Subtree
 * Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
 * Difficulty: Medium
 * Time: O(n) where n is the number of nodes in the tree
 * Space: O(n) recursive stack space used for traversing the tree 
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if not root:
                return (0,0)
            leftTree=dfs(root.left)
            rightTree=dfs(root.right)
            sum=leftTree[0]+rightTree[0]+root.val
            nodes=leftTree[1]+rightTree[1]+1
            if root.val==sum//nodes: ans+=1
            return (sum,nodes)
        dfs(root)
        return ans