//!/bin/java

class Solution {
  public int strStr(String haystack, String needle) {
    // Variable to hold the length of the needle
    int m = needle.length();
    int[] ind = new int[]{-1};
    int i = 0;
    
    while (i < haystack.length()-m+1) {
      if ((haystack.substring(i,i+m)).equals(needle)) {
        ind[0] = i;
        break;
      }
      i += 1;
    }

    if (ind[0] >= 0) {
      return ind[0];
    } else {
      return ind[0];
    }
  }
}
