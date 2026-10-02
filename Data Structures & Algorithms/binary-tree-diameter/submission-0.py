# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _,res = self.recurse(root)
        return res

    def recurse(self, node: Optional[Treenode]) -> (int,int):
        if not node:
            return 0,0
        left, right = 0,0
        lmax, rmax = 0,0
        if node.left:
            left, lmax = self.recurse(node.left)
        if node.right:
            right, rmax = self.recurse(node.right)    
        candidate = left + right
        resmax = max(lmax, rmax)
        resmax = max(resmax, candidate)
        resdepth = max(left, right) +1
        return resdepth, resmax



        

            