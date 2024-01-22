# 654. Set Mismatch
class Solution:
    def findErrorNums(self, nums: list) -> list:
        duplicate = sum(nums) - sum(set(nums))
        n = len(nums)
        missing = (n*(n+1))//2 - sum(set(nums))
        return [duplicate, missing]
