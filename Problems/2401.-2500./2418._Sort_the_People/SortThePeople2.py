#!/bin/python3

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [n for n, h in sorted(zip(names, heights), key = lambda a: a[1])][::-1]
