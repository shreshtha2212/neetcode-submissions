# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def ht(root):
            nonlocal diameter
            if root is None:
                return 0
            
            leftt=ht(root.left)
            rightt=ht(root.right)
            diameter=max(diameter,leftt+rightt)
            return 1+max(leftt,rightt)
        ht(root)
        return diameter
        