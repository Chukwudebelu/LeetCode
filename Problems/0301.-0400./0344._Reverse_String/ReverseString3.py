#!/bin/python3

class Solution(object):
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        # Base cases
        if (n == 0):   # empty string: ""
            return ['']
        elif (n == 0): # unary string: "a"
            return [s[0]]
        else:   # binary strings or more: "ab", "abc", ...
            i = 0   # 1-pointer recursive approach
            
            if (n % 2): # odd number of characters
                while (i != n-i-1):
                    s[i], s[n-i-1] = s[n-i-1], s[i] # swap
                    i += 1
            else:   # even number of characters
                while (i < int(n/2)):
                    s[i], s[n-i-1] = s[n-i-1], s[i] # swap
                    i += 1
            return self.reverseString(s[i:n-i-1])
