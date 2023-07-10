# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        left = list1
        for i in range(a - 1):
            left = left.next

        right = list1
        for i in range(b):
            right = right.next
            
        tail = list2
        while tail.next:
            tail = tail.next
                
        left.next = list2
        tail.next = right.next
                
        return list1
