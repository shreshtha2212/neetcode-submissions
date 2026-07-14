# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def find(target,instart,inend):
            for i in range(instart,inend+1):
                if inorder[i]==target:
                    return i
            return -1
        def tree(instart,inend,ind):
            if instart>inend:
                return None
            h=TreeNode(preorder[ind])
            pos=find(h.val,instart,inend)
            h.left=tree(instart,pos-1,ind+1)
            h.right=tree(pos+1,inend,ind+(pos-instart+1))
            return h
        return tree(0,len(inorder)-1,0)
        