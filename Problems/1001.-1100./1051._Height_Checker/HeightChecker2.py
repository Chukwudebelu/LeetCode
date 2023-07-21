#!/bin/python3

class Solution:
  def heightChecker(self, heights: list) -> int:
    return sum([heights[i] != sorted(heights)[i] for i in range(len(heights))])
