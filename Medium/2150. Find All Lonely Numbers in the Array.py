class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        ans = []
        for j in seen:
            if seen[j] > 1 or j + 1 in seen or j - 1 in seen:
                continue
            else:
                ans.append(j)
        return ans
