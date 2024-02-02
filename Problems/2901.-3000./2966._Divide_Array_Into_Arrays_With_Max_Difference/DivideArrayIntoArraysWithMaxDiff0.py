# 2966. Divide Array Into Arrays With Max Difference

class Solution:
    def divideArray(self, nums: list, k: int) -> list:
        n = len(nums) # array size
        nums.sort(reverse=False) # Sort the array
        arr, i = [], 0

        while (i <= n - 3):
            sub_arr = []
            if ((nums[i+1] - nums[i]) <= k) and ((nums[i+2] - nums[i]) <= k):
                sub_arr += [nums[i], nums[i+1], nums[i+2]]
                arr.append(sub_arr)
                i += 3
            else:
                i += 1
    
        # Check that output array has a length: n/3
        if (n > len(arr)*3):
            return []
        else:
            return arr
