# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def traverse(root, p, q):
            if not root:
                return False, False
            
            pf = qf = False
            if root.left:
                lpf, lqf = traverse(root.left, p, q)
                pf = pf or lpf
                qf = qf or lqf
            if root.right:
                rpf, rqf = traverse(root.right, p, q)
                pf = pf or rpf
                qf = qf or rqf

            if not pf:
                if root == p:
                    pf = True
            if not qf:
                if root == q:
                    qf = True

            nonlocal res
            if pf and qf and not res:
                res = root

            return pf,qf
        
        traverse(root,p,q)
        return res   
                
