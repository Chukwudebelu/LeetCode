#!/bin/python3
class Solution:
    def validMountainArray(self, arr: list) -> bool:
        i, j, k = 0, len(arr)-1, 0

        # Loop over the entire array
        while (k < len(arr)):
            if (i < len(arr)-1 and arr[i+1] > arr[i]): # Strictly INCREASING
                i += 1
            if (j > 0 and arr[j] < arr[j-1]): # Strictly DECREASING
                j -= 1
            k += 1
        return (i > 0 and i == j and j < len(arr)-1)
