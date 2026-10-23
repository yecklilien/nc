"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_map = {}
        q = deque()
        node_map[node.val] = Node(node.val)
        q.append((node_map[node.val], node))

        while(len(q)>0):
            new_node, old_node = q.popleft()

            for ne in old_node.neighbors:
                if ne.val not in node_map:
                    node_map[ne.val] = Node(ne.val)
                    q.append((node_map[ne.val], ne))

                new_node.neighbors.append(node_map[ne.val])
        return node_map[1]    