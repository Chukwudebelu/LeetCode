//!/bin/java
class Solution {
    public void duplicateZeros(int[] arr) {
        // Number of lements in arr[]     
        int n = arr.length;
        
        for (int j = 0; j < n-1; j++) {
            // Check if the element is 0
            if (arr[j] == 0) {
                // Move elements 1 place to the right
                for (int i = n-2; i >= j; i--) {
                    arr[i + 1] = arr[i];
                }
                arr[j+1] = 0;
                ++j;
            }
        }
    // return arr;
    }
}
