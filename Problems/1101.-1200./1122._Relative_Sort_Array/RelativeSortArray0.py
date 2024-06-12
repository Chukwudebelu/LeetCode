#!/bin/python3
# 1122. Relative Sort Array

class Solution:
  def relativeSortArray(self, arr1: list, arr2: list) -> list:
    arr3, arr4 = [], []

    # Dynamic array to hold all elements that match those in arr2
    for j in range(0, len(arr2)):
      for i in range(0, len(arr1)):
        if (arr1[i] in arr2 and arr1[i] == arr2[j]):
          arr3.append(arr1[i])
        # Capture elements that don't appear in arr2
        elif (j == 0 and arr1[i] not in arr2):
          arr4 += [arr1[i]]

    # Sort elements not in arr2
    arr4.sort(reverse = False)
    arr3.extend(arr4)
    return arr3
