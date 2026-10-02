# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def traverse(node):
            nonlocal balanced
            if not node or not balanced:
                return 0
            left, right = 0,0
            if node.left:
                left = traverse(node.left)
            if node.right:
                right = traverse(node.right)
            
            if abs(left - right) > 1:
                balanced = False
            
            return max(left, right) + 1
        
        traverse(root)
        return balanced
