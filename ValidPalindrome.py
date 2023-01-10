# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        lst = []
        for char in s:
            if char.isalnum():
                lst += [char.lower()]
        word = ''.join(lst)
        return word == word[::-1]
