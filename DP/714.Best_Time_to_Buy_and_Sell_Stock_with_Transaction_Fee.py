"""
 * LeetCode: 714 - Best Time to Buy and Sell Stock with Transaction Fee
 * Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
 * Difficulty: Medium
 * Time: O(n) where n is the length of the array
 * Space: O(1)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold=-prices[0]
        sold=0
        n=len(prices)
        for i in range(1,n):
            p=prices[i]
            nh=max(hold,sold-p)
            ns=max(sold,hold+p-fee)
            hold=nh
            sold=ns
        return sold