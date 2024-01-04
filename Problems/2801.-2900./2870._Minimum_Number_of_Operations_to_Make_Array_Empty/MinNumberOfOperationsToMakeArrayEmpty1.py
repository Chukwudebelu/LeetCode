#!/bin/python3
import math
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_count, ops = Counter(nums), 0

        for val in num_count.values():
            if (val == 1):
                return -1
            else:
                ops += math.ceil(val / 3)
        return ops
