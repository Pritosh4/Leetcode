class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in seen:
                return [seen[rem], i]
            else:
                seen[nums[i]] = i


