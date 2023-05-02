class Solution:
    def signFunc(self, product):
        if product < 0:
            return -1
        elif product > 0:
            return 1
        else:
            return 0 

    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in nums:
            mul *= i
        return self.signFunc(mul)
    
