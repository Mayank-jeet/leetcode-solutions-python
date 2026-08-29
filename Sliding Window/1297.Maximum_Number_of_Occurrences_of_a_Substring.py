"""
 * LeetCode: 1297 - Maximum Number of Occurrences of a Substring
 * Link: https://leetcode.com/maximum-number-of-occurrences-of-a-substring/
 * Difficulty: Medium
 * Time: O(n) where n is length of input string
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr_freq=defaultdict(int) 
        letter_freq=defaultdict(int) 
        low=0
        unique_letter_count=0
        n=len(s)
        ans=0
        for i in range(n):
            letter_freq[s[i]]+=1
            if letter_freq[s[i]]==1: unique_letter_count+=1
            if i-low+1>minSize:
                letter_freq[s[low]]-=1
                if letter_freq[s[low]]==0: unique_letter_count-=1
                low+=1
            if i-low+1==minSize and unique_letter_count<=maxLetters:
                sub_string=s[low:i+1]
                substr_freq[sub_string]+=1
                ans=max(ans,substr_freq[sub_string])
        return ans