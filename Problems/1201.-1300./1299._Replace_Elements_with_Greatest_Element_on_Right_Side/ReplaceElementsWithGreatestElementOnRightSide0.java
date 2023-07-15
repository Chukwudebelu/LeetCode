//!/bin/java

class Solution {
  public int[] replaceElements(int[] arr) {
    if (arr.length == 1) return new int[]{-1};
        
    // Replace the last element with -1
    int temp = arr[arr.length-1];
    arr[arr.length-1] = -1;
    
    // Replace the 2nd last elements with last element
    int maxVal = Math.max(temp,arr[arr.length-2]);
    arr[arr.length-2] = temp;
    
    // Continue with loop
    for (int i = arr.length-3; i >= 0; i--) {
        temp = arr[i];
        arr[i] = maxVal;
        maxVal = Math.max(temp,maxVal);
    }
    return arr;
  }
}
