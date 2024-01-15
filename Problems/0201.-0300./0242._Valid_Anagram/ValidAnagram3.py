# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = [dict() for _ in range(2)]

        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return (dict_s == dict_t)
