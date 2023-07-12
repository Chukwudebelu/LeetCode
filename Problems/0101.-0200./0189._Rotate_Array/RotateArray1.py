#!/bin/python3

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums); k %= n
        if (n > k):
            '''
            create a new array to hold elements from the kth index (behind) to the end
            nums                     arr
            [1, 2, 3, 4, 5, 6, 7] -> [5, 6, 7] if k = 3
            (length-k to length-1)
            '''
            arr = [0]*k
            arr1 = [0]*(n-k)
            for i in range(k-1,-1,-1):
                arr[i] = nums[n-k+i]

            for j in range(n-k):
                arr1[j] = nums[j]
            
            for m in range(n):
                nums[m] = arr[m] if (m < k) else arr1[m-k]
