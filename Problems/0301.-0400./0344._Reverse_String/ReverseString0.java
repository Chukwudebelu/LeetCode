//#!/bin/java
class Solution {
    public void reverseString(char[] s) {
        /* Python3 code
        # 2-pointer approach
        i = 0; j = len(s)-1
        
        while (i < len(s)//2):
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i += 1
            j -= 1
        */
        // 2-pointer approach
        int i = 0;
        int j = s.length-1;
        char temp; // declare dummy variable for swapping
        
        while (i < s.length/2) {
            temp = s[j];
            s[j] = s[i];
            s[i] = temp;
            i++;
            j--;
        }
    }
}
