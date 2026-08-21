# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 > 2 > 3 > 4 > None 
#         h       e

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        for i in range(n):
            end = end.next

        prev=None
        node=head
        while end:
            prev = node
            end = end.next
            node = node.next
        
        if prev:
            prev.next = node.next
        else: #means head is the target
            head = head.next
        return head
