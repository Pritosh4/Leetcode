class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        nums.sort()
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= len(nums) - mid:
                if mid == 0 or nums[mid-1] < len(nums) - mid:
                    return len(nums) - mid
                else:
                    right = mid - 1
            elif nums[mid] < len(nums) - mid:
                left = mid + 1
        return -1
    
    
