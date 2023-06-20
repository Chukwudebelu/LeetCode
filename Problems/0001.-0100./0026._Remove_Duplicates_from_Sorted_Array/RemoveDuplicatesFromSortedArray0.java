//!/bin/java
class Solution {
    public int removeDuplicates(int[] nums) {
        int i, len = nums.length;
        
        for (i = 0; i < len-1; ++i) {
            if (nums[i] == nums[i+1]) { // Check that no 2 elements are equal; if 
                // they're then there's a duplicate
                int j = i;
                while (j < len-1) {
                    nums[j] = nums[j+1];
                    ++j;
                }
                len--; i--; // decrease the overall length
            }
        }
        return len;
    }
}
