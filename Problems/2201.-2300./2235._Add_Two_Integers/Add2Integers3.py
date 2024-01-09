import operator
from itertools import accumulate

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return list(accumulate([num1, num2], operator.add))[-1]
