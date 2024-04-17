##Couldn't solve. 

# 101. Symmetric Tree - https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Intuition
# -----------

# 2 trees are symmetric if value at root is same and (the left subtree of one tree, right subtree of another) 
# and (right subtree of one tree and the left subtree of another is same).

# Now we need a wrapper function because we add a layer 0 on top of the first subproblem.

# Base - When p and q are both none -> we reached the end return True
#   When only one of them is None -> structure discrepancy -> return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, p, q):
        if (p is None and q is None):
            return True
        if(p is None or q is None):
            return False
        return (p.val == q.val) and self.isMirror(p.left, q.right) and \
        self.isMirror(p.right, q.left)

        
