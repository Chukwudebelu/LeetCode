#!/bin/python3
# 75. Sort Colors

class Solution:
    def sortColors(self, nums: int) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if (nums[i] > nums[j]):
                    # Swap nums[i] and nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
