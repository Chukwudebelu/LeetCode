//!/bin/java
class Solution {
    public boolean validMountainArray(int[] arr) {
        int i, j, count, n = arr.length;

        // If the array has at most 2 elements
        if (n <= 2) return false;

        i = 0;
        count = 1; // Count elements in arr
        // Loop while strictly INCREASING
        while (i < n-1) {
            if (arr[i+1] > arr[i]) {
                i++;
                count++;
            } else {break;}
        }
        // When count = 1, arr is sorted in DESCENDING order
        // When count = n, arr is sorted in ASCENDING order
        if (count == 1 || count == n) return false;

        j = i;
        // Loop while strictly DECREASING
        while (j < n-1) {
            if (arr[j+1] < arr[j]) {
                j++;
                count++;
            } else {break;}
        }
        return (count == n) ? true : false;
    }
}
