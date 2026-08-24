"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = randomizer
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        new_curr = dummy
        curr = head
        node_map = {}
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            new_curr.next = new_node
            new_curr = new_node
            curr = curr.next
        
        curr = head
        while curr:
            curr_random = curr.random
            if curr_random:
                node_map[curr].random = node_map[curr_random]
            curr = curr.next
        
        return dummy.next