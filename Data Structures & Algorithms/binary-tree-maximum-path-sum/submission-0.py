# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float("-inf")
        
        
        def maxCalc(root):
            nonlocal maxi
            if root is None:
                return 0
            
            maxiL=max(maxCalc(root.left),0)
          
            maxiR=max(maxCalc(root.right),0)
            maxi=max(maxi,maxiL+maxiR+root.val)
            return max(maxiL, maxiR)+root.val
        maxCalc(root)
        
        return maxi
        
        
        