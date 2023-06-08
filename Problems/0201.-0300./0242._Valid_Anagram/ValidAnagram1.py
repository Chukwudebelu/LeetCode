#!/bin/python3
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use a Counter object to get the frequenices of characters in each string
        char_count_s = Counter(s)
        char_count_t = Counter(t)

        return char_count_s == char_count_t
