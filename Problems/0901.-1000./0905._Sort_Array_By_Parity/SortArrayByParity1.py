#!/bin/python3
class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        return [i for i in nums if i % 2 == 0] + [j for j in nums if j % 2]
