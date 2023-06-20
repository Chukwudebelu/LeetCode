#!/bin/python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while (i < length-1):
            if (nums[i] == nums[i+1]): # Check that no 2 elements are equal;
                # if they're then there's a duplicate
                j = i;
                while (j < length-1):
                    nums[j] = nums[j+1]
                    j += 1
                length -= 1 # decrease the overall length
                i -= 1
            i += 1
        return length
