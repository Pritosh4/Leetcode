# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        height_min, height_max = self.min_max(root)
        return height_max - height_min <= 1 # Only when height different less than one, this tree is complete
    
    def min_max(self, root):
        if root is None:
            return 0, 0 # when reach the bottom, MIN MAX height are both zero
        left_min, left_max = self.min_max(root.left)
        right_min, right_max = self.min_max(root.right)
        if left_max >= left_min >= right_max >= right_min and left_max <= right_min + 1:  # to be clear, the logic here is redundent
		# if left_min >= right_max and left_max <= right_min + 1: # this is the concise version
            return right_min + 1, left_max + 1  
        return float("-inf"), float("inf")
