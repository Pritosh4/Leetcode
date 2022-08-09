class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if target>nums[len(nums)-1]:
                return len(nums)
            elif target<=nums[0]:
                return 0
            elif mid>0 and nums[mid-1]<target<=nums[mid]:
                return mid
            elif nums[mid]<target:
                lo=mid+1
            else:
                hi=mid-1
