"""
 * LeetCode: 3414 - Maximum Score of Non-overlapping Intervals
 * Link: https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
 * Difficulty: Hard
 * Time: O(nlog(n)) where n is size of input list
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        sortedIntervals=[(r,l,weight,i) for i,(l,r,weight) in enumerate(intervals)]
        sortedIntervals.sort(key=lambda x: x[0])
        dp=[[(0,[]) for _ in range(5)] for _ in range(len(intervals)+1)]
        for i,(end,start,weight,originalIndex) in enumerate(sortedIntervals):
            k=bisect_left(sortedIntervals,(start,),hi=i) 
            for j in range(1,5):
                prevWeight,prevIndices=dp[k][j-1]
                skip=dp[i][j]
                takeWeight=prevWeight-weight
                takeIndices=sorted(prevIndices+[originalIndex])
                take=(takeWeight,takeIndices)          
                dp[i+1][j]=min(skip, take)
        return dp[-1][4][1]