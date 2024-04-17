100. Same Tree - https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

Intuition
-----------

Problem - Check if both trees are same
Now trees are same if value at root is same and both left subtrees and both right subtrees are same.
Check if value at root is same, if same proceed to next subproblem.
Next Subproblem -> check for left subtrees of both roots and check for right subtrees of both roots

Base Condition -> when both current root pointers are None (they have reached the end), return true
                  but if only one of them is None, there is a discrepency in the structure hence return false.


 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None: # when execution goes past the first if condition, we cross out the possibility that both p and q are None (that might satisfy the next if condition)
            return False
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
                                                                                             
                    
