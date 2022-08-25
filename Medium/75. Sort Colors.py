class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            count += 1
        
