# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.reverse(self.find_mid(head))
        ptr1 = head
        ptr2 = mid
        while ptr2:
            if ptr1.val == ptr2.val:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            else:
                return False
        return True
        
        
        
    def find_mid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reverse(self, head):
        ptr = head
        prev = None
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        return prev
