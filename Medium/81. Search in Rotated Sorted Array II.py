class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        # shifting to remove duplicate elements
        while low<high and nums[low] == nums[low+1]:
            low=low+1
        while low<high and nums[high] == nums[high-1]:
            high=high-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
        
