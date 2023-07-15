# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        for i in range(n):
            ptr1 = ptr1.next
        if ptr1 == None:
            return head.next
        while ptr1.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        ptr2.next = ptr2.next.next
        return head        
