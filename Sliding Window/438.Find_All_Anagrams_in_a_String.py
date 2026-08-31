"""
 * LeetCode: 438 - Find All Anagrams in a String
 * Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
 * Difficulty: Medium
 * Time: O(max(p_length,s_length)) where p_length and s_length are lengths of input strings s and p respectively
 * Space: O(u) where u is number of unique elements in input sting p
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        s_length=len(s)
        p_length=len(p)
        if s_length<p_length: return ans
        u_map=defaultdict(int)
        distEl=0
        for el in p:
            u_map[el]+=1
            if u_map[el]==1: distEl+=1
        for i in range(s_length):
            if i-p_length>=0:
                if s[i-p_length] in u_map:
                    u_map[s[i-p_length]]+=1
                    if u_map[s[i-p_length]]==0:
                        distEl-=1
                    elif u_map[s[i-p_length]]==1:
                        distEl+=1

            if s[i] in u_map:
                u_map[s[i]]-=1
                if u_map[s[i]]==0:
                    distEl-=1
                elif u_map[s[i]]==-1:
                    distEl+=1
                if distEl==0:
                    ans.append(i-p_length+1)

        return ans