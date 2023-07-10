# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = self.reverse(head)
        ptr1 = head1
        while ptr1 and ptr1.next:
            if ptr1.val > ptr1.next.val:
                ptr1.next = ptr1.next.next
            else:
                ptr1 = ptr1.next
        return self.reverse(head1)

    def reverse(self, head):
        prev = None
        ptr = head
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        return prev
    
