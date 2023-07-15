# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        ptr = slow
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        
        ptr1 = head
        ptr2 = prev
        while ptr2.next:
            nxt1 = ptr1.next
            ptr1.next = ptr2
            ptr1 = nxt1
            nxt2 = ptr2.next
            ptr2.next = ptr1
            ptr2 = nxt2
        return head
