class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b%a, a)
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for i in range(1, len(numsDivide)):
            g = self.gcd(g, numsDivide[i])
        nums.sort()
        for i in range(len(nums)):
            if g % nums[i] == 0:
                return i
        return -1
