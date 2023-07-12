'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        total = 0
        carry = 0
        ans = ListNode()
        while s1 or s2:
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            ans.val = total % 10
            carry = total // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total = carry
        return ans.next if carry == 0 else ans

    
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = self.reverse(l1)
        ptr2 = self.reverse(l2)
        carry = 0
        dummy = ListNode(0)
        cur = dummy

        while ptr1 is not None or ptr2 is not None or carry != 0:
            ptr1val = ptr1.val if ptr1 else 0
            ptr2val = ptr2.val if ptr2 else 0
            total = ptr1val + ptr2val + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        return self.reverse(dummy.next)


    
    def reverse(self, head):
        prev = None
        ptr = head
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        return prev


