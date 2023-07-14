# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        width = count // k
        rem = count % k
        
        ans = []
        for i in range(k):
            ptr = head
            if i < rem:
                add = 1
            else:
                add = 0
            for j in range(width + add - 1):
                if ptr:
                    ptr = ptr.next
            ans.append(head)
            if ptr:
                head = ptr.next
                ptr.next = None
            else:
                head = None
        return ans

