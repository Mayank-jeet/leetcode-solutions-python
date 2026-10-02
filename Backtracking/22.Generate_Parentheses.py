"""
 * LeetCode: 22 - Generate Parentheses
 * Link: https://leetcode.com/problems/generate-parentheses/
 * Difficulty: Medium
 * Time: O(n*(Cn))
 * Space: O(n*(Cn))
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def generateParenthesis(self,n:int)->list[str]:
        result=[]
        current=[]
        def generate(open_count:int,close_count:int)->None:
            if len(current)==2*n:
                result.append("".join(current))
                return
            if open_count<n:
                current.append("(")
                generate(open_count+1,close_count)
                current.pop()
            if close_count<open_count:
                current.append(")")
                generate(open_count,close_count+1)
                current.pop()
        generate(0,0)
        return result