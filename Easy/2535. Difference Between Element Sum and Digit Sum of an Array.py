class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e_sum = 0
        d_sum = 0
        for i in nums:
            if i // 10 == 0:
                continue
            else:
                e_sum += i
                while i != 0:
                    d_sum += i % 10
                    i = i // 10
            
        return abs(e_sum - d_sum) 
