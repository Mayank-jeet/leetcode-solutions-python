"""
 * LeetCode: 11 - Container With Most Water
 * Link: https://leetcode.com/problems/container-with-most-water/
 * Difficulty: Medium
 * Time: O(n) where n is the size of the input vector
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        ans=0
        area=0
        while i<j:
            area=min(height[i],height[j])*(j-i)
            ans=max(area,ans)
            if height[i]>height[j]: j-=1
            else: i+=1
        return ans