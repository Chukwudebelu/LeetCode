# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if (len(pattern) == len(s)):
            chars1, chars2 = map(list, [set(pattern), set(s)])
            pattern = tuple(pattern)
            lst = [(i, j) for i, j in zip(pattern, s)]
            return len(chars1) == len(chars2) and len(chars1) == len(set(lst))
        else:
            return 0
