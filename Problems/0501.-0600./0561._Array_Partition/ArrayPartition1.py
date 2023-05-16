#!/bin/python3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
    
        # To maximize the sum of pairs sort the array
        nums = sorted(nums, reverse = 0)
        
        n -= 1; 
        max_sum = 0
        while (n >= 0):
            max_sum += min(nums[n], nums[n-1])
            n -= 2
        return max_sum

        
