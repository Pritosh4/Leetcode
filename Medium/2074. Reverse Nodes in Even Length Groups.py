# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None or head.next.next is None:
            return head
        
        ptr = len_check = before = head
        group = 1
        while ptr:
            length = 0
            while len_check and length < group:
                len_check = len_check.next
                length += 1
            
            if length % 2 == 1:
                for i in range(length):
                    before = ptr
                    ptr = ptr.next
            else:
                tail = ptr
                prev = None
                for j in range(length):
                    nxt = ptr.next
                    ptr.next = prev
                    prev = ptr
                    ptr = nxt
                before.next = prev
                before = tail
                tail.next = ptr

            group += 1
        return head
