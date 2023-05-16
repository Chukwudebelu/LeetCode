//#!/bin/java
class Solution {
    public int arrayPairSum(int[] nums) {
        /* Python3 code
        n = len(nums)
    
        # To maximize the sum of pairs sort the array
        for i in range(n):
            for j in range(i+1,n):
                if (nums[j] < nums[i]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                else:
                    continue
        
        k = n-1; 
        max_sum = 0
        while (k >= 0):
            max_sum += min(nums[k],nums[k-1])
            k -= 2
        return max_sum
        */
        int n = nums.length;
        int swap_num;

        // To maximize the sum of pairs sort the array
        Arrays.sort(nums);
        /*
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (nums[j] < nums[i]) {
                    swap_num = nums[i];
                    nums[i] = nums[j];
                    nums[j] = swap_num;
                }
            }
        }
        */

        // Index for going over the minimum of pairs
        n--;
        int max_sum = 0;
        while (n >= 1) {
            max_sum += Math.min(nums[n-1], nums[n]);
            n -= 2;
        }
        return max_sum;
    }
}
