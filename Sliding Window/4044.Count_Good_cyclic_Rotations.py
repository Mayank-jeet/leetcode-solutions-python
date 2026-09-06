"""
 * LeetCode: 4044 - Count Good Cyclic Rotations
 * Link: https://leetcode.com/problems/count-good-cyclic-rotations/
 * Difficulty: Medium
 * Time: O(n)
 * Space: O(1)
"""
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        sum1=0
        sum2=0
        n=len(nums)
        for i in range(n):
            if i<n/2: sum1+=nums[i]
            else: sum2+=nums[i]
        ans=0
        for i in range(n):
            if sum1>sum2: ans+=1
            sum2+=nums[i]
            sum2-=nums[(int)(i+n/2)%n]
            sum1+=nums[(int)(i+n/2)%n]
            sum1-=nums[i]
        return ans