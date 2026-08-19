# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        firstNode = list1
        secondNode = list2
        head = None
        curr = None 

        while firstNode != None and secondNode != None:
            next_node = None
            if firstNode.val < secondNode.val:
                next_node = firstNode
                firstNode = firstNode.next
            else:
                next_node = secondNode
                secondNode = secondNode.next
            
            if curr == None:
                curr = next_node
                head = curr
            else:
                curr.next = next_node
                curr = next_node
        
        if firstNode == None and secondNode != None:
            curr.next = secondNode
        if firstNode != None and secondNode == None:
            curr.next = firstNode

        return head