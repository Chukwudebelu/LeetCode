#!/bin/python3
from functools import reduce

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        return the maximized sum for an integer array of even length
        """
        # To maximize the sum of pairs sort the array
        nums.sort()
        return reduce(lambda a, b: a + b, [min(nums[i], nums[i-1]) for i in range(len(nums)-1,-1,-2)])
