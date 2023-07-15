# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return
    
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next

        ptr1 = head
        ptr2 = head
        for i in range(k % count):
            ptr1 = ptr1.next
        while ptr1.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        ptr1.next = head
        ans = ptr2.next
        ptr2.next = None
        return ans
        
