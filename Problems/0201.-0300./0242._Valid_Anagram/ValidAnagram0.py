#!/bin/python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Dictionary to hold chars in s
        dict_s = {}

        for char in s:
            if char not in dict.keys(dict_s):
                dict_s[char] = 0
            else:
                dict_s[char] += 1

        # Dictionary to hold chars in t
        dict_t = {}

        for char in t:
            if char not in dict.keys(dict_t):
                dict_t[char] = 0
            else:
                dict_t[char] += 1
        return dict_s == dict_t
