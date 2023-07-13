#!/bin/python3
import math;

class Solution:
    def getRow(self, rowIndex: int) -> list:
        lst2 = []
        for i in range(rowIndex+1):
            lst = []
            for j in range(i+1):
                lst.append(math.comb(i,j))
            lst2 += [lst]
        return lst2[rowIndex]
