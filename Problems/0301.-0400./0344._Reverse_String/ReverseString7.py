#!/bin/python3

class Solution(object):
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[len(s)::-1]
