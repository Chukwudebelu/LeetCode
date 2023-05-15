#!/bin/python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 1-pointer approach
        i = 0;
        
        while (i < len(s)//2):
            temp = s[len(s)-i-1]
            s[len(s)-i-1] = s[i]
            s[i] = temp
            i += 1
