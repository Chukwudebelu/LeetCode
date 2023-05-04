class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Convert each to a list
        # lst1 = list(haystack)
        # lst2 = list(needle)

        # Create a variable to hold the length of the needle word
        n = len(needle)
        lst = []
        i = 0
        if needle in haystack:
            while i < len(haystack)- n and lst == []:
                if haystack[i:i+n] == needle:
                    lst.append(i)
                    break
                i += 1
            return i
        else:
            return -1
