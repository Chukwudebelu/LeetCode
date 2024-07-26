#!/bin/python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if (root is None or root.val == val):
            return root
        elif (root.val > val):
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
