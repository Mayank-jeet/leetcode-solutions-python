"""
 * LeetCode: 32 - Longest Valid Parentheses
 * Link: https://leetcode.com/problems/longest-valid-parentheses/
 * Difficulty: Hard
 * Time: O(n) where n is the length of the input string
 * Space: O(n) in worst case where all characters are '('
 """
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0
        n=len(s)
        st=[]
        dp={}
        for i in range(n):
            if s[i]=='(': st.append(i)
            else:
                if len(st)==0: continue
                else:
                    last=st[-1]
                    st.pop()
                    length=(i-last+1)
                    if last-1>=0 and dp.get(last-1): length+=dp[last-1]
                    dp[i]=length
                    ans=max(ans,length)
        return ans