class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')
        min1 = float('+inf')
        min2 = float('+inf')
        for i in nums:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        return (max1 * max2) - (min1 * min2)
