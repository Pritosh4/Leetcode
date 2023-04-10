class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dic = {}
        for i in nums:
            if i in dic:
                if dic[i] == 1:
                    count += 1
                else:
                    count += dic[i]
                dic[i] += 1
            else:
                dic[i] = 1
        return count
