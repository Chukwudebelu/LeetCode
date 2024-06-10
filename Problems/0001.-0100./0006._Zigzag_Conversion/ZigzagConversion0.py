#!/bin/python3

class Solution:
    # simulate and add each character to the corresponding row
    # go down -> reach bottom -> go up -> reach top -> go down ...
    def convert(self, s: str, n: int) -> str:
        # edge case
        if (n == 1): return s
        rows = ['' for _ in range(n)]
        # j is the index to track which rows a character should be added to
        # d is the direction: -1 means go up, 1 means go down
        j, d = 0, 1
        for i in range(len(s)):
            # add the current character to corresponding row
            rows[j] += s[i]
            # if it reaches to the last row, we need to go up
            if j == n - 1: d = -1
            # if it reaches to the first row, we need to go down
            elif j == 0: d = 1
            # move j pointer
            j += d;
        # rows would look like below in the first example
        # ['PAHN', 'APLSIIG', 'YIR']
        # we use join to build the final answer
        return ''.join(rows)
