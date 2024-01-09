class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return list(accumulate([num1, num2], lambda a, b: a + b))[-1]
