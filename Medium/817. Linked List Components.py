# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        ptr = head
        nums = set(nums)
        while ptr:
            if ptr.val in nums and (ptr.next == None or ptr.next.val not in nums):
                count += 1
            ptr = ptr.next
        return count
