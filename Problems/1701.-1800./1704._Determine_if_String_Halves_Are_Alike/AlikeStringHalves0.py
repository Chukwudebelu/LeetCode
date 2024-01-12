class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        firstHalf = s[:len(s)//2]
        secondHalf = s[len(s)//2:]
        return self.vowelCounter(firstHalf) == self.vowelCounter(secondHalf)
    
    def vowelCounter(self, s: str) -> int:
        dictVowels, countVowel = {}, 1
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        for i in range(len(s)):
            if s[i] in vowels:
                countVowel += 1
        return countVowel
