"""
 * LeetCode: 123 - Best Time to Buy and Sell Stock III
 * Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
 * Difficulty: Hard
 * Time: O(n) where n is the length of the array
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1=-float('inf')
        buy2=-float('inf')
        sold1=0
        sold2=0
        for p in prices:
            buy1=max(buy1,-p)
            sold1=max(sold1,buy1+p)
            buy2=max(buy2,sold1-p)
            sold2=max(sold2,buy2+p)
        return sold2