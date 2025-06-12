#!/bin/python3

class Solution(Object):
    def maxAdjacentDistance(self, nums: list]) -> int:
        return max(max([abs(nums[i+1] - nums[i]) for i in range(0, len(nums)-1)]), abs(nums[len(nums)-1] - nums[0]))
