class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
    
        # To maximize the sum of pairs sort the array
        nums = sorted(nums, key = lambda x: x)
        
        n -= 1
        max_sum = 0
        for i in range(n,-1,-2):
            max_sum += min(nums[i], nums[i-1])
        return max_sum
