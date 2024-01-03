#!/bin/python3

class Solution:
    def findMatrix(self, nums: list) -> list:
        main_list = list()

        # Dictionary to count the frequency of each number
        freqs = {}

        for num in nums:
            if num not in freqs: # freqs[num] = freqs.get(num, 0) + 1
                freqs[num] = 1
            else:
                freqs[num] += 1
        # The number with the most occurences is the number of rows
        # in the 2D array (run a loop that many times)
        m = max(freqs.values())

        for _ in range(m):
            sub_list = []; i = 0
            while (i < len(nums)):
                if nums[i] not in sub_list:
                    sub_list += [nums[i]] # append
                    del nums[i]
                else: # if the number is in the sublist (move forward)
                    i += 1
            main_list.append(sub_list)
        return main_list
