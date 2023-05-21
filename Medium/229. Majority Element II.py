class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        ans = []
        for i in seen:
            if seen[i] > len(nums) / 3:
                ans.append(i)
        return ans
