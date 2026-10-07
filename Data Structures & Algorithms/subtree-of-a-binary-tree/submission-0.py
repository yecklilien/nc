# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root,subRoot):
                return True
        
        if root.left:
            if self.isSubtree(root.left,subRoot):
                return True
        
        if root.right:
            if self.isSubtree(root.right,subRoot):
                return True
        
        return False

    def isSameTree(self, a, b):
        if a == b == None:
            return True
        if not a or not b:
            return False
        
        if a.val != b.val:
            return False
        ans = True
        if a.left or b.left:
            ans = ans and self.isSameTree(a.left, b.left)
        if a.right or b.right:
            ans = ans and self.isSameTree(a.right, b.right)
        return ans

        