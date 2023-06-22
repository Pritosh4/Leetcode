class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                value, index = stack.pop()
                ans[index] = i - index
            stack.append([temperatures[i], i])
        return ans
