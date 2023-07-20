#!/bin/python3

class Solution:
  def heightChecker(self, heights: list) -> int:
    # expected[] is the ascending order of heights
    # Hence, sort the heights[] array
    expected = sorted(heights)
    n = len(heights)
    return len([i for i in range(n) if heights[i] != expected[i]])
