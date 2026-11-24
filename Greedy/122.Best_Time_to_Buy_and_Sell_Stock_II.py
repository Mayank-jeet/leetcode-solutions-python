"""
 * LeetCode: 122 - Best Time to Buy and Sell Stock II
 * Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
 * Difficulty: Medium
 * Time: O(n) where n is length of input list
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]: ans+=prices[i]-prices[i-1]
        return ans