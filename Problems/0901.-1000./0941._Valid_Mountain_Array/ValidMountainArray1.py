#!/bin/python3
class Solution(object):
    def validMountainArray(self, arr: list) -> bool:
        i, j = 0, len(arr)-1
        # Strictly INCREASING loop
        while (i < len(arr)-1 and arr[i] < arr[i+1]):
            i += 1
        # Strictly DECREASING loop
        while (j > 0 and arr[j-1] > arr[j]):
            j -= 1
        '''
        If the array is a VALID MOUNTAIN, i and j meet
        at the same index
        '''
        return (i > 0 and i == j and j < len(arr)-1)
