"""
 * LeetCode: 3947 - Maximum Number of Items From Sale II
 * Link: https://leetcode.com/problems/prime-subset-selection-i/
 * Difficulty: Medium
 * Time: O(nlog(n))
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def maximumSaleItems(self,items:List[List[int]],budget:int)->int:
        n=len(items)
        cheapest=min(price for _,price in items)
        have=[0]*(n+1)
        for factor,_ in items:
            have[factor]+=1
        deals=[-1]*(n+1)
        for f in range(1,n+1):
            for m in range(f,n+1,f):
                deals[f]+=have[m]
        copies=0
        for factor,price in sorted(items,key=lambda x:x[1]):
            if price>=2*cheapest or price>budget:
                break
            pairs=min(deals[factor],budget//price)
            copies+=2*pairs
            budget-=pairs*price
        return copies+budget//cheapest