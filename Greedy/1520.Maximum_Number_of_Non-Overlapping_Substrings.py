""" 
* LeetCode: 1520 - Maximum Number of Non-Overlapping Substrings
 * Link: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
 * Difficulty: Medium
 * Time: O(n) where n is length of input string
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        ans=[]
        n=len(s)
        u_map={}
        for i in range(n):
            if s[i] not in u_map:
                u_map[s[i]]=[1,i,i]
            else:
                u_map[s[i]][0]+=1
                u_map[s[i]][2]=i
        intervals=[]
        for c in range(ord('a'),ord('z')+1):
            c=chr(c)
            if c not in u_map:
                continue
            startIndex=u_map[c][1]
            endIndex=u_map[c][2]
            valid=True
            for i in range(startIndex,endIndex+1):
                x=s[i]
                if u_map[x][1]<startIndex:
                    valid=False
                    break
                endIndex=max(endIndex,u_map[x][2])
            if valid:
                intervals.append([startIndex,endIndex])
        intervals.sort(key=lambda x:x[1])
        prevIndex=-1
        for interval in intervals:
            startIndex=interval[0]
            endIndex=interval[1]
            if startIndex>prevIndex:
                ans.append(s[startIndex:endIndex+1])
                prevIndex=endIndex
        return ans