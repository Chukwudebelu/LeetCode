#!/bin/python3
class Solution:
    def arrayPairSum(self, nums: list) -> int:
        """
        return the maximized sum for an integer array of even length
        """
        n = len(nums)
    
        # To maximize the sum of pairs sort the array
        nums.sort(reverse = False);
        
        k = n-1; 
        max_sum = 0
        while (k >= 0):
            max_sum += min(nums[k], nums[k-1])
            k -= 2
        return max_sum
