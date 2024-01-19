# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1): return n
        else:
            a, b = 1, 2 # n = 1 or n = 2 steps
            lst = [0]*n
            lst[0] = a; lst[1] = b

            for i in range(len(lst)-2):
                lst[i+2] = lst[i] + lst[i+1]
            return lst[n-1]
