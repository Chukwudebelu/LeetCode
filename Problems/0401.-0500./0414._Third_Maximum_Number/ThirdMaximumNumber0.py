#!/bin/python3
# 414. Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Get the 1st unique maximum
        first_max = -10**10-7; i = 0
        while (i < len(nums)):
            if (nums[i] > first_max):
                first_max = nums[i]
            i += 1

        # Get the 2nd unique maximum number
        second_max = -10**10-8; j = 0
        while (j < len(nums)):
            if (nums[j] > second_max and nums[j] < first_max):
                second_max = nums[j]
            j += 1

        # Get the 3rd unique maximum number
        third_max = -10**10-9; k = 0
        while (k < len(nums)):
            if (nums[k] > third_max and nums[k] < second_max):
                third_max = nums[k]
            k += 1
        return (third_max if (third_max != -10**10-9) else first_max)
