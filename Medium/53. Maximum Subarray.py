class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float(-inf)
        max_till_here = 0
        for i in nums:
            max_till_here += i
            if max_till_here > max_sum:
                max_sum = max_till_here
            if max_till_here < 0:
                max_till_here = 0
        return max_sum
        




'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float(inf)
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    ## subarray = nums[i:j]
        return max_sum
      
start from the begining and take a window starting from i to j and calculate the temporary sum of the window and if the sum is greater than the max sum that has been 
recordeed up until now then then we replce the ,ax sum and also replace the subarray as the new subarray '''
