//#!/bin/java
class Solution {
    public void reverseString(char[] s) {
        /*
        # 1-pointer approach
        i = 0
        
        while (i < len(s)//2):
            temp = s[len(s)-i-1]
            s[len(s)-i-1] = s[i]
            s[i] = temp
            i += 1
        */
        // 1-pointer approach
        int i = 0;
        char temp; // declare dummy variable for swapping
        
        while (i < s.length/2) {
            temp = s[s.length-i-1];
            s[s.length-i-1] = s[i];
            s[i] = temp;
            i++;
        }
    }
}
