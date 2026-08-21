# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2 > 4 > 6 > 8
#     s   f
# 2 > 4 > 6 > 8 > 10 
# s   s   s      f

# 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 > 10
# s   s   s   s   s       f       f   f

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the mid
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None #Cut the link

        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

        # Reverse mid to the end
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        curr = prev
        while curr:
            print(curr.val)
            curr = curr.next

        # Merge
        dummy = ListNode()
        head1 = head
        head2 = prev
        while head1 and head2:
            dummy.next = head1
            head1 = head1.next
            dummy = dummy.next
            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next

        dummy.next = head1 or head2