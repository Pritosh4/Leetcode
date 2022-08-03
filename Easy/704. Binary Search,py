class Solution:
    def location(self,nums, target, mid):
        if target==nums[mid]:
            return "Found"
        elif target>nums[mid]:
            return "Right"
        elif target<nums[mid]:
            return "Left"
        else:
            return -1
        
    def search(self, nums: List[int], target: int) -> int:
        low, high=0, len(nums)-1
        while low<=high:
            mid=(low+high)//2
            result=self.location(nums, target, mid)
            if result=="Found":
                return mid
            elif result=="Left":
                high=mid-1
            elif result=="Right":
                low=mid+1
        return -1
