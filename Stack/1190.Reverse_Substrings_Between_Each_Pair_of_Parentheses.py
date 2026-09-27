"""
 * LeetCode: 1190 - Reverse Substrings Between Each Pair of Parentheses
 * Link: https://leetcode.com/problems/reorder-list/
 * Difficulty: Medium
 * Time: O(n) is n length of input vector
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n=len(s)
        mat=[0]*n
        st=[]
        for i in range(n):
            if s[i]=='(': st.append(i)
            elif s[i]==')':
                open=st[-1]
                st.pop()
                mat[open]=i
                mat[i]=open
        result=[]
        direction=1
        i=0
        while 0<=i<n:
            if s[i]=='(' or s[i]==')':
                i=mat[i]
                direction=-direction
            else:
                result.append(s[i])
            i+=direction
        return ''.join(result)