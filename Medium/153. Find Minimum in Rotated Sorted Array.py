class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[high]:
                return nums[low]
            elif mid>0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]<=nums[high]:
                high=mid-1
            elif nums[mid]>=nums[low]:
                low=mid+1
