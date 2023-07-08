class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        fi = 0
        for i in range(len(nums)):
            fi +=  i * nums[i]
        ans = fi
        total = sum(nums)
        for i in range(len(nums)):
            fi = fi + total - (len(nums) * nums[len(nums) - i - 1])
            ans = max(ans, fi)
        return ans
