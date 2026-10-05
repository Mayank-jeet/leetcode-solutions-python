"""
 * LeetCode: 856 - Score of Parentheses
 * Link: https://leetcode.com/problems/score-of-parentheses/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the string
 * Space: O(n) for the stack in worst case
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        st.append(0)
        for el in s:
            if el=='(': st.append(0)
            else:
                v=st[-1]
                st.pop()
                w=st[-1]
                st.pop()
                st.append(w+max(2*v,1))
        return st[-1]