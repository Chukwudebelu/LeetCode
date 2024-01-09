#!/bin/python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    sum_val = 0

    if (root is None): return sum_val

    if (root.val < low):
      return self.rangeSumBST(root.right, low, high)
    elif (root.val > high):
      return self.rangeSumBST(root.left, low, high)
    else:
      sum_val += root.val
      sum_val += (self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high))
    return sum_val
