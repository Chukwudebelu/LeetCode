//!/bin/java

class Solution {
  public int heightChecker(int[] heights) {
    int total = 0;
    int clone[] = heights.clone();
    Arrays.sort(clone);
    
    for (int i = 0; i < heights.length; i++){
      if (heights[i] != clone[i]) {
        total++;
      }
    }
    return total;       
  }
}
