//!/bin/java
class Solution {
    public boolean validMountainArray(int[] arr) {
        int n = arr.length, i = 0, j = n-1;

        // Strictly INCREASING loop
        while (i < n-1 && arr[i] < arr[i+1])
            i++;

        // Strictly DECREASING loop
        while (j > 0 && arr[j-1] > arr[j])
            j--;

        /*
         * If the array is a VALID MOUNTAIN array,  i and j meet
         * at the same index
         */
        return (i > 0 && i == j && j < n-1);
    }
}
