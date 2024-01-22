# 520. Detect Capital
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1 or len(word) == 0:
            return True
        else:
            lst = []
            for i in range(1,len(word)):
                lst += [word[i].isupper()]
            if word[0].isupper():
                if all(lst):
                    return True
                elif any(lst):
                    return False
                else:
                    return True
            else:
                if any(lst):
                    return False
                elif all(lst):
                    return False
                else:
                    return True
