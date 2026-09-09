"""
 * LeetCode: 3871 - Count Commas in Range II
 * Link: https://leetcode.com/problems/count-commas-in-range-ii/
 * Difficulty: Medium
 * Time: O(d) where d is the number of degits in n
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000000: return max(n-999,0)
        ans=0
        temp=n
        count=0
        commas=0
        lastCount=1
        currentCount=1000
        while temp>0:
            count+=1
            if count>1 and (count-1)%3==0:
                if count>6:
                    lastCount*=1000
                    currentCount*=1000
                    ans+=commas*(currentCount-lastCount)
                commas+=1
                if temp<1000: break
            temp/=10
        ans+=commas*(n-currentCount+1)
        return ans