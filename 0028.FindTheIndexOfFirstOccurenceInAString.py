class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Create a variable to hold the length of the needle word
        n = len(needle)
        i = 0
        if needle in haystack:
            while i < len(haystack)- n:
                if haystack[i:i+n] == needle:
                    break
                i += 1
            return i
        else:
            return -1
