#!/bin/python3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while (root):
            if (root.val == val):
                return root
            elif (root.val > val):
                root = root.left
            elif (root.val < val):
                root = root.right
        return root
