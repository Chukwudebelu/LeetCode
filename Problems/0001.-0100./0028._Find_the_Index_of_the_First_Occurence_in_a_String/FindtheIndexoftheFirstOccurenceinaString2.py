#!/bin/python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        
        ind = [i for i in range(len(haystack)-n+1) if haystack[i:i+n] == needle]
        
        return ind[0] if ind != [] else -1
            
        
