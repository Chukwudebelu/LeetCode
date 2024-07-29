#!/bin/python3
# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1, nums2 = map(sorted, [nums1, nums2])
        lst = []
        i, j = 0, 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                lst += [nums1[i]]
                j += 1
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1                
        return lst
