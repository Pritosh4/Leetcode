# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        ptr = head
        while ptr and ptr.next:
            prev.next = ptr.next
            ptr.next = ptr.next.next
            prev.next.next = ptr
            prev = ptr
            ptr = ptr.next
        return dummy.next
