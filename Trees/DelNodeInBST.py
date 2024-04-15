#450. Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

#Facts about BST:
#1. Inorder traversal leads to ascending order of elements in the BST.
#2. Successor of the node (next largest in the inorder array) can be found by moving once to right and then left untill possible
#3. Predecessor of the node (the largest val < node; i.e, the previous element in the inroder array) can be found by moving left once and right until possible.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None and root.right == None:
                root = None 
            elif root.right: # if right subtree found; update the root value with succesor and recursively delete the successor in the right subtree. Assign the right subtree root to return value of the recursive delete.
                root.val = self.find_next_largest(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.find_previous_largest(root) # if left subtree found; update the root value with predecessor and recursively delete the predecessor in the left subtree. Assign the left subtree root to return value of the recursive delete.
                root.left = self.deleteNode(root.left, root.val)
        return root
    '''
    If the node to be deleted has a right subtree, the node which will replace it is in the right subtree. Where? Go right once and then left utill it allows. This gives the node which is largest node after the current node.
    '''
    def find_next_largest(self, root): 
        root = root.right
        while root.left:
            root = root.left
        return root.val
    '''
    If the node to be deleted doesn't have a right subtree but has a left, the node which will replace it is in the left subtree. Where? Go left once and then right utill it allows. This gives the node which is largest node right before the current node.
    '''
    def find_previous_largest(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
