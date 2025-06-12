#!/bin/python3
# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

class Solution:
    def maxAdjacentDistance(self, nums: list) -> int:
        if len(nums) == 2:
            return abs(nums[1] - nums[0]) if (nums[1] > nums[0]) else (abs(nums[0] - nums[1]) if (nums[0] > nums[1]) else 0)
        else:
            largest = -101
            for i in range(0, len(nums)-1):
                diff = abs(nums[i+1] - nums[i])
                largest = max(diff, largest)
            
            return max(largest, abs(nums[len(nums)-1] - nums[0]))
