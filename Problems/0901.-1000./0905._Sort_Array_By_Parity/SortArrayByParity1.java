//!/bin/java
class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] lst = new int[nums.length];
        int i = 0, countEven = 1;
        int j = 0, countOdd = 1;

        while (i < nums.length) {
            if (nums[i] % 2 == 0) {
                lst[countEven-1] = nums[i];
                countEven++;
            }
            i++;
        }
        while (j < nums.length) {
            if (nums[j] % 2 == 1) {
                lst[countEven+countOdd-2] = nums[j];
                countOdd++;
            }
            j++;
        }
        return lst;
    }
}
