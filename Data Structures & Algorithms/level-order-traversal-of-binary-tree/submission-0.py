# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append((root,0))
        res = []
        while len(q) > 0:
            node, level = q.popleft()
            if node:
                if len(res) <= level:
                    res.append([])
                res[level].append(node.val)
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))
            
        return res
