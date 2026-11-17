"""
 * LeetCode: 2911 - Minimum Changes to Make K Semi-palindromes
 * Link: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
 * Difficulty: Hard
 * Time: O(n³log(n)+n²k) where n is the length of the array
 * Space: O(n²+nk)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for L in range(2 * d, n + 1, d):
                divs[L].append(d)
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                for d in divs[L]:
                    m = L // d
                    cur = 0
                    for r in range(d):
                        for t in range(m // 2):
                            cur += s[i + r + t * d] != s[i + r + (m - 1 - t) * d]
                    cost[i][j] = min(cost[i][j], cur)
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for p in range(1, k + 1):
                for prev in range(i - 1):
                    if dp[prev][p - 1] != INF:
                        dp[i][p] = min(dp[i][p], dp[prev][p - 1] + cost[prev][i - 1])
        return dp[n][k]