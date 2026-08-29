"""
 * LeetCode: 143 - Reorder List
 * Link: https://leetcode.com/problems/reorder-list/
 * Difficulty: Medium
 * Time: O(n) is n is the number of nodes in the linked list
 * Space: O(s) for stack
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None: return
        slow=head
        fast=head
        s=[]
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        while slow:
            slow=slow.next
            if slow: s.append(slow)
        slow=head
        while len(s)!=0:
            copy=slow.next
            slow.next=s[-1]
            s[-1].next=copy
            s.pop()
            slow=slow.next.next
        slow.next=None