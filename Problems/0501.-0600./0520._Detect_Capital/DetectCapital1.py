# 520. Detect Capital
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        upper_count = 0

        for char in word:
            if ("A" <= char <= "Z"):
                upper_count += 1

        if (0 < upper_count < n):
            if (upper_count > 1):
                return False
            if not ("A" <= word[0] <= "Z"):
                return False
        return True
