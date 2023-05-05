#!/bin/python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1,1]]
        # Pascal's Triangle for n <= 2
        if (numRows <= 2):
            return triangle[:numRows]
        else:
            # Iterate through each i-th row, considering the fact that we already have [[1],[1,1]]
            for i in range(2,numRows):
                row = [1] # j = 0
                # may need to iterate through each j-th element in the i-th row
                for j in range(1,i): # numRows also represenets the number of elements in a row
                    row += [triangle[i-1][j-1] + triangle[i-1][j]]
                triangle.append(row + [1]) # Put 1 at the end
            return triangle           
