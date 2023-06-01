#!/bin/python3
class Solution:
    def duplicateZeros(self, arr: list) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Number of elements in arr
        n = len(arr); j = 0

        while (0 <= j < n-1):
            # Check if the element is 0
            if (arr[j] == 0):
                for i in range(n-2, j, -1):
                    arr[i+1] = arr[i]
                # Insert 0
                arr[j+1] = 0
                j += 1 # Skip to the next element
            # Loop variable
            j += 1
