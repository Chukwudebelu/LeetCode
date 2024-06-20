class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if (len(nums) <= 2):
            return max(nums)
        else:
            return sorted(nums, reverse=True)[2]
