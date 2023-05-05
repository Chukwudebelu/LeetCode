#!/bin/python3
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        common_str = ""; m = len(strs); lst_common = []
        # If there's only one element in the list, return that entry
        if m == 1:
            return strs[0]
        
        # For at least 2 elements
        for i in range(m-1):
            # For more than 1 element (compare 2 strings)
            common_str = str()
            smaller = min(len(strs[i]), len(strs[i+1]))

            # Check for the common string between i-th & j-th elements
            for k in range(smaller):
                if strs[i][k] == strs[i+1][k]:
                    common_str += str(strs[i][k])    # or str(strs[i+1][k])
                else: # if there's an element mismatch, exit loop
                    break
            # Append this common string to a list of strings of adjacent elements
            lst_common.append(common_str)
        return min(lst_common)
