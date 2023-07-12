# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        count = 0
        ptr = head
        while ptr:
            ans.append(0)
            while stack and stack[-1][0] < ptr.val:
                val, i = stack.pop()
                ans[i] = ptr.val
            stack.append([ptr.val, count])
            count += 1
            ptr = ptr.next
        return ans
