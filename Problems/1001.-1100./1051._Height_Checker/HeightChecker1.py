#!/bin/python3

class Solution:
  def heightChecker(self, heights: list) -> int:
    return len([i for i in range(len(heights)) if heights[i] != sorted(heights)[i]])
