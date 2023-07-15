# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        hashmap = set()
        ptr = head
        while ptr:
            if ptr in hashmap:
                return ptr
            else:
                hashmap.add(ptr)
            ptr = ptr.next
        return None
        '''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if fast == None or fast.next == None:
            return
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast
