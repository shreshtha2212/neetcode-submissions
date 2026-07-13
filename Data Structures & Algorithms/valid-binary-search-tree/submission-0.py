# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isVal(root,mini,maxi):
            if root is None:
                return True
            if root.val>=maxi or root.val<=mini:
                return False
            return isVal(root.left,mini, root.val) and isVal(root.right, root.val, maxi)
        return isVal(root,float("-inf"), float("inf"))

        