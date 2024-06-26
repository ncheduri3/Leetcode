#700. Search in a Binary Search Tree - https://leetcode.com/problems/delete-node-in-a-bst/submissions/1232755440/?envType=study-plan-v2&envId=leetcode-75


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if (val > root.val):
            return self.searchBST(root.right, val)
        elif (val < root.val):
            return self.searchBST(root.left, val)
        elif (val == root.val):
            return root
        
