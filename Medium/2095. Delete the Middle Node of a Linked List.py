# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        slow, fast = head, head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return dummy.next
