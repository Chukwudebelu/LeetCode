#!/bin/python3
# 1636. Sort Array by Increasing Frequency

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        unique_nums = [*set(nums)]  # Get unique numbers in nums
        lists = []

        for num in unique_nums:  # Store numbers & their frequencies as an ordered pair: (num, freq)
            lists += [(num, nums.count(num))]

        sorted_nums_with_freqs = sorted(lists, key = lambda x: (x[1], -x[0]))
        
        sorted_nums = list()

        for i, j in sorted_nums_with_freqs:
            sorted_nums.extend([i] * j)

        return sorted_nums
