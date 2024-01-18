# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        def cal(x: int):
            x = str(x)
            if (x[0] == '-'):
                k = x[1:(len(x)+1)]
                return 0 - int(k[::-1])
            else:
                return int(x[::-1])
                
        def cond(x): # Check for Overflow
            return (x > -2**31 and x < 2**31-1)
            
        if cond(x):
            c = cal(x)
            if cond(c):
                return c
            else:
                return 0
        else:
            return 0
