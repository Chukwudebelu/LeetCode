class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        dummy_num = nums.copy()
        max_num = max(nums)
        nums.remove(max_num)
        
        if max_num >= 2*max(nums):
            return dummy_num.index(max_num)
        else:
            return -1
