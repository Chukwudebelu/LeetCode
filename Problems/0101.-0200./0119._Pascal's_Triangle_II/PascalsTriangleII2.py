#!/bin/python3
from math import comb as nCr;

class Solution:
  def getRow(self, rowIndex: int) -> list:
    return [[nCr(i,j) for j in range(rowIndex+1)] for i in range(rowIndex+1)][rowIndex]
