# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        
        prev = dummy
        while count >= k:
            ptr = prev.next
            nxt = ptr.next
            for i in range(k-1):
                ptr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = ptr.next
            prev = ptr
            count -= k
        return dummy.next
