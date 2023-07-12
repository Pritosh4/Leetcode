# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        ptr1 = l1
        ptr2 = l2
        while ptr1 != None or ptr2 != None or carry != 0:
            if ptr1:
                ptr1val = ptr1.val
                ptr1 = ptr1.next
            else:
                ptr1val = 0

            if ptr2:
                ptr2val = ptr2.val
                ptr2 = ptr2.next
            else:
                ptr2val = 0

            total = carry + ptr1val + ptr2val
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            
        return dummy.next
