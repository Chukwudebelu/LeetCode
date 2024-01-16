# 125. Valid Palindrome
import re

class Solution(object):
    def isPalindrome(self, s):
        new_s = re.sub(r"[^a-zA-Z0-9\\s+]", "", s).lower()
        return new_s == new_s[::-1]
