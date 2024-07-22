#!/bin/python3
# 2418. Sort the people

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        names_heights = [(i, j) for i, j in zip(names, heights)]
        sorted_names_heights = sorted(names_heights, key = lambda x: x[1], reverse = True)
        return [name for name, _ in sorted_names_heights]
