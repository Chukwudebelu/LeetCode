#!/bin/python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 2-pointer approach
        i = 0; j = len(s)-1
        
        while (i < len(s)//2):
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i += 1
            j -= 1
