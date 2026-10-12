"""
 * LeetCode: 4079 - Prime Subset Selection I
 * Link: https://leetcode.com/problems/prime-subset-selection-i/
 * Difficulty: Medium
 * Time: O(n√n)
 * Space: O(k) for ans, where k is the number of primes picked
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def maxPrimes(self,n,s):
        if n<2 or s<2:
            return []
        is_prime=[True]*(n+1)
        is_prime[0]=is_prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n+1,i):
                    is_prime[j]=False
        ans=[]
        total=0
        for i in range(2,n+1):
            if is_prime[i]:
                if total+i>s:
                    break
                total+=i
                ans.append(i)
        return ans