//!/bin/java
import java.util.Arrays;

class Solution {
  public int heightChecker(int[] heights) {
    int count = 0;
    int[] arr = new int[heights.length]; // Initialize expected array
      
    for (int e : heights){
      arr[count] = e;
      count++;
    }
    
    count = 0;
    Arrays.sort(arr); // Sort the heights array
        
    for (int i = 0; i < heights.length; i++) {
      if (heights[i] != arr[i]) {
        count++;
      }
    }
    return count;
  }
}
