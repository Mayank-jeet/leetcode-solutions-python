"""
 * LeetCode: 4066 - Maximum Equal Adjacent Pairs After at Most One Replacement
 * Link: https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-at-most-one-replacement/
 * Difficulty: Medium
 * Time: O(n) where n is length of input vector
 * Space: O(n)
"""
from collections import deque, defaultdict, Counter
from typing import List, Optional
import heapq
from collections import defaultdict
class Solution:
    def maxEqualAdjacentPairs(self,nums:list[int])->int:
        replace_map=defaultdict(lambda:defaultdict(int))
        pairMap=defaultdict(int)
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i-1]!=nums[i]:
                replace_map[nums[i-1]][nums[i]]+=1
            if i<n-1:
                if nums[i+1]==nums[i]:
                    pairMap[nums[i]]+=1
                else:
                    replace_map[nums[i+1]][nums[i]]+=1
        baseline=sum(pairMap.values())
        ans=baseline
        for outer_val in replace_map.values():
            for inner_val in outer_val.values():
                ans=max(ans,baseline+inner_val)
        return ans