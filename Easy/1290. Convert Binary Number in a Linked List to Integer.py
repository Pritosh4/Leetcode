# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr = head
        bin = ''
        while ptr:
            bin = bin + str(ptr.val)
            ptr = ptr.next
        mul = 1
        ans = 0
        for i in range(len(bin)-1, -1, -1):
            if bin[i] == '1':
                ans = ans + mul
            mul *= 2
        return ans

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr = head
        ans = 0
        while ptr:
            #ans = ans * 2 + ptr.val 
            ans = ans << 1 | ptr.val
            ptr = ptr.next
        return ans
