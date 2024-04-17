#112. Path Sum - https://leetcode.com/problems/path-sum/description/

# The intuition for recursion is to break the problem into subproblems. 
# SO find if the sum is present in the current tree
# next subproblem -> find if sum-root.val is present in left subtree or if it's present in the right subtree. 

# The base condition is when we reach the leaf node. We identify leaf node by checking that both the children are None. At this point we 
# return True if the sum is depleted to 0 through the recursion chain. Else we return false. 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum = targetSum - root.val
        if(root.right == None and root.left == None):
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
