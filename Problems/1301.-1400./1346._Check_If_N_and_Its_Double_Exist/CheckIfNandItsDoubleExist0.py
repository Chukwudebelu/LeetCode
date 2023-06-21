#!/bin/python3
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        '''
        Check if there exists any 2 elements in arr, such
        that one is double the other
        '''
        logic = False
        length = len(arr)
        for i in range(0,length-1):
            for j in range(i+1,length):
                if (arr[i] == 2*arr[j] or arr[i]*2 == arr[j]):
                    logic = True
        return logic
