class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i != len(nums):
            add = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if add == nums[i]:
                ans.append(str(add))
            else:
                ans.append(str(add) + '->' + str(nums[i]))
            i += 1
        return ans
