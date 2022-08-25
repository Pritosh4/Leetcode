class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for i in nums:
            if i == 0:
                zero += 1 #Counting the number of 0s
            elif i == 1:
                one += 1 #Counting the number of 1s
            elif i == 2:
                two += 1 #Counting the number of 2s
        #modifying the list with the number of 0s, 1s, 2s that have been counted
        for i in range(0,zero): 
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one, zero + one + two):
            nums[i] = 2
