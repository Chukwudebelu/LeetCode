#!/bin/python3
from itertools import accumulate

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        return the maximized sum for an integer array of even length
        """    
        # To maximize the sum of pairs sort the array
        nums = sorted(nums)
        return [*accumulate([min(nums[i], nums[i-1]) for i in range(len(nums)-1,-1,-2)], lambda a, b: a + b)][-1]
