#!/bin/python3

class Solution(object):
    def getRow(self, rowIndex: int) -> list[int]:
        if (rowIndex == 0):  # Base Case 1
            return list((1,))
        elif (rowIndex == 1):  # Base Case 2
            return list((1,1,))
        else:  # Recursive
            current_row = [self.getRow(0)[0]]  # i.e. l = [1]
            previous_row = self.getRow(rowIndex-1)
            
            for i in range(rowIndex-1):
                current_row.append(previous_row[i] + previous_row[i+1])
            current_row += [1]

            return (current_row)
