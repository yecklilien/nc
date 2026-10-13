# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def traverse(node, maxOnPath):
            if not node:
                return
            nonlocal res
            if node.val >= maxOnPath:
                maxOnPath = node.val
                res+=1

            traverse(node.left, maxOnPath)
            traverse(node.right, maxOnPath)

        traverse(root, -1000)
        return res
