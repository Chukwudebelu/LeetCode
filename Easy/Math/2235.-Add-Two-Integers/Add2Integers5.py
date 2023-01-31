from functools import reduce

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return reduce(lambda a, b: a + b, [num1, num2])
