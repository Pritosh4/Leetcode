class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num % 3 == 0:
            x = num // 3
            ans.append(x - 1)
            ans.append(x)
            ans.append(x + 1)
        return ans
        
