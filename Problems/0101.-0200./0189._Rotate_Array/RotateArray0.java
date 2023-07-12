//#!/bin/java
  
class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        if (nums.length > k) {
            // create a new array to hold elements from the kth index (behind) to the end
            // nums                     arr
            // [1, 2, 3, 4, 5, 6, 7] -> [5, 6, 7] if k = 3
            // (length-k to length-1)
            int[] arr = new int[k]; 
            int[] arr1 = new int[nums.length-k];

            for (int i = k-1; i >= 0; i--)
                arr[i] = nums[nums.length-(k-i)];

            for (int j = 0; j < nums.length-k;j++)
                arr1[j] = nums[j];
        
            for (int m = 0; m < nums.length; m++) {
                if (m < k) nums[m] = arr[m];
                else  nums[m] = arr1[m-k];
            }
        }
    }
}
