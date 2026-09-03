"""
 * LeetCode: 3876 - Construct Uniform Parity Array II
 * Link: https://leetcode.com/problems/construct-uniform-parity-array-ii/
 * Difficulty: Medium
 * Time: O(n*√m) where n is size of input vector and m is maximum element is input vector
 * Space: O(k) where k is number of distinct elements in input vector
"""
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallestOdd=1e9
        odd=True
        even=True
        for el in nums1:
            if el%2==1: smallestOdd=min(smallestOdd,el)
        for el in nums1:
            if el%2==0:
                if smallestOdd>=el: odd=False
            else:
                if smallestOdd>=el: even=False
        return odd or even