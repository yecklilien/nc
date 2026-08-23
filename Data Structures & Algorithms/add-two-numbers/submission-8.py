# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        extra = 0
        curr = dummy
        while l1 and l2:
            val, extra = self.getSumAndExtra(l1.val + l2.val + extra)
            newNode = ListNode(val)
            curr.next = newNode
            curr=newNode
            l1 = l1.next
            l2 = l2.next
        
        remaining = l1 or l2
        while remaining:
            val, extra = self.getSumAndExtra(remaining.val + extra)
            newNode = ListNode(val)
            curr.next = newNode
            curr = newNode
            remaining = remaining.next
        
        if extra > 0:
            newNode = ListNode(extra)
            curr.next = newNode
            curr = newNode
        
        return dummy.next


    def getSumAndExtra(self:int, sum:int) -> (int, int):
        extra = 0
        if sum >= 10:
            extra = 1
            sum %= 10
        return sum, extra



        