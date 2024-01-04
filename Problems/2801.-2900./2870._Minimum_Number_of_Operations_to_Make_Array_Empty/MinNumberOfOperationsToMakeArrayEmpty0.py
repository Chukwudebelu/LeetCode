#!/bin/python3

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Store the frequencies of the numbers
        freqs = dict()

        for num in nums:
            freqs[num] = freqs.get(num,0) + 1

        if list(freqs.values()).__contains__(1):
            return -1
        else: # Hashmap does not have any 1s
            min_ops = 0
            for i in list(freqs.values()):
                if i % 3 == 0: # multiple of 3
                    min_ops += (i // 3)
                elif i % 3 == 1: # remainder of 1
                    min_ops += math.ceil(i / 3)
                elif i % 3 == 2: # remainder of 2
                    min_ops += ((i+1)//3)
            return min_ops
