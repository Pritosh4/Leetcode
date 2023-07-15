# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = h1 = ListNode(0)
        l2 = h2 = ListNode(0)
        ptr = head
        while ptr:
            if ptr.val < x:
                l1.next = ptr
                l1= l1.next
            else:
                l2.next = ptr
                l2 = l2.next
            ptr = ptr.next
        l2.next = None
        l1.next = h2.next
        return h1.next
