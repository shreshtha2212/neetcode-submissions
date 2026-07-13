# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans=[]
        from collections import deque
        q=deque([root])
        while q:
            p=[]
            for _ in range(len(q)):
                t=q.popleft()
                p.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            ans.append(p[-1])
        return ans
        