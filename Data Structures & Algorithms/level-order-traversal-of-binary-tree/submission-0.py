# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q=deque([root])
        ans=[]
        
        while q:
            j=[]
            
            
            for i in range(len(q)):
                p=q.popleft()
                j.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            ans.append(j)
        return ans
                
            


        