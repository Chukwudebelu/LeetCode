class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the #s in the list, then check every triple using
        # the triangle inequality
        nums = sorted(nums, reverse=False)
        m = 3
        lst = []
        for i in range(len(nums)-m+1):
            a = nums[i]; b = nums[i+1]; c = nums[i+2]
            if a + b > c and a + c > b and b + c > a:
                # Store all possible perimeters
                lst.append(a + b + c)
        return sorted(lst)[-1] if lst else 0
