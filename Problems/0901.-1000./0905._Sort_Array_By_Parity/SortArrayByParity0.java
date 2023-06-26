//!/bin/java
import java.util.ArrayList;

class Solution {
    public int[] sortArrayByParity(int[] nums) {
        ArrayList<Integer> evenNumbers = new ArrayList<>();
        ArrayList<Integer> oddNumbers = new ArrayList<>();
        
        // Check if each element is EVEN or ODD
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 1) oddNumbers.add(nums[i]); // odd #s
            else evenNumbers.add(nums[i]); // even #s
        }
      
        // Combine even & odd number ArrayLists
        evenNumbers.addAll(oddNumbers);
        
        // Convert ArrayList to int[] array
        int[] ints = evenNumbers.stream().mapToInt(Integer::intValue).toArray();
        return ints;
    }
}
