# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]  # if x = 0: sign = -1
        rev = sign * int(''.join(reversed(str(abs(x)))))
        return [0, rev][-2**31 <= rev <= 2**31-1]
