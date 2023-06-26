#!/bin/python3
class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        """
        Move all the even integers at the beginning of 
        the array followed by all the odd integers
        """
        evens = [e for e in nums if e % 2 == 0]
        odds = [o for o in nums if o % 2]
        evens.extend(odds)
        return evens
