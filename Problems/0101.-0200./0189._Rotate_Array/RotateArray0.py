#!/bin/python3

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if (len(nums) > k):
            arr = nums[:len(nums)-k]
            arr1 = nums[len(nums)-k:]
            for i in range(len(nums)):
                nums[i] = arr1[i] if (i < k) else arr[i-k]
