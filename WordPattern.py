# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) == len(s):
            chars1 = list(set(pattern))
            chars2 = list(set(s))
            pattern = tuple(pattern)
            lst = []
            for i, j in zip(pattern, s):
                lst.append((i,j))
            if len(chars1) == len(chars2) and len(chars1) == len(set(lst)):
                return True
            else:
                return False
        else:
            return False
