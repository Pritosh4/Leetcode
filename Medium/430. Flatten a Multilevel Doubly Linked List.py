"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        while ptr is not None:
            if ptr.child:
                self.merge(ptr)
            ptr = ptr.next
        return head
    
    def merge(self, ptr):
        child = ptr.child
        while child.next is not None:
            child = child.next
        if ptr.next:
            child.next = ptr.next
            ptr.next.prev = child
        
        ptr.next = ptr.child
        ptr.child.prev = ptr
        ptr.child = None
