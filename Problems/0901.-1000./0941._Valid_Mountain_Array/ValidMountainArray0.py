#!/bin/python3
class Solution:
    def validMountainArray(self, arr: list) -> bool:
        n = len(arr)
        
        # If the array has at most 2 elements
        if (n <= 2):
            return False
        
        i = 0
        count = 1 # count elements in arr
        
        # Loop while strictly INCREASING
        while (i < n-1):
            if (arr[i+1] > arr[i]):
                i += 1
                count += 1
            else:
                break
        # When count = 1, arr is sorted in DESCENDING order
        # When count = n, arr is sorted in ASCENDING order
        if (count == 1 or count == n):
            return False
        
        j = i
        # Loop while strictly DECREASING
        while (j < n-1):
            if (arr[j+1] < arr[j]):
                j += 1
                count += 1
            else:
                break
        return count == n
