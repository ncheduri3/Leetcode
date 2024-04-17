226. Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150


# Intuition
# -----------

# Problem -> Invert the tree
# This can be done by exchanging the left subtree and right subtree

# next subproblem -> Invert the subtrees of left and right subtrees. 
# Base Condition -> when we reach end return none
# Exchange the root.right and root.left 
# return the root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
        
