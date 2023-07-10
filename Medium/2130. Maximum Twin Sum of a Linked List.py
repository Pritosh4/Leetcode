# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ptr1 = head
        ptr2 = self.reverse(self.mid(head))
        ans = 0
        while ptr2:
            ans = max(ans, ptr1.val + ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ans

    def reverse(self, head):
        prev = None
        ptr = head
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        return prev
    
    def mid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
