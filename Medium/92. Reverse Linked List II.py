# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        ptr = dummy.next
        for i in range(left - 1):
            ptr = ptr.next
            prev = prev.next
        
        previous, nxt = None, None
        temp = ptr
        for j in range(right - left + 1):
            nxt = ptr.next
            ptr.next = previous
            previous = ptr
            ptr = nxt
        prev.next = previous
        temp.next = nxt
        return dummy.next
        
