class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(self, nums: List[int], target: int):
            lo = 0
            hi = len(nums)-1
            while lo <= hi:
                mid = (hi + lo) // 2
                if mid == 0 and nums[mid] == target:
                    return mid
                elif nums[mid] == target and nums[mid-1] != target:
                    return mid
                elif nums[mid] >= target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
            return -1
        def last(self, nums: List[int], target: int):
            lo = 0
            hi = len(nums)-1
            while lo <= hi:
                mid = (hi + lo) // 2
                if mid == len(nums)-1 and nums[mid] == target:
                    return mid
                elif nums[mid] == target and nums[mid+1] != target:
                    return mid
                elif nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] <= target:
                    lo = mid + 1
            return -1
        return [first(self,nums,target), last(self,nums,target)]
        
