# 104. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Intuition
# -----------

# Problem -> mex depth of tree
# next Subproblem -> 1 + max (max depth of left subtree, max depth of right subtree)
# Base condition -> when we reach the child of a root node, we reached the end hence we return 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max (self.maxDepth(root.right), self.maxDepth(root.left))
