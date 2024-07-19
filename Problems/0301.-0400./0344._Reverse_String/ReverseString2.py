#!/bin/python3

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Base cases
        if (len(s) == 0):   # empty string: ""
            return ['']
        elif (len(s) == 0): # unary string: "a"
            return [s[0]]
        else:   # binary strings or more: "ab", "abc", ...
            i, j = 0, len(s)-1  # 2-pointer recursive approach
            
            if (len(s) % 2 == 1): # odd number of characters
                while (i != j):
                    s[i], s[j] = s[j], s[i] # swap
                    i += 1
                    j -= 1
            else:   # even number of characters
                while (i < len(s)//2):
                    s[i], s[j] = s[j], s[i] # swap
                    i += 1
                    j -= 1
            return self.reverseString(s[i:j])
