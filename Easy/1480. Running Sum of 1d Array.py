class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        tot = 0
        for i in nums:
            tot += i
            ans.append(tot)
        return ans
        
