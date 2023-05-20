class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tot = sum(nums)
        length = len(nums)
        ans = []
        prefix = 0
        for i in range(length):
            prefix += nums[i]
            tot -= nums[i]
            ans.append(tot - prefix + 2 * (i +1) * nums[i] - (nums[i] * length))
    
        return ans
