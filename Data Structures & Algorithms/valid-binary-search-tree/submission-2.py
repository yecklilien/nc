# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverseBST(node):
            cmin = cmax =  node.val
            if node.left:
                lres, lmin, lmax = traverseBST(node.left)
                if not lres or lmax >= node.val:
                    return False, cmin, cmax
                cmin = lmin
            if node.right:
                rres, rmin, rmax = traverseBST(node.right)
                if not rres or rmin <= node.val:
                    return False, cmin, cmax
                cmax = rmax
            return True, cmin, cmax
        
        if not root:
            return True
        res, _ , _ = traverseBST(root)
        return res

