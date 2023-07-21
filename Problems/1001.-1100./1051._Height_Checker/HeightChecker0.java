//!/bin/java

class Solution {
    public int heightChecker(int[] heights) {
        // Initialize the expected array
        int[] expected = new int[heights.length];

        // Copy the heights array
        for (int e = 0; e < heights.length; e++)
            expected[e] = heights[e];

        int temp;
        // Sort the heights array
        for (int i = 0; i < expected.length; i++) {
            for (int j = i+1; j < expected.length; j++) {
                if (expected[j] < expected[i]) {
                    temp = expected[j];
                    expected[j] = expected[i];
                    expected[i] = temp;
                }
            }
        }

        int count = 0;
        for (int k = 0; k < heights.length; k++) {
            if (heights[k] != expected[k]) count++;
        }

        return count;
    }
}
