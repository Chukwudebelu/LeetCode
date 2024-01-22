# 654. Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = sum(nums) - sum(set(nums))
        s = {i for i in range(1, len(nums)+1)}
        return [duplicate] + list(set(nums) ^ s)
