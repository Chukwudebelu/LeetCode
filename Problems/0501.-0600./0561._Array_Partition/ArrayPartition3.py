#!/bin/python3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        return the maximized sum for an integer array of even length
        """
        n = len(nums)
    
        # To maximize the sum of pairs sort the array
        nums.sort()
        return sum([min(nums[i], nums[i-1]) for i in range(n-1,-1,-2)])
