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
        
