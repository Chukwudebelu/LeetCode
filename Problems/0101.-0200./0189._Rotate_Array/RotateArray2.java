//!/bin/java

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
      
        if (n > k) {
            int arr[] = new int[k];
            for (int i = n-1; i >= n-k; i--)
                arr[k-n+i] = nums[i];

            int j = 0, l = n-k-1;
            while (n-- > 0) {
                if (l >= 0) {
                    nums[l+k] = nums[l];
                    l--;
                }
                else {
                    nums[j] = arr[j];
                    j++;
                }
            }
        }
    }
}
