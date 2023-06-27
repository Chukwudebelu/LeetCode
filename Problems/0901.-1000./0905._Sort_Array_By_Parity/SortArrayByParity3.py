#!/bin/python3

class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        lst = list()
        i = 0
      
        while (i < len(nums)): # Insert all EVEN #s first
            if (nums[i] % 2 == 0):
                lst += [nums[i]]
            i += 1
        
        j = 0
        while (j < len(nums)): # Then, insert all ODD #s
            if (nums[j] % 2):
                lst += [nums[j]]
            j += 1
        return lst
