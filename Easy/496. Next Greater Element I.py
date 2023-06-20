class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        ans = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        for j in stack:
            mapping[j] = -1
        
        for k in nums1:
            ans.append(mapping[k])
        return ans
