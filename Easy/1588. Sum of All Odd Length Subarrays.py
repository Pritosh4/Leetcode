class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i, e in enumerate(arr):
            left, right = i, n - i - 1
            ans += e * (left//2 + 1) * (right//2 + 1)
            ans += e * ((left + 1)//2) * ((right + 1)//2)
        return ans
