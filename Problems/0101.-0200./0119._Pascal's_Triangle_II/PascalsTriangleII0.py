#!/bin/python3

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if (rowIndex < 1):
            return [1]*(rowIndex+1)
        else:
            lst = [[1]]
            for i in range(1,rowIndex+1):
                lst2 = [1] + [0 for _ in range(1,i)] + [1]
                for j in range(1,len(lst)):
                    lst2[j] = lst[i-1][j-1] + lst[i-1][j] 
                lst += [lst2]
            return lst[rowIndex]
