"""
 * LeetCode: 4071 - Minimum Rotations to Dial a Number II
 * Link: https://leetcode.com/problems/minimum-rotations-to-dial-a-number-ii/
 * Difficulty: Medium
 * Time: O(n) where n is length of input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minRotations(self, n: int, s: str) -> int:
        ans=0
        curr=0
        for el in s:
            currentEl=ord(el)-ord('0')
            ans+=min(abs(currentEl-curr),10-abs(currentEl-curr))
            curr=currentEl
        tempAns=ans
        lastEl=ord(s[n-1])-ord('0')
        first=ord(s[0])-ord('0')
        ans=min(ans,tempAns-min(first,10-first)+min(lastEl,10-lastEl))
        for i in range(n-2,-1,-1):
            currentEl=ord(s[i+1])-ord('0')
            src=ord(s[i])-ord('0')
            tempAns-=min(abs(currentEl-src),10-abs(currentEl-src))
            tempAns+=min(abs(lastEl-src),10-abs(lastEl-src))
            ans=min(ans,tempAns)
            tempAns-=min(abs(lastEl-src),10-abs(lastEl-src))
            tempAns+=min(abs(currentEl-src),10-abs(currentEl-src))
        return ans