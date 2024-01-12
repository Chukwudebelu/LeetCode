class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        return sum(i in vowels for i in s[:len(s)//2]) == sum(j in vowels for j in s[len(s)//2:])
