class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        for j in nums:
            if j + k in seen:
                count += seen[j + k]
        return count
