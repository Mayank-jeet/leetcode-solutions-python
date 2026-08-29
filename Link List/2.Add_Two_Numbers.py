""""
 * LeetCode: 2 - Add Two Numbers
 * Link: https://leetcode.com/add-two-numbers/
 * Difficulty: Medium
 * Time: O(max(n,m)) where n and m are number of nodes in list l1 and l2 respectively
 * Space: O(max(n,m))
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            ans=ListNode(0)
            curr=ans
            carry=0
            while l1 or l2:
                digit=carry
                if l1:
                    digit+=l1.val
                    l1=l1.next
                if l2:
                    digit+=l2.val
                    l2=l2.next
                carry=int(digit/10)
                curr.next=ListNode(digit%10)
                curr=curr.next
            if carry!=0:
                curr.next=ListNode(carry)
            return ans.next