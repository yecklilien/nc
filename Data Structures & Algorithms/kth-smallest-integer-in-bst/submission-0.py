# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        res = -1
        def traverse(node):
            nonlocal res, i
            if not node or res != -1:
                return
            traverse(node.left)
            i+=1
            if i == k:
                res = node.val
                return
            traverse(node.right)
        traverse(root)
        return res


        