#!/bin/python3
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in range(len(arr)):
            # Check if element's Double is in arr
            if 2 * arr[i] in seen:
                return True
            # Check Double is even and exists
            elif arr[i] % 2 == 0 and arr[i] / 2 in seen:
                return True
            else:
                seen.add(arr[i])
        return False
