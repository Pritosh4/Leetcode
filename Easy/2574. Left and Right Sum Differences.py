class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        prefix = 0
        suffix = sum(nums)
        for i in nums:
            prefix += i
            answer.append(abs(prefix - suffix))
            suffix -= i
        return answer
