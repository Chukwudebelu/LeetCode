import operator

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return reduce(operator.add, [num1, num2])
