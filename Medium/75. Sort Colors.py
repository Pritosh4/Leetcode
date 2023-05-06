class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0 #Indicates the pointer for the next place where the 0 should come
        p2 = len(nums)-1 #Indicates the pointer for the next place where the 2 should come
        i = 0 #Pointer used to  traverse each element of the list
        count = 0 #Counts the number of elements that are put in the right order
        while count < len(nums):
            # If the number of pointer i is 0 then swap with the p0 position
            if nums[i] == 0: 
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            # If the number of pointer i is 1 then we ignore as the 1s will get sorted automatically
            elif nums[i] == 1:
                i += 1
            # If the number of pointer i is 2 then swap with the p2 position
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1 #We do not increment i as the new swapped elements needs to be checked again
            count += 1
        
### OR
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c0, c1, c2 = 0, 0, 0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1
        for j in range(len(nums)):
            if c0 != 0:
                nums[j] = 0
                c0 -= 1
            else:
                if c1 != 0:
                    nums[j] = 1
                    c1 -= 1
                else:
                    nums[j] = 2
