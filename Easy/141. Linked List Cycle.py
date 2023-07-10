# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        hashmap = {}
        ptr = head
        while ptr:
            if ptr in hashmap:
                return True
            else:
                hashmap[ptr] = 1
            ptr = ptr.next
        return False
        '''

        slow, fast = None, head
        while fast and fast.next:
            if slow and slow == fast:
                return True
            if slow:
                slow = slow.next
            else:
                slow = fast.next
            fast = fast.next.next
        return False
