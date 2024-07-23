#!/bin/python3

import collections as clt

class Solution(object):
    def frequencySort(self, nums: list[int]) -> list[int]:
        numFreqs = clt.Counter(nums)
        return sorted(nums, key = lambda x: (numFreqs[x], -x))
