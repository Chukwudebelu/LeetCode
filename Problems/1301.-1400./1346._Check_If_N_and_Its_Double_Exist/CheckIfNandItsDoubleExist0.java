//!/bin/java
class Solution {
    public boolean checkIfExist(int[] arr) {
        boolean logic = false;
        for (int i = 0; i < arr.length-1; ++i) {
            for (int j = i+1; j < arr.length; ++j) {
                if (arr[i] == 2*arr[j] || arr[i]*2 == arr[j]) {
                    logic = true;
                    break;
                }
            }
        }
        return logic;
    }
}
