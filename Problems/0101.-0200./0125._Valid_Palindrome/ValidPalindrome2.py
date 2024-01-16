# 125. Valid Palindrome
class Solution:
  def isPalindrome(self, s: str) -> bool:
    return ("".join([char.lower() for char in s.strip() if char.isalnum()]) == "".join([char.lower() for char in s.strip() if char.isalnum()])[::-1])
