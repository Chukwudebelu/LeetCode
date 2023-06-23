//!/bin/java
class Solution {
    public boolean validMountainArray(int[] arr) {
        int n = arr.length, i = 0, j = n-1, k = 0;

        // Loop over the entire array
        while (k < n) {
            if (i < n-1 && arr[i+1] > arr[i]) // Strictly INCREASING
                ++i;
            if (j > 0 && arr[j] < arr[j-1]) // Strictly DECREASING
                --j;
            k++;
        }
        return (i > 0 && i == j && j < n-1);
    }
}
