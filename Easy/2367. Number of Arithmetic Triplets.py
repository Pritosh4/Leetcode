class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        dic = {}
        for i in nums:
            dic[i] = True
            if i - diff in dic and i - 2 * diff in dic:
                count += 1
        return count 
