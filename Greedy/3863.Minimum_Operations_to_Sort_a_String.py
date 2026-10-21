"""
 * LeetCode: 3863 - Minimum Operations to Sort a String
 * Link: https://leetcode.com/problems/minimum-operations-to-sort-a-string/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def minOperations(self, s: str) -> int:
        if len(s)==1: return 0
        elif len(s)==2:
            if s[1]<s[0]: return -1
            else: return 0
        minChar='z'
        maxChar='a'
        n=len(s)
        needSorting=False
        maxCharCount=1
        minCharCount=1
        for i in range(n):
            if i!=n-1 and s[i]>s[i+1]: needSorting=True
            if s[i]<minChar:
                minChar=s[i]
                minCharCount=1
            elif s[i]==minChar: minCharCount+=1
            if s[i]>maxChar:
                maxChar=s[i]
                maxCharCount=1
            elif s[i]==maxChar: maxCharCount+=1
        if needSorting:
            if s[0]==minChar or s[n-1]==maxChar: return 1
            elif s[0]==maxChar and s[n-1]==minChar and maxCharCount==1 and minCharCount==1: return 3
            else: return 2
        return 0