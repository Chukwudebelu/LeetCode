#!/bin/python3

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while (0 <= i < len(nums)):
            if nums.count(nums[i]) > 1:
                nums.remove(nums[i])
                i -= 1
            i += 1
        return len(nums)
