class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0
        for i in range(len(nums1)):
            low = i
            high = len(nums2) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums2[mid] >= nums1[i]:
                    low = mid + 1
                else:
                    high = mid - 1
            if high - i > max_distance:
                max_distance = high - i 
        return max_distance
