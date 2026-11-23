"""
 * LeetCode: 1352 - Product of the Last K Numbers
 * Link: https://leetcode.com/problems/product-of-the-last-k-numbers/
 * Difficulty: Medium
 * Time: O(1) for both add and getProduct
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class ProductOfNumbers:

    def __init__(self):
        self.nearestZero=float("-inf")
        self.prod=1
        self.products=[]

    def add(self, num: int) -> None:
        self.prod*=num
        self.products.append(self.prod)
        if num==0:
            self.prod=1
            self.nearestZero=len(self.products)-1

    def getProduct(self, k: int) -> int:
        n=len(self.products)
        if n-k<=self.nearestZero: return 0
        elif n==k or self.products[n-1-k]==0: return self.prod
        return self.prod