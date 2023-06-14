//!/bin/java

class Solution {
    public int removeElement(int[] nums, int val) {
        int len, i;
        len = nums.length;
        i = 0; 
        
        while (0 <= i && i < len) {
            if (nums[i] == val) {
                for (int j = i; j < len-1; j++) {
                    nums[j] = nums[j+1]; // loop to move elements left
                }
                len -= 1;
                i -= 1;
            }
            i += 1;
        }
    return len;
    }
}
