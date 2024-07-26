#!/bin/python3
# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if (not root):  # Empty Binary Search Tree:
            return None
        elif (root.val == val):
            return root
        elif (root.val > val):  # Left substree of Binary Search Tree
            return self.searchBST(root.left, val)
        elif (root.val < val):  # Right subtree of Binary Search Tree
            return self.searchBST(root.right, val)
