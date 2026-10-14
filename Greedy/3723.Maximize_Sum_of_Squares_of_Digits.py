"""
 * LeetCode: 3723 - Maximize Sum of Squares of Digits
 * Link: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
 * Difficulty: Medium
 * Time: O(num)
 * Space: O(num) for ans string
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num: return ""
        ans=[]
        for _ in range(num):
            digit=min(sum,9)
            ans.append(str(digit))
            sum-=digit
        return "".join(ans)