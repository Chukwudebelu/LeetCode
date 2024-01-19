# 1833. Maximum Ice Cream Bars

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        n, ice_cream = len(costs), 0

        while (ice_cream < n and costs[ice_cream] <= coins):
            coins -= costs[ice_cream]
            ice_cream += 1
        return ice_cream
