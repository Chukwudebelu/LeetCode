# 1207. Unique Number of Occurences
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        return len(set(Counter(arr).values())) == len(Counter(arr).keys())
