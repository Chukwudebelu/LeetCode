#!/bin/python3

class Solution:
    def sortArrayByParity(self, nums: list) -> list:
        """
        Move all the even integers at the beginning of the array 
        followed by all the odd integers.
        """
        lsteven = []
        lstodd = []
        for i in nums:
            if i % 2: # odd
                lstodd += [i]
            else:
                lsteven += [i]
        return lsteven + lstodd
