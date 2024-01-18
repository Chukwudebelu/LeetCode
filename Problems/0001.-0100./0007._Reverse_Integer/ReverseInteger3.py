# 7. Reverse Integer
import math

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31-1
        reverse = 0

        while (x != 0):
            digit = [(x % -10), x % 10][x > 0] # (x % 10) if (x > 10) else (x % -10)
            reverse = reverse * 10 + digit
            x = math.trunc(x / 10) # x //= 10
        
        return 0 if (reverse.bit_length() > 31) else reverse
