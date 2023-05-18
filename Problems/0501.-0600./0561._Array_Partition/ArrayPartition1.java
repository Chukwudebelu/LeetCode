//#!/bin/java
class Solution {
    public int arrayPairSum(int[] nums) {
        // Sort the array
        Arrays.sort(nums);
        
        // Hold the maximum sum
        int max_sum = 0;
        for (int i = nums.length-1; i > -1; i -= 2) {
            max_sum += Math.min(nums[i-1], nums[i]);
        }
        return max_sum;
    }
}
