""" 
 * LeetCode: 1401 - Circle and Rectangle Overlapping
 * Link: https://leetcode.com/problems/circle-and-rectangle-overlapping/
 * Difficulty: Medium
 * Time: O(1)
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def clamp(value,minimum,maximum):
            return max(minimum,min(value,maximum))
        x=clamp(xCenter,x1,x2)-xCenter
        y=clamp(yCenter,y1,y2)-yCenter
        return x*x+y*y<=radius*radius