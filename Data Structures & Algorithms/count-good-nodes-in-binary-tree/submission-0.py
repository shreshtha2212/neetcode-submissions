# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxi=float("-inf")
        cnt=0
        
        def check(maxi,root):
            nonlocal cnt
            if not root:
                return
            if root.val>=maxi:
                maxi=root.val
                cnt+=1
            check(maxi,root.left)
            check(maxi,root.right)
        check(maxi,root)
        return cnt
            

        