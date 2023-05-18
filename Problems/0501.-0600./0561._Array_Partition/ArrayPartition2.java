//#!/bin/java
import java.util.ArrayList<E>;

class Solution {
    public int arrayPairSum(int[] nums) {
        // Sort the array
        Arrays.sort(nums);
        
        // Hold the maximum sum
        int max_sum = 0;
                
        // Store all the minimums of pairs
        List<Integer> mins = new ArrayList<>(0);
        
        // Loop through pairs
        for (int j = nums.length-1; j > -1; j -= 2)
            mins.add(Math.min(nums[j-1], nums[j]));
        
        // Sum the items in the arraylist collection
        for (int m : mins)
            max_sum += m;
        
        return max_sum;
    }
}
