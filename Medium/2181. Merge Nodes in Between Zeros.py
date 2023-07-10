# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        ptr = head
        while ptr.next:
            if ptr.val == 0:
                ptr = ptr.next
                tot = 0
                while ptr.val != 0:
                    tot += ptr.val
                    ptr = ptr.next
                prev.val = tot
                if ptr.next:
                    prev.next = ptr
                    prev = ptr
                else:
                    prev.next = None
        return head
