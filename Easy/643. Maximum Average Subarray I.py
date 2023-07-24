class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = sum(nums[0:k])
        avg = tot / k
        for i in range(1, len(nums) - k + 1):
            tot += nums[i + k - 1] - nums [i - 1]
            avg = max(avg, tot/k)
        return avg
