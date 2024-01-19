# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        current_step, next_step = 1, 2
        for i in range(2, n+1):
            next_step, current_step = next_step + current_step, next_step
        return current_step
