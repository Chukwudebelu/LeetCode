#!/bin/python3

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0; length = len(nums)
    
        while (0 <= i < length):
            if (nums[i] == val):
                for j in range(i, length-1):
                    nums[j] = nums[j+1]
                length -= 1
                i -= 1  # In case of duplicate
            i += 1
        return length
