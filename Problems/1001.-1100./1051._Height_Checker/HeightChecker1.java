//!/bin/java
import java.util.Arrays;

class Solution {
  public int heightChecker(int[] heights) {
    // Initialize the expected array
    int[] expected = new int[heights.length];
    
    // Copy the heights array
    for (int i = 0; i < heights.length; i++)
      expected[i] = heights[i];

    // Sort the heights array
    Arrays.sort(expected);

    int count = 0;
    for (int j = 0; j < heights.length; j++)
      if (heights[j] != expected[j]) count++;

    return count;
  }
}
