"""
 * LeetCode: 2472 - Maximum Number of Non-overlapping Palindrome Substrings
 * Link: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
 * Difficulty: Hard
 * Time: O(n^2) in worst case, where n is the length of the input string
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        end=-1
        ans=0
        for i in range(n-int((k-1)/2)):
            for l in [i-1,i]:
                r=i
                while l>=0 and r<n and s[l]==s[r] and l>end:
                    if r-l+1>=k:
                        ans+=1
                        end=r
                        break
                    l-=1;r+=1
        return ans