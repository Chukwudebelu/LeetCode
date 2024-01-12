class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return (len([i for i in s[:len(s)//2] if i in 'aeiouAEIOU']) == len([j for j in s[len(s)//2:] if j in 'aeiouAEIOU']))
