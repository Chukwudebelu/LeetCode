# 520. Detect Capital
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper(): # All letters in this word are capitals
            return 1
        elif word.islower(): # All letters in this word are not capitals
            return 1
        elif word[0].isupper() and word[1:].islower(): # Only the 1st letter is capital
            return 1
        else:
            return 0
