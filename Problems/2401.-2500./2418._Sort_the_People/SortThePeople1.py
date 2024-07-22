#!/bin/python3

class Solution(object):
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(names)
        namesHeights = list()
        for i in range(0, n):
            namesHeights += [(names[i], heights[i])]

        for j in range(n-1):
            for k in range(j+1,n):
                if (namesHeights[k][1] > namesHeights[j][1]):   # Check for heights
                    namesHeights[k], namesHeights[j] = namesHeights[j], namesHeights[k] # swap name & height pairs

        descendingHeights = [person[0] for person in namesHeights]
        return descendingHeights
