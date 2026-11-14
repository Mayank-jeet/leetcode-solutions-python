"""
 * LeetCode: 309 - Best Time to Buy and Sell Stock with Cooldown
 * Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldowns/
 * Difficulty: Medium
 * Time: O(n) where n is the length of prices
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold=-prices[0]
        sold=0
        rest=0
        for p in prices:
            nh=max(hold,rest-p)
            ns=hold+p
            nr=max(rest,sold)
            hold=nh;sold=ns;rest=nr
        return max(sold,rest)