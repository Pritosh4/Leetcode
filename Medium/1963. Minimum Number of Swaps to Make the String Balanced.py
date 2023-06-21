class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in s:
            if stack and i == ']':
                stack.pop()
            elif i == '[':
                stack.append(i)
        return (len(stack) + 1) // 2

class Solution:
    def minSwaps(self, s: str) -> int:
        open_count = 0
        for i in s:
            if open_count > 0 and i == ']':
                open_count -= 1
            elif i == '[':
                open_count += 1
        return (open_count + 1) // 2
