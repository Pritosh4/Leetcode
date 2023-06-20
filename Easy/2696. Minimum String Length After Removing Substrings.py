class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 1 and (stack[-2] + stack[-1] == 'AB' or stack[-2] + stack[-1] == 'CD'):
                stack.pop()
                stack.pop()
        return len(stack)
